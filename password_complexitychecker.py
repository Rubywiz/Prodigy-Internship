import re

def password_strength(password):
    # Define criteria
    min_length = 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Assess the strength
    length_criteria = len(password) >= min_length
    strength = {
        'Length': length_criteria,
        'Uppercase': bool(has_upper),
        'Lowercase': bool(has_lower),
        'Digit': bool(has_digit),
        'Special Character': bool(has_special)
    }

    # Provide feedback
    feedback = []
    suggestions = []

    if not length_criteria:
        feedback.append(f"Password should be at least {min_length} characters long.")
        suggestions.append("Try adding more characters to your password to increase its length.")
    if not has_upper:
        feedback.append("Password should contain at least one uppercase letter.")
        suggestions.append("Include uppercase letters (A-Z) to make your password stronger.")
    if not has_lower:
        feedback.append("Password should contain at least one lowercase letter.")
        suggestions.append("Include lowercase letters (a-z) to make your password more secure.")
    if not has_digit:
        feedback.append("Password should contain at least one digit.")
        suggestions.append("Add numbers (0-9) to enhance the complexity of your password.")
    if not has_special:
        feedback.append("Password should contain at least one special character.")
        suggestions.append("Use special characters (!@#$%^&*(),.?\":{}|<>) to increase password strength.")

    if all(strength.values()):
        feedback.append("Your password is strong.")
    else:
        feedback.append("Your password is weak. Here are some suggestions to improve it:")
        feedback.extend(suggestions)

    return strength, feedback

# Example usage
password = input("Enter your password: ")
strength, feedback = password_strength(password)

print("Password Strength:")
for criterion, met in strength.items():
    print(f"{criterion}: {'Met' if met else 'Not Met'}")

print("\nFeedback:")
for f in feedback:
    print(f)
