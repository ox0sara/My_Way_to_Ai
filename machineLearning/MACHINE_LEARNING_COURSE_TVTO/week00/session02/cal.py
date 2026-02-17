# Get two numbers from user input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Perform basic arithmetic operations
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")

# Handle division by zero
if b != 0:
    print(f"Division: {a / b}")
else:
    print("Division by zero is not allowed.")
