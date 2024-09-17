<h1 align="center">Task No. 1</h1>

# Red-Blue Nim Game
The Red-Blue Nim Game is a two-player strategy game implemented in Python, where players take turns removing marbles from two piles (red and blue). The game is based on the classic Nim game but with two different versions: the Standard Version and the Misère Version.
### Game Rules
#### 1. Standard Version:
* Players lose if either pile is empty on their turn.
#### 2. Misere Version:
* Players win if either pile is empty on their turn.
### Scoring System
* Each red marble left: 2 points.
* Each blue marble left: 3 points.

The game is played between the user and an computer opponent, where the computer uses a basic strategy to remove marbles. The user starts first, and the number of red and blue marbles is randomly chosen between 10 and 15 at the start of each game.

## Features
* __Two Game Versions:__ Standard and Misère versions, where players win or lose based on the emptiness of the piles.
* __computer Opponent:__ The computer opponent uses a strategy to make moves, and a default search depth of 5 is used for its decision-making process.
* __Turn-based Gameplay:__ The game alternates between the user and computer players.
* __Score Calculation:__ Scores are calculated based on the marbles left in the piles after each move. The final score is shown at the end of the game.
* __Player Name Customization:__ The game asks the player to enter their name and uses it throughout the game.
* __Random Initial Marbles:__ The number of red and blue marbles is randomly set between 10 and 15 at the beginning of each game.

## How To Play

**1.** First enter your name.

**2.** Then choose the version you want to play (`standard` or `misere`).
   
   

**3.** The game starts with a display of the initial piles and total points. The player always plays first, and on each turn:

   ![Screenshot 2024-09-11 230339](https://github.com/user-attachments/assets/047daf35-ed54-470a-968f-b29477f66b7d)
   
**4.** Choose which pile (red or blue) to remove marbles from and select the number of marbles to remove (either 1 or 2).

   ![Screenshot 2024-09-11 230402](https://github.com/user-attachments/assets/d99ee3e0-1e11-47bf-b405-81b73cc6dffa)



**5.** After the player’s move, the computer makes its move.

  ![Screenshot 2024-09-11 230435](https://github.com/user-attachments/assets/714ff3fd-d955-42e9-8c8c-767c0d56432c)

**6.** The game ends when either pile becomes empty. The winner is determined based on the game version:
   - In **Standard Version**, the player who causes the other player to make a move when a pile is empty wins.
   - In **Misère Version**, the player who causes a pile to become empty on their own turn wins.

**7.** At the end of the game, the final score and the winner are displayed.

## Demonstration

  ![Screenshot 2024-09-11 231608](https://github.com/user-attachments/assets/af437e3e-3bfe-45c9-a73d-98bed54648ad)
