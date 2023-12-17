# caesar_cipher.py

def caesar_cipher(text, shift):
    """
    Encrypts or decrypts a given text using the Caesar cipher.

    :param text: The input text to be encrypted or decrypted.
    :param shift: The shift value for the Caesar cipher.
    :return: The encrypted or decrypted text.
    """
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char) - ord('a')
            char_code = (char_code + shift) % 26
            char = chr(char_code + ord('a'))
            if is_upper:
                char = char.upper()

        result += char

    return result


def main():
    """
    Main function to demonstrate the usage of the Caesar cipher.
    """
    plaintext = "Hello, World!"
    shift_value = 3

    # Encryption
    encrypted_text = caesar_cipher(plaintext, shift_value)
    print("Encrypted:", encrypted_text)

    # Decryption
    decrypted_text = caesar_cipher(encrypted_text, -shift_value)
    print("Decrypted:", decrypted_text)


if __name__ == "__main__":
    main()
