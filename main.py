from generator import generate_password
from strength import check_strength
from file_handler import save_password
from crack_time import estimate_crack_time

def get_choice(prompt):
    choice = input(prompt).strip().lower()
    return choice == "y"


def main():
    print("=" * 45)
    print("      PYTHON PASSWORD GENERATOR")
    print("=" * 45)

    try:
        length = int(input("Enter password length: "))
        count = int(input("How many passwords do you want? "))

        print("\nPassword Generation Mode")
        print("1. Random Password")
        print("2. Keyword Based Password")

        mode = input("Choose option (1/2): ").strip()

        keyword = ""

        if mode == "2":
            keyword = input("Enter your keyword: ").strip()

        print()

        use_upper = get_choice("Include Uppercase? (Y/N): ")
        use_lower = get_choice("Include Lowercase? (Y/N): ")
        use_digits = get_choice("Include Numbers? (Y/N): ")
        use_symbols = get_choice("Include Symbols? (Y/N): ")

        print("\nGenerated Passwords")
        print("-" * 45)

        for i in range(count):
            password = generate_password(
                length,
                use_upper,
                use_lower,
                use_digits,
                use_symbols,
                keyword
            )

            strength = check_strength(password)
            crack_time = estimate_crack_time(password)

            save_password(password, strength)   

            print(f"{i + 1}. {password}")
            print(f"   Strength : {strength}")
            print(f"   Crack Time : {crack_time}")
            print()

    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()