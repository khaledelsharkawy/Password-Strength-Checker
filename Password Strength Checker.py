import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    upper_case_criteria = re.search(r'[A-Z]', password) is not None
    lower_case_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    score = sum([length_criteria, upper_case_criteria, lower_case_criteria,
                 number_criteria, special_char_criteria])

    if score < 3:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, {
        "Length (8 or more characters)": length_criteria,
        "Contains uppercase letters": upper_case_criteria,
        "Contains lowercase letters": lower_case_criteria,
        "Contains numbers": number_criteria,
        "Contains special characters": special_char_criteria,
    }

def main():
    print("Welcome to the Password Strength Checker!")
    password = input("Please enter a password: ")
    strength, criteria_feedback = assess_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print("Criteria Feedback:")
    for criterion, met in criteria_feedback.items():
        status = "✔️ Met" if met else "❌ Not Met"
        print(f"- {criterion}: {status}")

if __name__ == "__main__":
    main()
