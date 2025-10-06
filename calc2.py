# calculator of (division(d) ,mutiplycation(m) ,addition(a) ,subsration(s))
while True:
    print("simple calculator\n1.pick (D) to divide\n2.pick (M) to mutiply\n3.pick (A) to add\n4.pick (S) to subtract\nIf done type (X)")
    option = input("select operator: ").upper()
    if option == "X":
        print("Shut Down")
        break 
    num1 = float(input("select first number: "))
    num2 = float(input("select second number: "))
    if option == "D":
        if num2 == 0:
            print("math error")
        else:    
            print(f"result: {num1 / num2} ")
    elif option == "M":
        print(f"result: {num1 * num2} ")
    elif option == "A":
        print(f"result: {num1 + num2} ")
    elif option == "S":
        print(f"result: {num1 - num2} ")
    else:
        print("invalid number")
