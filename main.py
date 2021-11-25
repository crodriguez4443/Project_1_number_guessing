"""
Project 1 - Number Guessing Game
--------------------------------
"""
import random
from statistics import median
from statistics import mean
from statistics import mode

print("welcome message")  # generic welcome message


def start_game():
    random_number = random.randint(0, 10)
    print(random_number)
    guess = int(input("guess a number between 0 and 10. "))
    while guess != random_number:
        attempts = 0
        guess_list = []
        if guess < random_number:
            guess = int(input(f"your guess of {guess} is lower than the number. Try again. "))
            guess_list.append(attempts)
            print(f"here are your guesses so far: {guess_list}")
            continue
        elif guess > random_number:
            guess = int(input(f"your guess of {guess} is higher than the number. Try again. "))
            guess_list.append(guess)
            continue
        else:
            print(f"That's correct! it only took you {attempts} attempts!")
            mean_guess = mean(guess_list)
            median_guess = median(guess_list)
            mode_guess = mode(guess_list)
            print(f"mean: {mean_guess}, median: {median_guess}, mode: {mode_guess}")
            play_again = input("would you like to tray again? Y/N")
            play_again.lower()
            if play_again == "y":
                print("sure, lets get started")
                break
            elif play_again == "n":
                print("thanks for playing!")
                break
            else:
                continue









    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player. DONE
    2. Store a random number as the answer/solution. DONE
    3. Continuously prompt the player for a guess. DONE
      a. If the guess greater than the solution, display to the player "It's lower". DONE
      b. If the guess is less than the solution, display to the player "It's higher". DONE

    4. Once the guess is correct, stop looping, inform the user they "Got it" DONE
         and show how many attempts it took them to get the correct number.
    5. Save their attempt number to a list.
    6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.
    7. Ask the player if they want to play again.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


# Kick off the program by calling the start_game function.

start_game()