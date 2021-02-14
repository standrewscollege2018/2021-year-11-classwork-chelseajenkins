#This code asks for a name until you enter the right name.

loop = True
while loop == True:
    name = input("Enter your name ")
    if name == "kotori" or name == "Kotori":
        loop = False
    else:
        print("wrong name")
print("Hi Kotori")