import secrets
import string


def generate_password():
    print("\n=== Password Generator ===")

    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))

            if length < 8:
                print("Password length must be at least 8.")
                continue

            break

        except ValueError:
            print("Please enter a valid whole number.")

    selected = []

    if input("Include uppercase letters? (yes/no): ").strip().lower() == "yes":
        selected.append(string.ascii_uppercase)

    if input("Include lowercase letters? (yes/no): ").strip().lower() == "yes":
        selected.append(string.ascii_lowercase)

    if input("Include numbers? (yes/no): ").strip().lower() == "yes":
        selected.append(string.digits)

    if input("Include special characters? (yes/no): ").strip().lower() == "yes":
        selected.append(string.punctuation)

    if not selected:
        print("Please select at least one character type.")
        return

    all_chars = "".join(selected)

    # Include at least one character from every selected type.
    password_chars = [secrets.choice(group) for group in selected]

    # Fill the remaining length.
    password_chars.extend(
        secrets.choice(all_chars)
        for _ in range(length - len(password_chars))
    )

    # Shuffle the characters securely.
    secrets.SystemRandom().shuffle(password_chars)

    password = "".join(password_chars)
    print("\nYour generated password is:", password)


if __name__ == "__main__":
    generate_password()
