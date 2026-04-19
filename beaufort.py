def prepare_text(text):
    return text.upper().replace(" ", "")

def generate_key_stream(text,key):
    key =prepare_text(key)
    return(key*((len(text)//len(key))+1))[:len(text)]

def encrypt_beaufort(text,key):
    text=prepare_text(text)
    key_stream=generate_key_stream(text,key)
    ciphertext=[]
    for p_char, k_char in zip(text, key_stream):
        if not p_char.isalpha():
            ciphertext.append(p_char)
            continue
        p = ord(p_char) - ord('A')
        k = ord(k_char) - ord('A')
        c = (k - p) % 26
        ciphertext.append(chr(c + ord('A')))
    return "".join(ciphertext)

def decrypt_beaufort(ciphertext, key):
    
    plaintext = ""
    ciphertext = prepare_text(ciphertext)
    key = key.upper()

    key_index = 0  

    for char in ciphertext:
        if char.isalpha():
            c_val = ord(char) - ord('A')
            k_val = ord(key[key_index % len(key)])- ord('A')

            m_val = (k_val - c_val) % 26

            plaintext += chr(m_val + ord('A'))

            key_index += 1
        else:
            plaintext += char

    return plaintext

