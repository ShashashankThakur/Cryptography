from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def generate_key():
    """
    Generates a random 256-bit AES key.

    :return: The generated key.
    """
    return os.urandom(32)

def pad_data(data):
    """
    Pads the data using PKCS7 padding.

    :param data: The data to be padded.
    :return: The padded data.
    """
    # PKCS7 padding adds bytes to the data to make its length a multiple of the block size (128 bits for AES).
    # The number of bytes added is equal to the value of the padding byte.
    padder = padding.PKCS7(128).padder()
    return padder.update(data) + padder.finalize()

def unpad_data(data):
    """
    Unpads the data using PKCS7 padding.

    :param data: The data to be unpadded.
    :return: The unpadded data.
    """
    # PKCS7 unpadding removes the added padding bytes to restore the original data.
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(data) + unpadder.finalize()

def encrypt_file(input_file, output_file, key):
    """
    Encrypts a file using the AES algorithm.

    :param input_file: The path to the input file.
    :param output_file: The path to the output (encrypted) file.
    :param key: The encryption key.
    """
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    # Create an AES cipher object with CFB mode.
    cipher = Cipher(algorithms.AES(key), modes.CFB(), backend=default_backend())

    # Create an encryptor object from the cipher.
    encryptor = cipher.encryptor()

    # Encrypt the data and apply PKCS7 padding.
    ciphertext = encryptor.update(pad_data(plaintext)) + encryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(ciphertext)

def decrypt_file(input_file, output_file, key):
    """
    Decrypts a file using the AES algorithm.

    :param input_file: The path to the input (encrypted) file.
    :param output_file: The path to the output (decrypted) file.
    :param key: The decryption key.
    """
    with open(input_file, 'rb') as file:
        ciphertext = file.read()

    # Create an AES cipher object with CFB mode.
    cipher = Cipher(algorithms.AES(key), modes.CFB(), backend=default_backend())

    # Create a decryptor object from the cipher.
    decryptor = cipher.decryptor()

    # Decrypt the data, remove PKCS7 padding, and obtain the original data.
    decrypted_data = unpad_data(decryptor.update(ciphertext) + decryptor.finalize())

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

def main():
    """
    Main function to demonstrate the usage of file encryption and decryption.
    """
    key = generate_key()

    input_file = "sample.txt"
    encrypted_file = "encrypted_sample.enc"
    decrypted_file = "decrypted_sample.txt"

    # Encrypt the file
    encrypt_file(input_file, encrypted_file, key)
    print(f"File '{input_file}' encrypted and saved as '{encrypted_file}'.")

    # Decrypt the file
    decrypt_file(encrypted_file, decrypted_file, key)
    print(f"File '{encrypted_file}' decrypted and saved as '{decrypted_file}'.")

if __name__ == "__main__":
    main()
