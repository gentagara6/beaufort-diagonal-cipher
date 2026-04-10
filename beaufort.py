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

if __name__=="__main__":
    plaintext="HELLO WORLD"
    key="KEY"
    print("Beaufort Cipher Demo")
    print(f"Plaintext  : {plaintext}")
    print(f"Key        : {key}")
    encrypted =encrypt_beaufort(plaintext,key)
    print(f"Beaufort   : {encrypted}")