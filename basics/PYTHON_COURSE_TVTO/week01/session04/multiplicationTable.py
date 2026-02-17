# Multiplication Table (1 to 10)

print("\n Multiplication Table (1 to 10):\n")

for i in range(1, 11):  # Rows
    for j in range(1, 11):  # Columns
        print(i * j, end="\t")  # Print product with spacing
    print()  # Move to next line after each row
