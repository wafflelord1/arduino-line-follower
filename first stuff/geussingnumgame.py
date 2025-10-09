import random
answer= random.randint(1,10)
while True:
    try:
        number= int(input("geuss the number between 1 and 10: "))

        if number> answer:
            print("too high")
        elif number < answer:
            print("too low")
        else:
            print("correct answer")
            break
    except ValueError:
        print("select numder in range")

    
