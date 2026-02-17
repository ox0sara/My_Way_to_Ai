# Homework
print("🧮 Welcome to the Calculator!")
print("-----------------------------")
print("Please choose an operation:")
print("  ➕  Enter '+' for Addition")
print("  ➖  Enter '-' for Subtraction")
print("  ✖️  Enter '*' for Multiplication")
print("  ➗  Enter '/' for Division")
print("-----------------------------")

cal = input("Your choice: ")

# Get numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# calculations
if cal == "+":
    print("✅ The result  is: ", x + y )
elif cal == "-":
    print("✅ The result  is: ", x - y)
elif cal == "*":
    print("✅ The result  is: ", x * y)
elif cal == "/":
    if y != 0:
        print("✅ The result  is: ", x / y)
    else:
        print("❌ Error: Division by zero is not allowed.")
else:
    print("❗ Invalid operation. Please restart and choose a valid option.")
