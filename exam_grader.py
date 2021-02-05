#This is a program that determines what grade you get fom an exam mark.

loop = True
CUT_A = 90
CUT_B = 70
CUT_C = 50

#This code ask for their mark
mark = int(input("Enter your exam mark "))
if mark <=100 and mark >=0:
    loop = False

#This code sets a boundary of the possible exam mark.
while loop == True:
    mark = int(input("Enter a valid exam mark "))
    if mark <=100 and mark >=0:
        loop = False
#This code sets determines which grade they'll get.
if mark >CUT_A:
    print("You have got an A")
elif mark >CUT_B:
    print("You have got a B")
elif mark >CUT_C:
    print("You have got a C")
elif mark <CUT_C:
    print("You have failed")
else:
    print("Fail")