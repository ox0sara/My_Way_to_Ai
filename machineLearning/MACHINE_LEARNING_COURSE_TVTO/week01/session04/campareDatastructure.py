# List example
print("\n Creating a list: " )
my_list = [1, 2, 3, 4]
print(" List created:", my_list, "\n" + "." * 50)

# Try to import numpy and handle missing module
print("\n Creating a NumPy array: ")
try:
    import numpy as np
    a = np.array([1, 2, 3, 4])
    print(" NumPy array created:", a,  "\n" + "." * 50)
except ModuleNotFoundError:
    print(" NumPy is not installed. Please run 'pip install numpy' and try again.\n" + "." * 50)

# Stack using list
print("\n Demonstrating stack using list: ")
stack = []
stack.append("A")
stack.append("B")
print(" Current stack:", stack)
print(" Popping top item:", stack.pop())
print(" Stack after pop:", stack, "\n" + "." * 50)

# Stack using deque
print("\n Demonstrating stack using deque...")
from collections import deque
stack = deque()
stack.append("X")
stack.append("Y")
print(" Current stack (deque):", list(stack))
print(" Popping top item (deque):", stack.pop())
print(" Stack after pop (deque):", list(stack))
