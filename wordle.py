import os
import random
import pandas as pd
import msvcrt

# Setting up the possible words
allowed_data = pd.read_csv('allowed_words.txt').values.tolist()
possible_data = pd.read_csv('possible_words.txt').values.tolist()
al = [allowed_data[i][0] for i in range(len(allowed_data))]
pos = [possible_data[i][0] for i in range(len(possible_data))]
all_words = al + pos
alpha = 'abcdefghijklmnopqrstuvwxyz'

# Characters for keyboard
qwerty = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

# Set up coloured text in the terminal
os.system('color')


def check(guess, x):
    ret = [0, 0, 0, 0, 0]
    # 1-exact, 2-wrong pos, 0-wrong
    for i in range(5):
        for j in range(5):
            if guess[i] == x[j] and ret[i] != 1:
                if i == j:
                    ret[i] = 1
                else:
                    ret[i] = 2
    return ret


def inputs():
    to_try = ''
    while 1:
        num_letters = len(to_try)

        # Print the input line
        print('\r| ', end="")
        for i in range(5):
            if i < num_letters:
                print(to_try[i].capitalize(), end=" ")
            else:
                print('_', end=" ")
        
        # I'm not sure why the code even works, but it does
        print('\r| ', end="")
        if num_letters != 0:
            for i in range(num_letters):
                print(to_try[i].capitalize(), end=" ")
        
        input_raw = msvcrt.getch()
        input = str(input_raw)[2]

        # Check if input is allowed
        allow = 0
        for i in alpha:
            if input == i:
                allow = 1

        # Append to try if allowed
        if allow == 1 and len(to_try)<5:
            to_try += input

        # Check if input is enter
        if input_raw == b'\r' and len(to_try) == 5:
            for j in all_words:
                if to_try == j:
                    return to_try
            print("-Try another word-", end="")
        
        # Check if input is backspace
        if input_raw == b'\x08':
            to_try = to_try[:-1]
            print(' '*18, end="")

def print_keyboard(keyboard):
    print()
    spaces = [6, 7, 9]
    for i in range(3):
        print(' '*spaces[i], end="")
        for j in qwerty[i]:
            if keyboard[j] == 0:
                print(j, end=" ")
            elif keyboard[j] == 1:
                print('\033[92m'+j+'\033[0m', end=" ")
            elif keyboard[j] == -1:
                print('\033[91m'+j+'\033[0m', end=" ")
            else:
                print('\033[93m' + j + '\033[0m', end=" ")
        print()
    print("\033[F"*4 , end="")


def game():
    word_to_guess = pos[random.randrange(len(pos))]
    checks = [0, 0, 0, 0, 0, 0]
    keyboard = {f'{x}' : 0 for x in alpha}

    # Print the border and the keyboard
    print('-'*32)
    print('|' + ' '*6 + 'Welcome to Wordle!' + ' '*6 +'|')
    print('|' + ' '*2 + 'Guess the word in 6 tries!' + ' '*2 + '|') 
    print('-'*32)
    for i in range(11):
        print('|' + ' '*30 + '|')
    print('-'*32)
    print_keyboard(keyboard)

    for i in range(6):
        # Move cursor up if first guess
        if i == 0:
            print("\033[F"*12 , end="")
        
        # Get the guess and check it
        guess = inputs()
        current_guess = i
        checks[i] = check(guess.lower(), word_to_guess)

        # Print the guess with colours
        print('\r| ', end="")
        for j in range(5):
            if checks[i][j] == 0:
                print(guess[j].capitalize(), end=" ")
                keyboard[f'{guess[j]}'] = -1
            elif checks[i][j] == 1:
                print('\033[92m'+guess[j].capitalize()+'\033[0m', end=" ")
                keyboard[f'{guess[j]}'] = 1
            else:
                print('\033[93m' + guess[j].capitalize() + '\033[0m', end=" ")
                keyboard[f'{guess[j]}'] = 2

        # Print necessary elements
        print(' '*4 + f'Guess No.{i+1}' +' '*5 + '|', end="")
        print('                         ')
        print('\n'*(11-i), end="")
        print_keyboard(keyboard)
        print('\033[F'*(11 -i), end="")

        # Check if the word is guessed
        if checks[current_guess] == [1, 1, 1, 1, 1]:
            break
    
    # Print the result
    if checks[current_guess] == [1, 1, 1, 1, 1]:
        print('\n|' + ' '*4 + 'Congrats, you got it!')
    else:
        print('\n|' + ' '*9 + 'Not quite :(')
    print('|' +' '*5 +'The word was: ' + word_to_guess.capitalize())

    # Ask if the user wants to play again
    print('\n|' + ' '*7 + '--Again?--(y/n)', end="")
    while True:
        again = str(msvcrt.getch())[2]
        if again == 'y':
            os.system('cls')
            game()
            break
        elif again == 'n':
            print('\n'* 4)
            break
        else:
            again = msvcrt.getch()

game()