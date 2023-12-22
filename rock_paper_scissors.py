import random
from colorist import green, red, blue

def rock_paper_scissors():
    print("\nWelcome to Rock, Paper, Scissors!\n")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        determine_winner(user_choice, computer_choice)
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break


def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    print(f"You chose {user_choice}.")
    print(f"I chose {computer_choice}.")

    if user_choice == computer_choice:
        blue("It's a tie!")
        return
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        green("You win!")
        return
    else:
        red("You lose!")
        return