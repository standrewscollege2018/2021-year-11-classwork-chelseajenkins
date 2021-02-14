#this code prints the game FizzBuzz

#This gets the users input
end_number=int(input("What number should it go up to? "))
fizz=int(input("What number do you want it to fizz on? "))
buzz=int(input("What number do you want it to buzz on? "))
for i in range(1,end_number+1):
    if i%fizz==0 and i%buzz==0:
        print("FizzBuzz")
    elif i%fizz==0:
        print("Fizz")
    elif i%buzz==0:
        print("Buzz")
    else:
        print(i)