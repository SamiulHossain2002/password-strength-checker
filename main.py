# Beginner-friendly Password Strength Checker
# Author: Md. Samiul Hossain

# Function to check password strength
def check_password_strength(password):
    score = 0  # Tracks password strength points

    # Length check
    if len(password) >= 8:
        score += 1

    # Contains lowercase letters
    if any(char.islower() for char in password):
        score += 1

    # Contains uppercase letters
    if any(char.isupper() for char in password):
        score += 1

    # Contains digits
    if any(char.isdigit() for char in password):
        score += 1

    # Contains special characters
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(char in special_characters for char in password):
        score += 1

    # Feedback based on score
    if score <= 2:
        return "Weak Password ❌"
    elif score == 3 or score == 4:
        return "Medium Strength Password ⚠️"
    else:
        return "Strong Password ✅"

# Main program
password = input("Enter your password to check strength: ")
strength = check_password_strength(password)
print("Password Strength:", strength)
