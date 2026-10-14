# 🐍 Praktik Python — Pertemuan 04: Enkapsulasi

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 04](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Masalah: Data yang Bisa Diubah Sembarangan](#1-masalah-data-yang-bisa-diubah-sembarangan)
2. [Satu Garis Bawah dan Name Mangling](#2-satu-garis-bawah-dan-name-mangling)
3. [Property: Getter dan Setter ala Python](#3-property-getter-dan-setter-ala-python)
4. [Validasi di Konstruktor](#4-validasi-di-konstruktor)
5. [Atribut Read-Only](#5-atribut-read-only)
6. [Method Penjaga Aturan](#6-method-penjaga-aturan)
7. [Atribut Kelas yang Dilindungi](#7-atribut-kelas-yang-dilindungi)
8. [Anatomi Kelas Python yang Terenkapsulasi](#8-anatomi-kelas-python-yang-terenkapsulasi)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan Error](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/          <- 7 contoh kecil, dari yang paling sederhana
├── studi-kasus/     <- KedaiKita versi Pertemuan 04
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Cara menjalankan sebuah contoh dari terminal (Command Prompt, PowerShell, atau terminal VS Code):

```bash
cd Pertemuan-04-Enkapsulasi/python/contoh
python contoh01_data_bocor.py
```

> [!NOTE]
> Di macOS/Linux, gunakan `python3` sebagai ganti `python`. Jika kamu memakai VS Code, buka file `.py`-nya lalu klik tombol ▶ (*Run Python File*) di pojok kanan atas. Panduan instalasi lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

Saran belajar: **ketik ulang** kodenya, jangan hanya menyalin. Jari yang mengetik membantu otak mengingat.

## 1. Masalah: Data yang Bisa Diubah Sembarangan

File: [`contoh/contoh01_data_bocor.py`](contoh/contoh01_data_bocor.py)

Kita mulai dengan membandingkan dua kelas tabungan. Yang pertama "bocor", yang kedua menjaga saldonya sendiri.

```python
class TabunganBocor:
    """Tabungan tanpa perlindungan: atribut saldo bisa diubah siapa saja."""

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo  # [1] atribut biasa, bebas diubah dari luar kelas


class TabunganAman:
    """Tabungan yang menjaga saldonya sendiri."""

    def __init__(self, pemilik, saldo):
        self._pemilik = pemilik
        self._saldo = saldo  # [2] garis bawah: "urusan internal, jangan disentuh"

    def setor(self, jumlah):  # [3] pintu resmi untuk menambah saldo
        if jumlah <= 0:
            print(f"Setor Rp{jumlah} ditolak: jumlah harus lebih dari 0")
        else:
            self._saldo += jumlah
            print(f"Setor Rp{jumlah} berhasil")

    def tarik(self, jumlah):  # [4] pintu resmi untuk mengurangi saldo
        if jumlah <= 0:
            print(f"Tarik Rp{jumlah} ditolak: jumlah harus lebih dari 0")
        elif jumlah > self._saldo:
            print(f"Tarik Rp{jumlah} ditolak: saldo tidak cukup")
        else:
            self._saldo -= jumlah
            print(f"Tarik Rp{jumlah} berhasil")

    def cek_saldo(self):
        print(f"  Saldo {self._pemilik}: Rp{self._saldo}")


def main():
    print("=== TABUNGAN BOCOR ===")
    bocor = TabunganBocor("Budi", 500000)
    print(f"Saldo awal Budi: Rp{bocor.saldo}")
    bocor.saldo = bocor.saldo - 2000000  # [5] tarik melebihi saldo, tidak dicegah
    print(f"Setelah ditarik Rp2000000: Rp{bocor.saldo}")
    bocor.saldo = 999999999  # [6] saldo "disulap" langsung dari luar kelas
    print(f"Setelah disulap: Rp{bocor.saldo}")

    print()
    print("=== TABUNGAN AMAN ===")
    aman = TabunganAman("Siti", 500000)
    aman.cek_saldo()
    aman.tarik(2000000)  # [7] semua perubahan lewat method, aturan selalu dicek
    aman.setor(-100000)
    aman.setor(250000)
    aman.tarik(100000)
    aman.cek_saldo()
```

**Output:**

```text
=== TABUNGAN BOCOR ===
Saldo awal Budi: Rp500000
Setelah ditarik Rp2000000: Rp-1500000
Setelah disulap: Rp999999999

=== TABUNGAN AMAN ===
  Saldo Siti: Rp500000
Tarik Rp2000000 ditolak: saldo tidak cukup
Setor Rp-100000 ditolak: jumlah harus lebih dari 0
Setor Rp250000 berhasil
Tarik Rp100000 berhasil
  Saldo Siti: Rp650000
```

Penjelasan:

- **[1]** `saldo` adalah atribut biasa, persis seperti yang kita tulis di Pertemuan 02 dan 03. Siapa pun yang memegang objeknya bisa mengubah nilainya.
- **[2]** Nama yang diawali **satu garis bawah** (`_saldo`) adalah tanda bagi sesama programmer Python: "atribut ini urusan internal kelas, jangan diakses dari luar".
- **[3]** Method `setor()` menjadi satu-satunya pintu resmi untuk menambah saldo. Sebelum mengubah `_saldo`, method ini memeriksa aturannya dulu.
- **[4]** Method `tarik()` menolak jumlah yang tidak masuk akal dan penarikan yang melebihi saldo.
- **[5]** Pada tabungan bocor, saldo bisa langsung dikurangi melebihi isinya. Hasilnya minus, dan tidak ada yang mencegah.
- **[6]** Lebih parah lagi, saldo bisa "disulap" menjadi angka berapa pun.
- **[7]** Pada tabungan aman, kode di luar kelas tidak pernah menyentuh `_saldo`. Semua perubahan lewat method, sehingga aturan selalu diperiksa.

> [!WARNING]
> Garis bawah hanyalah **kesepakatan**. Python tidak melarang kode seperti `aman._saldo = 999999999`, dan kode itu tetap berjalan. Bedanya, setiap programmer Python yang membacanya tahu bahwa baris itu **melanggar aturan main**. Bagian berikutnya membahas apakah ada cara yang "lebih kuat".

> [!NOTE]
> Di contoh ini, penolakan masih berupa `print`. Cara itu punya kelemahan: kode pemanggil tidak tahu bahwa perintahnya gagal. Mulai bagian 3, kita memakai cara yang lebih tegas, yaitu *exception*.

> [!TIP]
> **Coba sendiri:** di akhir `main()`, buat `TabunganAman("Rina", -100000)` lalu panggil `cek_saldo()`-nya. Apakah saldo awal yang negatif itu ditolak?

<details>
<summary>Lihat jawaban</summary>

Tidak ditolak. Tercetak `Saldo Rina: Rp-100000`. Method `setor()` dan `tarik()` memang sudah menjaga aturan, tetapi **konstruktor** masih menyimpan saldo awal tanpa memeriksanya. Celah ini kita tutup di bagian 4.

</details>

## 2. Satu Garis Bawah dan Name Mangling

File: [`contoh/contoh02_name_mangling.py`](contoh/contoh02_name_mangling.py)

Bagaimana jika atribut diberi **dua** garis bawah? Contoh ini membandingkan `_pemilik` (satu garis bawah) dengan `__pin` (dua garis bawah), lalu mengintip apa yang sebenarnya disimpan Python.

```python
class Brankas:
    """Brankas sederhana: punya pemilik dan PIN."""

    def __init__(self, pemilik, pin):
        self._pemilik = pemilik  # [1] satu garis bawah: konvensi "internal"
        self.__pin = pin  # [2] dua garis bawah: namanya akan diganti oleh Python

    def buka(self, pin):
        if pin == self.__pin:  # [3] di DALAM kelas, __pin dipakai seperti biasa
            print(f"PIN benar. Brankas milik {self._pemilik} terbuka.")
        else:
            print("PIN salah. Brankas tetap terkunci.")


def ya_tidak(kondisi):
    """Mengubah True/False menjadi teks 'ya' atau 'tidak'."""
    if kondisi:
        return "ya"
    return "tidak"


def main():
    brankas = Brankas("Budi", "246810")

    print("=== MEMAKAI BRANKAS LEWAT METHOD ===")
    brankas.buka("123456")
    brankas.buka("246810")

    print()
    print("=== MENGINTIP DARI LUAR KELAS ===")
    print(f"brankas._pemilik      : {brankas._pemilik}")  # [4] tetap bisa dibaca
    print(f"Ada atribut '__pin'?  : {ya_tidak(hasattr(brankas, '__pin'))}")  # [5]
    print(f"Isi objek sebenarnya  : {vars(brankas)}")  # [6]

    print()
    print("=== NAME MANGLING BUKAN KEAMANAN ===")
    print(f"brankas._Brankas__pin : {brankas._Brankas__pin}")  # [7] PIN terbaca!
```

**Output:**

```text
=== MEMAKAI BRANKAS LEWAT METHOD ===
PIN salah. Brankas tetap terkunci.
PIN benar. Brankas milik Budi terbuka.

=== MENGINTIP DARI LUAR KELAS ===
brankas._pemilik      : Budi
Ada atribut '__pin'?  : tidak
Isi objek sebenarnya  : {'_pemilik': 'Budi', '_Brankas__pin': '246810'}

=== NAME MANGLING BUKAN KEAMANAN ===
brankas._Brankas__pin : 246810
```

Penjelasan:

- **[1]** `_pemilik` memakai satu garis bawah. Python tidak melakukan apa pun terhadap nama ini.
- **[2]** `__pin` memakai dua garis bawah di depan. Karena ditulis **di dalam kelas** `Brankas`, Python diam-diam menggantinya menjadi `_Brankas__pin`. Penggantian nama otomatis ini disebut ***name mangling***.
- **[3]** Di dalam kelas, kita tetap menulis `self.__pin`. Python otomatis menerjemahkannya ke nama baru, jadi method `buka()` bekerja normal.
- **[4]** Atribut bergaris bawah satu tetap bisa dibaca dari luar. Python tidak menghalangi.
- **[5]** Fungsi bawaan `hasattr(objek, "nama")` memeriksa apakah objek punya atribut dengan nama tertentu. Hasilnya `False` (dicetak sebagai "tidak" oleh fungsi `ya_tidak()`), karena nama `__pin` sudah tidak ada.
- **[6]** Fungsi bawaan `vars(objek)` menampilkan semua atribut objek beserta nilainya. Terlihat jelas bahwa yang tersimpan adalah `_Brankas__pin`.
- **[7]** Siapa pun yang tahu "rumus" penggantian nama bisa membaca PIN-nya. Jadi *name mangling* **bukan** pengamanan.

Jika di akhir `main()` kamu menambahkan baris `print(brankas.__pin)`, Python berhenti dengan pesan:

```text
Traceback (most recent call last):
  File "contoh02_name_mangling.py", line 58, in <module>
    main()
    ~~~~^^
  File "contoh02_name_mangling.py", line 54, in main
    print(brankas.__pin)
          ^^^^^^^^^^^^^
AttributeError: 'Brankas' object has no attribute '__pin'
```

Pesan itu muncul karena nama aslinya sudah diganti, **bukan** karena atributnya dikunci. Berikut gambaran penggantian nama tersebut:

```text
Yang kamu tulis di dalam kelas Brankas    Yang disimpan Python di objek
--------------------------------------    -----------------------------
self._pemilik = pemilik            --->   _pemilik        (tidak diubah)
self.__pin = pin                   --->   _Brankas__pin   (nama diganti!)
```

Lalu, untuk apa *name mangling* ada? Tujuan aslinya adalah **mencegah bentrok nama** saat sebuah kelas diwarisi oleh kelas lain (pewarisan, Pertemuan 07). Fitur ini tidak dirancang untuk menyembunyikan data.

> [!IMPORTANT]
> Kebiasaan programmer Python: pakai **satu garis bawah** (`_pin`) untuk data internal, lalu sediakan *property* sebagai pintu resminya (bagian 3). Pakai dua garis bawah hanya jika kamu benar-benar butuh pencegahan bentrok nama dalam pewarisan.

> [!TIP]
> **Coba sendiri:** di akhir file, tambahkan kode berikut lalu jalankan. Apakah brankas bisa dibuka dengan PIN `000000`?
> ```python
> brankas = Brankas("Budi", "246810")
> brankas.__pin = "000000"
> print(vars(brankas))
> brankas.buka("000000")
> ```

<details>
<summary>Lihat jawaban</summary>

Setelah output `main()`, muncul dua baris tambahan:

```text
{'_pemilik': 'Budi', '_Brankas__pin': '246810', '__pin': '000000'}
PIN salah. Brankas tetap terkunci.
```

Penggantian nama hanya terjadi untuk kode yang ditulis **di dalam kelas**. Baris `brankas.__pin = "000000"` ditulis di luar kelas, sehingga Python membuat atribut **baru** yang benar-benar bernama `__pin`. PIN asli di `_Brankas__pin` tidak tersentuh, dan brankas tetap terkunci.

</details>

## 3. Property: Getter dan Setter ala Python

File: [`contoh/contoh03_property.py`](contoh/contoh03_property.py)

Data internal sudah ditandai dengan garis bawah. Sekarang kita buat **pintu resminya**. Di Python, pintu itu bernama *property*.

```python
class Televisi:
    """Televisi dengan volume 0 sampai 100."""

    def __init__(self, merek):
        self._merek = merek
        self._volume = 10  # volume awal setiap TV baru

    @property
    def merek(self):  # [1] getter: dijalankan saat kita MEMBACA tv.merek
        return self._merek

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, nilai):  # [2] setter: dijalankan saat kita MENGISI tv.volume
        if nilai < 0 or nilai > 100:
            raise ValueError(f"Volume harus 0-100, bukan {nilai}")  # [3] tolak!
        self._volume = nilai  # [4] simpan ke atribut internal (bergaris bawah)


def main():
    tv = Televisi("Polytron")
    print("=== TV BARU DINYALAKAN ===")
    print(f"Merek : {tv.merek}")  # [5] dibaca seperti atribut, tanpa tanda kurung
    print(f"Volume: {tv.volume}")

    print()
    print("=== MENGATUR VOLUME ===")
    tv.volume = 25  # [6] terlihat seperti mengisi atribut, padahal setter yang bekerja
    print(f"Volume diatur ke 25, sekarang {tv.volume}")
    tv.volume += 10  # [7] getter membaca 25, lalu setter menyimpan 35
    print(f"Volume dinaikkan 10, sekarang {tv.volume}")

    print()
    print("=== DATA TIDAK VALID DITOLAK ===")
    try:  # [8] intip sekilas: "coba jalankan; jika ditolak, tangkap"
        tv.volume = 150
        print("Baris ini tidak pernah tercetak")
    except ValueError as e:
        print(f"Ditolak: {e}")
    print(f"Volume tetap {tv.volume}")
```

**Output:**

```text
=== TV BARU DINYALAKAN ===
Merek : Polytron
Volume: 10

=== MENGATUR VOLUME ===
Volume diatur ke 25, sekarang 25
Volume dinaikkan 10, sekarang 35

=== DATA TIDAK VALID DITOLAK ===
Ditolak: Volume harus 0-100, bukan 150
Volume tetap 35
```

Penjelasan:

- **[1]** Tanda `@property` di atas method disebut *decorator*. Ia mengubah method `merek()` menjadi **getter**: method yang otomatis dijalankan saat kita membaca `tv.merek`. Karena `merek` tidak punya setter, ia bersifat read-only.
- **[2]** `@volume.setter` membuat **setter** untuk property `volume`. Nama method-nya harus **sama persis** dengan nama property (`volume`), dan setter ditulis **setelah** getter-nya. Parameter `nilai` berisi nilai baru yang ingin disimpan.
- **[3]** `raise ValueError("...")` **melempar** *exception*. Perintah langsung dihentikan, dan baris setelahnya di dalam setter tidak dijalankan. `ValueError` adalah jenis exception bawaan Python untuk "nilai yang tidak sesuai".
- **[4]** Nilai disimpan ke `self._volume` (dengan garis bawah). Jangan menulis `self.volume = nilai` di sini, karena baris itu akan memanggil setter ini lagi tanpa henti (lihat [Kesalahan 2](#kesalahan-2-setter-memanggil-dirinya-sendiri)).
- **[5]** Dari luar, property dibaca **tanpa tanda kurung**: `tv.merek`, bukan `tv.merek()`.
- **[6]** `tv.volume = 25` terlihat seperti mengisi atribut biasa. Padahal, Python menjalankan setter dengan `nilai = 25`.
- **[7]** `tv.volume += 10` sama dengan `tv.volume = tv.volume + 10`. Getter membaca 25, lalu setter menerima 35 dan memeriksanya.
- **[8]** `try`/`except` kita intip sekilas. Python **mencoba** menjalankan blok `try`. Saat setter melempar `ValueError`, sisa blok `try` dilewati (baris "tidak pernah tercetak" memang tidak tercetak), lalu blok `except` dijalankan. Variabel `e` berisi exception tersebut, dan mencetaknya menampilkan pesannya.

```text
tv.volume = 150
      |
      v
setter volume(nilai=150) --> 150 > 100 --> raise ValueError(...)
      |
      v   (sisa blok try dilewati)
except ValueError as e:  -->  print(f"Ditolak: {e}")
```

> [!NOTE]
> Hari ini kita hanya **mengintip** `try`/`except` agar program bisa terus berjalan setelah data ditolak. Bahasan lengkapnya ada di Pertemuan 11.

### Kenapa tidak memakai `get_volume()` dan `set_volume()`?

Kamu mungkin pernah melihat gaya Java seperti `getVolume()`. Gaya itu bisa saja ditiru di Python, tetapi hasilnya terasa janggal:

```python
# Gaya Java yang dipaksakan ke Python (tidak lazim)
tv.set_volume(tv.get_volume() + 10)

# Gaya Python dengan property
tv.volume += 10
```

Ada tiga alasan programmer Python memilih *property*:

1. **Lebih mudah dibaca.** Data tetap diakses seperti atribut, sedangkan pemeriksaan terjadi di balik layar.
2. **Kode lama tidak perlu diubah.** Di Pertemuan 03, kita menulis `kopi.harga` dan `kopi.harga = 20000`. Saat `harga` diubah menjadi property, semua baris itu tetap berjalan, hanya sekarang ikut diperiksa.
3. **Kesepakatan komunitas.** Panduan gaya resmi Python (PEP 8) menganjurkan atribut biasa untuk data sederhana, lalu menggantinya dengan property jika kelak butuh pemeriksaan.

## 4. Validasi di Konstruktor

File: [`contoh/contoh04_validasi_konstruktor.py`](contoh/contoh04_validasi_konstruktor.py)

Setter sudah rajin memeriksa. Namun, data juga masuk lewat **konstruktor**. Contoh ini menunjukkan apa yang terjadi jika pintu yang satu itu lupa dijaga.

```python
class MahasiswaBercelah:
    """Setter-nya memeriksa data, tetapi konstruktornya tidak."""

    def __init__(self, nama, semester):
        self._nama = nama
        self._semester = semester  # [1] celah: disimpan langsung tanpa diperiksa
```

Getter `nama`, getter `semester`, dan setter `semester` milik `MahasiswaBercelah` sama persis dengan milik kelas `Mahasiswa` berikut. Perbedaannya hanya di konstruktor:

```python
class Mahasiswa:
    """Konstruktor memakai setter, jadi data diperiksa sejak objek lahir."""

    def __init__(self, nama, semester):
        self.nama = nama  # [2] tanpa garis bawah: yang dipanggil adalah setter nama
        self.semester = semester  # [3] setter semester ikut memeriksa

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nilai):
        if nilai.strip() == "":  # [4] strip() membuang spasi di awal dan akhir
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nilai

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, nilai):
        if nilai < 1 or nilai > 14:
            raise ValueError(f"Semester harus 1-14, bukan {nilai}")
        self._semester = nilai
```

Program utamanya:

```python
    print("=== VERSI BERCELAH ===")
    ayu = MahasiswaBercelah("Ayu", 20)  # [5] semester 20 lolos begitu saja!
    print(f"{ayu.nama} tercatat di semester {ayu.semester}")
    try:
        ayu.semester = 21
    except ValueError as e:
        print(f"Mengubah lewat setter ditolak: {e}")

    print()
    print("=== VERSI AMAN ===")
    bima = Mahasiswa("Bima", 3)
    print(f"{bima.nama} tercatat di semester {bima.semester}")
    try:
        citra = Mahasiswa("Citra", 20)  # [6] ditolak sejak lahir
        print(f"{citra.nama} berhasil dibuat")  # tidak pernah dijalankan
    except ValueError as e:
        print(f"Gagal membuat mahasiswa: {e}")
    try:
        Mahasiswa("   ", 2)  # nama berisi spasi saja
    except ValueError as e:
        print(f"Gagal membuat mahasiswa: {e}")
```

**Output:**

```text
=== VERSI BERCELAH ===
Ayu tercatat di semester 20
Mengubah lewat setter ditolak: Semester harus 1-14, bukan 21

=== VERSI AMAN ===
Bima tercatat di semester 3
Gagal membuat mahasiswa: Semester harus 1-14, bukan 20
Gagal membuat mahasiswa: Nama tidak boleh kosong
```

Penjelasan:

- **[1]** Konstruktor `MahasiswaBercelah` menulis langsung ke `self._semester`. Setter-nya tidak pernah dipanggil, sehingga nilai apa pun lolos.
- **[2]** Di kelas `Mahasiswa`, konstruktor menulis `self.nama = nama` **tanpa** garis bawah. Karena `nama` adalah property, baris ini menjalankan setter `nama`.
- **[3]** Begitu juga `self.semester = semester`. Aturan semester cukup ditulis **sekali** di setter, lalu dipakai oleh konstruktor dan oleh siapa pun yang mengubah semester kelak.
- **[4]** `strip()` membuang spasi di awal dan akhir teks. Jadi nama yang hanya berisi spasi juga dianggap kosong.
- **[5]** Lihat keanehannya: semester 20 lolos saat objek dibuat, tetapi semester 21 ditolak saat diubah lewat setter. Data objek ini tidak konsisten.
- **[6]** Pada versi aman, objek dengan semester 20 **tidak pernah tercipta**. Exception dilempar dari dalam konstruktor, sehingga baris `print` di bawahnya dilewati dan variabel `citra` tidak pernah terisi.

> [!IMPORTANT]
> Di dalam `__init__`, isi atribut yang punya setter **tanpa** garis bawah, misalnya `self.semester = semester`. Dengan begitu, konstruktor ikut melewati pemeriksaan yang sama.

> [!NOTE]
> Batas semester 1–14 hanyalah aturan contoh di program ini. Di dunia nyata, aturan seperti ini mengikuti ketentuan kampus masing-masing.

## 5. Atribut Read-Only

File: [`contoh/contoh05_read_only.py`](contoh/contoh05_read_only.py)

Property tanpa setter menghasilkan atribut yang hanya bisa dibaca. Kita pakai contoh data KTP: NIK tidak pernah berubah, tetapi alamat boleh berubah.

```python
class Penduduk:
    """Data kependudukan sederhana."""

    def __init__(self, nik, nama, alamat):
        if len(nik) != 16:  # [1] satu-satunya kesempatan memeriksa NIK
            raise ValueError("NIK harus 16 digit")
        self._nik = nik
        self._nama = nama
        self.alamat = alamat  # lewat setter alamat

    @property
    def nik(self):  # [2] hanya getter, TANPA setter -> read-only
        return self._nik

    @property
    def nama(self):
        return self._nama

    @property
    def alamat(self):
        return self._alamat

    @alamat.setter
    def alamat(self, nilai):  # [3] alamat boleh berubah, asal tidak kosong
        if nilai.strip() == "":
            raise ValueError("Alamat tidak boleh kosong")
        self._alamat = nilai
```

Program utamanya:

```python
    warga = Penduduk("1234567890123456", "Rina Wulandari", "Jl. Pramuka, Samarinda")
    print("=== DATA AWAL ===")
    print(f"NIK   : {warga.nik}")
    print(f"Nama  : {warga.nama}")
    print(f"Alamat: {warga.alamat}")

    print()
    print("=== PINDAH RUMAH ===")
    warga.alamat = "Jl. Juanda, Samarinda"  # [4] diizinkan: alamat punya setter
    print(f"Alamat baru: {warga.alamat}")
    # warga.nik = "9999999999999999"  # [5] hapus tanda # untuk melihat error-nya

    print()
    print("=== DATA TIDAK VALID DITOLAK ===")
    try:
        warga.alamat = ""
    except ValueError as e:
        print(f"Ditolak: {e}")
    try:
        Penduduk("12345", "Doni Saputra", "Jl. Merdeka, Samarinda")
    except ValueError as e:
        print(f"Ditolak: {e}")
    print(f"Alamat {warga.nama} tetap: {warga.alamat}")
```

**Output:**

```text
=== DATA AWAL ===
NIK   : 1234567890123456
Nama  : Rina Wulandari
Alamat: Jl. Pramuka, Samarinda

=== PINDAH RUMAH ===
Alamat baru: Jl. Juanda, Samarinda

=== DATA TIDAK VALID DITOLAK ===
Ditolak: Alamat tidak boleh kosong
Ditolak: NIK harus 16 digit
Alamat Rina Wulandari tetap: Jl. Juanda, Samarinda
```

Penjelasan:

- **[1]** Karena `nik` tidak punya setter, pemeriksaannya ditulis langsung di konstruktor. Inilah satu-satunya kesempatan untuk memeriksa NIK.
- **[2]** `nik` dan `nama` hanya punya getter. Dari luar, keduanya bisa dibaca tetapi tidak bisa diubah.
- **[3]** `alamat` punya getter dan setter, jadi boleh diubah asal tidak kosong.
- **[4]** Mengubah alamat diizinkan dan tetap diperiksa oleh setter.
- **[5]** Baris ini sengaja diberi tanda `#` di awalnya. Jika tanda `#` pertama itu dihapus, program berhenti tepat di baris tersebut:

```text
Traceback (most recent call last):
  File "contoh05_read_only.py", line 74, in <module>
    main()
    ~~~~^^
  File "contoh05_read_only.py", line 58, in main
    warga.nik = "9999999999999999"  # [5] hapus tanda # untuk melihat error-nya
    ^^^^^^^^^
AttributeError: property 'nik' of 'Penduduk' object has no setter
```

Pesan itu berarti: "property `nik` milik objek `Penduduk` tidak punya setter". Dengan kata lain, `nik` memang dirancang read-only.

> [!NOTE]
> Di Python 3.10, pesan yang sama berbunyi `AttributeError: can't set attribute 'nik'`. Kata-katanya berbeda, tetapi jenis error-nya sama.

## 6. Method Penjaga Aturan

File: [`contoh/contoh06_method_penjaga_aturan.py`](contoh/contoh06_method_penjaga_aturan.py)

Jumlah motor di parkiran tidak diberi setter. Jumlah itu hanya berubah lewat dua pintu resmi, `masuk()` dan `keluar()`, yang masing-masing menjaga aturannya sendiri.

```python
class Parkiran:
    """Parkiran motor dengan kapasitas terbatas."""

    def __init__(self, nama, kapasitas):
        if kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari 0")
        self._nama = nama
        self._kapasitas = kapasitas
        self._terisi = 0  # [1] tanpa setter: hanya berubah lewat masuk()/keluar()
```

Property `nama`, `kapasitas`, dan `terisi` hanya berisi getter biasa. Bagian yang menarik ada setelahnya:

```python
    @property
    def sisa(self):  # [2] dihitung saat dibaca, tidak disimpan di atribut
        return self._kapasitas - self._terisi

    @property
    def penuh(self):  # [3] property bernilai True/False
        return self._terisi == self._kapasitas

    def masuk(self, jumlah):  # [4] pintu resmi untuk menambah jumlah motor
        if jumlah <= 0:
            raise ValueError("Jumlah motor harus lebih dari 0")
        if jumlah > self.sisa:
            raise ValueError(
                f"Tempat tidak cukup untuk {jumlah} motor (sisa {self.sisa})")
        self._terisi += jumlah

    def keluar(self, jumlah):  # [5] pintu resmi untuk mengurangi jumlah motor
        if jumlah <= 0:
            raise ValueError("Jumlah motor harus lebih dari 0")
        if jumlah > self._terisi:
            raise ValueError(f"Hanya ada {self._terisi} motor di parkiran")
        self._terisi -= jumlah
```

Program utamanya (fungsi `tampilkan()` mencetak satu baris status parkiran):

```python
    parkiran = Parkiran("Parkiran Gedung C", 5)

    print("=== PAGI: MOTOR BERDATANGAN ===")
    tampilkan(parkiran)
    parkiran.masuk(3)  # [6] "tell": suruh parkiran mencatat motor yang masuk
    print("3 motor masuk")
    parkiran.masuk(2)
    print("2 motor masuk")
    tampilkan(parkiran)
    try:
        parkiran.masuk(1)
        print("1 motor masuk")
    except ValueError as e:
        print(f"Ditolak: {e}")

    print()
    print("=== SORE: MOTOR PULANG ===")
    parkiran.keluar(4)
    print("4 motor keluar")
    tampilkan(parkiran)
    try:
        parkiran.keluar(2)
    except ValueError as e:
        print(f"Ditolak: {e}")
    try:
        parkiran.masuk(-2)  # [7] trik curang: "masuk" dengan angka negatif
    except ValueError as e:
        print(f"Ditolak: {e}")
```

**Output:**

```text
=== PAGI: MOTOR BERDATANGAN ===
  Parkiran Gedung C: terisi 0/5, sisa 5, penuh: tidak
3 motor masuk
2 motor masuk
  Parkiran Gedung C: terisi 5/5, sisa 0, penuh: ya
Ditolak: Tempat tidak cukup untuk 1 motor (sisa 0)

=== SORE: MOTOR PULANG ===
4 motor keluar
  Parkiran Gedung C: terisi 1/5, sisa 4, penuh: tidak
Ditolak: Hanya ada 1 motor di parkiran
Ditolak: Jumlah motor harus lebih dari 0
```

Penjelasan:

- **[1]** Atribut `_terisi` hanya punya getter (property `terisi`). Tidak ada cara resmi untuk menulis `parkiran.terisi = 100`.
- **[2]** Property `sisa` tidak menyimpan apa pun. Nilainya **dihitung** setiap kali dibaca, sehingga selalu cocok dengan `kapasitas` dan `terisi`.
- **[3]** Property `penuh` mengembalikan `True` atau `False`. Agar output-nya sama dengan versi Java, nilai itu dicetak sebagai "ya" atau "tidak" lewat fungsi `ya_tidak()`.
- **[4]** `masuk()` menolak jumlah nol atau negatif, juga jumlah yang melebihi sisa tempat.
- **[5]** `keluar()` menolak jumlah yang melebihi motor yang ada, sehingga `_terisi` tidak pernah minus.
- **[6]** Kode di luar kelas cukup **menyuruh**: "parkiran, catat 3 motor masuk". Parkiran sendiri yang memeriksa aturannya.
- **[7]** Tanpa pemeriksaan `jumlah <= 0`, perintah `masuk(-2)` diam-diam akan **mengurangi** jumlah motor dan melewati aturan di `keluar()`. Selalu periksa tanda bilangan pada method penjaga aturan.

Bandingkan dengan gaya "bertanya", yaitu mengambil datanya lalu mengubahnya sendiri dari luar kelas:

```python
# Gaya "bertanya" (hindari): aturan ditulis di luar kelas
if parkiran.terisi + 3 <= parkiran.kapasitas:
    parkiran.terisi = parkiran.terisi + 3  # ditolak: terisi tidak punya setter

# Gaya "menyuruh" (tell, don't ask): aturan dijaga di dalam kelas
parkiran.masuk(3)
```

Desain kelas `Parkiran` **memaksa** kita memakai gaya menyuruh, karena `terisi` memang tidak punya setter.

## 7. Atribut Kelas yang Dilindungi

File: [`contoh/contoh07_atribut_kelas_privat.py`](contoh/contoh07_atribut_kelas_privat.py)

Penghitung milik kelas juga perlu dilindungi. Contoh ini membuat tiket antrean bernomor otomatis yang tidak boleh kembar.

```python
class TiketAntrean:
    """Tiket antrean loket. Nomornya dibuat otomatis dan tidak boleh kembar."""

    _nomor_terakhir = 0  # [1] atribut kelas internal, dipakai bersama semua tiket

    def __init__(self, nama):
        if nama.strip() == "":
            raise ValueError("Nama tidak boleh kosong")
        TiketAntrean._nomor_terakhir += 1  # [2] naik HANYA jika data sudah valid
        self._nomor = TiketAntrean._nomor_terakhir
        self._nama = nama

    @classmethod
    def jumlah_tiket(cls):  # [3] "getter" milik kelas, dipanggil lewat nama kelas
        return cls._nomor_terakhir

    @property
    def nomor(self):  # [4] getter boleh menyajikan data dalam format yang rapi
        return f"A{self._nomor:03d}"

    @property
    def nama(self):
        return self._nama


def main():
    print("=== PENGAMBILAN TIKET ===")
    budi = TiketAntrean("Budi")
    print(f"{budi.nomor} - {budi.nama}")
    siti = TiketAntrean("Siti")
    print(f"{siti.nomor} - {siti.nama}")
    try:
        TiketAntrean("")  # [5] ditolak sebelum penghitung dinaikkan
    except ValueError as e:
        print(f"Ditolak: {e}")
    rina = TiketAntrean("Rina")
    print(f"{rina.nomor} - {rina.nama}")  # tetap A003, tidak ada nomor yang terlewat

    print()
    print(f"Jumlah tiket tercetak: {TiketAntrean.jumlah_tiket()}")  # [6]
```

**Output:**

```text
=== PENGAMBILAN TIKET ===
A001 - Budi
A002 - Siti
Ditolak: Nama tidak boleh kosong
A003 - Rina

Jumlah tiket tercetak: 3
```

Penjelasan:

- **[1]** `_nomor_terakhir` adalah **atribut kelas** (ingat Pertemuan 03): satu nilai yang dipakai bersama oleh semua tiket. Garis bawah menandakan bahwa atribut ini urusan internal.
- **[2]** Penghitung dinaikkan **setelah** pemeriksaan nama lolos. Jika nama kosong, exception sudah dilempar lebih dulu, sehingga penghitung tidak berubah.
- **[3]** `@classmethod` menjadikan `jumlah_tiket()` method milik kelas. Parameter `cls` berisi kelas `TiketAntrean` itu sendiri. Method ini berperan sebagai getter untuk atribut kelas.
- **[4]** Getter `nomor` tidak mengembalikan angka mentah, tetapi teks rapi seperti `A001`. Format `:03d` artinya "bilangan bulat, minimal 3 digit, diawali nol".
- **[5]** Tiket dengan nama kosong ditolak, dan tidak ada nomor yang "hangus".
- **[6]** Dari luar, jumlah tiket dibaca lewat nama kelas: `TiketAntrean.jumlah_tiket()`.

> [!TIP]
> **Coba sendiri:** tepat sebelum baris `rina = TiketAntrean("Rina")`, tambahkan baris `TiketAntrean._nomor_terakhir = 0`. Tebak dulu nomor tiket Rina, baru jalankan.

<details>
<summary>Lihat jawaban</summary>

Rina mendapat nomor **A001**, kembar dengan Budi, dan jumlah tiket tercetak menjadi 1:

```text
A001 - Budi
A002 - Siti
Ditolak: Nama tidak boleh kosong
A001 - Rina

Jumlah tiket tercetak: 1
```

Python tidak mencegah baris itu, karena garis bawah hanyalah kesepakatan. Itulah sebabnya kesepakatan ini harus dihormati: melanggarnya bisa merusak data yang dijaga kelas. Di Java, baris serupa ditolak oleh compiler.

</details>

## 8. Anatomi Kelas Python yang Terenkapsulasi

Berikut rangkuman bagian-bagian kelas Python yang menjaga datanya sendiri. Simpan gambar ini di kepala.

```text
class Menu:
    _jumlah_menu = 0                         <- atribut kelas internal (garis bawah)

    def __init__(self, kode, nama, harga):
        self._kode = kode                    <- atribut internal (garis bawah)
        self._nama = nama
        self.harga = harga                   <- TANPA garis bawah: lewat setter!
        Menu._jumlah_menu += 1               <- paling akhir, setelah semua lolos

    @classmethod
    def jumlah_menu(cls):                    <- getter milik kelas
        return cls._jumlah_menu

    @property
    def kode(self):                          <- getter saja = read-only
        return self._kode

    @property
    def harga(self):                         <- getter
        return self._harga

    @harga.setter
    def harga(self, nilai):                  <- setter: nama sama dengan getter
        if nilai <= 0:
            raise ValueError("...")          <- tolak data tidak valid
        self._harga = nilai                  <- simpan ke atribut bergaris bawah

    def _bantu_hitung(self):                 <- method internal juga boleh bergaris bawah
        ...
```

## 9. Studi Kasus KedaiKita

File: [`studi-kasus/kedaikita.py`](studi-kasus/kedaikita.py)

Saatnya KedaiKita menjaga datanya sendiri. Rancangan dan daftar aturannya sudah dibahas di [halaman konsep](../README.md#11-studi-kasus-kedaikita-menu-yang-menjaga-dirinya).

**Apa yang berubah dibanding Pertemuan 03?**

| Bagian | Pertemuan 03 | Pertemuan 04 |
|---|---|---|
| Atribut `Menu` | `self.harga`, `self.stok`, ... (bebas diubah) | `self._harga`, `self._stok`, ... (internal) |
| Membaca data | `kopi.harga` | tetap `kopi.harga`, tetapi lewat property |
| Mengubah harga | `kopi.harga = 20000` tanpa pemeriksaan | `kopi.harga = 20000` lewat setter yang memeriksa |
| Kode, nama, kategori | bisa diubah | read-only |
| Stok | `kopi.stok = 15` | hanya lewat `tambah_stok()` dan `kurangi_stok()` |
| Penghitung menu | `Menu.jumlah_menu` (atribut kelas publik) | `Menu._jumlah_menu` + `@classmethod` `Menu.jumlah_menu()` |
| Poin pelanggan | `budi.poin` bisa diubah langsung | hanya lewat `tambah_poin()` dan `tukar_poin()` |
| Data tidak valid | diterima begitu saja | ditolak dengan `raise ValueError(...)` |

Fungsi `format_rupiah()` tidak berubah. Berikut bagian-bagian yang baru. Pertama, konstruktor dan getter milik kelas:

```python
class Menu:
    """Satu menu KedaiKita. Datanya dilindungi dan hanya diubah lewat method."""

    _jumlah_menu = 0  # atribut kelas, dibaca lewat Menu.jumlah_menu()

    def __init__(self, kode, nama, harga, kategori, stok=0):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        self._kode = kode
        self._nama = nama
        self._kategori = kategori
        self._stok = stok
        self.harga = harga  # lewat setter, jadi ikut divalidasi
        Menu._jumlah_menu += 1  # dihitung hanya jika objek berhasil dibuat

    @classmethod
    def jumlah_menu(cls):
        """Banyaknya objek Menu yang berhasil dibuat."""
        return cls._jumlah_menu
```

- Stok awal diperiksa paling awal. Stok negatif langsung ditolak.
- Harga disimpan **lewat setter** (`self.harga = harga`), sehingga menu berharga 0 ditolak sejak dibuat.
- Penghitung naik di baris paling akhir. Menu yang gagal dibuat tidak ikut terhitung.
- Nama `jumlah_menu` kini dipakai oleh `@classmethod`, sedangkan angkanya disimpan di `_jumlah_menu`. Karena itu, dari luar kita menulis `Menu.jumlah_menu()` **dengan** tanda kurung.

Kedua, getter dan setter. Property `kode`, `nama`, `kategori`, dan `stok` hanya punya getter (bentuknya sama seperti `nik` di contoh 05), sehingga keempatnya **read-only** dari luar. Hanya `harga` yang punya setter:

```python
    # ----- getter + setter dengan validasi -----
    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        if nilai <= 0:
            raise ValueError("Harga harus lebih dari 0")
        self._harga = nilai
```

- Setter menolak harga nol atau negatif. Karena konstruktor memakai setter ini, aturan yang sama berlaku sejak menu dibuat.

Ketiga, method penjaga aturan untuk stok:

```python
    # ----- method pengubah stok -----
    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        if jumlah > self._stok:
            raise ValueError(f"Stok {self._nama} tidak cukup (sisa {self._stok})")
        self._stok -= jumlah
```

- Stok **tidak** punya setter. Restok memakai `tambah_stok()`, penjualan memakai `kurangi_stok()`.
- `kurangi_stok()` menolak penjualan yang melebihi stok, sehingga stok tidak pernah minus.
- Method `hitung_total()`, `harga_setelah_diskon()`, `stok_cukup()`, dan `__str__()` sama seperti Pertemuan 03. Bedanya, kini method itu membaca atribut bergaris bawah (`self._harga`, `self._stok`).

Keempat, kelas `Pelanggan`. Data `nama`, `no_hp`, dan `poin` kini disimpan di atribut bergaris bawah dan hanya punya getter (read-only). Poinnya hanya berubah lewat dua method berikut:

```python
    def tambah_poin(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Poin yang ditambahkan harus lebih dari 0")
        self._poin += jumlah

    def tukar_poin(self, jumlah):
        """Menukar poin menjadi potongan harga. 1 poin = Rp1.000."""
        if jumlah > self._poin:
            raise ValueError(f"Poin tidak cukup (sisa {self._poin})")
        self._poin -= jumlah
        return jumlah * 1000
```

- `tambah_poin()` menolak jumlah nol atau negatif, sehingga poin tidak bisa "dikurangi diam-diam" lewat pintu tambah.
- `tukar_poin()` adalah method penjaga aturan yang juga **mengembalikan nilai**, yaitu besar potongan harga dalam rupiah.

Terakhir, cara program utama menangani data yang ditolak (potongan dari `main()`):

```python
    print("=== DATA TIDAK VALID DITOLAK ===")
    try:
        Menu("M09", "Menu Gratis", 0, "Minuman")
    except ValueError as e:
        print(f"Gagal membuat menu: {e}")
    print(f"Jumlah menu terdaftar tetap: {Menu.jumlah_menu()}")
```

Pola yang sama dipakai untuk setter harga, `kurangi_stok()`, dan `tukar_poin()`. Kode lengkapnya ada di file studi kasus.

Cara menjalankan:

```bash
cd Pertemuan-04-Enkapsulasi/python/studi-kasus
python kedaikita.py
```

**Output:**

```text
=== MENU KEDAIKITA ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 15
Jumlah menu terdaftar: 3

=== DATA TIDAK VALID DITOLAK ===
Gagal membuat menu: Harga harus lebih dari 0
Jumlah menu terdaftar tetap: 3

=== MENGUBAH HARGA LEWAT SETTER ===
Harga Es Teh Manis naik menjadi Rp10.000
Gagal mengubah harga: Harga harus lebih dari 0
Harga Es Teh Manis tetap Rp10.000

=== MENGELOLA STOK ===
Stok awal Kopi Susu Gula Aren: 20
Terjual 5, stok sekarang 15
Restok 10, stok sekarang 25
Gagal menjual: Stok Kopi Susu Gula Aren tidak cukup (sisa 25)

=== POIN PELANGGAN ===
Budi Santoso (081234567890) - 0 poin
Budi Santoso (081234567890) - 12 poin
Tukar 10 poin -> potongan Rp10.000
Budi Santoso (081234567890) - 2 poin
Gagal menukar poin: Poin tidak cukup (sisa 2)
```

Perhatikan bahwa setiap penolakan meninggalkan data dalam keadaan **utuh**: jumlah menu tetap 3, harga es teh tetap Rp10.000, stok kopi tetap 25, dan poin Budi tetap 2.

> [!TIP]
> **Coba sendiri:**
> 1. Di bagian `=== DATA TIDAK VALID DITOLAK ===`, tambahkan percobaan membuat `Menu("M05", "Pisang Goreng Keju", 15000, "Makanan", -3)` di dalam `try`/`except` yang serupa. Pesan apa yang muncul, dan berapa jumlah menu terdaftar sesudahnya?
> 2. Tambahkan baris `kopi.stok = 100` di bagian stok, **tanpa** `try`. Apa yang terjadi?

<details>
<summary>Lihat jawaban</summary>

1. Tercetak `Gagal membuat menu: Stok tidak boleh negatif`, dan jumlah menu terdaftar tetap 3. Pemeriksaan stok terjadi sebelum penghitung dinaikkan.
2. Program berhenti dengan `AttributeError: property 'stok' of 'Menu' object has no setter`. Stok hanya boleh berubah lewat `tambah_stok()` dan `kurangi_stok()`.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan Error

Pesan error Python dibaca **dari bawah ke atas**. Baris paling bawah menyebutkan jenis error dan penyebabnya. Baris di atasnya menunjukkan lokasi (nama file dan nomor baris).

Untuk mencoba kesalahan 1, 3, 4, dan 5, buat file baru `coba.py` di folder `studi-kasus/`, lalu jalankan dengan `python coba.py`. Baris `from kedaikita import Menu` meminjam kelas `Menu` dari file `kedaikita.py` di folder yang sama (cara kerja `import` antarfile dibahas di Pertemuan 05).

### Kesalahan 1: Mengubah atribut yang read-only

```python
from kedaikita import Menu

kopi = Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20)
kopi.kode = "M10"
```

```text
Traceback (most recent call last):
  File "coba.py", line 4, in <module>
    kopi.kode = "M10"
    ^^^^^^^^^
AttributeError: property 'kode' of 'Menu' object has no setter
```

**Artinya:** `kode` adalah property tanpa setter, jadi tidak bisa diubah dari luar. Di Python 3.10, pesannya berbunyi `AttributeError: can't set attribute 'kode'`. **Perbaikan:** jika perubahan itu memang perlu, tambahkan setter (lengkap dengan validasinya). Jika tidak, berarti desainnya sudah benar dan kode pemanggil yang harus diubah.

### Kesalahan 2: Setter memanggil dirinya sendiri

```python
class Menu:
    def __init__(self, nama, harga):
        self._nama = nama
        self.harga = harga

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        if nilai <= 0:
            raise ValueError("Harga harus lebih dari 0")
        self.harga = nilai  # salah: seharusnya self._harga


kopi = Menu("Kopi Susu Gula Aren", 18000)
```

```text
Traceback (most recent call last):
  File "coba.py", line 17, in <module>
    kopi = Menu("Kopi Susu Gula Aren", 18000)
  File "coba.py", line 4, in __init__
    self.harga = harga
    ^^^^^^^^^^
  File "coba.py", line 14, in harga
    self.harga = nilai  # salah: seharusnya self._harga
    ^^^^^^^^^^
  File "coba.py", line 14, in harga
    self.harga = nilai  # salah: seharusnya self._harga
    ^^^^^^^^^^
  File "coba.py", line 14, in harga
    self.harga = nilai  # salah: seharusnya self._harga
    ^^^^^^^^^^
  [Previous line repeated 995 more times]
RecursionError: maximum recursion depth exceeded
```

**Artinya:** di dalam setter, `self.harga = nilai` memanggil setter `harga` **lagi**, yang memanggil setter lagi, dan seterusnya. Setelah sekitar seribu kali, Python menyerah dengan `RecursionError`. Baris `[Previous line repeated 995 more times]` adalah petunjuk khas kesalahan ini. **Perbaikan:** di dalam getter dan setter, selalu pakai atribut bergaris bawah: `self._harga = nilai`.

### Kesalahan 3: Memanggil property dengan tanda kurung

```python
from kedaikita import Menu

kopi = Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20)
print(kopi.harga())
```

```text
Traceback (most recent call last):
  File "coba.py", line 4, in <module>
    print(kopi.harga())
          ~~~~~~~~~~^^
TypeError: 'int' object is not callable
```

**Artinya:** `kopi.harga` sudah menghasilkan angka `18000`. Menambahkan `()` berarti mencoba "memanggil" angka itu seperti fungsi, padahal angka tidak bisa dipanggil (*not callable*). **Perbaikan:** baca property tanpa tanda kurung: `kopi.harga`. Ingat, `Menu.jumlah_menu()` tetap memakai tanda kurung karena ia `@classmethod`, bukan property.

### Kesalahan 4: Exception yang tidak ditangkap

```python
from kedaikita import Menu

kopi = Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20)
kopi.harga = -5000
print("Baris ini tidak pernah dijalankan")
```

```text
Traceback (most recent call last):
  File "coba.py", line 4, in <module>
    kopi.harga = -5000
    ^^^^^^^^^^
  File "kedaikita.py", line 70, in harga
    raise ValueError("Harga harus lebih dari 0")
ValueError: Harga harus lebih dari 0
```

**Artinya:** ini bukan *bug* pada kelas `Menu`. Justru validasinya **bekerja**: harga negatif ditolak dengan `ValueError`. Karena tidak ada `try`/`except` yang menangkapnya, program berhenti. Baca dari bawah: jenis error-nya `ValueError`, dilempar di `kedaikita.py` baris 70 (setter `harga`), akibat baris 4 di file kita. **Perbaikan:** jangan memasukkan data yang tidak valid, atau bungkus perintahnya dengan `try`/`except` jika data berasal dari luar (misalnya input pengguna).

### Kesalahan 5: Membobol lewat atribut bergaris bawah

```python
from kedaikita import Menu

kopi = Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20)
kopi._harga = -5000
print(kopi)
```

Tidak ada error sama sekali. Hasilnya:

```text
[M01] Kopi Susu Gula Aren (Minuman) - Rp-5.000 | stok 20
```

**Artinya:** Python tidak melarang akses ke `_harga`, sehingga setter terlewati dan harga menjadi minus. Inilah *bug* paling licin, karena Python diam saja. **Perbaikan:** jangan pernah menyentuh atribut bergaris bawah milik objek lain. Pakai pintu resminya: `kopi.harga = ...`.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi Python. Misalnya, tanda `^^^^` di bawah baris kode baru muncul sejak Python 3.11, dan jumlah pada `[Previous line repeated ...]` bisa sedikit berbeda. Fokuslah pada **jenis error** (`AttributeError`, `RecursionError`, `TypeError`, `ValueError`) dan kata-kata kunci di dalamnya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| Atribut internal | `self._nama = nilai` | `self._harga = harga` |
| Name mangling (jarang dipakai) | `self.__nama = nilai` | `self.__pin = pin` menjadi `_Brankas__pin` |
| Getter (property) | `@property` + `def nama(self): return self._nama` | `kopi.harga` |
| Setter | `@nama.setter` + `def nama(self, nilai): ...` | `kopi.harga = 20000` |
| Read-only | property **tanpa** setter | `kopi.kode` |
| Property hasil hitungan | `@property` yang mengembalikan hasil hitungan | `parkiran.sisa` |
| Menolak data | `raise ValueError("pesan")` | `raise ValueError("Harga harus lebih dari 0")` |
| Menangkap (intip) | `try: ... except ValueError as e: ...` | `print(f"Ditolak: {e}")` |
| Validasi di konstruktor | panggil setter: `self.nama = nama` | `self.harga = harga` |
| Atribut kelas internal | `_nama = nilai` di badan kelas | `_jumlah_menu = 0` |
| Getter milik kelas | `@classmethod` + `def nama(cls): ...` | `Menu.jumlah_menu()` |
| Method penjaga aturan | method biasa yang memeriksa lalu mengubah | `kopi.kurangi_stok(5)` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
