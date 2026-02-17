# 📝 Registration Eligibility Checker
print("\n")
print("🔍 Check if you're allowed to register")
print( "." * 40)

# Get user's age
age = int(input( "📅 Please enter your age: "))
print("\n" + "=" * 40)

# Evaluate conditions
if age >= 18:
    print("✅ You are allowed to register. Welcome! 🎉")
elif 14 < age < 18:
    print("⚠️ Your registration requires parental approval.")
else:
    print("❌ Sorry, you are not allowed to register.")

print("=" * 40)
