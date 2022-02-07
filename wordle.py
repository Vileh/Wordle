import random
wordlist = ["great", "alone", "drift", "table", "kicks", "poems", "about", "night", "horse", "tipsy"]
raw_word = random.choice(wordlist)

n = "b"
list = ("a", "b", "c", "d")

def truf():
  if n == list[1]:
    return True

print(list[1])
truf()

def split(raw_word):
    return [char for char in raw_word]
split_word = split(raw_word)
print(split_word)

print("Enter a 5 letter word:")
guess = input()

def split(guess):
    return [char for char in guess]
split_guess = split(guess)
print(split_guess)
