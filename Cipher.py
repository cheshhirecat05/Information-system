# Caesar Cipher

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine the starting ASCII value ('A' for uppercase, 'a' for lowercase)
            start = ord('A') if char.isupper() else ord('a')
            print(ord('H'))
            # Calculate the encrypted character by shifting its position within the alphabet
            encrypted = chr((ord(char) - start + shift) % 26 + start)
            result += encrypted
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# Main Program
text = input("Enter message: ")
shift = int(input("Enter shift value: "))

cipher = encrypt(text, shift)
print("Encrypted Text:", cipher)

plain = decrypt(cipher, shift)
print("Decrypted Text:", plain)