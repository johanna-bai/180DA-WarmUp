import random

while True: 
    player_move = input("Enter your choice (rock, paper, scissors): ").lower()
    while player_move not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        player_move = input("Enter your choice (rock, paper, scissors): ").lower()

    rand_move = random.choice(["rock", "paper", "scissors"])

    result = ""
    if player_move == rand_move:
        result = "It's a tie!"
    elif (
        (player_move == "rock" and rand_move == "scissors") or
        (player_move == "paper" and rand_move == "rock") or
        (player_move == "scissors" and rand_move == "paper")
    ):
        result = "You win!"
    else:
        result = "You lose!"
    
    print(f"You chose {player_move}.")
    print(f"Opponent chose {rand_move}.")
    print(result)

    play_again = input("Play again? (y/n) ").lower()
    
    while play_again not in ["y", "n"]:
        print("Invalid choice. Please enter y or n.")
        play_again = input("Play again? (y/n) ").lower()
    if play_again == "n": 
        print("Goodbye.")
        break