import requests
import os
import Hangman

RED = '\033[31m'
RESET = '\033[0m'
whitesspace = "\n" * 50

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)

    if response.status_code == 200:
        word = response.json()[0]
        return word
    else:
        raise Exception("Failed to fetch word")
    
def user_input():
    while True:
        user_word = input("Enter a word (at least 3 letters): ").strip()
        if len(user_word) >= 3 and user_word.isalpha():
            print(whitesspace)
            return user_word
        else:
            print("Invalid input. Please enter a valid word with at least 3 letters.")

def main(input_word):
    correct = False
    word = input_word.title()
    reaveled = ['_'] * len(word)
    incorrect = []

    while len(incorrect) < 11 and '_' in reaveled:
        os.system('cls')
        print(Hangman.ascii[len(incorrect)])

        print("Current word: " + ' '.join(reaveled))
        for i in incorrect:
            print(f"Incorrect guesses: {', '.join(incorrect).upper()}")
            break

        print(f"Attempts remaining: {11 - len(incorrect)}")

        if 'error' in locals():
            print(RED + error + RESET)
            del error

        print()


        guess = input("Guess a letter/word: ").strip().lower()

        if guess.isalpha() and len(guess) == len(word):
            if guess.lower() == word.lower():
                reaveled = list(word)
                print(Hangman.ascii[12])
                print(f"Congratulations! You guessed the word: {word}")
                input("Press Enter to continue...")
            elif guess != word:
                incorrect.append(guess)
                print(f"{RED}Incorrect guess.{RESET}")

        elif guess.isalpha() and len(guess) == 1:
            if guess in incorrect or guess.upper() in reaveled:
                error = ("You have already guessed that letter. Try again.")
                continue
            
            correct = False

            for i, letter in enumerate(word.lower()):
                if letter == guess:
                    reaveled[i] = guess.upper()
                    correct = True

            if correct == False:
                incorrect.append(guess)
                        
            correct == False
            print("Current word: " + ' '.join(reaveled))
        else:
            error = ("Invalid guess. Please enter a single letter.")
    
    if len(incorrect) == 11:
        print(Hangman.ascii[13])
        print(f"You lost! The word was: {word}")
        input("Press Enter to continue...")

    elif '_' not in reaveled:
        print(Hangman.ascii[12])
        print(f"Congratulations! You guessed the word: {word}")
        input("Press Enter to continue...")
    else:
        error = ("Error occurred.")

        
        

while True:
    print(whitesspace)
    print(Hangman.ascii[11])
    game_mode = input("Choose game mode - '1' for random word, '2' for user-defined word: ").strip()
    if game_mode == '1':
        secret_word = get_random_word()
        #print(f"Random word selected: {secret_word}")
        main(secret_word)

    elif game_mode == '2':
        secret_word = user_input()
        #print(f"User-defined word accepted: {secret_word}")
        main(secret_word)
    else:
        print("Invalid game mode selected.")

