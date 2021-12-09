"""
Project 1 - Number Guessing Game
--------------------------------
"""
import random
from statistics import median
from statistics import mean
from statistics import mode

print(">>>>>Guess the Magic Number<<<<<")  # welcome message
scoreboard = []


def start_game():
    random_number = random.randint(0, 10)
    try:
        print(f">>The current high score is {min(scoreboard)}<<")
    except ValueError:
        print("The current high score is N/A \n")

    #print(random_number)   <-- these are cheat codes
    attempts = 0
    guess_list = []
    while True:
        try:
            guess = int(input("guess a number between 0 and 10. "))
            if -1 < guess < 11:
                attempts += 1
                guess_list.append(guess)
                if guess == random_number:
                    print(f"That's correct! it only took you {attempts} attempts!")
                    scoreboard.append(attempts)
                    if attempts < min(scoreboard):
                        print("NEW HIGH SCORE!!!")
                        print(f"the new high score is {min(scoreboard)}")
                    else:
                        print(f"The current high score is {min(scoreboard)}")
                    break
                elif -1 < guess < random_number:
                    print(f"your guess of {guess} is lower than the number. Try again. ")
                    print(f"here are your guesses so far: {guess_list}")
                    print(f"Number of valid attempts: {attempts}")
                    continue
                elif random_number < guess < 11:
                    print(f"your guess of {guess} is higher than the number. Try again. ")
                    print(f"here are your guesses so far: {guess_list}")
                    print(f"Number of valid attempts: {attempts}")
                    continue
            else:
                raise ValueError
        except ValueError:
            print("""Provide a whole number between "0" and "10".**** """)
    while True:
        scoreboard_mean = float(mean(scoreboard))
        scoreboard_median = float(median(scoreboard))
        scoreboard_mode = mode(scoreboard)
        print(
            f"The high score statistics are | mean: {scoreboard_mean}, median: {scoreboard_median}, mode: {scoreboard_mode}\n")
        play_again = input(">>>Would you like to tray again? Y/N <<<")
        play_again.lower()
        if play_again == "y":
            print("sure, lets get started")
            start_game()
        elif play_again == "n":
            input("thanks for playing!")
        else:
            print("try again!")


start_game()
