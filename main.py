from beaufort import encrypt_beaufort, decrypt_beaufort
from diagonal import encrypt_diagonal, decrypt_diagonal

def menu():
    print("\n=== Beaufort and Diagonal Transposition Cipher ===")
    print("1. Beaufort Encrypt")
    print("2. Beaufort Decrypt")
    print("3. Diagonal Encrypt")
    print("4. Diagonal Decrypt")
    print("0. Exit")


def main():
    while True:
        menu()
        choice = input("Zgjedh opsionin: ")

        if choice in ["1", "2"]:
            text = input("Text: ")
            key = input("Key: ")

            if not key or not key.isalpha():
                print("Gabim: Celesi duhet vetem me shkronja!")
                continue

            if choice == "1":
                print("Encrypted:", encrypt_beaufort(text, key))
            else:
                print("Decrypted:", decrypt_beaufort(text, key))

        elif choice in ["3", "4"]:
            text = input("Text: ")
            cols = input("Columns: ")

            if not cols.isdigit() or int(cols) <= 0:
                print("Gabim: Numri i kolonave duhet te jete nje numer pozitiv!")
                continue

            cols = int(cols)

            if choice == "3":
                print("Encrypted:", encrypt_diagonal(text, cols))
            else:
                print("Decrypted:", decrypt_diagonal(text, cols))

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Opsioni i pavlefshem!")

if __name__ == "__main__":
    main()
