num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")
match operator:
    case _ if operator == "+":
        sum = num1 + num2
        print("The result is", sum, ".")
    case _ if operator == "-":
        subtract = num1 - num2
        print("The result is", subtract, ".")
    case _ if operator == "*":
        product = num1 * num2
        print("The result is", product, ".")
    case _ if operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            division = num1 / num2
            print("The result is", division, ".")