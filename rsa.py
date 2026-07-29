import random

def is_prime(num, k=5):
    # Basic primality test (Miller-Rabin for better accuracy)
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0:
        return False

    # Write num-1 as 2^r * d
    d = num - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, num - 2)
        x = pow(a, d, num)

        if x == 1 or x == num - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    # Generate a random prime number of a given bit length
    while True:
        p = random.getrandbits(bits)
        # Ensure it's odd and within the desired range
        p |= (1 << bits - 1) | 1
        if is_prime(p):
            return p

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    # Extended Euclidean Algorithm to find modular inverse
    m0 = phi
    y = 0
    x = 1

    if phi == 1:
        return 0

    while e > 1:
        q = e // m0
        t = m0

        m0 = e % m0
        e = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x = x + phi

    return x

def generate_keys(bits=16):
    # 1. Choose two distinct large prime numbers, p and q
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    while p == q: # Ensure p and q are distinct
        q = generate_prime(bits // 2)

    # 2. Calculate n = p * q (the modulus)
    n = p * q

    # 3. Calculate Euler's totient function: phi = (p-1) * (q-1)
    phi = (p - 1) * (q - 1)

    # 4. Choose an integer e (the public exponent) such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # 5. Calculate d (the private exponent) as the modular multiplicative inverse of e modulo phi
    d = multiplicative_inverse(e, phi)

    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    # C = M^e mod n
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

def decrypt(private_key, ciphertext):
    d, n = private_key
    # M = C^d mod n
    plain = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plain)

# --- RSA Demonstration ---
print("Generating RSA keys...")
public_key, private_key = generate_keys(bits=10) # Using 10-bit primes for demonstration
print(f"Public Key (e, n): {public_key}")
print(f"Private Key (d, n): {private_key}\n")

original_message = input("Enter a message to encrypt: ")

encrypted_message = encrypt(public_key, original_message)
print(f"Encrypted Message (as numbers): {encrypted_message}")

decrypted_message = decrypt(private_key, encrypted_message)
print(f"Decrypted Message: {decrypted_message}\n")

if original_message == decrypted_message:
    print("RSA Encryption and Decryption Successful!")
else:
    print("Error: Decrypted message does not match original.")
