from os.path import join
# Vigenere Cipher

def generate_key(text, key):
    key = list(key)

    if len(text) == len(key):
        return "".join(key)

    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])
    keystr="".join(key)
    print("key:",keystr)
    return keystr


def encrypt(text, key):
    cipher = ""

    for i in range(len(text)):
        if text[i].isalpha():
            x = (ord(text[i].upper()) +
                 ord(key[i].upper())) % 26
            x += ord('A')
            cipher += chr(x)
        else:
            cipher += text[i]

    return cipher


def decrypt(cipher, key):
    text = ""

    for i in range(len(cipher)):
        if cipher[i].isalpha():
            x = (ord(cipher[i].upper()) - ord(key[i].upper()) + 26) % 26 #retuns  only position of x
            x += ord('A') #for x+=ord('A') will bring ASCII of char x
            text += chr(x) #convert ASCII to Char
        else:
            text += cipher[i]

    return text


# Main Program
text = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()

generated_key = generate_key(text, key)

cipher = encrypt(text, generated_key)
print("Encrypted Text:", cipher)

plain = decrypt(cipher, generated_key)
print("Decrypted Text:", plain)