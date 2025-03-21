print("Kindly input two number and press enter")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sign= input("Enter sign: ")
match sign:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        print("Result:", num1 / num2 if num2 != 0 else "Error: Division by zero")
    case "%":
        print("Result:", num1 % num2 if num2 != 0 else "Error: Modulo by zero")
    case _:
        print("Invalid sign")