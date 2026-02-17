# Try to open and read a text file in the same folder as the script
print("...... Text File Viewer ......")

print("Checking if 'my_file.txt' exists in the same folder...\n" + "." * 60)

try:
    f = open("D:/projects/python_course_tvto/basics/week05/session12/my_file.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("The file does not exist.")
else:
    print("File content:")
    print(content)
finally:
    print("." * 60 , "\nProgram finished.")