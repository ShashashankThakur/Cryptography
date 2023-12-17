def basic_hash(text):
    """
    Basic hash function (not for cryptographic use).

    :param text: The input text to be hashed.
    :return: The hash value.
    """
    hash_value = 0

    for char in text:
        hash_value = (hash_value << 5) + ord(char)
        hash_value = hash_value & 0xFFFFFFFF  # Limit to 32 bits

    return hash_value


def main():
    """
    Main function to demonstrate the usage of the basic hash function.
    """
    input_text = "Hello, World!"

    # Hash the input text
    hash_result = basic_hash(input_text)

    # Display the result
    print(f"Hash value for '{input_text}': {hash_result}")


if __name__ == "__main__":
    main()
