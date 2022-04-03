# Puzzearch-15: Penyelesaian Persoalan 15-Puzzle dengan Algoritma _Branch and Bound_

> Implementasi algoritma _branch and bound_ untuk melakukan penyelesaian persoalan 15-puzzle
> dalam bentuk CLI dan GUI sebagai Tugas Kecil 2 Mata Kuliah IF2211 Strategi Algoritma

![gifstima](https://user-images.githubusercontent.com/71161031/161412029-ef911e65-a318-4a40-b3fe-cbf30e536a11.gif)



## Daftar Isi
- [Deskripsi Singkat](#deskripsi-singkat)
- [Requirements](#requirements)
- [Kompilasi](#kompilasi)
- [Penggunaan](#penggunaan)
- [Identitas](#identitas)

## Deskripsi Singkat
Program ini dibuat menggunakan bahasa Python untuk menyelesaikan persoalan 15-Puzzle dengan 
menggunakan algoritma _branch and bound_ seperti pada materi kuliah. Nilai bound tiap 
simpul adalah penjumlahan cost yang diperlukan untuk sampai suatu simpul x dari akar, 
dengan taksiran cost simpul x untuk sampai ke goal. Taksiran cost yang digunakan adalah 
jumlah ubin tidak kosong yang tidak berada pada tempat sesuai susunan akhir (goal state).

Program ini dapat menentukan apakah posisi awal suatu masukan dapat diselesaikan hingga 
mencapai susunan akhir, dengan mengimplementasikan fungsi Kurang(i) dan posisi ubin 
kosong di kondisi awal (X), seperti pada materi kuliah. Jika posisi awal tidak bisa mencapai 
susunan akhir, program akan menampilkan pesan tidak bisa diselesaikan,. Jika dapat 
diselesaikan, program dapat menampilkan urutan matriks rute (path) aksi yang dilakukan dari 
posisi awal ke susunan akhir. 


## Requirements
**[RECOMMENDED]**
- Python 3.9.4 64-bit

## Kompilasi
1. Pastikan berada di folder `src` (`root/src/lib`)
2. Untuk menjalankan CLI, lakukan kompilasi dengan command:
    ```py
    python main.py
    ```
    Sementara itu, untuk menjalankan GUI, lakukan kompilasi dengan command:
    ```py
    python gui.py
    ```
## Penggunaan
**[IMPORTANT]** Karena penggunaan heuristik berbasis _mismatched tiles_ tidak efisien, maka tidak semua persoalan dapat diselesaikan. _Testcases_ yang diberikan di _repository_ dapat diselesaikan dalam _scope_ waktu di bawah 1 detik, namun dalam beberapa kasus, suatu _testcase_ dapat diselesaikan dalam waktu di atas 30 detik.

### Penggunaan CLI
![image](https://user-images.githubusercontent.com/71161031/161386711-3646e805-dd7e-4c68-bab1-eba1ab94aa17.png)

1. Pengguna dapat memilih ingin memasukkan melalui _text file_ atau _input_ pengguna.
    - Pilih opsi [1] untuk melakukan input melalui _text file_. Masukkan nama file **tanpa ekstensi .txt**. Pastikan juga file **berada pada folder test** dan kompilasi dilakukan dari folder src.
    - Pilih opsi [2] untuk melakukan input pengguna. Untuk input pengguna, pengguna memasukkan 4 angka per baris, dengan bagian kosong diisikan dengan karakter `-`. 
2. Akan muncul daftar nilai `kurang[i]` serta total penjumlahan `kurang[i] + x`. Setelah itu, program akan mencoba menelusuri _puzzle states_ hingga ditemukan jalur yang ditemukan.
3. Program akan memberikan keluaran urutan gerakan yang harus diambil!

### Penggunaan GUI
![image](https://user-images.githubusercontent.com/71161031/161387117-e3e7a3dd-483c-4815-9d5e-47fb23fd55cf.png)
1. Pengguna dapat memilih ingin memasukkan melalui _text file_ atau _input_ pengguna.
    - Untuk _text file_, masukkan nama file **tanpa ekstensi .txt** pada _textbox_. Pengguna juga dapat memilih _delay_ waktu animasi pada _textbox_ bagian kanan (nilai default = 0.5s)
    - Untuk input pengguna, pengguna dapat langsung memasukkan nilai yang diinginkan ke dalam tabel.
    > **[IMPORTANT]** Apabila waktu pencarian memakan waktu yang lama, program tidak merespon karena program mengandalkan algoritma dalam `algo.py`
    > Selain itu, program akan mengutamakan input _text file_. Apabila pengguna memasukkan opsi via tabel dan memasukkan nama file, maka yang akan dicek adalah nama file.
    
2. Akan muncul daftar nilai `kurang[i]` serta total penjumlahan `kurang[i] + x`. Setelah itu, program akan mencoba menelusuri _puzzle states_ hingga ditemukan jalur yang ditemukan.
3. Program akan menampilkan urutan gerakan yang harus diambil dan informasi pencarian!

## Identitas
13520124 - Owen Christian Wijaya
