import time
import sys
import re

name = input("What is your name? ")

print("Hello " + name + ", Welcome to hangman!")

print('\n')

time.sleep(0.5)

print("Start your guess..")

time.sleep(0.5)

from random_word import RandomWords
r = RandomWords()
#if word has multiple symbol??

word = "bingo-test"
test = True
sym = re.compile(r"[^A-Za-z]")
while sym.search(word) is not None:
   # if (sym.search(word) == True):
    word = r.get_random_word()
   # print(word)
   # else:
   #if (sym.search(word) == false):
        #print(False)

#print(word)

guess = ''

turns = 10
#each turn,  user can input more than one char
while turns > 0:
    failed = 0
    for char in word:
        if char in guess:
            print(char + " ", end = '')
        else:
            print('_ ', end = '')
            failed += 1
    if failed == 0:
        print("You won")
        break
    guessNew = input("\nGuess a letter: ")
    guess += guessNew
    if guessNew not in word:
        turns -= 1
        print("Wrong letter, " + str(turns) + "turns left")
        if turns == 0:
            print("You lose")
        
