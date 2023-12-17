# vigenere_cipher.py

def vigenere_cipher(text, key, encrypt=True):
    """
    Encrypts or decrypts a given text using the Vigenère cipher.

    :param text: The input text to be encrypted or decrypted.
    :param key: The Vigenère cipher key.
    :param encrypt: True for encryption, False for decryption.
    :return: The encrypted or decrypted text.
    """
    result = ""
    key_length = len(key)
    key = key.lower()

    for i, char in enumerate(text):
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()

            key_char = key[i % key_length]
            key_shift = ord(key_char) - ord('a')

            if not encrypt:
                key_shift = -key_shift

            char_code = ord(char) - ord('a')
            char_code = (char_code + key_shift) % 26
            char = chr(char_code + ord('a'))

            if is_upper:
                char = char.upper()

        result += char

    return result


def main():
    """
    Main function to demonstrate the usage of the Vigenère cipher.
    """
    plaintext = "Hello, World!"
    vigenere_key = "KEY"

    # Encryption
    encrypted_text = vigenere_cipher(plaintext, vigenere_key)
    print("Encrypted:", encrypted_text)

    # Decryption
    decrypted_text = vigenere_cipher(encrypted_text, vigenere_key, encrypt=False)
    print("Decrypted:", decrypted_text)


if __name__ == "__main__":
    main()
