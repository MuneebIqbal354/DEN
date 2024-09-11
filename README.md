Red-Blue Nim Game
Project Overview
The Red-Blue Nim Game is a Python-based implementation of the traditional Nim game with a unique twist. It’s a turn-based, two-player game involving two piles of marbles — one red and one blue. The game has two modes: Standard Version and Misère Version, and pits the player against a computer opponent using basic AI.

Objective
The goal of the game is to either win by making the opponent face an empty pile (Standard Version) or by being the player to empty a pile (Misère Version). The game involves strategic decision-making, as players take turns removing marbles from one of the two piles.

Key Features
Two Game Versions:

Standard Version: The player who forces the opponent to make a move when a pile is empty wins.
Misère Version: The player who empties a pile on their own turn wins.
AI Opponent: The computer makes strategic moves based on a pre-defined algorithm with a search depth of 5, offering a basic level of challenge.

Turn-based Play: The player always goes first, followed by the AI opponent, with turns alternating until one of the game-ending conditions is met.

Randomized Starting Marbles: The game starts with a randomly selected number of red and blue marbles, between 10 and 15 in each pile, making every game unique.

Score Calculation: The score is calculated based on the number of red and blue marbles remaining at the end of the game. Each red marble is worth 2 points, and each blue marble is worth 3 points.

Game Rules
Standard Version:

Players lose if either pile is empty on their turn. The winner is the player who forces their opponent to make a move when one of the piles is empty.
Misère Version:

Players win if either pile is empty on their own turn. In this mode, the goal is to empty a pile on your turn to win.
Scoring:

Red marbles left: 2 points each.
Blue marbles left: 3 points each.
How to Play
Game Setup:

After starting the game, you are asked to enter your name.
You will then be prompted to choose which version of the game to play: Standard or Misère.
Gameplay:

The game begins with a display of the initial number of marbles in the red and blue piles, randomly chosen between 10 and 15.
The player always starts first.
On your turn, you will:
Choose a pile from which to remove marbles (either the red pile or the blue pile).
Choose how many marbles to remove from that pile (you can remove either 1 or 2 marbles).
After your move, the AI opponent will take its turn, removing marbles according to its own strategy.
End of the Game:

The game continues until one of the piles becomes empty.
In the Standard Version, the player who forces the opponent to face an empty pile wins.
In the Misère Version, the player who empties a pile on their own turn wins.
After the game ends, the final scores are calculated and displayed, and the winner is announced.
Score Calculation:

The remaining red and blue marbles are used to calculate the final score.
Each red marble left in the piles contributes 2 points, and each blue marble left contributes 3 points.
Example Playthrough
The game will begin with a message displaying the initial number of marbles in the piles and the total initial points.
You will take turns with the computer until one pile is emptied.
The game will display each player's score after every move.
When the game ends, the final score and the winner are displayed.
