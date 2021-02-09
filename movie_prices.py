#This program prints movie ticket costs based on their age and whether they're a student.

age = int(input("Enter your age "))
if age <5:
    print("free")
elif age <13:
    print("$7")
else:
    student = str(input("Are you a student? (yes/no) "))
    if student == "yes":
        print("$8")
    elif age <18:
        print("$9")
    elif age <110:
        print("$12")
    else:
        print("That's not a viable age")
