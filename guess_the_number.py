#A guessing game between 1 & 10

import random
num = random.randint(1,10)
loop = True
while loop == True:
    their_guess = int(input("Guess a number between 1 & 10: "))
    if their_guess >10 or their_guess <1:
        their_guess = int(input("Guess a number BETWEEN 1 and 10: "))
        if their_guess == num:
            print("That is correct!")
            loop = False
    elif their_guess == num:
        print("That is correct!")
        loop = False
    else:
        print("That's the wrong number")

