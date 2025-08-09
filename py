import re

def password_strength(password):
    score = 0
    strength = ""

    # Criteria checks
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength evaluation
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"

    return strength

# Example
user_password = input("Enter your password: ")
print("Password Strength:", password_strength(user_password))
