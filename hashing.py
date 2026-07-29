import hashlib

# Take input from the user
user_input = input("Enter a string to hash: ")
input_bytes = user_input.encode('utf-8')

print(f"\nInput string: '{user_input}'")

# --- First pass at hashing ---
print("\n--- First Hashing Pass ---")

# SHA-1
sha1_hash1 = hashlib.sha1(input_bytes).hexdigest()
print(f"SHA-1 (1st pass): {sha1_hash1}")

# MD5
md5_hash1 = hashlib.md5(input_bytes).hexdigest()
print(f"MD5 (1st pass): {md5_hash1}")

# SHA256
sha256_hash1 = hashlib.sha256(input_bytes).hexdigest()
print(f"SHA256 (1st pass): {sha256_hash1}")

# --- Second pass at hashing ---
print("\n--- Second Hashing Pass ---")

# SHA-1
sha1_hash2 = hashlib.sha1(input_bytes).hexdigest()
print(f"SHA-1 (2nd pass): {sha1_hash2}")

# MD5
md5_hash2 = hashlib.md5(input_bytes).hexdigest()
print(f"MD5 (2nd pass): {md5_hash2}")

# SHA256
sha256_hash2 = hashlib.sha256(input_bytes).hexdigest()
print(f"SHA256 (2nd pass): {sha256_hash2}")

# --- Comparison ---
print("\n--- Comparison Results ---")

print(f"SHA-1 hashes match: {sha1_hash1 == sha1_hash2}")
print(f"MD5 hashes match: {md5_hash1 == md5_hash2}")
print(f"SHA256 hashes match: {sha256_hash1 == sha256_hash2}")