import math

def pad_text(text, cols):
    text = text.replace(" ", "")
    rows = math.ceil(len(text) / cols)
    return text + "X" * (rows * cols - len(text))


def create_matrix(text, cols):
    text = pad_text(text, cols)
    rows = len(text) // cols

    matrix = []
    index = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(text[index])
            index += 1
        matrix.append(row)
        
    return matrix


def encrypt_diagonal(text, cols):
    matrix = create_matrix(text, cols)
    rows = len(matrix)

    result = []

    for col_start in range(cols):
        i, j = 0, col_start
        while i < rows and j < cols:
            result.append(matrix[i][j])
            i += 1
            j += 1

    for row_start in range(1, rows):
        i, j = row_start, 0
        while i < rows and j < cols:
            result.append(matrix[i][j])
            i += 1
            j += 1

    return "".join(result)

def decrypt_diagonal(ciphertext, cols):
    length = len(ciphertext)
    rows = math.ceil(length/cols)

    matrix = [[None for _ in range(cols)] for _ in range(rows)]
    index = 0

    for col_start in range(cols):
        i, j = 0, col_start
        while i < rows and j < cols:
            matrix[i][j] = ciphertext[index]
            index += 1
            i += 1
            j += 1

    for row_start in range(1, rows):
        i,j = row_start, 0
        while i < rows and j < cols:
            matrix[i][j] = ciphertext[index]
            index += 1
            i += 1
            j += 1
    
    plaintext = ""
    for row in matrix:
        plaintext += ''.join(row)

    return plaintext.rstrip('X')