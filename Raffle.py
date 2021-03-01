# This is a program that takes in names and randomises a winner for a raffle.

import random
ask_name = True
prize_value = True
names = []

print("Hello, this code picks the winner of a raffle")
prize = input("What is the prize? ")
while prize_value == True:
    try:
        value = int(input("How much is the prize worth? $"))
        prize_value = False
    except:
        print("Enter a valid prize amount")
print("When you're finished entering names type end")
while ask_name == True:
    name = input("Enter a name: ")
    if name == "end" or name == "End":
        if len(names) == 0:
            print("no one has entered the raffle")

        else:
            ask_name = False
            winner = random.randint(1, len(names)-1)
            print(names[winner],"has won the {} worth ${}".format(prize, value))
    else:
        names.append(name)