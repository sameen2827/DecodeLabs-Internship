import random
import string


def generate_password(length, characters):
    return ''.join(random.choice(characters) for _ in range(length))


def main():
    print("\n" + "=" * 45)
    print("      PROFESSIONAL PASSWORD GENERATOR")
    print("=" * 45)

    try:
        length = int(input("\nEnter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
            return

    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Character Sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Password Types
    simple_password = generate_password(length, letters)

    numeric_password = generate_password(length, digits)

    strong_password = generate_password(
        length,
        letters + digits + symbols
    )

    alphanumeric_password = generate_password(
        length,
        letters + digits
    )

    # Output
    print("\n" + "=" * 45)
    print("           GENERATED PASSWORDS")
    print("=" * 45)

    print(f"\n1. Simple Password       : {simple_password}")
    print(f"2. Numeric Password      : {numeric_password}")
    print(f"3. Alphanumeric Password : {alphanumeric_password}")
    print(f"4. Strong Password       : {strong_password}")

    print("\n" + "=" * 45)
    print(" Password generation completed successfully!")
    print("=" * 45)


if __name__ == "__main__":
    main()