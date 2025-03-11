num1 = print(input("enter the value of the first number"))
operation = print(input("enter the operation(+,-,*,/,%)"))
num2 = print(input("enter the value of the second number"))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
elif operation == '%':
    print(num1 % num2)
else:
    print("enter a valid operation and/or values")