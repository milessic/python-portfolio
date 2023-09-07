# Miłosz Jura milessic 2023
# uses Free Dictionary API
# saves last 10 searches
# https://api.dictionaryapi.dev/api/v2/entries/en/digital

import requests
import os


def clear():
    r"""clears console depending of user's OS"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_history():
    r"""prints last 10 searches items."""
    try:
        file = open("history.txt", "r")
        history_items = file.readlines()
    except FileNotFoundError:
        history_items = []
    print("===Last 10 searches:")
    for item in range (10):
        try:
            print(f"-- {history_items[len(history_items)-item-1][:-1]}")
        except IndexError:
            print("- ..")


def save_to_history(item):
    r"""saves provided item to the history file"""
    file = open("history.txt.", "a")
    file.write(f"{item}\n")
    file.close()


def print_info(item):
    r"""prints info of provided item in case of 200,
            in case of 404 informs user that word was not found
            in case of other status codes informs that word couldn't be reached

            if status was 200 also saves the item to the history
    """

    clear()
    print(f"=== Checking word '{item}'")
    print("-please wait...")

    resp = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{item}")
    if resp.status_code == 200:
        body = resp.json()
        body = body[0]
        body = body['meanings'][0]
        clear()
        print(f"=== Checking word '{item}'")
        speech_part = body['partOfSpeech']
        definition = body['definitions'][0]['definition']
        character_limit = 80
        print(f"--Speech part:\n{speech_part}")
        print(f"--Definition:")

        for line in range(len(definition)//character_limit+1):
            if line == 0:
                print(definition[:character_limit])
            else:
                print(definition[character_limit*line:character_limit*line+character_limit])
        save_to_history(item)
    elif resp.status_code == 404:
        clear()
        print(f"=== Checking word '{item}'")
        print("No word found, please check spelling...")
    else:
        clear()
        print(f"=== Checking word '{item}'")
        print(f"[{resp.status_code}] Cannot access server, please try again...")
    input("---\nPress ENTER to exit ...")


while True:
    clear()
    print("===English Dictionary program.")
    print_history()
    try:
        user_input = input("===Type word to check:\n-Ctrl+C to exit\n>>> ")
        print_info(user_input)
    except KeyboardInterrupt:
        try:
            clear()
            input("Thank you for using english_dictionary press ENTER to close... ")
        except KeyboardInterrupt:
            pass
        finally:
            break
