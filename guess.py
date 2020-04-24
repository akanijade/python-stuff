import random

hidden = random.randrange(1, 10)

guess = int(input("Guess my hidden number from 1 to 10! \n You only have 3 chances! "))

for i in range (0, 2):
    if guess != hidden:
        if guess < hidden:
            guess = int(input("Too Low "))
            i += 1
        else:
            guess = int(input("Too high "))
            i += 1
    else:
        break

if guess != hidden:
    print("Game over")
else:
    print("Correct")
