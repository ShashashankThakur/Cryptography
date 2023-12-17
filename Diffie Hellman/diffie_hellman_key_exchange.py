from random import randint

def is_prime(num):
    """
    Check if a number is prime.

    :param num: The number to check for primality.
    :return: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    """
    Generate a random prime number.

    :return: A random prime number.
    """
    while True:
        num = randint(10, 100)
        if is_prime(num):
            return num

def mod_exp(base, exp, mod):
    """
    Compute (base^exp) % mod efficiently using the modular exponentiation algorithm.

    :param base: The base.
    :param exp: The exponent.
    :param mod: The modulus.
    :return: The result of (base^exp) % mod.
    """
    result = 1
    base = base % mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod

    return result

def diffie_hellman_key_exchange():
    """
    Perform the Diffie-Hellman key exchange.

    :return: The shared secret key.
    """
    # Step 1: Select a large prime number (p)
    p = generate_prime()

    # Step 2: Select a primitive root modulo p (g)
    g = randint(2, p - 2)

    # Step 3: Each party selects a private key (a, b)
    a = randint(2, p - 2)
    b = randint(2, p - 2)

    # Step 4: Compute public keys (A, B)
    A = mod_exp(g, a, p)
    B = mod_exp(g, b, p)

    # Step 5: Exchange public keys (A, B)

    # Step 6: Compute shared secret key
    shared_secret_key_a = mod_exp(B, a, p)
    shared_secret_key_b = mod_exp(A, b, p)

    # Both parties now have the same shared secret key
    assert shared_secret_key_a == shared_secret_key_b

    return shared_secret_key_a

def main():
    """
    Main function to demonstrate the Diffie-Hellman key exchange.
    """
    shared_secret_key = diffie_hellman_key_exchange()
    print(f"Shared Secret Key: {shared_secret_key}")

if __name__ == "__main__":
    main()
