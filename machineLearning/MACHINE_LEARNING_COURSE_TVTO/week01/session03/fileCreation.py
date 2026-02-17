# Create a file and write multiple lines into it
with open("example.txt", "w") as file:
    file.write("Hello world\n")
    file.write("This is a text file.\n")
    file.write("I am learning Python.\n")

# Read and display the content of the file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
