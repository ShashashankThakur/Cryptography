import random

def is_prime(n, k=5):
    """
    Miller-Rabin primality test.

    :param n: The number to test for primality.
    :param k: Number of iterations for the test.
    :return: True if n is likely prime, False otherwise.
    """
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits=1024):
    """
    Generate a random prime number with a specified number of bits.

    :param bits: The number of bits in the prime number.
    :return: A random prime number.
    """
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: The GCD of a and b.
    """
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    """
    Calculate the modular multiplicative inverse.

    :param a: The number.
    :param m: The modulus.
    :return: The modular multiplicative inverse of a mod m.
    """
    m0, x0, x1 = m, 0, 1

    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1

def generate_keypair(bits=1024):
    """
    Generate a key pair for RSA encryption.

    :param bits: The number of bits in the key.
    :return: A tuple (public_key, private_key).
    """
    # Step 1: Generate two random prime numbers, p and q
    p = generate_prime(bits)
    q = generate_prime(bits)

    # Step 2: Compute n = p * q
    n = p * q

    # Step 3: Compute the totient (Euler's totient function) φ(n)
    phi = (p - 1) * (q - 1)

    # Step 4: Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Step 5: Compute d such that d * e ≡ 1 (mod φ(n))
    d = modinv(e, phi)

    # Public key: (n, e)
    public_key = (n, e)

    # Private key: (n, d)
    private_key = (n, d)

    return public_key, private_key

def encrypt(message, public_key):
    """
    Encrypt a message using the RSA algorithm.

    :param message: The message to encrypt.
    :param public_key: The public key (n, e).
    :return: The encrypted message.
    """
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    """
    Decrypt an encrypted message using the RSA algorithm.

    :param encrypted_message: The encrypted message.
    :param private_key: The private key (n, d).
    :return: The decrypted message.
    """
    n, d = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

def main():
    """
    Main function to demonstrate the RSA algorithm.
    """
    # Step 1: Generate a key pair
    public_key, private_key = generate_keypair()

    # Step 2: Encrypt a message
    message = "Hello, RSA!"
    encrypted_message = encrypt(message, public_key)
    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}")

    # Step 3: Decrypt the message
    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
