# Python Number Guessing Game

import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0

is_running = True

print("Python Number Guessing Game")
print(f"Guess a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Guess a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too Low! Try again")
        elif guess > answer:
            print("Too High! Try again")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"You got it in {guesses} guesses")
            is_running = False
    else:
        print("Invalid Guess")
        print(f"Guess a number between {lowest_num} and {highest_num}")
