from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def generate_keypair():
    """
    Generate a key pair for digital signatures.

    :return: A tuple (private_key, public_key).
    """
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    return private_key, public_key

def sign_message(message, private_key):
    """
    Sign a message with the private key.

    :param message: The message to sign.
    :param private_key: The private key for signing.
    :return: The digital signature.
    """
    signature = private_key.sign(
        message.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(message, signature, public_key):
    """
    Verify the digital signature with the public key.

    :param message: The original message.
    :param signature: The digital signature to verify.
    :param public_key: The public key for verification.
    :return: True if the signature is valid, False otherwise.
    """
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

def main():
    """
    Main function to demonstrate the digital signature system.
    """
    # Step 1: Generate a key pair
    private_key, public_key = generate_keypair()

    # Step 2: Sign a message
    message = "Hello, Digital Signature!"
    signature = sign_message(message, private_key)
    print(f"Original Message: {message}")
    print(f"Digital Signature: {signature.hex()}")

    # Step 3: Verify the signature
    is_valid = verify_signature(message, signature, public_key)
    if is_valid:
        print("Signature is valid.")
    else:
        print("Signature is not valid.")

if __name__ == "__main__":
    main()
