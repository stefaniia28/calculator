def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operation = input('Enter operation (add, sub, mul, div): ')

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == 'add':
    print(f'Result: {add(num1, num2)}')
elif operation == 'sub':
    print(f'Result: {subtract(num1, num2)}')
elif operation == 'mul':
    print(f'Result: {multiply(num1, num2)}')
elif operation == 'div':
    print(f'Result: {divide(num1, num2)}')
