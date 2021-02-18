#A guessing game between 1 & 10

import random
num = random.randint(1,100)
loop = True
another_loop = True
while loop == True:
    their_guess = int(input("Guess a number between 1 & 100: "))
    if their_guess <=100 and their_guess >=0:
        another_loop = False
        if their_guess == num:
            print("That is correct!")
            loop = False
        elif their_guess <num:
            print("The number is bigger than", their_guess)
            print()
        elif their_guess >num:
            print("The number is smaller than", their_guess)
    else:
        while another_loop == True:
            their_guess = int(input("Guess a number BETWEEN 1 & 100: "))
            if their_guess <= 100 and their_guess >= 1:
                another_loop = False