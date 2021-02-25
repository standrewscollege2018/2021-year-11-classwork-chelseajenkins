# A guessing game between 1 & 10

import random
num = random.randint(1,100)
loop = True
check_number = True
record = 0
while loop == True:
    # This asks for a guess and if its not a number it excepts it
    try:
        their_guess = int(input("Guess a number between 1 & 100: "))
        check_number = False
    except:
        print("Please enter an integer ")
    if their_guess <=0 or their_guess >=101:
        print("Read the question carefully")
    elif their_guess == num:
        print("That is correct!")
        loop = False
    elif their_guess <num:
        print("The number is bigger than", their_guess)
    elif their_guess >num:
            print("The number is smaller than", their_guess)
    record = record+1
    print(record)
