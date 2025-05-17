import signal
import threading
from src.game_utils.game_mode import GameMode
from src.io_utils.input_provider import InputProvider
from src.io_utils.countdown_timer import CountdownTimer


class TimeoutException(Exception):
    """Exception raised when a timeout occurs during input."""
    pass


def timeout_handler(signum, frame):
    """Handler for timeout signal."""
    raise TimeoutException()


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

    def player_rps_request(self, player_id, choices, time_limit: int = None) -> str:
        """
        Request a player's move with an optional time limit.
        
        Args:
            player_id: The ID of the player making the move
            choices: The available choices
            time_limit: Time limit in seconds (None for no limit)
            
        Returns:
            The player's input, or an empty string if timed out
        """
        prompt = f"Player {player_id}: Enter your move ({choices}), or enter 'e' to exit the game\n"
        
        # If no time limit, just use regular input
        if not time_limit:
            return input(prompt).strip()
        
        # Print the prompt first
        print(prompt, end="")
        
        # Create and start the countdown timer
        timer = CountdownTimer(time_limit)
        timer.start()
        
        # Set up the timeout handler
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(time_limit)
        
        try:
            user_input = input("")  # No prompt, as we've already printed it
            # Cancel the alarm if input received
            signal.alarm(0)
            # Stop the timer
            timer.stop()
            print()  # Print a newline to move past the timer line
            return user_input.strip()
        except TimeoutException:
            # If timeout occurred, return empty string
            timer.stop()
            print("\nTime's up!")
            signal.alarm(0)  # Cancel the alarm
            return ""
        finally:
            # Ensure alarm is canceled and timer is stopped
            signal.alarm(0)
            timer.stop()

    def rounds_of_game_request(self, max_rounds: int) -> str:
        return input(f"How many rounds of Rock, Paper, Scissors would you like to play? (Max: {max_rounds}) \n").strip()