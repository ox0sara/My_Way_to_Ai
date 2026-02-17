print("\n" + "Welcome to the Geometry Calculator App!\n" 
      + 
      "In this application you will asked to put two numbers as inputs to calculate the area and preimeter of a rectangle\n")
print("_" *80 + "\n")

# Rectangle class 
class Ranctangle: 
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    # Calculate the area 
    def area(self):
        return self.length * self.width
    # Calculate the preimeter
    def perimeter(self):
        return 2 * (self.length + self.width)

# Get inputs from users 
length = float(input("Enter the length of the rectangle: "))
print()

width = float(input("Enter the width of the rectangle: "))
print()

print("." *50 + "\n")
print("\n" + "Here you can see the results: \n")

# Create a object from class
myRectangle = Ranctangle(length, width)

# Print the results
print(f"Area of the rectangle: {myRectangle.area()}")
print()

print(f"Perimeter of the rectangle: {myRectangle.perimeter()}")
print()