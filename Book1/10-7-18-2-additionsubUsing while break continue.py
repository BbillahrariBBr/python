terminatet_program = False
while not terminatet_program:
    number1 = input("Please Enter a Number:")
    number1 = int(number1)
    number2 = input("Please Enter a Number:")
    number2 = int(number2)

    while True:
        operation = input("Please enter add/sub/mul/div or quit to exit: ")

        if operation == "quit":
            terminatet_program = True
            break
    
        if operation not in ["add", "sub", "mul" , "div"]:
            print("Unknown operation!")
            continue

        if operation == "add":
            print(number1, " + ", number2, " = ",number1 +number2)
            break
        if operation == "sub":
            print(number1, " - ", number2, " = ", number1-number2)
            break
        if operation == "mul":
            print(number1, " x ", number2, " = ", number1*number2)
            break
        if operation == "div":
            print(number1, " / ", number2, " = ", number1/number2)
            break
