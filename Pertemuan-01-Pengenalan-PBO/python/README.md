# 🐍 Praktik Python — Pertemuan 01: Pengenalan PBO & Persiapan Alat

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 01](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

Halaman ini punya dua misi. Pertama, **memanaskan kembali** dasar-dasar Python yang akan terus kita pakai: variabel, percabangan, perulangan, list, dan fungsi. Kedua, **membedah KedaiKita versi prosedural** untuk melihat sendiri masalahnya, lalu mengintip versi berorientasi objeknya.

> [!TIP]
> Sudah lancar Python? Kamu boleh membaca cepat bagian 1 sampai 5. Namun, jangan lewatkan bagian 6 dan 7, karena di sanalah inti pertemuan ini.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Program Pertama dan Struktur File](#1-program-pertama-dan-struktur-file)
2. [Variabel dan Tipe Data](#2-variabel-dan-tipe-data)
3. [Percabangan dan Perulangan](#3-percabangan-dan-perulangan)
4. [List: Menyimpan Banyak Data](#4-list-menyimpan-banyak-data)
5. [Fungsi dengan Parameter dan Nilai Kembalian](#5-fungsi-dengan-parameter-dan-nilai-kembalian)
6. [Data Paralel: Rapi tetapi Rapuh](#6-data-paralel-rapi-tetapi-rapuh)
7. [Studi Kasus KedaiKita](#7-studi-kasus-kedaikita)
8. [Kesalahan Umum dan Cara Membaca Pesan Error](#8-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

### Cek instalasi Python

Buka terminal. Di Windows, pakai **Command Prompt** atau **PowerShell**. Di macOS/Linux, pakai **Terminal**. Kamu juga bisa memakai terminal bawaan VS Code (menu *Terminal → New Terminal*). Lalu ketik:

```bash
python --version
```

Jika Python sudah terpasang, akan muncul nomor versinya, misalnya `Python 3.12.4`. Pastikan versinya **3.10 atau lebih baru**.

> [!NOTE]
> - Di macOS/Linux, gunakan `python3` sebagai ganti `python`, misalnya `python3 --version`.
> - Di Windows, jika perintah `python` malah membuka Microsoft Store atau muncul pesan bahwa perintah tidak dikenali, berarti Python belum terpasang dengan benar. Ikuti panduan [00-Persiapan](../../00-Persiapan/README.md).

### Struktur folder

```text
python/
├── contoh/          <- 6 contoh kecil untuk pemanasan dasar Python
├── studi-kasus/     <- KedaiKita versi prosedural dan versi objek
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

### Cara menjalankan program

Pindah dulu ke folder tempat file berada dengan perintah `cd` (*change directory*), lalu jalankan file-nya:

```bash
cd Pertemuan-01-Pengenalan-PBO/python/contoh
python contoh01_halo.py
```

Jika memakai VS Code, buka file `.py`-nya lalu klik tombol ▶ (*Run Python File*) di pojok kanan atas.

Saran belajar: **ketik ulang** kodenya, jangan hanya menyalin. Jari yang mengetik membantu otak mengingat.

## 1. Program Pertama dan Struktur File

File: [`contoh/contoh01_halo.py`](contoh/contoh01_halo.py)

```python
def main():  # [1] fungsi utama: tempat perintah-perintah kita
    print("=== PROGRAM PERTAMAKU ===")  # [2] print menampilkan teks ke layar
    print("Halo, Samarinda!")
    print("Selamat datang di mata kuliah PBO 2026.")
    print()  # [3] print tanpa isi = baris kosong
    # [4] baris yang diawali tanda pagar adalah komentar, tidak dijalankan
    print("Perintah dijalankan berurutan dari atas ke bawah:")
    print("Langkah 1: siapkan alat")
    print("Langkah 2: tulis kode")
    print("Langkah 3: jalankan program")


if __name__ == "__main__":  # [5] pintu masuk: benar jika file ini dijalankan langsung
    main()  # [6] memanggil fungsi main
```

**Output:**

```text
=== PROGRAM PERTAMAKU ===
Halo, Samarinda!
Selamat datang di mata kuliah PBO 2026.

Perintah dijalankan berurutan dari atas ke bawah:
Langkah 1: siapkan alat
Langkah 2: tulis kode
Langkah 3: jalankan program
```

Penjelasan:

- **[1]** `def main():` mendefinisikan fungsi bernama `main`. Semua baris di bawahnya yang **menjorok ke dalam** (indentasi 4 spasi) adalah isi fungsi ini. Nama `main` (utama) hanyalah kesepakatan, tetapi kita akan selalu memakainya.
- **[2]** `print(...)` menampilkan teks di dalam tanda kurung ke layar, lalu pindah ke baris berikutnya. Teks diapit tanda kutip.
- **[3]** `print()` tanpa isi mencetak baris kosong. Gunanya memberi jarak antarbagian output.
- **[4]** Baris yang diawali `#` adalah **komentar**, yaitu catatan untuk manusia yang diabaikan Python. Teks di antara tiga tanda kutip `"""` di awal file juga berfungsi sebagai catatan dan disebut *docstring*.
- **[5]** Inilah **pintu masuk** program. Saat file dijalankan langsung, Python mengisi variabel khusus `__name__` dengan teks `"__main__"`, sehingga kondisi ini benar.
- **[6]** Karena kondisinya benar, `main()` dipanggil. Perintah di dalamnya dijalankan **berurutan dari atas ke bawah**. Inilah ciri khas gaya prosedural.

Struktur berikut akan kamu temui di **semua** program Python mata kuliah ini:

```text
"""                                    <- docstring: penjelasan isi file
Contoh 01 - Program Pertamaku             dan cara menjalankannya
...
"""


def main():                            <- fungsi utama
    print("Halo, Samarinda!")          <- isi fungsi menjorok 4 spasi


if __name__ == "__main__":             <- pintu masuk program
    main()                             <- panggil fungsi main
```

Mengapa repot memakai `main()`? Python sebenarnya bisa menjalankan perintah yang ditulis langsung tanpa fungsi. Namun, dengan `main()` program menjadi rapi, karena ada **satu tempat yang jelas** di mana program dimulai. Selain itu, mulai Pertemuan 05 kita memecah program ke beberapa file. Saat sebuah file dipakai (di-*import*) oleh file lain, `__name__` berisi nama modulnya (nama file tanpa `.py`), bukan `"__main__"`, sehingga `main()` tidak ikut berjalan tanpa sengaja.

> [!IMPORTANT]
> Python memakai **indentasi** (spasi di awal baris) untuk menandai blok kode. Baris-baris yang menjorok sama dalam berada di blok yang sama. Gunakan **4 spasi** per tingkat dan jangan mencampur spasi dengan tombol Tab. VS Code biasanya sudah mengaturnya secara otomatis.

> [!TIP]
> **Coba sendiri:** ganti baris `main()` paling bawah dengan `pass` (perintah yang artinya "tidak melakukan apa-apa"), lalu jalankan. Tebak dulu: apa yang tercetak?

<details>
<summary>Lihat jawaban</summary>

Tidak ada yang tercetak, dan tidak ada error. Fungsi `main` memang didefinisikan, tetapi tidak pernah **dipanggil**. Mendefinisikan fungsi itu seperti menulis resep: masakannya belum jadi sebelum resepnya dijalankan.

</details>

## 2. Variabel dan Tipe Data

File: [`contoh/contoh02_variabel_dan_tipe.py`](contoh/contoh02_variabel_dan_tipe.py)

Variabel adalah "kotak bernama" untuk menyimpan nilai. Di Python, kamu cukup menulis `nama = nilai`, dan tipe variabel mengikuti nilai yang disimpan.

```python
def main():
    # [1] variabel dibuat saat pertama kali diisi; tipenya mengikuti nilainya
    nama = "Ayu Lestari"  # str: teks, diapit tanda kutip
    inisial = "A"  # str juga (Python tidak punya tipe khusus untuk satu huruf)
    semester = 3  # int: bilangan bulat
    ipk = 3.75  # float: bilangan pecahan, memakai TITIK desimal

    print("=== DATA MAHASISWA ===")
    print(f"Nama     : {nama}")  # [2] f-string: nilai di dalam {} ikut dicetak
    print(f"Inisial  : {inisial}")
    print(f"Semester : {semester}")
    print(f"IPK      : {ipk}")

    print()
    print("=== HITUNG UANG JAJAN ===")
    uang_saku = 50000
    harga_kopi = 18000
    jumlah_cup = uang_saku // harga_kopi  # [3] // pembagian bulat (sisanya dibuang)
    sisa_uang = uang_saku % harga_kopi  # [4] % sisa hasil bagi
    print(f"Uang saku     : Rp{uang_saku}")
    print(f"Harga kopi    : Rp{harga_kopi}")
    print(f"Bisa beli     : {jumlah_cup} cup")
    print(f"Total belanja : Rp{jumlah_cup * harga_kopi}")  # [5] boleh berisi hitungan
    print(f"Sisa uang     : Rp{sisa_uang}")

    print()
    print("=== MENGUBAH NILAI VARIABEL ===")
    semester = semester + 1  # [6] nilai lama diganti dengan nilai baru
    print(f"Semester depan {nama} masuk semester {semester}")
```

**Output:**

```text
=== DATA MAHASISWA ===
Nama     : Ayu Lestari
Inisial  : A
Semester : 3
IPK      : 3.75

=== HITUNG UANG JAJAN ===
Uang saku     : Rp50000
Harga kopi    : Rp18000
Bisa beli     : 2 cup
Total belanja : Rp36000
Sisa uang     : Rp14000

=== MENGUBAH NILAI VARIABEL ===
Semester depan Ayu Lestari masuk semester 4
```

Penjelasan:

- **[1]** Tanda `=` berarti **mengisi**, bukan "sama dengan" seperti di matematika. Nilai di sebelah kanan disimpan ke variabel di sebelah kiri. Python menentukan tipenya dari nilai: teks dalam tanda kutip menjadi `str`, bilangan bulat menjadi `int`, dan bilangan pecahan yang ditulis dengan **titik** (misalnya `3.75`, bukan `3,75`) menjadi `float`.
- **[2]** *f-string* adalah teks yang diawali huruf `f`. Apa pun yang ditulis di dalam kurung kurawal `{}` diganti dengan nilainya.
- **[3]** `//` adalah pembagian bulat: `50000 // 18000` hasilnya `2`, sisanya dibuang.
- **[4]** `%` (modulo) menghasilkan sisa hasil bagi: `50000 % 18000` hasilnya `14000`.
- **[5]** Di dalam `{}` boleh ada perhitungan, misalnya `{jumlah_cup * harga_kopi}`.
- **[6]** Nilai variabel bisa diubah kapan saja. `semester = semester + 1` dibaca: "ambil nilai `semester` sekarang, tambah 1, lalu simpan kembali ke `semester`".

Tipe data dasar yang akan sering kita pakai:

| Tipe | Isi | Contoh nilai |
|---|---|---|
| `int` | bilangan bulat | `3`, `18000`, `-5` |
| `float` | bilangan pecahan (memakai titik) | `3.75`, `0.5` |
| `str` | teks (*string*) | `"Ayu Lestari"`, `"A"` |
| `bool` | benar atau salah | `True`, `False` (dipakai di bagian 3) |

Operator aritmetika:

| Operator | Arti | Contoh | Hasil |
|---|---|---|---|
| `+` `-` `*` | tambah, kurang, kali | `3 * 4` | `12` |
| `/` | bagi, hasilnya selalu pecahan | `7 / 2` | `3.5` |
| `//` | bagi bulat | `7 // 2` | `3` |
| `%` | sisa bagi | `7 % 2` | `1` |
| `**` | pangkat | `2 ** 3` | `8` |

> [!IMPORTANT]
> Di seluruh materi ini, **uang selalu disimpan sebagai bilangan bulat** (Rupiah), tidak pernah sebagai `float`. Bilangan pecahan disimpan komputer dalam bentuk biner, sehingga kadang tidak tepat: `0.1 + 0.2` menghasilkan `0.30000000000000004`. Untuk menghitung persen, gunakan pola `nilai * persen // 100`.

Aturan memberi nama variabel:

- Gunakan gaya **snake_case**: huruf kecil, antarkata dipisah garis bawah, misalnya `uang_saku` atau `harga_kopi`.
- Huruf besar dan kecil dibedakan: `nama` dan `Nama` adalah dua variabel yang berbeda.
- Nama tidak boleh diawali angka dan tidak boleh mengandung spasi.

> [!TIP]
> **Coba sendiri:** tambahkan `print(type(ipk))` di akhir `main()`. Python akan mencetak `<class 'float'>`. Perhatikan kata **class** di situ! Di Python, setiap nilai, termasuk angka dan teks, sebenarnya adalah **objek** dari sebuah kelas. Artinya akan kita pahami mulai Pertemuan 02.

## 3. Percabangan dan Perulangan

File: [`contoh/contoh03_percabangan_perulangan.py`](contoh/contoh03_percabangan_perulangan.py)

```python
def main():
    print("=== PERCABANGAN: DISKON TOKO ALAT TULIS ===")
    total_belanja = 120000
    member = True  # [1] bool: hanya bernilai True atau False

    if total_belanja >= 100000:  # [2] diperiksa dari atas; yang pertama benar dipilih
        persen_diskon = 10
    elif total_belanja >= 50000:
        persen_diskon = 5
    else:
        persen_diskon = 0

    if member:  # [3] kondisi berupa variabel bool
        persen_diskon = persen_diskon + 5

    potongan = total_belanja * persen_diskon // 100
    print(f"Total belanja : Rp{total_belanja}")
    print(f"Diskon        : {persen_diskon}%")
    print(f"Potongan      : Rp{potongan}")
    print(f"Harus dibayar : Rp{total_belanja - potongan}")

    hari = "Sabtu"
    if hari == "Sabtu" or hari == "Minggu":  # [4] or: cukup salah satu yang benar
        print(f"Hari {hari}: toko tutup pukul 15.00")
    else:
        print(f"Hari {hari}: toko tutup pukul 21.00")

    print()
    print("=== PERULANGAN FOR: DAFTAR HARGA FOTOKOPI ===")
    harga_per_lembar = 500
    for lembar in range(1, 6):  # [5] range(1, 6) menghasilkan 1, 2, 3, 4, 5
        print(f"{lembar} lembar = Rp{lembar * harga_per_lembar}")

    print()
    print("=== PERULANGAN WHILE: MENABUNG UNTUK BUKU ===")
    target = 100000
    tabungan = 0
    minggu = 0
    while tabungan < target:  # [6] diulang SELAMA kondisinya benar
        tabungan = tabungan + 30000
        minggu = minggu + 1
        print(f"Minggu ke-{minggu}: tabungan Rp{tabungan}")
    print(f"Target Rp{target} tercapai dalam {minggu} minggu")
```

**Output:**

```text
=== PERCABANGAN: DISKON TOKO ALAT TULIS ===
Total belanja : Rp120000
Diskon        : 15%
Potongan      : Rp18000
Harus dibayar : Rp102000
Hari Sabtu: toko tutup pukul 15.00

=== PERULANGAN FOR: DAFTAR HARGA FOTOKOPI ===
1 lembar = Rp500
2 lembar = Rp1000
3 lembar = Rp1500
4 lembar = Rp2000
5 lembar = Rp2500

=== PERULANGAN WHILE: MENABUNG UNTUK BUKU ===
Minggu ke-1: tabungan Rp30000
Minggu ke-2: tabungan Rp60000
Minggu ke-3: tabungan Rp90000
Minggu ke-4: tabungan Rp120000
Target Rp100000 tercapai dalam 4 minggu
```

Penjelasan:

- **[1]** Tipe `bool` hanya punya dua nilai: `True` dan `False`. Huruf awalnya wajib kapital.
- **[2]** `if`, `elif` (singkatan *else if*), dan `else` diperiksa dari atas ke bawah. Begitu ada kondisi yang benar, bloknya dijalankan dan sisanya dilewati. Total 120000 sudah memenuhi syarat pertama, jadi diskonnya 10.
- **[3]** Kondisi boleh berupa variabel `bool` secara langsung. `if member:` artinya "jika `member` bernilai `True`". Diskon bertambah 5, menjadi 15.
- **[4]** `or` bernilai benar jika **salah satu** syarat benar. Ada juga `and` (kedua syarat harus benar) dan `not` (membalik benar menjadi salah).
- **[5]** `for lembar in range(1, 6):` mengulang blok untuk `lembar` = 1, 2, 3, 4, 5. Angka akhir (6) **tidak** ikut.
- **[6]** `while` mengulang **selama** kondisinya benar. Setelah minggu ke-4, tabungan menjadi 120000. Kondisi `tabungan < target` menjadi salah, dan perulangan berhenti.

Operator perbandingan dan logika:

| Operator | Arti | Contoh |
|---|---|---|
| `==` | sama dengan | `hari == "Sabtu"` |
| `!=` | tidak sama dengan | `hari != "Minggu"` |
| `<` `>` | kurang dari, lebih dari | `tabungan < target` |
| `<=` `>=` | kurang dari atau sama dengan, lebih dari atau sama dengan | `total_belanja >= 100000` |
| `and` | kedua syarat harus benar | `member and total_belanja >= 100000` |
| `or` | salah satu syarat benar sudah cukup | `hari == "Sabtu" or hari == "Minggu"` |
| `not` | membalik nilai benar/salah | `not member` |

Bentuk-bentuk `range()`:

| Bentuk | Menghasilkan |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 |

> [!WARNING]
> Jangan tertukar antara `=` (mengisi) dan `==` (membandingkan). Menulis `if hari = "Sabtu":` menghasilkan `SyntaxError`, dan Python versi baru bahkan menyarankan: *Maybe you meant '==' ... instead of '='?*

> [!WARNING]
> Pada `while`, pastikan ada baris yang membuat kondisinya suatu saat menjadi salah. Jika baris `tabungan = tabungan + 30000` terhapus, tabungan tidak pernah bertambah dan perulangan berjalan **tanpa henti**. Hentikan program seperti itu dengan menekan **Ctrl+C** di terminal.

> [!TIP]
> **Coba sendiri:** ubah `total_belanja` menjadi `60000` dan `member` menjadi `False`. Tebak dulu berapa diskon, potongan, dan jumlah yang harus dibayar.

<details>
<summary>Lihat jawaban</summary>

Diskon 5% (karena 60000 ≥ 50000 dan bukan member), potongan Rp3000, dan yang harus dibayar Rp57000.

</details>

## 4. List: Menyimpan Banyak Data

File: [`contoh/contoh04_list.py`](contoh/contoh04_list.py)

Bayangkan menyimpan nilai kuis 40 mahasiswa dengan 40 variabel berbeda. Repot sekali! **List** menyimpan banyak nilai dalam satu variabel.

```python
def main():
    nilai = [78, 92, 65, 88, 70]  # [1] list berisi lima nilai kuis

    print("=== NILAI KUIS ===")
    print(f"Banyak data    : {len(nilai)}")  # [2] len() menghitung jumlah elemen
    print(f"Nilai pertama  : {nilai[0]}")  # [3] indeks pertama adalah 0
    print(f"Nilai terakhir : {nilai[len(nilai) - 1]}")  # indeks terakhir = len - 1

    print()
    print("=== SEMUA NILAI ===")
    for i in range(len(nilai)):  # [4] perulangan dengan indeks: i = 0, 1, 2, 3, 4
        print(f"Mahasiswa ke-{i + 1}: {nilai[i]}")

    total = 0
    tertinggi = nilai[0]
    for n in nilai:  # [5] perulangan langsung: n berisi setiap elemen bergantian
        total = total + n
        if n > tertinggi:
            tertinggi = n
    print(f"Total          : {total}")
    print(f"Rata-rata      : {total // len(nilai)}")  # dibulatkan ke bawah
    print(f"Tertinggi      : {tertinggi}")

    print()
    print("=== MENGUBAH DAN MENGURUTKAN ===")
    nilai[2] = 75  # [6] mengganti elemen di indeks 2 (elemen ketiga)
    print(f"Setelah nilai ke-3 diperbaiki: {nilai}")  # [7] mencetak seluruh list
    nilai.sort()  # [8] mengurutkan dari kecil ke besar
    print(f"Setelah diurutkan            : {nilai}")

    kota = ["Samarinda", "Balikpapan", "Bontang"]
    kota.sort()  # teks diurutkan sesuai abjad
    daftar_kota = ", ".join(kota)  # [9] menggabungkan isi list menjadi satu teks
    print(f"Kota urut abjad: {daftar_kota}")
```

**Output:**

```text
=== NILAI KUIS ===
Banyak data    : 5
Nilai pertama  : 78
Nilai terakhir : 70

=== SEMUA NILAI ===
Mahasiswa ke-1: 78
Mahasiswa ke-2: 92
Mahasiswa ke-3: 65
Mahasiswa ke-4: 88
Mahasiswa ke-5: 70
Total          : 393
Rata-rata      : 78
Tertinggi      : 92

=== MENGUBAH DAN MENGURUTKAN ===
Setelah nilai ke-3 diperbaiki: [78, 92, 75, 88, 70]
Setelah diurutkan            : [70, 75, 78, 88, 92]
Kota urut abjad: Balikpapan, Bontang, Samarinda
```

Setiap elemen list punya nomor urut yang disebut **indeks**, dimulai dari **0**:

```text
nilai  = [ 78,  92,  65,  88,  70 ]
indeks:    0    1    2    3    4
```

Penjelasan:

- **[1]** List ditulis dengan kurung siku `[ ]`, dan elemennya dipisah koma.
- **[2]** `len(nilai)` menghitung banyaknya elemen, yaitu 5.
- **[3]** `nilai[0]` adalah elemen **pertama**. Elemen terakhir ada di indeks `len(nilai) - 1`, yaitu 4.
- **[4]** `range(len(nilai))` menghasilkan 0 sampai 4. Cara ini dipakai jika kita butuh nomor indeksnya, misalnya untuk menulis "Mahasiswa ke-1".
- **[5]** `for n in nilai:` langsung mengambil isi list satu per satu, tanpa indeks. Lebih ringkas jika nomor indeks tidak dibutuhkan.
- **[6]** Isi list bisa diubah lewat indeksnya.
- **[7]** `print` pada list menampilkan seluruh isinya dalam kurung siku.
- **[8]** `nilai.sort()` mengurutkan isi list **itu sendiri** dari kecil ke besar. Untuk teks, urutannya sesuai abjad. Ingat baik-baik perintah ini, karena ia akan muncul lagi di studi kasus.
- **[9]** `", ".join(kota)` menggabungkan semua teks di dalam list, dengan `", "` sebagai pemisah.

> [!NOTE]
> - List Python bisa **bertambah panjang** dengan `append`, misalnya `nilai.append(95)`.
> - Indeks negatif menghitung dari belakang: `nilai[-1]` adalah elemen terakhir.
> - Python punya fungsi bawaan `sum()`, `max()`, dan `min()`. Di contoh ini kita menghitung total dan nilai tertinggi secara manual agar terbiasa dengan perulangan.

> [!TIP]
> **Coba sendiri:** tambahkan baris `nilai.append(95)` tepat sebelum `nilai.sort()`. Tebak dulu isi list setelah diurutkan.

<details>
<summary>Lihat jawaban</summary>

`Setelah diurutkan            : [70, 75, 78, 88, 92, 95]`. Elemen 95 ditambahkan di akhir list, lalu ikut diurutkan.

</details>

## 5. Fungsi dengan Parameter dan Nilai Kembalian

File: [`contoh/contoh05_fungsi.py`](contoh/contoh05_fungsi.py)

Fungsi adalah sekumpulan perintah yang diberi nama, sehingga bisa dipanggil berulang kali. Contoh ini menghitung ongkos ojek online dengan tarif rekaan: Rp10000 untuk 4 km pertama, ditambah Rp2500 untuk setiap km berikutnya.

```python
TARIF_DASAR = 10000  # [1] konstanta: nama HURUF BESAR, nilainya tidak pernah diubah
TARIF_PER_KM = 2500


def hitung_ongkos(jarak_km):  # [2] jarak_km adalah parameter
    """Tarif dasar untuk 4 km pertama, ditambah tarif per km berikutnya."""
    if jarak_km <= 4:
        return TARIF_DASAR  # [3] return langsung mengakhiri fungsi
    return TARIF_DASAR + (jarak_km - 4) * TARIF_PER_KM


def label_jarak(jarak_km):  # fungsi juga boleh mengembalikan teks
    if jarak_km <= 4:
        return "dekat"
    elif jarak_km <= 10:
        return "sedang"
    else:
        return "jauh"


def hitung_potongan(total, persen):  # boleh punya lebih dari satu parameter
    return total * persen // 100  # persen dihitung dengan bilangan bulat


def cetak_garis(panjang):  # [4] fungsi tanpa return: tugasnya hanya mencetak
    print("-" * panjang)


def main():
    print("=== TARIF OJEK ONLINE ===")
    cetak_garis(32)
    jarak_budi = 3
    jarak_siti = 7
    jarak_rina = 12
    ongkos_budi = hitung_ongkos(jarak_budi)  # [5] nilai kembalian disimpan ke variabel
    ongkos_siti = hitung_ongkos(jarak_siti)
    ongkos_rina = hitung_ongkos(jarak_rina)
    # [6] nilai kembalian juga bisa langsung dipakai di dalam f-string
    print(f"Budi : {jarak_budi} km ({label_jarak(jarak_budi)}) -> Rp{ongkos_budi}")
    print(f"Siti : {jarak_siti} km ({label_jarak(jarak_siti)}) -> Rp{ongkos_siti}")
    print(f"Rina : {jarak_rina} km ({label_jarak(jarak_rina)}) -> Rp{ongkos_rina}")
    cetak_garis(32)

    total = ongkos_budi + ongkos_siti + ongkos_rina
    potongan = hitung_potongan(total, 20)
    print(f"Total ongkos        : Rp{total}")
    print(f"Promo 20%           : -Rp{potongan}")
    print(f"Total setelah promo : Rp{total - potongan}")
```

**Output:**

```text
=== TARIF OJEK ONLINE ===
--------------------------------
Budi : 3 km (dekat) -> Rp10000
Siti : 7 km (sedang) -> Rp17500
Rina : 12 km (jauh) -> Rp30000
--------------------------------
Total ongkos        : Rp57500
Promo 20%           : -Rp11500
Total setelah promo : Rp46000
```

Penjelasan:

- **[1]** **Konstanta** adalah variabel yang nilainya tidak dimaksudkan untuk diubah. Python tidak melarang kita mengubahnya, tetapi nama berhuruf besar semua adalah tanda bagi sesama programmer: "jangan diubah".
- **[2]** `jarak_km` adalah **parameter**, yaitu "pintu masuk" data ke dalam fungsi. Nilai yang dikirim saat memanggil fungsi, misalnya `3`, disebut **argumen**.
- **[3]** `return` mengirim hasil kembali ke pemanggil sekaligus **mengakhiri** fungsi. Karena itu, baris `return` kedua hanya dijalankan jika jarak lebih dari 4 km.
- **[4]** `cetak_garis` tidak punya `return`. Tugasnya hanya mencetak garis. `"-" * panjang` mengulang teks `"-"` sebanyak `panjang` kali.
- **[5]** Hasil `return` disimpan ke variabel, sehingga bisa dipakai lagi untuk menghitung total.
- **[6]** Nilai kembalian juga bisa langsung dipakai di dalam f-string tanpa disimpan dulu.

Anatomi sebuah fungsi:

```text
def hitung_ongkos(jarak_km):          <- def + nama fungsi + (parameter) + titik dua
    if jarak_km <= 4:                     isi fungsi menjorok ke dalam
        return TARIF_DASAR            <- return: kirim hasil ke pemanggil
    return TARIF_DASAR + ...

ongkos = hitung_ongkos(7)             <- argumen 7 masuk ke parameter jarak_km,
                                         hasilnya (17500) disimpan ke ongkos
```

> [!IMPORTANT]
> Bedakan **mencetak** (`print`) dengan **mengembalikan** (`return`). Hasil fungsi yang di-`return` bisa disimpan, dijumlahkan, atau dibandingkan. Fungsi yang hanya mencetak, hasilnya tidak bisa diolah lagi. Fungsi tanpa `return` sebenarnya tetap mengembalikan nilai khusus bernama `None` ("tidak ada").

> [!NOTE]
> Fungsi harus sudah **didefinisikan** sebelum dipanggil saat program berjalan. Di file ini semua fungsi didefinisikan di atas, sedangkan `main()` baru dipanggil di baris paling bawah, jadi aman.

> [!TIP]
> **Coba sendiri:** berapa ongkos untuk jarak 4 km dan 5 km? Tebak dulu, lalu buktikan dengan menambahkan `print(hitung_ongkos(4))` dan `print(hitung_ongkos(5))` di `main()`.

<details>
<summary>Lihat jawaban</summary>

4 km → Rp10000 (masih tarif dasar). 5 km → 10000 + (5 - 4) x 2500 = Rp12500.

</details>

## 6. Data Paralel: Rapi tetapi Rapuh

File: [`contoh/contoh06_data_paralel.py`](contoh/contoh06_data_paralel.py)

Sekarang kita gabungkan semua bekal tadi untuk melihat masalah yang dibahas di halaman konsep. Data empat mahasiswa disimpan di tiga list **paralel**: nama, NIM, dan nilai. Indeks yang sama berarti mahasiswa yang sama.

Ceritanya begini. Fungsi pengurut ditulis ketika datanya baru berisi nama dan nilai. Belakangan, list NIM ditambahkan, tetapi fungsi pengurut **lupa diperbarui**.

```python
def tampilkan(nama, nim, nilai):
    for i in range(len(nama)):
        print(f"{i + 1}. {nim[i]} {nama[i]} - nilai {nilai[i]}")


def urutkan_berdasarkan_nilai(nama, nilai):  # [1] fungsi lama: hanya kenal 2 list
    """Bubble sort: bandingkan dua tetangga, tukar jika urutannya salah."""
    n = len(nilai)
    for putaran in range(n - 1):
        for i in range(n - 1 - putaran):
            if nilai[i] > nilai[i + 1]:
                # [2] tukar nilai, lalu tukar nama di posisi yang sama
                nilai[i], nilai[i + 1] = nilai[i + 1], nilai[i]
                nama[i], nama[i + 1] = nama[i + 1], nama[i]


def main():
    # [3] tiga list paralel: indeks yang sama = mahasiswa yang sama
    nama = ["Ayu", "Bima", "Citra", "Dimas"]
    nim = ["2409106001", "2409106002", "2409106003", "2409106004"]
    nilai = [90, 55, 78, 62]

    print("=== DATA AWAL ===")
    tampilkan(nama, nim, nilai)

    print()
    print("=== DIURUTKAN DARI NILAI TERKECIL ===")
    urutkan_berdasarkan_nilai(nama, nilai)  # [4] list nim tidak ikut dikirim!
    tampilkan(nama, nim, nilai)

    print()
    print("Nama dan nilai pindah bersama, tetapi NIM tertinggal di tempatnya.")
    print(f"Sekarang NIM {nim[0]} milik Ayu tercatat bersama {nama[0]}!")
```

**Output:**

```text
=== DATA AWAL ===
1. 2409106001 Ayu - nilai 90
2. 2409106002 Bima - nilai 55
3. 2409106003 Citra - nilai 78
4. 2409106004 Dimas - nilai 62

=== DIURUTKAN DARI NILAI TERKECIL ===
1. 2409106001 Bima - nilai 55
2. 2409106002 Dimas - nilai 62
3. 2409106003 Citra - nilai 78
4. 2409106004 Ayu - nilai 90

Nama dan nilai pindah bersama, tetapi NIM tertinggal di tempatnya.
Sekarang NIM 2409106001 milik Ayu tercatat bersama Bima!
```

Penjelasan:

- **[1]** Fungsi ini memakai algoritma *bubble sort*: dua elemen yang bertetangga dibandingkan, lalu ditukar jika urutannya salah. Proses ini diulang sampai semua urut. Tidak perlu menghafal algoritmanya. Fokuslah pada bagian penukarannya.
- **[2]** `a, b = b, a` adalah cara Python menukar dua nilai dalam satu baris. Setiap kali dua nilai ditukar, dua nama di posisi yang sama juga ditukar, agar tetap sejajar.
- **[3]** Ketiga list sejajar: `nama[0]`, `nim[0]`, dan `nilai[0]` adalah milik Ayu.
- **[4]** Fungsi menerima list yang **sama** dengan milik `main()`, bukan salinannya. Karena itu, perubahan urutan di dalam fungsi ikut terlihat di `main()` (alasan lengkapnya dibahas di Pertemuan 03). Masalahnya, list `nim` tidak pernah dikirim, sehingga tidak ikut ditukar.

Seperti inilah yang terjadi pada penukaran pertama:

```text
                 indeks 0      indeks 1
nilai SEBELUM :  90            55             -> 90 > 55, maka ditukar
nilai SESUDAH :  55            90
nama  SESUDAH :  "Bima"        "Ayu"          <- ikut ditukar
nim           :  "2409106001"  "2409106002"   <- TIDAK disentuh!
```

> [!IMPORTANT]
> Fungsi `urutkan_berdasarkan_nilai` **tidak salah saat ditulis**. Ia menjadi salah ketika program **membesar** dan list baru ditambahkan. Inilah kelemahan data paralel: setiap fungsi yang memindahkan data harus selalu ingat **semua** list yang ada.

> [!TIP]
> **Coba sendiri:** perbaiki fungsinya agar menerima parameter `nim` dan ikut menukarnya. Berapa baris yang harus kamu ubah? Sekarang bayangkan jika ada sepuluh list dan dua puluh fungsi yang memindahkan data.

## 7. Studi Kasus KedaiKita

Saatnya membedah studi kasus pertemuan ini. Ada dua file di folder `studi-kasus/`:

| File | Isi |
|---|---|
| [`kedaikita_prosedural.py`](studi-kasus/kedaikita_prosedural.py) | Versi prosedural: data menu di tiga list terpisah. Datanya tertukar saat diurutkan. |
| [`kedaikita_oop.py`](studi-kasus/kedaikita_oop.py) | Versi berorientasi objek (intipan): setiap menu adalah satu objek. Datanya aman. |

Skenario keduanya sudah kita bahas di [halaman konsep](../README.md#11-studi-kasus-kedaikita-apa-yang-kita-bangun-hari-ini).

### Versi prosedural: jalankan dulu

```bash
cd Pertemuan-01-Pengenalan-PBO/python/studi-kasus
python kedaikita_prosedural.py
```

**Output:**

```text
=== DAFTAR MENU KEDAIKITA ===
1. Kopi Susu Gula Aren - Rp18000 (stok 20)
2. Nasi Goreng Kampung - Rp25000 (stok 15)
3. Es Teh Manis - Rp8000 (stok 30)

Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis
Total bayar : Rp44000

Mengurutkan nama menu sesuai abjad...
=== DAFTAR MENU KEDAIKITA ===
1. Es Teh Manis - Rp18000 (stok 18)
2. Kopi Susu Gula Aren - Rp25000 (stok 15)
3. Nasi Goreng Kampung - Rp8000 (stok 29)

Lho? Es Teh Manis jadi Rp18000 dan Nasi Goreng Kampung jadi Rp8000!
Data satu menu tercerai-berai di tiga list, jadi mudah tertukar.
```

Sekarang kita bedah kodenya bagian demi bagian.

### Bagian A — Data menu di tiga list global

```python
# Data menu dipisah ke tiga list. Indeks yang sama = menu yang sama.
nama_menu = ["Kopi Susu Gula Aren", "Nasi Goreng Kampung", "Es Teh Manis"]
harga_menu = [18000, 25000, 8000]
stok_menu = [20, 15, 30]
```

- Ketiga list ditulis di luar fungsi mana pun, sehingga menjadi variabel **global**. Semua fungsi di file ini bisa membacanya.
- Data Kopi Susu Gula Aren ada di indeks 0 pada ketiga list, Nasi Goreng Kampung di indeks 1, dan Es Teh Manis di indeks 2. Satu-satunya "lem" yang menyatukan data satu menu adalah **nomor indeks yang sama**.

### Bagian B — Fungsi `tampilkan_menu()`

```python
def tampilkan_menu():
    """Mencetak semua menu beserta harga dan stoknya."""
    print("=== DAFTAR MENU KEDAIKITA ===")
    for i in range(len(nama_menu)):
        print(f"{i + 1}. {nama_menu[i]} - Rp{harga_menu[i]} (stok {stok_menu[i]})")
```

- Teks di antara `"""` tepat di bawah `def` adalah *docstring* fungsi: penjelasan singkat tentang tugas fungsi tersebut.
- `range(len(nama_menu))` menghasilkan indeks 0, 1, 2.
- Untuk setiap indeks `i`, fungsi mengambil elemen dari **tiga** list sekaligus. Fungsi ini "percaya" bahwa indeks `i` di ketiga list adalah milik menu yang sama.
- `i + 1` dipakai agar penomoran yang tampil dimulai dari 1, bukan 0.

### Bagian C — Fungsi `hitung_total()`

```python
def hitung_total(daftar_pesanan):
    """Menghitung total harga sekaligus mengurangi stok.

    daftar_pesanan berisi pasangan (indeks_menu, jumlah).
    """
    total = 0
    for indeks, jumlah in daftar_pesanan:
        total = total + harga_menu[indeks] * jumlah
        stok_menu[indeks] = stok_menu[indeks] - jumlah
    return total
```

- `daftar_pesanan` adalah list berisi pasangan nilai seperti `(0, 2)`, artinya "menu di indeks 0 sebanyak 2 porsi". Bentuk `(0, 2)` disebut *tuple*: mirip list, tetapi isinya tidak bisa diubah setelah dibuat. Detail *tuple* dibahas di Pertemuan 12. Untuk sekarang, anggap saja sebagai "pasangan nilai".
- `for indeks, jumlah in daftar_pesanan:` membongkar setiap pasangan ke dua variabel sekaligus. Putaran pertama: `indeks = 0`, `jumlah = 2`.
- Fungsi ini menjumlahkan harga **dan** mengurangi stok di list global `stok_menu`. Perhatikan: fungsi mana pun boleh mengubah isi list global tanpa izin apa pun. Inilah "data global yang bisa diubah siapa saja" dari halaman konsep.

> [!NOTE]
> Python mengizinkan fungsi mengubah **isi** list global, seperti `stok_menu[indeks] = ...` di atas. Lain halnya jika fungsi menulis `stok_menu = [...]` (mengganti variabelnya dengan list baru). Python akan menganggapnya sebagai variabel **lokal** baru milik fungsi itu, kecuali dideklarasikan dengan kata kunci `global`. Kita tidak memakai `global` di mata kuliah ini.

### Bagian D — Fungsi `main()`: skenarionya

```python
def main():
    tampilkan_menu()
    print()

    # Budi memesan 2 Kopi Susu Gula Aren (indeks 0) dan 1 Es Teh Manis (indeks 2)
    pesanan_budi = [(0, 2), (2, 1)]
    total = hitung_total(pesanan_budi)
    print("Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis")
    print(f"Total bayar : Rp{total}")
    print()

    # Pemilik kedai ingin daftar menu tampil urut abjad.
    # Ia hanya mengurutkan list nama... dan lupa bahwa harga & stok ada di list lain!
    print("Mengurutkan nama menu sesuai abjad...")
    nama_menu.sort()
    tampilkan_menu()
    print()
    print("Lho? Es Teh Manis jadi Rp18000 dan Nasi Goreng Kampung jadi Rp8000!")
    print("Data satu menu tercerai-berai di tiga list, jadi mudah tertukar.")
```

- Pesanan Budi ditulis dengan **indeks**, bukan nama menu. Totalnya 18000 x 2 + 8000 x 1 = 44000. Stok kopi berkurang dari 20 menjadi 18, stok es teh dari 30 menjadi 29.
- `nama_menu.sort()` adalah **sumber masalahnya**. Perintah ini hanya mengurutkan list nama. List harga dan stok tidak tahu-menahu.
- Setelah itu, `tampilkan_menu()` dengan polos memasangkan nama di indeks `i` dengan harga dan stok di indeks `i`. Hasilnya kacau.

### Masalahnya: mengapa data tertukar?

```text
                SEBELUM nama_menu.sort()         SESUDAH nama_menu.sort()
indeks 0:  Kopi Susu Gula Aren | 18000 | 18      Es Teh Manis        | 18000 | 18
indeks 1:  Nasi Goreng Kampung | 25000 | 15      Kopi Susu Gula Aren | 25000 | 15
indeks 2:  Es Teh Manis        |  8000 | 29      Nasi Goreng Kampung |  8000 | 29
                                                 ^^^ hanya kolom ini yang berpindah
```

Pelajaran dari studi kasus ini:

1. **Data satu menu tercerai-berai** di tiga list. Satu-satunya pengikatnya adalah nomor indeks.
2. **Data global** bisa diubah oleh fungsi atau perintah mana saja, termasuk perintah yang ceroboh.
3. **Indeks itu rapuh.** Setelah diurutkan, indeks 0 bukan lagi Kopi Susu Gula Aren. Pesanan lama yang menyimpan indeks `(0, 2)` kini menunjuk menu lain.
4. **Tidak ada pesan error.** Python menjalankan semuanya dengan patuh. Kesalahan logika seperti ini paling sulit dilacak.

> [!TIP]
> **Coba sendiri:** hapus baris `nama_menu.sort()` lalu jalankan lagi. Datanya tidak tertukar, tetapi menu juga tidak urut abjad. Bisakah kamu mengurutkan menu **tanpa** merusak data, tetap dengan tiga list? Itulah tantangan [Latihan 6](../latihan.md).

### Intipan versi berorientasi objek

File: [`studi-kasus/kedaikita_oop.py`](studi-kasus/kedaikita_oop.py)

> [!NOTE]
> Bagian ini hanya **intipan**. Jangan khawatir jika sintaks `class`, `__init__`, dan `self` masih terasa asing. Semuanya kita bahas pelan-pelan di Pertemuan 02. Untuk sekarang, cukup perhatikan **idenya**.

```python
class Menu:
    """Cetak biru untuk satu menu: punya nama, harga, dan stok."""

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def kurangi_stok(self, jumlah):
        self.stok = self.stok - jumlah


def tampilkan_menu(daftar_menu):
    print("=== DAFTAR MENU KEDAIKITA ===")
    nomor = 1
    for menu in daftar_menu:
        print(f"{nomor}. {menu.nama} - Rp{menu.harga} (stok {menu.stok})")
        nomor = nomor + 1


def main():
    kopi = Menu("Kopi Susu Gula Aren", 18000, 20)
    nasi_goreng = Menu("Nasi Goreng Kampung", 25000, 15)
    es_teh = Menu("Es Teh Manis", 8000, 30)
    daftar_menu = [kopi, nasi_goreng, es_teh]

    tampilkan_menu(daftar_menu)
    print()

    # Budi memesan 2 Kopi Susu Gula Aren dan 1 Es Teh Manis
    total = kopi.harga * 2 + es_teh.harga * 1
    kopi.kurangi_stok(2)
    es_teh.kurangi_stok(1)
    print("Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis")
    print(f"Total bayar : Rp{total}")
    print()

    # Mengurutkan daftar menu berdasarkan nama.
    # Yang dipindah adalah OBJEK-nya, jadi harga & stok ikut terbawa.
    print("Mengurutkan menu sesuai abjad...")
    daftar_menu.sort(key=lambda menu: menu.nama)
    tampilkan_menu(daftar_menu)
    print()
    print("Aman! Setiap menu membawa datanya sendiri, jadi tidak ada yang tertukar.")
```

Cara menjalankan (masih di folder `studi-kasus`):

```bash
python kedaikita_oop.py
```

**Output:**

```text
=== DAFTAR MENU KEDAIKITA ===
1. Kopi Susu Gula Aren - Rp18000 (stok 20)
2. Nasi Goreng Kampung - Rp25000 (stok 15)
3. Es Teh Manis - Rp8000 (stok 30)

Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis
Total bayar : Rp44000

Mengurutkan menu sesuai abjad...
=== DAFTAR MENU KEDAIKITA ===
1. Es Teh Manis - Rp8000 (stok 29)
2. Kopi Susu Gula Aren - Rp18000 (stok 18)
3. Nasi Goreng Kampung - Rp25000 (stok 15)

Aman! Setiap menu membawa datanya sendiri, jadi tidak ada yang tertukar.
```

Baca kodenya dengan "kacamata" konsep, tanpa memusingkan sintaksnya:

- `class Menu:` adalah **kelas**, rancangan untuk semua menu: setiap menu punya nama, harga, dan stok, serta bisa mengurangi stoknya.
- `Menu("Kopi Susu Gula Aren", 18000, 20)` membuat satu **objek** menu. Kita membuat tiga objek dari satu kelas yang sama.
- `kopi.harga` dibaca "harga milik kopi". Datanya menempel pada objek, bukan tersebar di list lain.
- `kopi.kurangi_stok(2)` adalah **mengirim pesan** ke objek kopi: "kurangi stokmu 2". Objek kopi sendiri yang mengurus stoknya.
- `daftar_menu.sort(key=lambda menu: menu.nama)` artinya "urutkan daftar menu berdasarkan nama setiap menu". Yang berpindah adalah objeknya, utuh dengan harga dan stoknya. Bentuk `lambda` dibahas di Pertemuan 12.

| Hal | Versi prosedural | Versi objek |
|---|---|---|
| Data satu menu | tersebar: `nama_menu[0]`, `harga_menu[0]`, `stok_menu[0]` | menyatu: `kopi.nama`, `kopi.harga`, `kopi.stok` |
| Menyebut menu yang dipesan | lewat indeks, misalnya `(0, 2)` | lewat objeknya, misalnya `kopi` |
| Mengurangi stok | fungsi mengubah list global | `kopi.kurangi_stok(2)`: objek mengurus dirinya sendiri |
| Mengurutkan | `nama_menu.sort()` hanya memindahkan nama | `daftar_menu.sort(...)` memindahkan objek utuh |
| Hasil | harga dan stok tertukar | semua data tetap benar |

> [!TIP]
> **Coba sendiri:** di versi objek, tambahkan menu keempat dengan baris `pisang = Menu("Pisang Goreng Keju", 15000, 10)`, lalu masukkan `pisang` ke dalam `daftar_menu`. Jalankan dan perhatikan: kamu sama sekali **tidak perlu mengubah** perintah pengurutnya.

<details>
<summary>Lihat jawaban</summary>

Bagian akhir output menjadi:

```text
Mengurutkan menu sesuai abjad...
=== DAFTAR MENU KEDAIKITA ===
1. Es Teh Manis - Rp8000 (stok 29)
2. Kopi Susu Gula Aren - Rp18000 (stok 18)
3. Nasi Goreng Kampung - Rp25000 (stok 15)
4. Pisang Goreng Keju - Rp15000 (stok 10)
```

Menu baru langsung ikut terurut dengan benar, tanpa satu pun perubahan pada perintah pengurut.

</details>

Selamat! Kamu baru saja melihat sendiri **mengapa** PBO dibutuhkan. Masalahnya hilang bukan karena kita lebih teliti, tetapi karena **cara menyimpan datanya** membuat kesalahan itu tidak mungkin terjadi. Di Pertemuan 02, kita belajar menulis kelas seperti `Menu` ini dari nol.

## 8. Kesalahan Umum dan Cara Membaca Pesan Error

Pesan error Python dibaca **dari bawah ke atas**. Baris paling bawah menyebutkan **jenis** error dan penyebabnya. Baris-baris di atasnya menunjukkan **lokasinya**: nama file dan nomor baris. Pada contoh di bawah, kodenya disimpan sebagai file `coba.py`.

### Kesalahan 1: Lupa indentasi setelah titik dua

```python
def main():
    total = 0
    for harga in [18000, 8000]:
    total = total + harga
    print(total)
```

Pesan error-nya:

```text
  File "coba.py", line 4
    total = total + harga
    ^
IndentationError: expected an indented block after 'for' statement on line 3
```

**Artinya:** setelah baris `for` yang diakhiri titik dua (baris 3), Python menunggu blok yang menjorok ke dalam, tetapi baris 4 sejajar dengan `for`. **Perbaikan:** tambahkan 4 spasi di depan `total = total + harga`.

### Kesalahan 2: Indentasi berlebih

```python
def main():
    nama = "Ayu"
     print(nama)
```

Pesan error-nya:

```text
  File "coba.py", line 3
    print(nama)
IndentationError: unexpected indent
```

**Artinya:** baris 3 menjorok **lebih dalam** daripada baris sebelumnya padahal tidak ada blok baru (tidak ada titik dua di baris 2). **Perbaikan:** samakan indentasinya dengan baris di atasnya.

### Kesalahan 3: Salah ketik nama variabel (`NameError`)

```python
def main():
    total = 44000
    print(f"Total bayar: Rp{totl}")
```

Pesan error-nya:

```text
Traceback (most recent call last):
  File "coba.py", line 6, in <module>
    main()
  File "coba.py", line 3, in main
    print(f"Total bayar: Rp{totl}")
                            ^^^^
NameError: name 'totl' is not defined. Did you mean: 'total'?
```

**Artinya:** Python tidak mengenal nama `totl`. Baca dari bawah: jenis error-nya `NameError`, terjadi di baris 3 di dalam fungsi `main`, dan Python bahkan menebak maksudmu: *Did you mean: 'total'?* **Perbaikan:** periksa ejaan. Kesalahan yang sama terjadi jika kamu salah mengetik nama fungsi, misalnya `mian()`.

### Kesalahan 4: Menggabungkan teks dengan angka (`TypeError`)

```python
def main():
    semester = 3
    print("Semester: " + semester)
```

Pesan error-nya:

```text
Traceback (most recent call last):
  File "coba.py", line 6, in <module>
    main()
  File "coba.py", line 3, in main
    print("Semester: " + semester)
          ~~~~~~~~~~~~~^~~~~~~~~~
TypeError: can only concatenate str (not "int") to str
```

**Artinya:** operator `+` hanya bisa menyambung teks (`str`) dengan teks lagi, bukan dengan angka (`int`). **Perbaikan:** gunakan f-string `f"Semester: {semester}"`, atau ubah angkanya menjadi teks dengan `"Semester: " + str(semester)`.

### Kesalahan 5: Lupa titik dua (`SyntaxError`)

```python
def main():
    nilai = 85
    if nilai >= 80
        print("A")
```

Pesan error-nya:

```text
  File "coba.py", line 3
    if nilai >= 80
                  ^
SyntaxError: expected ':'
```

**Artinya:** baris yang memulai blok (`if`, `elif`, `else`, `for`, `while`, `def`) wajib diakhiri titik dua. Tanda `^` menunjuk tempat titik dua seharusnya berada. **Perbaikan:** `if nilai >= 80:`.

### Kesalahan 6: Indeks di luar batas list (`IndexError`)

```python
def main():
    nilai = [78, 92, 65]
    print(nilai[3])
```

Pesan error-nya:

```text
Traceback (most recent call last):
  File "coba.py", line 6, in <module>
    main()
  File "coba.py", line 3, in main
    print(nilai[3])
          ~~~~~^^^
IndexError: list index out of range
```

**Artinya:** list berisi 3 elemen, jadi indeks yang sah hanya 0, 1, dan 2. Indeks 3 tidak ada. **Perbaikan:** ingat bahwa indeks terakhir adalah `len(nilai) - 1`.

> [!NOTE]
> Contoh pesan di atas berasal dari Python 3.12. Bunyi pesan dan tanda `^` atau `~` bisa sedikit berbeda antarversi Python. Misalnya, Python 3.13 menambahkan garis `~~~~^^` di bawah `main()`. Fokuslah pada **jenis error** (`IndentationError`, `NameError`, `TypeError`, dan seterusnya) serta **nomor barisnya**.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| Menampilkan teks | `print(...)` | `print("Halo, Samarinda!")` |
| Komentar | `# ...` | `# ini komentar` |
| Mengisi variabel | `nama = nilai` | `harga_kopi = 18000` |
| Menyisipkan nilai ke teks | `f"...{variabel}..."` | `f"Rp{harga_kopi}"` |
| Pembagian bulat dan sisa bagi | `//` dan `%` | `50000 // 18000` |
| Percabangan | `if ...:` / `elif ...:` / `else:` | `if total_belanja >= 100000:` |
| Operator logika | `and`, `or`, `not` | `hari == "Sabtu" or hari == "Minggu"` |
| Perulangan dengan rentang | `for x in range(a, b):` | `for lembar in range(1, 6):` |
| Perulangan bersyarat | `while kondisi:` | `while tabungan < target:` |
| Membuat list | `[a, b, c]` | `nilai = [78, 92, 65]` |
| Mengakses elemen list | `daftar[indeks]` | `nilai[0]` |
| Banyak elemen list | `len(daftar)` | `len(nilai)` |
| Menelusuri list | `for x in daftar:` | `for n in nilai:` |
| Mengurutkan list | `daftar.sort()` | `nilai.sort()` |
| Mendefinisikan fungsi | `def nama(parameter):` | `def hitung_ongkos(jarak_km):` |
| Mengembalikan nilai | `return nilai` | `return TARIF_DASAR` |
| Pintu masuk program | `if __name__ == "__main__":` | `main()` di dalamnya |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).
- Setelah itu, lanjutkan ke [Pertemuan 02](../../Pertemuan-02-Kelas-dan-Objek/README.md) untuk belajar menulis kelas dan objek.

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
