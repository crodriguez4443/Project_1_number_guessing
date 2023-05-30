import random as rn
#generates random integer between 0 and 10

# print(ran_num)

print("#### WELCOME TO THE GAME ###\n\n")
highscores = []

def guessing_game():
    counter = 0
    ran_num = rn.randint(0,10)
    while True:
        try:
            guess = int(input("Guess the random number:\n"))
            counter += 1
            print(f"the counter is {counter}")
            if guess == ran_num:
                highscores.append(counter)
                print("###YOU WON!!!###\n")
                print("It took you {} tries to guess.\n\n".format(counter))
                print(f"the high score was {min(highscores)}")
                break
            elif guess < 0 or guess > 10:
                raise ValueError("Ooops! That didn't work. Guess a number between 0 and 10")
            elif 0 <= guess < 10 and guess < ran_num:
                print("guess higher")
            elif 0 <= guess >= 10 and guess > ran_num:
                print("guess lower")
        except ValueError:
            print("try a number between 0 and 10")
    play_again()

def play_again():               
    while True:
        try:
            replay = input("would you like to play again Yes or No? ")
            if replay.lower() == "yes":
                guessing_game()
                break
            elif replay.lower() == "no":
                print("Thanks for playing!")
                break
            else:
                print("give a yes or no response\n")
        except ValueError as er:
            print(f"{er} oops that didn't work. tray again")

guessing_game()