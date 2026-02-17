print("This program will keep printing the numbers you enter as long as they are positive.")
print("-----------------------------------------------------------------------------------")

number = int(input("Please enter a number: "))

while number > 0:
    print("You entered a positive number:", number)
    number = int(input("Please enter another number: "))

print("You entered zero or a negative number. Program ended.")
