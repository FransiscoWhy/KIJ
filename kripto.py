def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key_length = len(key)
    
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            key_char = key[i % key_length].lower()
            
            if mode == 'encrypt':
                shifted_char = chr(((ord(char) + ord(key_char) - 2 * ord('a')) % 26) + ord('a'))
            else:  # mode == 'decrypt'
                shifted_char = chr(((ord(char) - ord(key_char) + 26) % 26) + ord('a'))
            
            if is_upper:
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    
    return result

def main():
    plain_text = input("Masukkan teks: ")
    key = input("Masukkan kunci: ")
    mode = input("Enkripsi (e) atau Dekripsi (d): ").lower()

    if mode == 'e':
        result = vigenere_cipher(plain_text, key, 'encrypt')
        print("Hasil Enkripsi: ", result)
    elif mode == 'd':
        result = vigenere_cipher(plain_text, key, 'decrypt')
        print("Hasil Dekripsi: ", result)
    else:
        print("Mode tidak valid. Pilih 'e' untuk enkripsi atau 'd' untuk dekripsi.")

if __name__ == "__main__":
    main()


