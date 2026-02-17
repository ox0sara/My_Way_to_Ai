print(
    "\nWelcome to the Geometry Calculator App!\n"
    + "You will be asked to enter the rectangle's name, length, and width.\n"
    + "The program will then calculate and display the area for you.\n"
)
print("_" * 80 + "\n")

# Define the base class called Shape
class Shape:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(" ✅ Name of the shape: ", self.name)

# Define a derived class called Rectangle that inherits from Shape
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Get inputs from users 
name = input("Enter the name of the shape : ")
print()

length = float(input(f"Enter the length of the {name}: "))
print()

width = float(input(f"Enter the width of the {name}: "))
print()

print("." *50 + "\n")
print("\n" + "Here you can see the results: \n")

rectan = Rectangle(name, length, width)
rectan.start()
print(" ✅ Area:", rectan.area())  