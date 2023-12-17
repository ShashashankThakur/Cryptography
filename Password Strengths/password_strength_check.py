import re

def load_wordlist(filename="wordlist.txt"):
    """
    Loads a wordlist from a file.

    :param filename: The name of the wordlist file.
    :return: A set containing words from the wordlist.
    """
    wordlist = set()
    try:
        with open(filename, 'r') as file:
            for line in file:
                wordlist.add(line.strip().lower())
    except FileNotFoundError:
        print(f"Wordlist file '{filename}' not found.")
    return wordlist

def is_strong_password(password, wordlist):
    """
    Evaluates the strength of a password based on common criteria.

    :param password: The password to be evaluated.
    :param wordlist: A set containing words from the wordlist.
    :return: True if the password is strong; False otherwise.
    """
    # Minimum length criterion
    if len(password) < 8:
        return False

    # Complexity criteria
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Require at least one uppercase letter, one lowercase letter, one digit, and one special character
    if not (has_uppercase and has_lowercase and has_digit and has_special_char):
        return False

    # Resistance to common attacks using wordlist
    if password.lower() in wordlist:
        return False

    # Additional criteria (customize based on security requirements)
    # For example, check if the password is not based on the username, etc.

    # If all criteria are met, consider the password strong
    return True

def main():
    """
    Main function to demonstrate the usage of the password strength evaluator.
    """
    wordlist = load_wordlist()

    if not wordlist:
        return

    password = input("Enter a password to evaluate its strength: ")

    # Evaluate the strength of the password
    if is_strong_password(password, wordlist):
        print("Password is strong!")
    else:
        print("Password is weak. Please choose a stronger password.")

if __name__ == "__main__":
    main()
