# A program that asks for a name and says hello three times.

# This asks how many names they'd like to input.
amount = int(input("How many names do you wish to enter? "))
for variables in range(1,amount+1):
    name = input("{}. What is your name? ".format(variables))
    print("Hello", name)