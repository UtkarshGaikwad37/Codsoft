def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operation (+, -, *, /): ")

if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = sub(num1, num2)
elif operator == '*':
    result = mul(num1, num2)
elif operator == '/':
    result = div(num1, num2)
else:
    result = "Error: Invalid operator."

print(f"Result: {result}")
