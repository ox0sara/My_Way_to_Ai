print("\n" + "Welcome to the Student ID Management System!\n")
print("." *50 + "\n")


# Initial list of student IDs 
students_id = [100, 102, 103, 104, 105, 105, 106, 107, 108, 108]
print("Initial list of student IDs:")
print(students_id)
print()

# Remove the last student ID using pop()
students_id.pop()
print("After removing the last ID (pop):")
print(students_id)
print()

# Add a new student ID at the end using append()
students_id.append(109)
print("After adding a new student ID (109) using append:")
print(students_id)
print()

# Remove the first 105 ID using remove()
students_id.remove(105)
print("After removing the first 105 ID:")
print(students_id)
print()

# Change the first student ID from 100 to 101
students_id[0] = 101
print("After changing the first student ID to 101:")
print(students_id)
print()

# Access and print the fifth student ID (index 4)
print("The fifth student ID in the list is:")
print(students_id[4])
