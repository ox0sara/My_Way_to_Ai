# 🐍 Python Basics – Session  3

## ✅ What I Learned

### 🔁 Loop Structures in Python

Python has two main types of loops:

1. **`for` loop** – used to iterate over a sequence (like a list, string, or `range`)
2. **`while` loop** – repeats as long as a condition is true

---

## 🔹 Session 3: Loop Syntax and Basics

### 🔸 `for` Loop


for variable in sequence:
    # Code to repeat

```python
for i in range(1, 6):
    print(i)
```

- `range(n)` means numbers from `0` to `n-1`

#### 📌 Example: Loop over a list
```python
fruits = {"grape", "banana", "apple"}
for fruit in fruits:
    print(fruit)
```
### 🔸 `while` Loop
while condition code have to repeat
```python

x = 0
while x < 6:
    print(x)
    x += 1
```
⚠️ **Infinite loop warning:** If the condition is always true and the variable never changes, the loop runs forever.

---
### 🚦 Control Statements

#### 🔹 `break` – Exit the loop completely
```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
# Output: 1 2 3
```

#### 🔹 `continue` – Skip to the next iteration
```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```
#### 🔹 `pass` – Placeholder that does nothing
```python
for i in range(5):
    pass  # Code to be added later
```
---
## 🧪 Practice Exercises

### 1. Print numbers from 1 to 10 but skip number 7:
Use a `for` loop to print numbers from 1 to 10. When the loop reaches number 7, skip printing it using the `continue` statement.

### 2. Ask for numbers and print them as long as they are positive:
Use a `while` loop to keep asking the user for a number. If the number is positive, print it and ask again. If the number is zero or negative, end the program.

**How this program works:**

1. Gets a number from the user.
2. If the number is positive:
   - Prints the number
   - Asks for another number
3. If the number is zero or negative:
   - Loop ends
   - Prints the end message

