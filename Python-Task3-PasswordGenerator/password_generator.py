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

    groups = [
        ("Include uppercase letters? (yes/no): ", string.ascii_uppercase),
        ("Include lowercase letters? (yes/no): ", string.ascii_lowercase),
        ("Include numbers? (yes/no): ", string.digits),
        ("Include special characters? (yes/no): ", string.punctuation),
    ]

    selected = []
    for prompt, characters in groups:
        if input(prompt).strip().lower() == "yes":
            selected.append(characters)

    if len(selected) < 2:
        print("Please select at least two character types.")
        return

    all_chars = "".join(selected)
    password_chars = [secrets.choice(group) for group in selected]
    password_chars.extend(
        secrets.choice(all_chars)
        for _ in range(length - len(password_chars))
    )
    secrets.SystemRandom().shuffle(password_chars)

    print("\nYour generated password is:", "".join(password_chars))


if __name__ == "__main__":
    while True:
        generate_password()
        again = input("\nGenerate another password? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Password Generator!")
            break
