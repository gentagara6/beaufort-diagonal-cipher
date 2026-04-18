import math

def pad_text(text, cols):
    text = text.replace(" ", "")
    while len(text) % cols != 0:
        text += 'X'
    return text


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
    cols = len(matrix[0]) 

    result = []

    for start_col in range(cols):
        i, j = 0, start_col
        while i < rows and j >= 0:
            result.append(matrix[i][j])
            i += 1
            j -= 1

    for start_row in range(1, rows):
        i, j = start_row, cols - 1
        while i < rows and j >= 0:
            result.append(matrix[i][j])
            i += 1
            j -= 1

    return "".join(result)

def decrypt_diagonal(ciphertext, cols):
    length = len(ciphertext)
    rows = math.ceil(length/cols)

    matrix = [[''for _ in range(cols)]for _ in range(rows)]

    index = 0

    for start_col in range(cols):
        i,j = 0, start_col
        while i< rows and j >= 0:
            if index < length:
                matrix[i][j] = ciphertext[index]
                index += 1
            i += 1
            j -= 1

    for start_row in range(1, rows):
        i,j = start_row, cols - 1
        while i < rows and j >= 0:
            if index < length:
                matrix[i][j] = ciphertext[index]
                index += 1
            i += 1
            j -= 1
    
    plaintext = ""
    for row in matrix:
        plaintext += ''.join(row)

    return plaintext.rstrip('X')