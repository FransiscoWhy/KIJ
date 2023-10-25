def vigenere_cipher(text, key, mode='encrypt'):: Ini adalah deklarasi fungsi vigenere_cipher yang mengambil tiga argumen: text (teks yang akan dienkripsi atau didekripsi), key (kata kunci), dan mode (mode operasi yang dapat berisi 'encrypt' atau 'decrypt', dengan nilai default 'encrypt').

result = "": Membuat variabel result yang awalnya kosong untuk menyimpan hasil enkripsi atau dekripsi.

key_length = len(key): Menghitung panjang kata kunci yang akan digunakan dalam proses enkripsi atau dekripsi.

for i in range(len(text)):: Memulai loop untuk mengakses setiap karakter dalam teks yang akan dienkripsi atau didekripsi.

char = text[i]: Mengambil karakter saat ini dalam teks dan menyimpannya dalam variabel char.

if char.isalpha():: Memeriksa apakah karakter saat ini adalah huruf alfabet.

is_upper = char.isupper(): Memeriksa apakah karakter saat ini adalah huruf besar dan menyimpan hasilnya dalam variabel is_upper.

char = char.lower(): Mengubah karakter menjadi huruf kecil agar lebih mudah dikelola, karena Vigenere Cipher menganggap semua karakter sebagai huruf kecil.

key_char = key[i % key_length].lower(): Mengambil karakter yang sesuai dari kata kunci, dengan kata kunci yang diulang-ulang untuk cocok dengan panjang teks, dan mengubahnya menjadi huruf kecil.

if mode == 'encrypt':: Memeriksa mode operasi. Jika mode adalah 'encrypt', maka kode berikut akan dijalankan.

shifted_char = chr(((ord(char) + ord(key_char) - 2 * ord('a')) % 26) + ord('a')): Ini adalah langkah enkripsi. Kami menghitung pergeseran karakter menggunakan rumus Vigenere Cipher. Kami menambahkan karakter teks dengan karakter kata kunci, mengurangi dua kali nilai kode huruf 'a', dan kemudian mengambil hasil modulus 26 dan menambahkannya lagi dengan kode huruf 'a'.

else: # mode == 'decrypt': Jika mode adalah 'decrypt', maka kode berikut ini yang akan dijalankan.

shifted_char = chr(((ord(char) - ord(key_char) + 26) % 26) + ord('a')): Ini adalah langkah dekripsi. Kami menghitung pergeseran karakter yang berlawanan dengan langkah enkripsi, menggunakan rumus yang sama.

if is_upper:: Jika karakter asli adalah huruf besar, maka kode berikut ini akan dijalankan.

shifted_char = shifted_char.upper(): Kami mengubah karakter terenkripsi atau terdekripsi kembali menjadi huruf besar jika karakter asli adalah huruf besar.

result += shifted_char: Hasil enkripsi atau dekripsi ditambahkan ke variabel result.

else:: Jika karakter saat ini bukan huruf alfabet, maka karakter tersebut ditambahkan ke variabel result tanpa perubahan.

return result: Hasil enkripsi atau dekripsi dikembalikan sebagai output dari fungsi vigenere_cipher.
