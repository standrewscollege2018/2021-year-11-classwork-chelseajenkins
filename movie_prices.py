#This program prints movie ticket costs based on their age and whether they're a student.

age = int(input("Enter your age "))
if age <5:
    print("free")
elif age >=18:
    print("$12")
elif age >=13:
    print("$9")
elif age >=5:
    print("$7")
