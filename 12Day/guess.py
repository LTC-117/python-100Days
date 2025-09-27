import art
import random


mode = {
    "easy": 10,
    "hard": 5
}

chosen_number = random.randint(0, 100)

def number_guessing(diff):
    lives = diff

    if lives == 0:
        print("You've run out of guesses! You lose")
        exit(0)

    print(f"You have {lives} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))

    if user_guess < chosen_number:
        print("Too low\nGuess again.")
        number_guessing(lives - 1)
    elif user_guess > chosen_number:
        print("Too high\nGuess again.")
        number_guessing(lives - 1)
    else:
        print(f"You got it! The answer was {user_guess}.")



print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty not in mode:
    print("Error: Invalid difficulty! Try again later!")
    exit(0)

number_guessing(mode[difficulty])

