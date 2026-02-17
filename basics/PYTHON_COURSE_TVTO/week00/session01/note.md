# 🗓️ First Session – Getting Started with Python
In our first session, we got familiar with the basics of Python programming.

---

## 📁 File Naming Rules in Python

Before creating any Python file, there are some basic naming rules you should follow:

- Use **letters** to start your file name.
- You can include **numbers**, but **no spaces or special characters** (e.g., `@`, `$`, `%`, etc.).
- It's best practice to use **underscores (`_`)** instead of spaces.
- All Python files should end with the **`.py` extension**.

**✅ Correct examples:**
- `my_script.py`
- `hello_world.py`

**❌ Avoid:**
- `123file.py` (starts with a number)
- `my file.py` (contains a space)

---

## ✅ What We Did This Week

We completed several hands-on tasks to get comfortable with our environment:

1. 🔧 Installed **PyCharm** (our code editor of choice).
2. 📂 Created a new folder named after ourselves (e.g., `sara_python`).
3. 🗂️ Started a new Python **project** inside the folder.
4. 📄 Created our very first Python file: `hello_world.py`.
5. 🖨️ Wrote our first line of code.
6. ▶️ Ran the file to view the output in the terminal.


---

## 🧪 Mini Test: "Hello World"
```python
print("Hello, world!") //output: Hello, world!
```
---
## 👨‍💻 First Project: User Input

We learned how to get input from the user and display it back:

```python
str = input("Put your name: ")
print(str) //output: yourname
```
---
## 👩‍💻 Second Project: Welcome the User

In this project, I created a friendly script that welcomes the user, collects their name and family name, and prints a personalized message with nice formatting and emojis.

```python
# Welcome the user 
print("\n" + "👋 Welcome! Let's get to know you.")
print("." * 40 + "\n")

# Get user input
name = input("📝 Please enter your first name: ")
family = input("📝 Please enter your last name: ")

# Print a separator
print("\n" + "=" * 40)

# Display the full name nicely
print("\n✅ Nice to meet you: " + name + " " + family) //output: Nice to meet you: Sara Dev
```