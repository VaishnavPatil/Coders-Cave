import random
import string


def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: Please select at least one character type.")
        return None

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password


def get_user_input():
    length = int(input("Enter password length: "))

    use_uppercase = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return length, use_uppercase, use_lowercase, use_digits, use_symbols


def main():
    print("Welcome to the Simple Password Generator!")

    length, use_uppercase, use_lowercase, use_digits, use_symbols = get_user_input()

    generated_password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)

    if generated_password:
        print(f"\nYour generated password: {generated_password}")


if __name__ == "__main__":
    main()
