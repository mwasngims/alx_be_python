num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
    print("The result is", result)
elif operator == '-':
    result = num1 - num2
    print("The result is", result)
elif operator == '*':
    result = num1 * num2
    print("The result is", result)
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print("The result is", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")
