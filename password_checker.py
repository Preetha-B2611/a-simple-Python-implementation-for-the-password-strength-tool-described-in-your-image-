#!/usr/bin/env python3
"""
Password Strength Checker
-------------------------
A simple tool to assess the strength of a password based on:
- Length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
"""

import re

def password_strength(password: str) -> str:
    score = 0

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

    # Evaluate strength
    if score <= 2:
        return "Weak"
    elif score in [3, 4]:
        return "Moderate"
    else:
        return "Strong"

if __name__ == "__main__":
    pwd = input("Enter your password: ")
    print(f"Password Strength: {password_strength(pwd)}")
