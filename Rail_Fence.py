# Simple Rail Fence Cipher Program
# ---------------- ENCRYPTION ----------------
def encrypt(message, rails):

    # Create empty rows
    rail_matrix = []

    for i in range(rails):
        rail_matrix.append(["*" for j in range(len(message))])

    row = 0
    direction = 1
    # direction = 1 means moving downward
    # direction = -1 means moving upward

    # Put characters in zig-zag form
    for col in range(len(message)):

        rail_matrix[row][col] = message[col]

        # Change direction at top or bottom rail
        if row == 0:
            direction = 1

        elif row == rails - 1:
            direction = -1

        row = row + direction

    # Display zig-zag pattern
    print("\nRail Matrix:")

    for r in rail_matrix:
        print(" ".join(r))

    # Read row by row to create cipher text
    cipher = ""

    for i in range(rails):
        for j in range(len(message)):

            if rail_matrix[i][j] != "*": # Changed condition to check for * instead of space
                cipher = cipher + rail_matrix[i][j]

    return cipher


# ---------------- DECRYPTION ----------------
def decrypt(cipher, rails):

    # Create empty matrix
    rail_matrix = []

    for i in range(rails):
        rail_matrix.append([" " for j in range(len(cipher))])

    row = 0
    direction = 1

    # Step 1: Mark zig-zag positions with *
    for col in range(len(cipher)):

        rail_matrix[row][col] = "*"

        if row == 0:
            direction = 1

        elif row == rails - 1:
            direction = -1

        row = row + direction

    # Step 2: Fill marked positions with cipher text
    index = 0

    for i in range(rails):
        for j in range(len(cipher)):

            if rail_matrix[i][j] == "*":
                rail_matrix[i][j] = cipher[index]
                index += 1

    # Step 3: Read matrix in zig-zag manner
    result = ""

    row = 0
    direction = 1

    for col in range(len(cipher)):

        result = result + rail_matrix[row][col]

        if row == 0:
            direction = 1

        elif row == rails - 1:
            direction = -1

        row = row + direction

    return result


# ---------------- MAIN PROGRAM ----------------

message = input("Enter message: ")
rails = int(input("Enter number of rails: "))

cipher_text = encrypt(message, rails)

print("\nEncrypted Text:", cipher_text)

plain_text = decrypt(cipher_text, rails)

print("Decrypted Text:", plain_text)