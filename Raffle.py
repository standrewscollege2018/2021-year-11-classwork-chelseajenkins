# This is a program that takes in names and randomises a winner for a raffle.

import random
ask_name = True
names = []

print("Hello this code picks the winner of a raffle")
prize = input("What is the prize? ")
value = int(input("How much is the prize worth? $"))
print("When you're finished entering names type end")
while ask_name == True:
    name = input("Enter a name: ")
    if name == "end" or name == "End":
        ask_name = False
    else:
        names.append(name)
winner = random.randint(0, len(names)-1)
print(names[winner],"has won the {} worth ${}".format(prize, value))