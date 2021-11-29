"""
Project 1 - Number Guessing Game
--------------------------------
"""
import random
from statistics import median
from statistics import mean
from statistics import mode

print(">>>>>Guess the Magic Number<<<<<")  # welcome message
scoreboard = [10]
high_score = min(scoreboard)
print(f"The current high score is {high_score}")


def start_game():
    random_number = random.randint(0, 10)
    print(random_number)
    attempts = 1
    guess = int(input("guess a number between 0 and 10. "))
    guess_list = [guess]
    while True:
        try:
            if guess == random_number:
                print(f"That's correct! it only took you {attempts} attempts!")
                guess_mean = float(mean(guess_list))
                guess_median = float(median(guess_list))
                guess_mode = mode(guess_list)
                print(f"mean: {guess_mean}, median: {guess_median}, mode: {guess_mode}")
                break
            elif 0 < guess < random_number:
                guess = int(input(f"your guess of {guess} is lower than the number. Try again. "))
                guess_list.append(guess)
                attempts += 1
                print(f"here are your guesses so far: {guess_list}")
                print(f"Number of attempts: {attempts}")
            elif random_number < guess < 11:
                guess = int(input(f"your guess of {guess} is higher than the number. Try again. "))
                guess_list.append(guess)
                attempts += 1
                print(f"here are your guesses so far: {guess_list}")
                print(f"Number of attempts: {attempts}")
            else:
                raise ValueError
        except ValueError:
            guess = int(input("""Provide a whole number between "0" and "10". """))
    while True:
        if attempts < min(scoreboard):
            scoreboard.append(attempts)
            print("NEW HIGH SCORE!!!")
            print(f"the new high score is {min(scoreboard)}")
        else:
            print(f"The current high score is still {min(scoreboard)}")
        play_again = input("would you like to tray again? Y/N ")
        play_again.lower()
        if play_again == "y":
            print("sure, lets get started")
            start_game()
        elif play_again == "n":
            input("thanks for playing!")
            break
        else:
            print("try again!")

start_game()