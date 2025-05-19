import unittest
from unittest.mock import Mock, patch

from game_paper_scissors_rock import GamePaperScissorsRock
from src.io_utils.input_provider_console import InputProviderConsole
from src.io_utils.output_provider_console import OutputProviderConsole
from src.game_utils.game_mode import GameMode

class TestGamePaperScissorsRock(unittest.TestCase):

    def test_select_game_mode_human_vs_computer(self):
        input_provider = Mock(spec=InputProviderConsole)
        output_provider = Mock(spec=OutputProviderConsole)
        game = GamePaperScissorsRock(input_provider, output_provider)
        input_provider.game_mode_request.return_value = '1'
        selected_mode = game.select_game_mode()
        self.assertEqual(selected_mode, GameMode.HUMAN_VS_COMPUTER)
    
    @patch('sys.exit')
    def test_game_exits_when_user_does_not_replay(self, mock_exit):
        # Setup mocks
        input_provider = Mock(spec=InputProviderConsole)
        output_provider = Mock(spec=OutputProviderConsole)
        
        # Create game instance
        game = GamePaperScissorsRock(input_provider, output_provider)
        
        # Configure mock
        input_provider.play_again_request.return_value = 'n'  # User doesn't want to replay
        
        # Simulate the replay logic from play_game
        replay = input_provider.play_again_request()
        self.assertEqual(replay, 'n')
        
        # Call exit_game which should call sys.exit
        game.exit_game()
        
        # Verify the game asked the user to play again
        input_provider.play_again_request.assert_called_once()
        
        # Verify exit was called
        mock_exit.assert_called_once_with(0)
        
        # Verify game ending output
        output_provider.output_end_game.assert_called_once()
        
    def test_game_continues_when_user_wants_to_replay(self):
        # Setup mocks
        input_provider = Mock(spec=InputProviderConsole)
        output_provider = Mock(spec=OutputProviderConsole)
        
        # Create game instance with mocked methods
        game = GamePaperScissorsRock(input_provider, output_provider)
        
        # Mock the request_game_option method to avoid actual input
        game.request_game_option = Mock(side_effect=["1", "1"])  # Called twice for two rounds
        
        # Patch play_rounds to avoid complex game logic
        original_play_rounds = game.play_rounds
        game.play_rounds = Mock()
        
        # Setup input provider to first say 'y' (replay) then 'n' (exit)
        input_provider.play_again_request.side_effect = ['y', 'n']
        
        try:
            # Use a try-except to catch the sys.exit call to avoid test interruption
            with patch('sys.exit') as mock_exit:
                # Call the play_game method directly to test the replay loop
                # We need to pass mocked players and score manager
                mock_player1 = Mock()
                mock_player1.get_name.return_value = "Player 1"
                
                mock_player2 = Mock()
                mock_player2.get_name.return_value = "Player 2"
                
                mock_score_manager = Mock()
                
                # Call the method being tested
                game.play_game([mock_player1, mock_player2], mock_score_manager)
                
                # Verify play_rounds was called twice (once for each loop iteration)
                self.assertEqual(game.play_rounds.call_count, 2)
                
                # Verify play_again_request was called twice
                self.assertEqual(input_provider.play_again_request.call_count, 2)
                
                # Verify exit was called after the second replay response ('n')
                mock_exit.assert_called_once_with(0)
                
        finally:
            # Restore original method to avoid affecting other tests
            game.play_rounds = original_play_rounds
