from abc import abstractmethod, ABC

class Player(ABC):
    """
    Abstract base class representing a player in the Paper, Scissors, Rock game.
    This class serves as a template for both human and computer players, providing
    common functionality like player name and move validation.
    """
    MAX_NAME_LENGTH = 20

    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def make_move(self):
        pass

    @staticmethod
    def name_is_invalid(name: str) -> bool:
        return len(name) == 0 or len(name) > Player.MAX_NAME_LENGTH