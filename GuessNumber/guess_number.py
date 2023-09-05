# guess the number game
# Milosz Jura milessic
# 09.2023

from random import randint
import os
from time import sleep

long_line = "================================================="
user_score = 0

# this class helps to exit the program from 2 level loop
class GetOutOfLoop( Exception ):
    pass


# oppening highscore file, if not found setting highscore as 0
while True:
    try:
        file = open("highscore", "r")
        highscore = file.readline()
        file.close()
        break
    except FileNotFoundError:
        highscore = 0
        break
    except PermissionError:
        input("Problem loading highscore...\nPlease try again, click ENTER to continue....\n>>> ")


# saving highscore if it's higher than one in highscore file, if file doens't exist, create one.
def save_highscore(t_score):
    while True:
        try:
            t_file = open("highscore", "r")
            t_highscore = t_file.readline()
            if t_score > int(t_highscore):
                t_file.close()
                t_file = open("highscore","w")
                print(f"New highscore! {t_score}")
                t_file.write(f"{t_score}")
                t_highscore = t_score
            break
        except FileNotFoundError:
            t_highscore = t_score
            t_file = open("highscore", "w")
            print(f"New highscore! {t_score}")
            t_file.write(f"{t_score}")
            break
        finally:
            t_file.close()
    return t_highscore


# clears conosle, support for windows and unix based systems
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# prints HUD at the top with score and highscore
def print_hud(t_score, t_highscore):
    clear_console()
    print(f"{long_line}\n=== your score: {t_score}\ttop score: {t_highscore}\n{long_line}")


# loop where the game takes place , in case of EOFError or KeyboardInterrupt, close the game.
while True:
    rand = randint(0,10)
    try:
        while True:
            try:
                print_hud(user_score, highscore)
                user_input = int(input("Guess the number from 0 to 10\n>>> "))
                break
            except ValueError:
                print("Sorry, only int numbers are supported!")
                input("click ENTER to proceed...")
            except (EOFError, KeyboardInterrupt):
                raise GetOutOfLoop
    except GetOutOfLoop:
        break
    if user_input == rand:
        user_score += 1
        print(f"Point added, the misterious number was {rand}")
        sleep(2)
        print_hud(user_score, highscore)
        #input()
        highscore = save_highscore(user_score)
    else:
        print(f"You didn't guess! the misterious number was {rand}")
        sleep(2)
input("\n=== milessic 2023===\nThank you for playing my guess the number game!\nclick ENTER to exit... ")