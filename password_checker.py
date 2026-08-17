import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit check
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$% etc).")

    # Print result
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    print(f"\nPassword Strength: {strength_levels[score]}")
    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print(f"  - {tip}")
    else:
        print("Great password!")

# Run the tool
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    check_password_strength(pwd)
