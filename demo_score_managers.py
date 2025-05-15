#!/usr/bin/env python3
"""
Demo script to show how to use different score managers with the RPS game.
This demonstrates the Open-Closed Principle in action - we can add new scoring
strategies without modifying the existing game code.
"""

import sys

from src.io_utils.input_provider_console import InputProviderConsole
from src.io_utils.output_provider_console import OutputProviderConsole
from src.game_factory import GameFactory
from game_paper_scissors_rock import GamePaperScissorsRock


def main():
    # Register the game with the factory
    GamePaperScissorsRock.register()
    
    # Create providers
    input_provider = InputProviderConsole()
    output_provider = OutputProviderConsole()
    
    # Get the score manager type from command line or use default
    if len(sys.argv) > 1 and sys.argv[1] in ["standard", "streak"]:
        score_manager_type = sys.argv[1]
    else:
        print("Available score managers:")
        print("  standard - Standard scoring (1 point per win, 0.5 per draw)")
        print("  streak   - Streak scoring (consecutive wins worth more points)")
        print("\nUsage: python demo_score_managers.py [standard|streak]")
        score_manager_type = input("Select score manager type [standard]: ") or "standard"
    
    # Create the game using the factory
    rps_game = GameFactory.create_game(
        GamePaperScissorsRock.GAME_TYPE, 
        input_provider, 
        output_provider
    )
    
    # Set the score manager type
    GamePaperScissorsRock.SCORE_MANAGER_TYPE = score_manager_type
    
    print(f"\nUsing {score_manager_type} score manager")
    rps_game.start_game()


if __name__ == "__main__":
    main() 