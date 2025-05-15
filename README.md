# Paper Scissors Rock

A classic **Rock Paper Scissors** game built in Python with a modular, object-oriented design.

## Getting Started

## Pre-requisites

- Python 3.13+
- PyTest 3.10+

### 1. Open the repository

``` bash
unzip SPR.zip
cd SPR
```

### 2. Run the tests
```bash
pytest tests/
```

### 3. Run the application

```bash
python game_paper_scissors_rock.py
```

### 4. In-Game Activity
1. Select a Mode to play (only Human vs Computer is available)
2. Enter your players name
3. Enter the number of rounds to play
4. Play by entering numbers that correspond to hand gestures
5. Receive the leaderboard after each turn and the final winner
6. Decide if you would like to replay by choosing 'y' at the end


## Developer Notes

### Design Process
- The game has been designed to fit into a larger 'Arcade' application
  - The GamePaperScissorsRock class implements the Game class which can be used as an abstraction for all games within an Arcade
- The code is designed to be extensible and adaptable for other types of interfaces (e.g., GUI or web-based).
- I have used abstract classes to promote extensibility across several areas:
  - User input medium
  - System output medium
  - Types of players (Virtual players can make move through an API)
- The GameMode and HandGesture are stored as enums for lightweight extensions of their behaviour
