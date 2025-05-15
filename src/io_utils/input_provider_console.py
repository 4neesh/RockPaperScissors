from src.game_utils.game_mode import GameMode
from src.io_utils.input_provider import InputProvider


class InputProviderConsole(InputProvider):
    """
    An implementation of the InputProvider class that handles user input 
    via the console.
    """
    def game_mode_request(self) -> str:
        return input(f"Please enter a number to select a game mode: {', '.join(GameMode.formatted_choices())} \n").strip()

    def player_name_request(self, player_id: int) -> str:
        return input(f"Please enter player {player_id} name: ").strip()

    def play_again_request(self) -> str:
        return input("\nEnter 'y' to replay, or any key to exit \n").strip()

    def player_rps_request(self, player_id, choices) -> str:
        return input(f"Player {player_id}: Enter your move ({choices}), or enter 'e' to exit the game\n").strip()

    def rounds_of_game_request(self, max_rounds: int) -> str:
        return input(f"How many rounds of Rock, Paper, Scissors would you like to play? (Max: {max_rounds}) \n").strip()