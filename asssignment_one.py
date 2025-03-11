// Create a simple Python program that asks the user to input two numbers and 
// a mathematical operation (addition, subtraction, multiplication, or division).
// Perform the operation based on the user's input and print the result.


num1 = print(input("enter the value of first number"))
operation = print("enter the opetion ")
num2 = print(input("enter the value of second number"))

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print("enter a valid operand")

