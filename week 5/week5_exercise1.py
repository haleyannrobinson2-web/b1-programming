import string  # Provides constants like ascii_uppercase, ascii_lowercase, digits, punctuation
import random  # Optional: for hints or suggestions

# Modular Validation with Python Imports
# -----------------------
# Part A: Individual Validation Functions
# -----------------------

def check_min_length(password, min_len=8):
    """
    Check if password meets minimum length requirement.

    Args:
        password (str): The password string to validate
        min_len (int): Minimum required length (default: 8)

    Returns:
        bool: True if password meets length requirement, False otherwise
    """
    return len(password) >= min_len


def has_uppercase(password):
    """
    Check if password contains at least one uppercase letter.

    Args:
        password (str): The password string to validate

    Returns:
        bool: True if password contains uppercase letter, False otherwise
    """
    return any(char in string.ascii_uppercase for char in password)


def has_lowercase(password):
    """
    Check if password contains at least one lowercase letter.

    Args:
        password (str): The password string to validate

    Returns:
        bool: True if password contains lowercase letter, False otherwise
    """
    return any(char in string.ascii_lowercase for char in password)


def has_digit(password):
    """
    Check if password contains at least one numeric digit.

    Args:
        password (str): The password string to validate

    Returns:
        bool: True if password contains a digit, False otherwise
    """
    return any(char in string.digits for char in password)


def has_special_char(password):
    """
    Check if password contains at least one special character.

    Args:
        password (str): The password string to validate

    Returns:
        bool: True if password contains special character, False otherwise
    """
    return any(char in string.punctuation for char in password)


# -----------------------
# Part B: Master Validation Function
# -----------------------

def validate_password(password):
    """
    Perform comprehensive password validation using all criteria.

    Args:
        password (str): The password string to validate

    Returns:
        dict: Results of each individual check plus overall validity
    """
    results = {
        'min_length': check_min_length(password),
        'has_uppercase': has_uppercase(password),
        'has_lowercase': has_lowercase(password),
        'has_digit': has_digit(password),
        'has_special': has_special_char(password)
    }
    # Overall validity requires all checks to pass
    results['is_valid'] = all(results.values())
    return results


# -----------------------
# Part C: User Interface and Testing
# -----------------------

def main():
    """
    Main program that tests password validation with user input.
    Displays detailed results for each criterion.
    """
    print("=" * 50)
    print("PASSWORD STRENGTH VALIDATOR")
    print("=" * 50)

    print("\nPassword Requirements:")
    print("  - Minimum 8 characters")
    print("  - At least one uppercase letter")
    print("  - At least one lowercase letter")
    print("  - At least one digit")
    print("  - At least one special character (!@#$%^&* etc.)\n")

    # Prompt user for password
    password = input("Enter password to validate: ")

    # Validate password
    results = validate_password(password)

    # Display individual criteria results
    print("\n" + "=" * 50)
    print("VALIDATION RESULTS")
    print("=" * 50)

    check_symbol = "✔"  # symbol for pass
    cross_symbol = "✖"  # symbol for fail

    print(f"{check_symbol if results['min_length'] else cross_symbol} Minimum length (8+ chars)")
    print(f"{check_symbol if results['has_uppercase'] else cross_symbol} Contains uppercase")
    print(f"{check_symbol if results['has_lowercase'] else cross_symbol} Contains lowercase")
    print(f"{check_symbol if results['has_digit'] else cross_symbol} Contains digit")
    print(f"{check_symbol if results['has_special'] else cross_symbol} Contains special char")

    # Overall result
    print("\n" + "=" * 50)
    if results['is_valid']:
        print(f"{check_symbol} PASSWORD IS STRONG!")
    else:
        print(f"{cross_symbol} PASSWORD IS WEAK - Please address failed requirements")

    # Optional: hint for missing criteria
    if not results['has_special']:
        hint = random.choice(string.punctuation)
        print(f"Hint: Try adding a special character like '{hint}'")
    print("=" * 50)


# Run the program only when the script is executed directly
if __name__ == "__main__":
    main()
