import math

def pad_text(text, cols):
    while len(text) % cols != 0:
        text += 'X'
    return text


def create_matrix(text, cols):
    rows = math.ceil(len(text) / cols)
    text = pad_text(text, cols)

    matrix = []
    index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(text[index])
            index += 1
        matrix.append(row)
    return matrix


def encrypt_diagonal(text, cols):
    text = text.upper().replace(" ", "")
    matrix = create_matrix(text, cols)

    rows = len(matrix)
    result = ""

    for d in range(rows + cols - 1):
        for i in range(rows):
            j = d - i
            if 0 <= j < cols:
                result += matrix[i][j]

    return result