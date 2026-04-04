from diagonal import encrypt_diagonal

text = input("Enter text to encrypt: ")
cols = int(input("Enter number of columns: "))

ciphertext = encrypt_diagonal(text, cols)

print("Encrypted text:", ciphertext)