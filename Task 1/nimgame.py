import random

# Check if the game is over based on the game version (Standard or Misère)
def game_over(piles, version):
    red, blue = piles
    return red == 0 or blue == 0  # In both versions, the game ends when a pile is empty

# Function to switch between players
def switch_player(current_player):
    return "human" if current_player == "computer" else "computer"

# Function for the human player to make a move
def human_move(piles, player_name):
    red, blue = piles
    print(f"\n------------------------- {player_name}'s turn ------------------------- \nCurrent piles - Red: {red}, Blue: {blue}")
    pile = input("Choose a pile (red/blue): ").lower()
    count = int(input("How many marbles to remove?: "))
    
    if pile == 'red' and 0 < count <= red:
        red -= count
    elif pile == 'blue' and 0 < count <= blue:
        blue -= count
    else:
        print("Invalid move!")
        return human_move(piles, player_name)  # Retry if the move is invalid
    
    return red, blue

# Function for the computer to make a move
def computer_move(piles, version):
    red, blue = piles
    
    # Simple AI logic: remove 1 or 2 marbles from the larger pile
    if version == "standard":
        if red >= blue and red > 0:
            remove_count = min(2, red)  # Computer picks up to 2 marbles from red
            red -= remove_count
            print(f"\n------------------------ Computer's turn ------------------------\nComputer removed {remove_count} red marble(s).")
        elif blue > 0:
            remove_count = min(2, blue)  # Computer picks up to 2 marbles from blue
            blue -= remove_count
            print(f"\n------------------------ Computer's turn ------------------------\nComputer removed {remove_count} blue marble(s).")
    else:  # Misère version, inverted strategy
        if blue >= red and blue > 0:
            remove_count = min(2, blue)
            blue -= remove_count
            print(f"\n------------------------ Computer's turn ------------------------\nComputer removed {remove_count} blue marble(s).")
        elif red > 0:
            remove_count = min(2, red)
            red -= remove_count
            print(f"\n------------------------ Computer's turn ------------------------\nComputer removed {remove_count} red marble(s).")
    
    return red, blue

# Function to calculate the score based on the piles
def calculate_score(piles):
    red, blue = piles
    return 2 * red + 3 * blue

# Function to determine the winner based on the game version
def determine_winner(current_player, version):
    if version == "standard":
        # In the standard version, the player who makes the last move loses
        return "Computer wins!" if current_player == "human" else "You win!"
    else:
        # In the Misère version, the player who makes the last move wins
        return "You win!" if current_player == "human" else "Computer wins!"

if __name__ == "__main__":
    # Ask for the player's name
    player_name = input("Enter your name: ")
    
    # Randomly choose the number of red and blue marbles between 10 and 15
    red = random.randint(10, 15)
    blue = random.randint(10, 15)
    
    # Ask user to choose the version
    version = input("Choose the version (standard/misere): ").lower()
    while version not in ["standard", "misere"]:
        print("Invalid version! Please choose either 'standard' or 'misere'.")
        version = input("Choose the version (standard/misere): ").lower()

    # Use default depth of 5 for the computer
    depth = 5
    
    current_player = "human"  # Human plays first by default
    
    # Print the starting piles and their corresponding points on the same line
    print(f"\nStarting piles - Red: {red}, Blue: {blue}, Total points: {calculate_score((red, blue))}")

    # Game loop
    while not game_over((red, blue), version):
        if current_player == "human":
            red, blue = human_move((red, blue), player_name)
            print(f"{player_name}'s score: {calculate_score((red, blue))}")
        else:
            red, blue = computer_move((red, blue), version)
            print(f"Computer's score: {calculate_score((red, blue))}")
        
        current_player = switch_player(current_player)
    
    # Game over: print final score and winner
    print("\nGame over!")
    print(f"Final score: {calculate_score((red, blue))}")
    print(determine_winner(current_player, version))
