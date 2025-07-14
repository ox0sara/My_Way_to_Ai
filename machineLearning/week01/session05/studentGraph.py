import matplotlib.pyplot as plt

x = ["Ali", "Sara", "Reza", "Niloofar", "Omid", "Hamed", "Maryam", "Arash", "Zahra", "Lila"]
y = [18, 17, 19.5, 16, 14.5, 20, 18.5, 13, 15.5, 19]

plt.plot(x, y)
plt.title("Student Scores")
plt.xlabel("Name")
plt.ylabel("Score")
plt.ylim(0, 20)
plt.grid(True)
plt.show()
