print("This program prints numbers from 1 to 10, but it skips the number 7.")
print("-----------------------------------------------------------------------")

i = 1
while i <= 10:
    if i == 7:
        i += 1
        continue  # Skip printing when i is 7
    print( i)
    i += 1