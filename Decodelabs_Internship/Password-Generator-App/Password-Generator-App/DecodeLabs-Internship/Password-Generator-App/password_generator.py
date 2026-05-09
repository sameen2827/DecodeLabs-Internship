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
            print("Password length should be atleast 4.")
            return

    except ValueError:
        print("Invalid input, please enter a valid number.")
        return

    
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    
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

   
    print("\n" + "=" * 45)
    print(" Generated Passwords")
    print("=" *45)

    print(f"\n1. Simple Password  :{simple_password}")
    print(f"2. Numeric Password  :{numeric_password}")
    print(f"3. Alphanumeric Password :{alphanumeric_password}")
    print(f"4. Strong Password :{strong_password}")

    print("\n" + "=" * 45)
    print(" Passwords Generated Successfully!")
    print("=" * 45 + "\n")


if __name__ == "__main__":
    main()
    