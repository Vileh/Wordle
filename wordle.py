import os
import random
import pandas as pd
import msvcrt
from readchar import readchar


al_data = pd.read_csv('allowed_words.txt')
pos_data = pd.read_csv('possible_words.txt')
allowed_data = al_data.values.tolist()
possible_data = pos_data.values.tolist()
al = [allowed_data[i][0] for i in range(len(allowed_data))]
pos = [possible_data[i][0] for i in range(len(possible_data))]
all_words = al + pos
alpha = 'abcdefghijklmnopqrstuvwxyz'
qwerty = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

os.system('color')


def check(guess, x):
    ret = [0, 0, 0, 0, 0]
    # 1-bull, 2-cow
    for i in range(5):
        for j in range(5):
            if guess[i] == x[j] and ret[i] != 1:
                if i == j:
                    ret[i] = 1
                else:
                    ret[i] = 2
    return ret


def inputs():
    tr = ''
    inp = ''
    while 1:
        ins = len(tr)

        print('\r| ', end="")
        for i in range(5):
            if i < ins:
                print(tr[i].capitalize(), end=" ")
            else:
                print('_', end=" ")
        
        print('\r| ', end="")
        if ins != 0:
            for i in range(ins):
                print(tr[i].capitalize(), end=" ")
        
        inp = msvcrt.getch()
        inp_let = str(inp)[2]
        let = 0
        for i in alpha:
            if inp_let == i:
                let = 1
        if let == 1 and len(tr)<5:
            tr += inp_let
        if inp == b'\r' and len(tr) == 5:
            for j in all_words:
                if tr == j:
                    return tr
            print("-Try another word-", end="")
        if inp == b'\x08':
            tr = tr[:-1]
            print(' '*18, end="")

def print_keyboard(keyboard):
    print()
    spaces = [6, 7, 8]
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
    x = pos[random.randrange(len(pos))]
    chck = [0, 0, 0, 0, 0, 0]
    keyboard = {f'{x}' : 0 for x in alpha}
    print('-'*32)
    print('|' + ' '*6 + 'Welcome to Wordle!' + ' '*6 +'|')
    print('|' + ' '*2 + 'Guess the word in 6 tries!' + ' '*2 + '|') 
    print('-'*32)
    for i in range(11):
        print('|' + ' '*30 + '|')
    print('-'*32)
    print_keyboard(keyboard)

    for i in range(6):
        if i == 0:
            print("\033[F"*12 , end="")
        guess = inputs()
        end = i
        chck[i] = check(guess.lower(), x)
        print('\r', end="")
        print('| ', end="")
        for j in range(5):
            if chck[i][j] == 0:
                print(guess[j].capitalize(), end=" ")
                keyboard[f'{guess[j]}'] = -1
            elif chck[i][j] == 1:
                print('\033[92m'+guess[j].capitalize()+'\033[0m', end=" ")
                keyboard[f'{guess[j]}'] = 1
            else:
                print('\033[93m' + guess[j].capitalize() + '\033[0m', end=" ")
                keyboard[f'{guess[j]}'] = 2

        print(' '*4 + f'Guess No.{i+1}' +' '*5 + '|', end="")
        print('                         ')

        print('\n'*(11-i), end="")
        print_keyboard(keyboard)
        print('\033[F'*(11 -i), end="")

        if chck[end] == [1, 1, 1, 1, 1]:
            break
    
    if chck[end] == [1, 1, 1, 1, 1]:
        print('\n|' + ' '*4 + 'Congrats, you got it!')
    else:
        print('\n|' + ' '*9 + 'Not quite :(')
    print('|' +' '*5 +'The word was: ' + x.capitalize())
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