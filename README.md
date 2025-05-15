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

### Extensibility
- New games
  - Can be added by implementing the ```Game``` class
- New gestures
  - Update the HandGesture enum, along with the rules and descriptions to implement a new gesture
  - Example, introducing Dynamite that can beat all other gestures:
```python
class HandGesture(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    DYNAMITE = 4
    ...
    rules: Dict[HandGesture, List[HandGesture]] = {
        HandGesture.ROCK: [HandGesture.SCISSORS],
        HandGesture.PAPER: [HandGesture.ROCK],
        HandGesture.SCISSORS: [HandGesture.PAPER],
        HandGesture.DYNAMITE: [HandGesture.SCISSORS, HandGesture.ROCK, HandGesture.PAPER]
    }
    # Descriptions for each gesture interaction
    descriptions: Dict[HandGesture, Dict[HandGesture, str]] = {
        HandGesture.ROCK: {HandGesture.SCISSORS: "blunts"},
        HandGesture.PAPER: {HandGesture.ROCK: "wraps"},
        HandGesture.SCISSORS: {HandGesture.PAPER: "cuts"},
        HandGesture.DYNAMITE: {HandGesture.PAPER: "destroys", HandGesture.SCISSORS: "destroys", HandGesture.ROCK: "destroys"}
    }
```
- Game modes
  - Further modes such as Human vs Human and Computer vs Computer can be enabled with a single line in the ```GameModes``` class
  - Example, updating the class with 1 line will enable 2 real people to play:
 ```python
    class GameMode(Enum):
        HUMAN_VS_COMPUTER = (1, 1)
        HUMAN_VS_HUMAN = (2, 0)
```
- OutputProvider
  - Implement the ```OutputProvider``` class from the io_utils package to extend the medium for which output is generated. 
  - Update the implementation of the ```OutputProvider``` used in the main method to assign its use.
  - For example, to a file, database or network 
- InputProvider
  - Implement the ```InputProvider``` class from the io_utils package to extend the medium for which input is retrieved. 
  - Update the implementation of the ```InputProvider``` used in the main method to assign its use.
  - For example, input can be received from a data stream or network 
