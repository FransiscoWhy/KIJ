def vigenere_cipher(text, key, mode='encrypt'):
    result = ""  # Membuat variabel untuk menyimpan hasil enkripsi atau dekripsi
    key_length = len(key)  # Menghitung panjang kata kunci

    for i in range(len(text)):  # Loop melalui setiap karakter dalam teks
        char = text[i]  # Mengambil karakter saat ini dalam teks dan menyimpannya dalam variabel 'char'
        if char.isalpha():  # Memeriksa apakah karakter saat ini adalah huruf alfabet
            is_upper = char.isupper()  # Memeriksa apakah karakter saat ini adalah huruf besar
            char = char.lower()  # Mengubah karakter menjadi huruf kecil agar lebih mudah dikelola

            key_char = key[i % key_length].lower()  # Mengambil karakter yang sesuai dari kata kunci dan mengubahnya menjadi huruf kecil

            if mode == 'encrypt':  # Memeriksa mode operasi (enkripsi atau dekripsi)
                # Langkah enkripsi: menghitung pergeseran karakter
                shifted_char = chr(((ord(char) + ord(key_char) - 2 * ord('a')) % 26) + ord('a'))
            else:  # mode == 'decrypt'
                # Langkah dekripsi: menghitung pergeseran yang berlawanan
                shifted_char = chr(((ord(char) - ord(key_char) + 26) % 26) + ord('a'))

            if is_upper:  # Jika karakter asli adalah huruf besar
                shifted_char = shifted_char.upper()  # Mengubah karakter terenkripsi atau terdekripsi kembali menjadi huruf besar

            result += shifted_char  # Menambahkan karakter terenkripsi atau terdekripsi ke 'result'
        else:
            result += char  # Jika karakter saat ini bukan huruf alfabet, menambahkannya ke 'result' tanpa perubahan

    return result  # Mengembalikan hasil enkripsi atau dekripsi sebagai output dari fungsi 'vigenere_cipher'

def main():
    plain_text = input("Masukkan teks: ")  # Meminta pengguna untuk memasukkan teks
    key = input("Masukkan kunci: ")  # Meminta pengguna untuk memasukkan kata kunci
    mode = input("Enkripsi (e) atau Dekripsi (d): ").lower()  # Meminta pengguna untuk memasukkan mode (enkripsi atau dekripsi)

    if mode == 'e':  # Jika mode adalah 'e' (enkripsi)
        result = vigenere_cipher(plain_text, key, 'encrypt')  # Memanggil fungsi enkripsi dan menyimpan hasilnya di 'result'
        print("Hasil Enkripsi: ", result)  # Menampilkan hasil enkripsi ke layar
    elif mode == 'd':  # Jika mode adalah 'd' (dekripsi)
        result = vigenere_cipher(plain_text, key, 'decrypt')  # Memanggil fungsi dekripsi dan menyimpan hasilnya di 'result'
        print("Hasil Dekripsi: ", result)  # Menampilkan hasil dekripsi ke layar
    else:
        print("Mode tidak valid. Pilih 'e' untuk enkripsi atau 'd' untuk dekripsi.")  # Menampilkan pesan kesalahan jika mode tidak valid

if __name__ == "__main__":
    main()  # Memanggil fungsi 'main' saat program dijalankan
