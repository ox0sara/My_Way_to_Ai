print( "\n","This program calculates the sum of all even two-digit numbers (from 10 to 99).", "\n")
print("------------------------------------------------------------------------------")


total = 0

for number in range(10, 100):
    if number % 2 == 0:
        print(number, end="-")
        total += number

print("\n", "-----------------------------------------------------------------------------")
print("\n", "The sum of all even two-digit numbers is:", total, "\n")
