import hashlib

def md5_hash(input_text):
    """
    Computes the MD5 hash of the input text.

    :param input_text: The input text to be hashed.
    :return: The MD5 hash in hexadecimal format.
    """
    # Create an MD5 hash object
    md5_hash_object = hashlib.md5()

    # Update the hash object with the bytes of the input text
    md5_hash_object.update(input_text.encode('utf-8'))

    # Get the hexadecimal representation of the MD5 hash
    return md5_hash_object.hexdigest()


def main():
    """
    Main function to demonstrate the usage of the MD5 hash function.
    """
    input_text = "Hello, World!"

    # Compute the MD5 hash
    md5_result = md5_hash(input_text)

    # Display the result
    print(f"MD5 hash for '{input_text}': {md5_result}")


if __name__ == "__main__":
    main()
