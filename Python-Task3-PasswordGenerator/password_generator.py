import random
import string

def generate_password():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter password length: "))

        if length < 1:
            print("Password length must be at least 1.")
            return

        selected = []

        if input("Include uppercase letters? (yes/no): ").lower() == "yes":
            selected.append(string.ascii_uppercase)

        if input("Include lowercase letters? (yes/no): ").lower() == "yes":
            selected.append(string.ascii_lowercase)

        if input("Include numbers? (yes/no): ").lower() == "yes":
            selected.append(string.digits)

        if input("Include special characters? (yes/no): ").lower() == "yes":
            selected.append(string.punctuation)

        if not selected:
            print("Please select at least one character type.")
            return

        if length < len(selected):
            print("Password length is too short for all selected types.")
            return

        password_chars = [
            random.choice(group) for group in selected
        ]

        all_chars = "".join(selected)

        password_chars.extend(
            random.choice(all_chars)
            for _ in range(length - len(password_chars))
        )

        random.SystemRandom().shuffle(password_chars)
        password = "".join(password_chars)

        print("Your generated password is:", password)

    except ValueError:
        print("Please enter a valid whole number.")


if __name__ == "__main__":
    generate_password()
