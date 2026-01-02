import secrets
import string

# Function to generate a secure password
def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")

    # Character categories
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(symbols),
        secrets.choice(string.ascii_uppercase)  # optional, adds diversity
    ]

    # Fill the rest of the password length
    all_characters = letters + digits + symbols
    password += [secrets.choice(all_characters) for _ in range(length - len(password))]

    # Shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)

    return "".join(password)

# Main program
print("----- SECURE PASSWORD GENERATOR -----")

try:
    length = int(input("Enter the desired password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
        exit()
    elif length > 100:
        print("Password length must not exceed 100.")
        exit()

except ValueError:
    print("Invalid input! Please enter a valid number.")
    exit()

# Generate and display the password
final_password = generate_password(length)
print("\nGenerated Password:")
print("-------------------")
print(final_password)
print("-------------------")
