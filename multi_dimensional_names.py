# This program demonstrates lists inside lists.
# Called multi-dimensional arrays.

people = [["Dr Evil", 45], ["Gru", 34], ["Emperor", 200]]

age_name = True
print("When done entering names enter end")
while age_name == True:
# This gets the persons name.
    age_loop = True
    person = []
    name = str(input("enter a name: "))
# This code makes sure the code can end.
    if name == "end" or name == "End":
        age_name = False
    else:
        person.append(name)
# This gets the persons age and checks it.
        while age_loop == True:
            try:
                age = (int(input("Enter an age: ")))
                person.append(age)
                age_loop = False
            except:
                print("enter a valid age")
            people.append(person)
# This prints the new list of names.
for i in range(len(people)):
    print("{} is {} years old".format(people[i][0], people[i][1]))