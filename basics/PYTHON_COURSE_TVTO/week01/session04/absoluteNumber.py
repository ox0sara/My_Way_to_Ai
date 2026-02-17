print("This program takes a number from you and prints its absolute value.")
print("-------------------------------------------------------------------------------------------")

number = int(input("Please enter a number: "))

if number < 0:
    number = -number  # If the number is negative, multiply by -1
    print(number)
else: 
    print(number)