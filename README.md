# Red-Blue Nim Game
## Overview
The Red-Blue Nim Game is a two-player strategy game implemented in Python, where players take turns removing marbles from two piles (red and blue). The game is based on the classic Nim game but with two different versions: the Standard Version and the Misère Version.
### Game Rules
#### 1. Standard Version:
•	Players lose if either pile is empty on their turn.
#### 1. Standard Version:
•	Players win if either pile is empty on their turn.
### Scoring System
•	Each red marble left: 2 points.
•	Each blue marble left: 3 points.

The game is played between a human player and an AI opponent, where the AI uses a basic strategy to remove marbles. The human player starts first, and the number of red and blue marbles is randomly chosen between 10 and 15 at the start of each game.

## Features
#### 1. Two Game Versions: 
Standard and Misère versions, where players win or lose based on the emptiness of the piles.
#### 2. AI Opponent:
The AI opponent uses a strategy to make moves, and a default search depth of 5 is used for its decision-making process.
#### 3. Turn-based Gameplay:
The game alternates between human and computer players.
#### 4. Score Calculation:
Scores are calculated based on the marbles left in the piles after each move. The final score is shown at the end of the game.
#### 5. Player Name Customization:
The game asks the player to enter their name and uses it throughout the game.
#### 6. Random Initial Marbles:
The number of red and blue marbles is randomly set between 10 and 15 at the beginning of each game.

## How To Play

1. Enter your name when prompted.

2. Choose the version you want to play (standard or misere).

3. The game starts with a display of the initial piles and total points. The player always plays first, and on each turn:

•	Choose which pile (red or blue) to remove marbles from.
•	Select the number of marbles to remove (either 1 or 2).

4. After the player’s move, the AI makes its move.

5. The game ends when either pile becomes empty. The winner is determined based on the game version:

•	In the Standard Version, the player who causes the other player to make a move when a pile is empty wins.
•	In the Misère Version, the player who causes a pile to become empty on their own turn wins.

7. At the end of the game, the final score and the winner are displayed.

Enter your name: Muneeb
Choose the version (standard/misere): standard

Starting piles - Red: 14, Blue: 13, Initial points: 67

Muneeb's turn! Current piles - Red: 14, Blue: 13
Choose a pile (red/blue): blue
How many marbles to remove?: 2
Muneeb's score: 61

Computer's turn! Computer removed 2 red marble(s).
Computer's score: 57

...

Game over!
Final score: 26
You win!
