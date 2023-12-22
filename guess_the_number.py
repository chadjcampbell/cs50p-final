import random
from colorist import green

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 1)
    attempts = 0

    while True:
        # Get user input
        guess = input("Your guess: ")

        # Check if the input is a valid integer
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Increment the attempts count
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            green(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")