# This program calculates how much a person should be fined based on speeding.
criminals = ["Helga Norman", "Zach Conroy", "John Smith"]
fines = []
speed_travelled = True
speed_limit_loop = True
speeder_loop = True
while speeder_loop == True:
    speeders_name = input("name: ")
    speed_travelled = True
    speed_limit_loop = True
    if speeders_name in criminals:
        print("Arrest them")
        speeder_loop = False
    else:
        while speed_limit_loop == True:
            try:
                speed_limit = int(input("What is the speed limit? "))
                if speed_limit <1:
                    print("This is not a possible speed limit")
                else:
                    speed_limit_loop = False
            except:
                print("Enter a valid speed limit: ")
        while speed_travelled == True:
            try:
                speed = int(input("What speed were they travelling at?: "))
                speed_travelled = False
            except:
                print("Enter a valid speed: ")
        if speed <= speed_limit:
            print(speeders_name, "was not speeding")
        else:
            over_limit = (speed - speed_limit)
            print(speeders_name, "was travelling", over_limit, "km over the speed limit and is fined money")
