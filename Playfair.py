# Playfair Cipher

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key:
        if ch not in used and ch.isalpha():
            used.add(ch)
            matrix.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            used.add(ch)
            matrix.append(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))

    prepared = ""
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'

        if a == b:
            prepared += a + 'X'
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += 'X'

    return prepared


def encrypt(text, matrix):
    text = prepare_text(text)
    result = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1 + 1) % 5]
            result += matrix[r2][(c2 + 1) % 5]

        elif c1 == c2:
            result += matrix[(r1 + 1) % 5][c1]
            result += matrix[(r2 + 1) % 5][c2]

        else:
            result += matrix[r1][c2]
            result += matrix[r2][c1]

    return result


# Main Program
key = input("Enter key: ")
text = input("Enter plaintext: ")

matrix = generate_key_matrix(key)
print(matrix)
print("Key Matrix:")
for row in matrix:
    print(row)

cipher = encrypt(text, matrix)
print("Encrypted Text:", cipher)