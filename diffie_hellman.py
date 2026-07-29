import random

def diffie_hellman():
    # 1. Agree on a large prime number (p) and a base (g)
    # These would typically be publicly known or exchanged securely.
    # For demonstration, we'll use small values.
    p = 23  # A prime number
    g = 5   # A primitive root modulo p (base)

    print(f"Publicly agreed values: p = {p}, g = {g}\n")

    # --- Alice's side ---
    # 2. Alice chooses a secret integer (a)
    a = random.randint(2, p - 2)
    print(f"Alice's secret integer (a): {a}")

    # 3. Alice calculates her public value (A)
    A = pow(g, a, p)
    print(f"Alice's public value (A): g^a mod p = {g}^{a} mod {p} = {A}\n")

    # --- Bob's side ---
    # 4. Bob chooses a secret integer (b)
    b = random.randint(2, p - 2)
    print(f"Bob's secret integer (b): {b}")

    # 5. Bob calculates his public value (B)
    B = pow(g, b, p)
    print(f"Bob's public value (B): g^b mod p = {g}^{b} mod {p} = {B}\n")

    # --- Exchange public values (A and B) over an insecure channel ---
    print("Alice sends A to Bob. Bob sends B to Alice.\n")

    # --- Alice calculates the shared secret key ---
    # 6. Alice computes K = B^a mod p
    shared_secret_alice = pow(B, a, p)
    print(f"Alice calculates shared secret: B^a mod p = {B}^{a} mod {p} = {shared_secret_alice}")

    # --- Bob calculates the shared secret key ---
    # 7. Bob computes K = A^b mod p
    shared_secret_bob = pow(A, b, p)
    print(f"Bob calculates shared secret: A^b mod p = {A}^{b} mod {p} = {shared_secret_bob}\n")

    # --- Verify if the keys match ---
    if shared_secret_alice == shared_secret_bob:
        print(f"Shared secrets match! The shared secret key is: {shared_secret_alice}")
    else:
        print("Error: Shared secrets do not match.")

# Run the Diffie-Hellman Key Exchange
diffie_hellman()
