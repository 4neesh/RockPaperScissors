import unittest
from unittest.mock import Mock

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

    def test_play_again_no_exits_game(self):
        """
        Test that the game exits when the user chooses not to replay ('n'),
        verifying behavior for both standard and best-of-5 modes.
        """
        input_provider = Mock(spec=InputProviderConsole)
        output_provider = Mock(spec=OutputProviderConsole)
        game = GamePaperScissorsRock(input_provider, output_provider)

        # Mock game mode selection (human vs computer)
        input_provider.game_mode_request.return_value = '1'

        # Test both game options: standard rounds and best-of-5
        for game_option in ['3', 'bo5']:  # 3 rounds and best-of-5
            with self.subTest(game_option=game_option):
                # Reset mocks for each subtest
                input_provider.reset_mock()
                output_provider.reset_mock()

                # Mock game flow
                input_provider.game_mode_request.return_value = '1'  # Human vs Computer
                input_provider.request_game_option.return_value = game_option
                input_provider.play_again_request.return_value = 'n'  # No replay

                # Mock player moves to avoid None (timeout) cases
                input_provider.player_rps_request.return_value = 'rock'

                # Mock sys.exit to prevent actual exit and verify it's called
                with unittest.mock.patch('sys.exit') as mock_exit:
                    game.start_game()

                    # Verify game flow
                    self.assertEqual(input_provider.game_mode_request.call_count, 1)
                    self.assertEqual(input_provider.request_game_option.call_count, 1)
                    self.assertEqual(input_provider.play_again_request.call_count, 1)

                    # Verify game introduction and end messages
                    output_provider.introduce_game.assert_called_once_with("Paper Scissors Rock")
                    output_provider.output_end_game.assert_called_once()

                    # Verify sys.exit was called
                    mock_exit.assert_called_once_with(0)

                    # Verify rounds played based on game option
                    if game_option == '3':
                        # For 3 rounds, expect 3 move requests per player
                        self.assertEqual(input_provider.player_rps_request.call_count, 6)  # 3 rounds * 2 players
                    elif game_option == 'bo5':
                        # For best-of-5, expect up to 5 rounds (could be less if someone wins early)
                        self.assertLessEqual(input_provider.player_rps_request.call_count, 10)  # 5 rounds * 2 players