# A guessing game between 1 & 10

import random
num = random.randint(1,100)
loop = True
while loop == True:
    their_guess = int(input("Guess a number between 1 & 100: "))
    if their_guess == num:
        print("That is correct!")
        loop = False
    elif their_guess <num:
        print("The number is bigger than", their_guess)
    elif their_guess >num:
            print("The number is smaller than", their_guess)