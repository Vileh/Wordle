import os
import random
import pandas as pd
import msvcrt


al_data = pd.read_csv('allowed_words.txt')
pos_data = pd.read_csv('possible_words.txt')
allowed_data = al_data.values.tolist()
possible_data = pos_data.values.tolist()
al = [allowed_data[i][0] for i in range(len(allowed_data))]
pos = [possible_data[i][0] for i in range(len(possible_data))]
all_words = al + pos
alpha = 'abcdefghigklmnopqrstuvwxyz'

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
        print('\r', end='')
        for i in range(5):
            print('_', end=" ")
        print('\r', end='')
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
            print("--Try another word--", end="")
        if inp == b'\x08':
            tr = tr[:-1]


def game():
    x = pos[random.randrange(len(pos))]
    chck = [0, 0, 0, 0, 0, 0]
    for i in range(6):
        guess = inputs()
        chck[i] = check(guess.lower(), x)
        print('\r', end="")
        for j in range(5):
            if chck[i][j] == 0:
                print(guess[j].capitalize(), end=" ")
            elif chck[i][j] == 1:
                print('\033[92m'+guess[j].capitalize()+'\033[0m', end=" ")
            else:
                print('\033[96m' + guess[j].capitalize() + '\033[0m', end=" ")
        print('                         ')
        if chck[i] == [1, 1, 1, 1, 1]:
            end = i
            break
    if chck[end] == [1, 1, 1, 1, 1]:
        print('Congrats, you got it!')
    else:
        print('Not quite :(')
    again = input('\n--Again?--(y/n)')
    if again == 'y':
        game()

game()