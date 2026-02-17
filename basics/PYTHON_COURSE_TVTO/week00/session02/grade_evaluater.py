# 🎓 Student Level Evaluation
print("\n" + "-" * 50)
print("📊 Examine Your Academic Level")
print("-" * 50)
print("This tool helps students understand their score level based on the classification below:\n")

print("🌟 18 - 20  → Excellent")
print("👍 15 - 17  → Good")
print("👌 13 - 14  → Mid")
print("📈 0  - 12  → Needs Improvement")

print("=" * 50)
print("\n🔍 Enter your score below to check your level:\n")

# Get user score
score = float(input("🧮 Enter your score: "))
print("\n"+"-" * 50)

# Evaluate the level
if 18 <= score <= 20:
    print("🌟 Bravo! You nailed it — Your level is **Excellent**.")
elif 15 <= score < 18:
    print("👍 Well done! Your level is **Good**.")
elif score == 14:
    print("👌 You're doing okay — Your level is **Mid**. Keep going!")
elif 0 <= score < 14:
    print("📈 Don't give up! You just need more practice.")
else:
    print("❗ Please enter a valid score between 0 and 20.")

print("-" * 50)
