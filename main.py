"""
Project 1 - Number Guessing Game
--------------------------------
"""
import random
from statistics import median
from statistics import mean
from statistics import mode

print("welcome to my game")  # welcome message


def start_game():
    random_number = random.randint(0, 10)
    print(random_number)
    guess = int(input("guess a number between 0 and 10. "))
    attempts = 0
    guess_list = [guess]

    if guess == random_number:
        print(f"That's correct! it only took you {attempts} attempts!")
        print(f"mean: N/A, median: N/A, mode: N/A")
        play_again = input("would you like to tray again? Y/N")
        play_again.lower()
        if play_again == "y":
            print("sure, lets get started")
            start_game()
        elif play_again == "n":
            print("thanks for playing!")
        else:
            print("please try again" )
    try:
        while int(guess) != random_number:
            if 0 < guess < random_number:
                guess = int(input(f"your guess of {guess} is lower than the number. Try again. "))
                guess_list.append(guess)
                attempts += 1
                print(f"here are your guesses so far: {guess_list}")
                continue
            elif random_number < guess < 11:
                guess = int(input(f"your guess of {guess} is higher than the number. Try again. "))
                guess_list.append(guess)
                attempts += 1
                print(f"here are your guesses so far: {guess_list}")
                continue
            else:
                raise ValueError
    except ValueError:
        guess = int(input("""Provide a whole number between "0" and "10".""" ))

    if guess == random_number:
        print(f"That's correct! it only took you {attempts} attempts!")
        guess_mean = float(mean(guess_list))
        guess_median = float(median(guess_list))
        guess_mode = mode(guess_list)
        print(f"mean: {guess_mean}, median: {guess_median}, mode: {guess_mode}")
        play_again = input("would you like to tray again? Y/N")
        play_again.lower()
        if play_again == "y":
            print("sure, lets get started")
            start_game()
        elif play_again == "n":
            print("thanks for playing!")







    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player. DONE
    2. Store a random number as the answer/solution. DONE
    3. Continuously prompt the player for a guess. DONE
      a. If the guess greater than the solution, display to the player "It's lower". DONE
      b. If the guess is less than the solution, display to the player "It's higher". DONE

    4. Once the guess is correct, stop looping, inform the user they "Got it" DONE
         and show how many attempts it took them to get the correct number. DONE
    5. Save their attempt number to a list. DONE
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list. DONE
    7. Ask the player if they want to play again. DONE

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


# Kick off the program by calling the start_game function.

start_game()