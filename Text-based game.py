import random

def guessing_game():
    number_to_guess = random.randint(1, 10)
    attempts = 3

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        guess = int(input("Enter your guess: "))

        if guess == number_to_guess:
            print(" Congratulations! You guessed it right.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        attempts -= 1

    if attempts == 0:
        print(f"Sorry! You've used all your attempts. The number was {number_to_guess}.")
guessing_game()
