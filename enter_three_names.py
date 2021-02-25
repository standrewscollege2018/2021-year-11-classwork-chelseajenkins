# This program takes three names and prints them in a list

# names list will store entered names
names = []
# This loops it three times
for i in range(3):
    name = input("Enter a name ".format(i))
    names.append(name)
for i in range(len(names)):
    print(i+1, names[i])