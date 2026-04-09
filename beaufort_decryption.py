# Implementimi i dekriptimit Beaufort Cipher
# Pershkrim: Ky program dekripton tekst duke perdorur algoritmin Beaufort.


def dekriptimi_beaufort(ciphertext, key):
    """
    Realizon dekriptimin e shifres Beaufort.
    Formula: M = (K - C) mod 26.

    Parametrat:
    ciphertext (str): Teksti i shifruar.
    key (str): Celesi i perdorur.

    Kthen:
    str: Teksti i dekriptuar (plaintext).
    """

    plaintext = ""

    # Konvertojme tekstin dhe celesin ne shkronja te medha
    ciphertext = ciphertext.upper()
    key = key.upper()

    key_index = 0  # Indeksi per levizjen neper celes

    for char in ciphertext:
        if char.isalpha():
            # Marrim vlerat numerike (A=0, B=1, ..., Z=25)
            c_val = ord(char) - ord('A')
            k_val = ord(key[key_index % len(key)]) - ord('A')

            # Formula Beaufort: (Celesi - Ciphertext) mod 26
            # Perdoret modulo 26 per me qendru brenda alfabetit A-Z
            m_val = (k_val - c_val) % 26

            # Kthejme vleren numerike ne shkronje
            plaintext += chr(m_val + ord('A'))

            # Kalojme te shkronja tjeter e celesit
            key_index += 1
        else:
            # Karakteret jo-shkronja mbeten te njejta
            plaintext += char

    return plaintext


def main():
    print("--- Moduli i Dekriptimit Beaufort ---")

    # Marrja e inputit nga perdoruesi
    teksti = input("Shkruani tekstin per dekriptim: ")
    celesi = input("Shkruani celesin: ")

    # Kontrollojme qe celesi permban vetem shkronja
    if not celesi.isalpha():
        print("Gabim: Celesi duhet te permbaje vetem shkronja!")
        return

    # Thirrja e funksionit per dekriptim
    rezultati = dekriptimi_beaufort(teksti, celesi)

    # Shfaqja e rezultateve
    print("\n---------------------------")
    print(f"Teksti i shifruar: {teksti}")
    print(f"Celesi i perdorur: {celesi}")
    print(f"Teksti i dekriptuar: {rezultati}")
    print("---------------------------")


# Pika hyrëse e programit
if __name__ == "__main__":
    main()


  


                                             
    
    
