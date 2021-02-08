# A code that recommends a parecetamol dose based on age and weight.


MAX_AGE = 12
MIN_AGE = 0
MIN_WEIGHT = 0
age = int(input("Enter your age "))

if age > MAX_AGE :
    print("It's recommended you take 2 500mg tablets")
elif age <=0:
    print("That age is impossible")
elif age >MIN_AGE:
    weight = int(input("Enter your weight "))
    print("The recommended dosage is {}mg".format(weight*10))