import random

while True:
    try:
        numberofdice = int(input("Number of Dice "))
    except ValueError:
        print("please enter correct Input")
        continue
    choice = input("Roll the Dice.(Y/N)").upper()
    if choice == "Y":
        dice = [random.randint(1, 6) for i in range(numberofdice)]
        print(f"({dice})")
    elif choice == "N":
        print("Thanks for playing")
        break
    else:
        print("Wrong input")
