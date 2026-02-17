# 🐍 Python Basics – Session 4

## ✅ What I Learned

### 🔁 Nested Loops & Advanced `print()` Usage

This session focused on using **nested loops** for complex structures (like multiplication tables) and mastering the output format using Python’s `print()` parameters.

---

## 🔹 Session 4: Nested Loops & `print()` Control

### 🔸 Nested Loops

A **nested loop** means placing one loop inside another. These are useful for working with:

- Multiplication tables
- Matrices
- Repeating patterns

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
```

### 🖨️ Customizing `print()` Output

By default, Python’s `print()` adds a **space** between items and moves to the **next line** after each call. You can control this using `sep` and `end`.

#### 🔹 `sep` – Custom Separator Between Items

```python
print("hello", "python", sep=" ---- ")
# Output: hello ---- python
```

#### 🔹 `end` – Prevent Line Breaks
``` python

for i in range(5):
    print(i, end=" ")
# Output: 0 1 2 3 4
```

#### 🔹 `Multiline Text` Using Triple Quotes
You can print multi-line strings with triple quotes """ or '''.

``` python
print("""Hello,
This is a
multiline message.""")
```

## 🧪 Practice Exercises
1. Print the sum of all two-digit even numbers
   - Use a loop and a condition to find even numbers between `10` and `99`, then add them together.

2. Get a number from the user and print its absolute value
   - Use `input()` and `a conditional` to print the positive version of any number.

3. Create a `multiplication table` using nested loops
   - Use two for loops to generate a `10x10` multiplication table.