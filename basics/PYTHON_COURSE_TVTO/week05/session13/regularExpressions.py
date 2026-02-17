full_name = input("Enter your full name: ")
print(full_name)
new_name = input("Enter a new name to replace your full name: ")
replaced_name = full_name.replace(full_name, new_name)
print(f"Updated name: {replaced_name}")

number_input = input("Enter a number: ")
clean_number = number_input.strip()
print(f"Cleaned number: {clean_number}")