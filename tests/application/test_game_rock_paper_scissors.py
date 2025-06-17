import unittest
from unittest.mock import Mock, patch

from game_paper_scissors_rock import GamePaperScissorsRock
from src.io_utils.input_provider_console import InputProviderConsole
from src.io_utils.output_provider_console import OutputProviderConsole
from src.game_utils.game_mode import GameMode
from src.players.player import Player

class TestGamePaperScissorsRock(unittest.TestCase):

    def test_select_game_mode_human_vs_computer(self):
        input_provider = Mock(spec=InputProviderConsole)
        output_provider = Mock(spec=OutputProviderConsole)
        game = GamePaperScissorsRock(input_provider, output_provider)
        input_provider.game_mode_request.return_value = '1'
        selected_mode = game.select_game_mode()
        self.assertEqual(selected_mode, GameMode.HUMAN_VS_COMPUTER)

    @patch('sys.exit')
    def test_game_exit_when_replay_declined(self, mock_exit):
        # Setup mocks
        input_provider = Mock(spec=InputProviderConsole)
        output_provider = Mock(spec=OutputProviderConsole)
        game = GamePaperScissorsRock(input_provider, output_provider)

        # Mock game mode selection
        input_provider.game_mode_request.return_value = '1'  # Human vs Computer

        # Mock player setup
        mock_player1 = Mock(spec=Player)
        mock_player2 = Mock(spec=Player)
        mock_player1.get_name.return_value = "Player 1"
        mock_player2.get_name.return_value = "Player 2"

        # Mock the game mode to return our mock players
        mock_game_mode = Mock()
        mock_game_mode.initialise_players_in_game.return_value = [mock_player1, mock_player2]

        # Mock select_game_mode to return our mock game mode
        game.select_game_mode = Mock(return_value=mock_game_mode)

        # Mock game option request
        game.request_game_option = Mock(return_value="1")  # 1 round

        # Mock player moves
        mock_player1.make_move.return_value = "rock"
        mock_player2.make_move.return_value = "scissors"

        # Mock score manager
        mock_score_manager = Mock()

        # Mock play_rounds to avoid actual gameplay
        game.play_rounds = Mock()

        # Mock play_again_request to return 'n' (no replay)
        input_provider.play_again_request.return_value = 'n'

        # Call start_game
        with patch('src.game_utils.score_manager_factory.ScoreManagerFactory.create_score_manager',
                   return_value=mock_score_manager):
            game.start_game()

        # Verify that exit_game was called
        output_provider.output_end_game.assert_called_once()
        mock_exit.assert_called_once_with(0)