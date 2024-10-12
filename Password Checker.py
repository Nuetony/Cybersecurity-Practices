import re

def password_strength(password):
    # Criteria to evaluate
    length_criteria = len(password) >= 12
    lowercase_criteria = re.search("[a-z]", password) is not None
    uppercase_criteria = re.search("[A-Z]", password) is not None
    digit_criteria = re.search("[0-9]", password) is not None
    special_char_criteria = re.search("[@#$%^&*!]", password) is not None

    # Entropy approximation (considering diversity)
    character_types = sum([lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    # Scoring
    score = 0
    if length_criteria:
        score += 2
    score += character_types

    # Assess strength
    if score >= 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

# Test the function
password = input("Enter a password: ")
strength = password_strength(password)
print(f"Password Strength: {strength}")
