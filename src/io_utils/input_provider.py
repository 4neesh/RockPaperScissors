from abc import ABC, abstractmethod


class InputProvider(ABC):
    """
    Abstract base class for input providers that handle user input during the game.
    Specific input methods (console, GUI, etc.) should inherit from this class and implement
    the abstract methods for requesting various types of input.
    """
    @abstractmethod
    def player_name_request(self, player_id: int) -> str:
        pass

    @abstractmethod
    def play_again_request(self) -> str:
        pass

    @abstractmethod
    def player_rps_request(self, player_id: int, choices: str) -> str:
        pass

    @abstractmethod
    def rounds_of_game_request(self, max_rounds: int) -> str:
        pass

    @abstractmethod
    def game_mode_request(self) -> str:
        pass
