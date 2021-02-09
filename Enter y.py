#This program is a loop that will end when the correct answer is entered.

loop = True

correct = str(input("Enter y "))
if correct == "y":
    loop = False
while loop == True:
    correct = str(input("ENTER y "))
    if correct == "y":
        loop = False
if correct == "y":
    print("good job you have entered y ")