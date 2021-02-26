# This program demonstrates lists inside lists
# Called multi-dimensional arrays

people = [["Dr Evil", 45], ["Gru", 34], ["Emperor", 200]]

age_name = True
print("When done entering names enter end")
while age_name == True:
    person = []
    try:
        name = str(input("enter a name: "))

            print("Enter a valid name: ")
    except:
        print("Please enter a valid answer")
    if name == "end" or name == "end":
        age_name = False
    else:
        person.append(name)
        person.append(int(input("Enter an age: ")))
        people.append(person)
for i in range(len(people)):
    print("{} is {} years old".format(people[i][0], people[i][1]))