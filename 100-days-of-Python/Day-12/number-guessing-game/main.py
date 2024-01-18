# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random


def start():
    """Guessing number"""
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    target_number = random.randint(1, 100)
    game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attemps_remaining = 0

    if game_level == "easy":
        attemps_remaining = 10
    elif game_level == "hard":
        attemps_remaining = 5

    is_continued = True

    while is_continued:
        print(f"You have {attemps_remaining} attemps remaining to guess the number")
        guess = int(input("Make a guess: "))

        if guess > target_number:
            print("Too high.")
            print("Guess again.")
            attemps_remaining -= 1
        elif guess < target_number:
            print("Too low.")
            print("Guess again.")
            attemps_remaining -= 1
        elif guess == target_number:
            print(f"You got it! The answer was {guess}.")
            is_continued = False

        if attemps_remaining == 0:
            print("You've run out of guesses, you lose")
            is_continued = False


if __name__ == "__main__":
    is_inprogress = True
    while is_inprogress:
        user_choice = input("Do you want to play? Type 'y' or 'n': ")

        if user_choice == "y":
            start()
        else:
            is_inprogress = False
            print("Bye")
