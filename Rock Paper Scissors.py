# Rock Paper Scissors
import random

def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ['rock', 'paper', 'scissors']:
            return choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (
        (player == 'rock' and computer == 'scissors') or
        (player == 'paper' and computer == 'rock') or
        (player == 'scissors' and computer == 'paper')
    ):
        return "You win!"
    else:
        return "I win."

def play_game():
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    print(f"Your choice was {player_choice}. and I chose {computer_choice}.")
    print(determine_winner(player_choice, computer_choice))

play_game()