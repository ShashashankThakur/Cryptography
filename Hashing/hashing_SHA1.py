import hashlib

def sha1_hash(input_text):
    """
    Computes the SHA-1 hash of the input text.

    :param input_text: The input text to be hashed.
    :return: The SHA-1 hash in hexadecimal format.
    """
    # Create a SHA-1 hash object
    sha1_hash_object = hashlib.sha1()

    # Update the hash object with the bytes of the input text
    sha1_hash_object.update(input_text.encode('utf-8'))

    # Get the hexadecimal representation of the SHA-1 hash
    return sha1_hash_object.hexdigest()


def main():
    """
    Main function to demonstrate the usage of the SHA-1 hash function.
    """
    input_text = "Hello, World!"

    # Compute the SHA-1 hash
    sha1_result = sha1_hash(input_text)

    # Display the result
    print(f"SHA-1 hash for '{input_text}': {sha1_result}")


if __name__ == "__main__":
    main()
