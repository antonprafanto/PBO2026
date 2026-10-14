# 🐍 Praktik Python Pertemuan 02: Kelas dan Objek

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 02](../README.md). Semua contoh dan studi kasus di halaman ini ada di folder `contoh/` dan `studi-kasus/`. Semuanya bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Kelas dan Objek Pertamamu](#1-kelas-dan-objek-pertamamu)
2. [Konstruktor `__init__`](#2-konstruktor-__init__)
3. [*Method*: Memberi Objek Kemampuan](#3-method-memberi-objek-kemampuan)
4. [Parameter dan Nilai Kembalian](#4-parameter-dan-nilai-kembalian)
5. [Memahami `self`](#5-memahami-self)
6. [Setiap Objek Menyimpan Datanya Sendiri](#6-setiap-objek-menyimpan-datanya-sendiri)
7. [Banyak Objek dalam *List*](#7-banyak-objek-dalam-list)
8. [Anatomi Kelas Python](#8-anatomi-kelas-python)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** Python 3.10 atau lebih baru, VS Code dengan ekstensi Python, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/          <- 7 contoh kecil, dari yang paling sederhana
├── studi-kasus/     <- KedaiKita versi Pertemuan 02
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

### Cara Menjalankan Contoh

Pilih salah satu cara. Hasilnya sama.

**Cara 1: tombol ▷ di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-02-Kelas-dan-Objek/python`. Di panel **Explorer** sebelah kiri, klik folder `contoh`, lalu klik *file* contoh yang ingin dicoba. Setelah *file* terbuka, klik tombol ▷ (**Run Python File**) di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** di bagian bawah. Baris pertama di panel itu berisi perintah panjang yang diketik VS Code secara otomatis; *output* programmu muncul di bawahnya.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-02-Kelas-dan-Objek/python/contoh` |
| folder `python` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu jalankan:

```bash
python contoh01_kelas_dan_objek.py
```

Belum yakin sudah berada di folder yang benar? Ketik `dir` (Windows) atau `ls` (macOS/Linux). Jika nama *file* yang ingin dijalankan muncul di daftar, kamu sudah di tempat yang tepat. *File* di folder `studi-kasus` dan `solusi` dijalankan dengan cara yang sama; ganti saja `contoh` dengan nama folder itu.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Di macOS/Linux, ketik `python3` sebagai ganti `python`. Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya.

### Tempat Menyimpan Kodemu Sendiri

Simpan semua kode buatanmu (hasil mengetik ulang, percobaan "Coba sendiri", *file* coretan seperti `coba.py`, dan jawaban latihan) di folder `PBO-latihan-saya/pertemuan-02/`, **di luar** folder materi. Jika sebuah percobaan memintamu mengubah *file* contoh, salin dulu *file* itu ke folder tersebut, lalu ubah dan jalankan salinannya. Untuk menjalankan salinan itu, buka folder tersebut di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**) atau arahkan terminal ke sana dengan `cd`. Alasan dan cara menyalinnya ada di [aturan emas 00-Persiapan](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri).

### Cara Membaca Kode di Halaman Ini

- Setiap bagian diawali baris ***File*:** atau **Potongan dari** yang menautkan *file* contohnya.
- ***File*:** berarti kode di bawahnya adalah isi lengkap *file* itu, hanya tanpa komentar pembuka, termasuk dua baris penutup `if __name__ == "__main__":` dan `main()`. Hasil ketik ulangnya bisa langsung dijalankan.
- **Potongan dari** berarti yang ditampilkan hanya sebagian. Jangan mengetik ulang potongannya saja; jalankan *file* lengkapnya dengan cara di atas.
- Tanda `# [1]`, `# [2]`, dan seterusnya di dalam kode dijelaskan satu per satu tepat di bawah blok kode.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* itu dijalankan.

## 1. Kelas dan Objek Pertamamu

*File*: [`contoh/contoh01_kelas_dan_objek.py`](contoh/contoh01_kelas_dan_objek.py)

Kita mulai dari kelas yang paling sederhana: kelas `Kucing`. Berikut isi lengkap *file*-nya, tanpa komentar pembuka:

```python
class Kucing:  # [1] mendefinisikan kelas bernama Kucing
    """Cetak biru untuk semua kucing."""


def main():
    oyen = Kucing()  # [2] membuat objek pertama dari kelas Kucing
    oyen.nama = "Oyen"  # [3] mengisi atribut milik objek oyen
    oyen.warna = "oranye"

    belang = Kucing()  # objek kedua dari kelas yang SAMA
    belang.nama = "Belang"
    belang.warna = "hitam putih"

    print("=== DUA OBJEK DARI SATU KELAS ===")
    print(f"Kucing pertama: {oyen.nama}, warnanya {oyen.warna}")  # [4]
    print(f"Kucing kedua  : {belang.nama}, warnanya {belang.warna}")
    print(f"oyen dibuat dari kelas  : {type(oyen).__name__}")  # [5]
    print(f"belang dibuat dari kelas: {type(belang).__name__}")
    if oyen is belang:  # [6] apakah keduanya objek yang sama?
        print("oyen dan belang adalah objek yang sama")
    else:
        print("oyen dan belang adalah dua objek yang berbeda")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== DUA OBJEK DARI SATU KELAS ===
Kucing pertama: Oyen, warnanya oranye
Kucing kedua  : Belang, warnanya hitam putih
oyen dibuat dari kelas  : Kucing
belang dibuat dari kelas: Kucing
oyen dan belang adalah dua objek yang berbeda
```

Penjelasan:

- **[1]** Kata kunci `class` diikuti nama kelas dan titik dua. Badan kelas harus menjorok ke dalam (indentasi 4 spasi). Badan kelas tidak boleh kosong; di sini kita mengisinya dengan *docstring* (teks penjelasan dalam tanda kutip tiga). Alternatifnya, kamu bisa menulis `pass`.
- **[2]** `Kucing()` **membuat objek baru** dari kelas `Kucing`. Objek itu lalu disimpan ke variabel `oyen`. Perhatikan tanda kurungnya: nama kelas "dipanggil" seperti fungsi.
- **[3]** Notasi titik `oyen.nama = "Oyen"` mengisi atribut `nama` **milik objek oyen**.
- **[4]** `oyen.nama` membaca atribut milik oyen. Ucapkan dalam hati: "nama milik oyen".
- **[5]** `type(oyen)` memberi tahu kelas asal objek. `.__name__` mengambil namanya saja.
- **[6]** Operator `is` memeriksa apakah dua variabel menunjuk ke **objek yang sama**. Hasilnya tidak karena `Kucing()` dipanggil dua kali sehingga tercipta dua objek berbeda.
- Fungsi `main()` berisi program utamanya. Fungsi ini dijalankan oleh dua baris terakhir (`if __name__ == "__main__":` lalu `main()`); maknanya kita bahas di bagian 9. Jika kamu mengetik ulang contoh ini, jangan lupa dua baris itu. Tanpa keduanya, program tidak mencetak apa pun.

> [!WARNING]
> Python memang mengizinkan kita menambah atribut dari luar seperti `oyen.nama = "Oyen"`. Namun, cara ini **rawan lupa**: bisa saja ada objek kucing yang tidak pernah diberi nama. Karena itu, pemrogram Python hampir selalu mengisi atribut di dalam **konstruktor**. Konstruktor kita pelajari di bagian berikutnya.

> [!TIP]
> **Coba sendiri:** salin `contoh01_kelas_dan_objek.py` ke folder `PBO-latihan-saya/pertemuan-02/`. Di salinan itu, hapus baris `belang.warna = "hitam putih"`, simpan, lalu jalankan. Apa yang terjadi? Bandingkan dengan hasil di bawah.

<details>
<summary>Lihat hasilnya</summary>

Dua baris pertama masih tercetak, lalu program berhenti dengan pesan *error* yang diakhiri baris ini:

```text
AttributeError: 'Kucing' object has no attribute 'warna'
```

Artinya: objek `belang` tidak punya atribut `warna` karena atribut itu tidak pernah diisi. Inilah masalah "objek setengah jadi" yang dibahas di halaman konsep. Konstruktor di bagian berikutnya mencegah masalah ini.

</details>

## 2. Konstruktor `__init__`

*File*: [`contoh/contoh02_konstruktor.py`](contoh/contoh02_konstruktor.py)

Konstruktor di Python adalah *method* bernama `__init__` (dua garis bawah di depan dan di belakang). *Method* ini dipanggil **otomatis** setiap kali objek dibuat. Berikut isi lengkap *file*-nya, tanpa komentar pembuka:

```python
class Mobil:
    """Cetak biru mobil: setiap mobil punya merek, warna, dan tahun."""

    def __init__(self, merek, warna, tahun):  # [1] konstruktor
        print(f"  (konstruktor dipanggil untuk mobil {merek})")  # [2]
        self.merek = merek  # [3] simpan parameter ke atribut objek
        self.warna = warna
        self.tahun = tahun


def main():
    print("=== MEMBUAT TIGA OBJEK MOBIL ===")
    mobil_budi = Mobil("Avanza", "hitam", 2019)  # [4] argumen dikirim ke __init__
    mobil_siti = Mobil("Brio", "merah", 2022)
    mobil_rina = Mobil("Xpander", "putih", 2021)

    print()
    print("=== DATA SETIAP MOBIL ===")
    print(f"Mobil Budi: {mobil_budi.merek} {mobil_budi.warna} ({mobil_budi.tahun})")
    print(f"Mobil Siti: {mobil_siti.merek} {mobil_siti.warna} ({mobil_siti.tahun})")
    print(f"Mobil Rina: {mobil_rina.merek} {mobil_rina.warna} ({mobil_rina.tahun})")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== MEMBUAT TIGA OBJEK MOBIL ===
  (konstruktor dipanggil untuk mobil Avanza)
  (konstruktor dipanggil untuk mobil Brio)
  (konstruktor dipanggil untuk mobil Xpander)

=== DATA SETIAP MOBIL ===
Mobil Budi: Avanza hitam (2019)
Mobil Siti: Brio merah (2022)
Mobil Rina: Xpander putih (2021)
```

Penjelasan:

- **[1]** `__init__` menerima parameter `self` (selalu di urutan pertama) ditambah data yang kita butuhkan: `merek`, `warna`, `tahun`.
- **[2]** Baris `print` ini sengaja ditambahkan untuk **membuktikan** bahwa konstruktor berjalan sendiri. Kita tidak pernah menulis `mobil_budi.__init__(...)`, tetapi pesannya tetap muncul tiga kali.
- **[3]** `self.merek = merek` berarti: "atribut `merek` milik objek ini diisi dengan nilai parameter `merek`". Tanpa `self.`, nilai itu hanya tersimpan sementara di dalam *method* dan hilang begitu *method* selesai.
- **[4]** Saat menulis `Mobil("Avanza", "hitam", 2019)`, Python membuat objek baru lalu memanggil `__init__` dengan `self` = objek baru itu, `merek` = "Avanza", `warna` = "hitam", `tahun` = 2019.

Urutan pengiriman argumen ke parameter terlihat seperti ini. Argumen pertama masuk ke parameter pertama setelah `self`, argumen kedua ke parameter kedua, dan seterusnya:

```text
Mobil(      "Avanza", "hitam", 2019)
                 |      |       |
                 v      v       v
__init__(self, merek, warna, tahun)
           ^
           |
           diisi otomatis oleh Python dengan objek yang baru dibuat
```

Spasi tambahan setelah `Mobil(` hanya agar panahnya lurus. Di kode sungguhan, tulis saja `Mobil("Avanza", "hitam", 2019)`.

> [!NOTE]
> Secara teknis, objek sudah dibuat sesaat sebelum `__init__` berjalan. Tugas `__init__` adalah **mengisi** objek baru itu dengan data awal. Karena perannya sama dengan konstruktor di bahasa lain, `__init__` lazim disebut konstruktor.

## 3. *Method*: Memberi Objek Kemampuan

*File*: [`contoh/contoh03_method.py`](contoh/contoh03_method.py)

*Method* ditulis seperti fungsi biasa, tetapi **di dalam kelas** dan dengan parameter pertama `self`. Berikut isi lengkap *file*-nya, tanpa komentar pembuka:

```python
class Lampu:
    """Lampu yang bisa dinyalakan dan dimatikan."""

    def __init__(self, ruangan):
        self.ruangan = ruangan
        self.menyala = False  # [1] nilai awal tidak harus dari parameter

    def nyalakan(self):  # [2] method yang mengubah atribut
        self.menyala = True
        print(f"Lampu {self.ruangan} dinyalakan")

    def matikan(self):
        self.menyala = False
        print(f"Lampu {self.ruangan} dimatikan")

    def tampilkan_status(self):  # [3] method yang hanya membaca atribut
        if self.menyala:
            print(f"Status lampu {self.ruangan}: MENYALA")
        else:
            print(f"Status lampu {self.ruangan}: PADAM")


def main():
    lampu_kamar = Lampu("kamar")
    lampu_dapur = Lampu("dapur")

    print("=== KONDISI AWAL ===")
    lampu_kamar.tampilkan_status()  # [4] memanggil method
    lampu_dapur.tampilkan_status()

    print()
    print("=== SETELAH DIOPERASIKAN ===")
    lampu_kamar.nyalakan()
    lampu_kamar.tampilkan_status()
    lampu_dapur.tampilkan_status()  # lampu dapur tidak terpengaruh
    lampu_kamar.matikan()
    lampu_kamar.tampilkan_status()


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== KONDISI AWAL ===
Status lampu kamar: PADAM
Status lampu dapur: PADAM

=== SETELAH DIOPERASIKAN ===
Lampu kamar dinyalakan
Status lampu kamar: MENYALA
Status lampu dapur: PADAM
Lampu kamar dimatikan
Status lampu kamar: PADAM
```

Penjelasan:

- **[1]** Tidak semua atribut harus berasal dari parameter. Setiap lampu baru otomatis dalam keadaan padam (`False`).
- **[2]** *Method* `nyalakan()` **mengubah keadaan** (*state*) objek. Inilah inti PBO: data (`menyala`) dan perilaku yang mengubahnya (`nyalakan`) berada di tempat yang sama.
- **[3]** *Method* `tampilkan_status()` hanya **membaca** atribut, tidak mengubahnya.
- **[4]** Saat memanggil *method*, kita **tidak** mengisi `self`. Python mengisinya sendiri dengan objek di sebelah kiri titik. Jadi `lampu_kamar.nyalakan()` sama artinya dengan "jalankan `nyalakan` dengan `self` = `lampu_kamar`".

> [!TIP]
> **Coba sendiri:** salin `contoh03_method.py` ke folder `PBO-latihan-saya/pertemuan-02/`. Di salinan itu, tambahkan *method* `saklar()` di dalam kelas `Lampu` yang membalik keadaan lampu (menyala menjadi padam, padam menjadi menyala). Petunjuk: `self.menyala = not self.menyala`. Lalu, di akhir `main()`, panggil `lampu_dapur.saklar()` dan `lampu_dapur.tampilkan_status()`. Simpan, jalankan, lalu bandingkan baris terakhir *output*-nya dengan jawaban di bawah.

<details>
<summary>Lihat jawaban</summary>

Tambahkan *method* ini di dalam kelas `Lampu`, sejajar dengan `matikan()`:

```python
    def saklar(self):
        self.menyala = not self.menyala
```

Lalu tambahkan dua baris ini di akhir `main()`:

```python
    lampu_dapur.saklar()
    lampu_dapur.tampilkan_status()
```

Baris terakhir *output*-nya menjadi `Status lampu dapur: MENYALA` karena lampu dapur yang tadinya padam kini dibalik menjadi menyala.

</details>

## 4. Parameter dan Nilai Kembalian

*File*: [`contoh/contoh04_parameter_dan_return.py`](contoh/contoh04_parameter_dan_return.py)

*Method* bisa menerima parameter tambahan dan bisa **mengembalikan** hasil dengan `return`. Berikut isi lengkap *file*-nya, tanpa komentar pembuka:

```python
class PersegiPanjang:
    """Bangun datar persegi panjang dengan panjang dan lebar (cm)."""

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):  # [1] mengembalikan nilai
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def perbesar(self, faktor):  # [2] menerima parameter dan mengubah atribut
        self.panjang = self.panjang * faktor
        self.lebar = self.lebar * faktor


def main():
    meja = PersegiPanjang(120, 60)
    luas = meja.hitung_luas()  # [3] hasil return disimpan ke variabel
    print("=== MEJA BELAJAR ===")
    print(f"Ukuran   : {meja.panjang} x {meja.lebar} cm")
    print(f"Luas     : {luas} cm2")
    print(f"Keliling : {meja.hitung_keliling()} cm")  # [4] langsung dipakai

    print()
    meja.perbesar(2)  # [5] mengirim argumen ke parameter faktor
    print("=== SETELAH DIPERBESAR 2 KALI ===")
    print(f"Ukuran   : {meja.panjang} x {meja.lebar} cm")
    print(f"Luas     : {meja.hitung_luas()} cm2")
    print(f"Luas naik {meja.hitung_luas() // luas} kali lipat")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== MEJA BELAJAR ===
Ukuran   : 120 x 60 cm
Luas     : 7200 cm2
Keliling : 360 cm

=== SETELAH DIPERBESAR 2 KALI ===
Ukuran   : 240 x 120 cm
Luas     : 28800 cm2
Luas naik 4 kali lipat
```

Penjelasan:

- **[1]** `return` mengirim hasil perhitungan kembali ke pemanggil. *Method* ini tidak mencetak apa pun. Ia hanya "menjawab".
- **[2]** Parameter `faktor` ditulis setelah `self`. Saat dipanggil, kita hanya mengirim `faktor`.
- **[3]** Nilai kembalian bisa disimpan ke variabel untuk dipakai lagi nanti.
- **[4]** Nilai kembalian juga bisa langsung dipakai di dalam ekspresi atau *f-string*.
- **[5]** `meja.perbesar(2)` mengisi `faktor` dengan 2. `self` tetap diisi otomatis dengan `meja`.

> [!IMPORTANT]
> Bedakan **mencetak** (`print`) dengan **mengembalikan** (`return`). *Method* yang mengembalikan nilai lebih fleksibel: hasilnya bisa dicetak, dijumlahkan, dibandingkan, atau disimpan. Hasil *method* yang hanya mencetak tidak bisa dipakai lagi.

## 5. Memahami `self`

*File*: [`contoh/contoh05_self.py`](contoh/contoh05_self.py)

Contoh ini menunjukkan tiga peran `self` sekaligus. Berikut isi lengkap *file*-nya, tanpa komentar pembuka:

```python
class Akun:
    """Akun aplikasi dengan username dan email."""

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def ganti_email(self, email):
        # [1] kiri: atribut milik objek, kanan: parameter yang baru diterima
        print(f"{self.username}: email {self.email} diganti ke {email}")
        self.email = email

    def sapa(self):
        return f"Halo, {self.username}!"

    def tampilkan_profil(self):
        print(self.sapa())  # [2] memanggil method lain lewat self
        print(f"  Email terdaftar: {self.email}")


def main():
    akun_budi = Akun("budi_s", "budi@contoh.id")
    akun_siti = Akun("siti_a", "siti@contoh.id")

    print("=== PROFIL AWAL ===")
    akun_budi.tampilkan_profil()  # [3] di dalam method, self = akun_budi
    akun_siti.tampilkan_profil()  #     di dalam method, self = akun_siti

    print()
    print("=== BUDI MENGGANTI EMAIL ===")
    akun_budi.ganti_email("budi.santoso@contoh.id")
    akun_budi.tampilkan_profil()
    akun_siti.tampilkan_profil()  # email Siti tidak ikut berubah


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== PROFIL AWAL ===
Halo, budi_s!
  Email terdaftar: budi@contoh.id
Halo, siti_a!
  Email terdaftar: siti@contoh.id

=== BUDI MENGGANTI EMAIL ===
budi_s: email budi@contoh.id diganti ke budi.santoso@contoh.id
Halo, budi_s!
  Email terdaftar: budi.santoso@contoh.id
Halo, siti_a!
  Email terdaftar: siti@contoh.id
```

Penjelasan:

- **[1]** Di dalam `ganti_email`, ada dua "*email*": `self.email` adalah atribut milik objek (*email* lama), sedangkan `email` adalah parameter (*email* baru). `self.` membuat keduanya tidak tertukar.
- **[2]** *Method* boleh memanggil *method* lain milik objek yang sama dengan `self.nama_method()`.
- **[3]** *Method* `tampilkan_profil` ditulis sekali, tetapi dijalankan dua kali dengan `self` yang berbeda. Itulah sebabnya hasilnya berbeda.

Di balik layar, Python menerjemahkan pemanggilan *method* kira-kira seperti ini:

```text
akun_budi.tampilkan_profil()   ->  Python menjalankan  Akun.tampilkan_profil(akun_budi)
akun_siti.tampilkan_profil()   ->  Python menjalankan  Akun.tampilkan_profil(akun_siti)
```

> [!NOTE]
> `self` hanyalah nama yang disepakati bersama oleh pemrogram Python. Secara teknis, kamu bisa menamainya apa saja, tetapi **jangan**. Semua pemrogram Python di dunia memakai `self`, dan editor seperti VS Code juga mengandalkannya.

## 6. Setiap Objek Menyimpan Datanya Sendiri

Potongan dari [`contoh/contoh06_objek_mandiri.py`](contoh/contoh06_objek_mandiri.py)

Yang ditampilkan hanya bagian kelasnya. Untuk melihat hasilnya, jalankan *file* lengkapnya, jangan mengetik ulang potongan ini saja.

```python
class RekeningBank:
    """Rekening tabungan sederhana."""

    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.saldo = saldo_awal

    def setor(self, jumlah):
        self.saldo = self.saldo + jumlah
        print(f"{self.pemilik} setor Rp{jumlah}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print(f"{self.pemilik} gagal tarik Rp{jumlah}: saldo tidak cukup")
        else:
            self.saldo = self.saldo - jumlah
            print(f"{self.pemilik} tarik Rp{jumlah}")

    def cek_saldo(self):
        print(f"  Saldo {self.pemilik}: Rp{self.saldo}")
```

Fungsi `main()` di *file* yang sama membuat rekening Budi (saldo awal Rp500.000) dan Siti (saldo awal Rp750.000), lalu melakukan beberapa transaksi.

***Output:***

```text
=== SALDO AWAL ===
  Saldo Budi: Rp500000
  Saldo Siti: Rp750000

=== TRANSAKSI ===
Budi setor Rp200000
Budi gagal tarik Rp1000000: saldo tidak cukup
Siti tarik Rp250000

=== SALDO AKHIR ===
  Saldo Budi: Rp700000
  Saldo Siti: Rp500000
```

Setor dan tarik pada rekening Budi tidak menyentuh saldo Siti sama sekali. Perhatikan juga bahwa *method* `tarik` **menjaga** agar saldo tidak menjadi negatif. Menjaga data agar tetap masuk akal adalah tugas penting sebuah kelas. Di Pertemuan 04 (Enkapsulasi), kita akan belajar cara menjaga data dengan lebih ketat.

## 7. Banyak Objek dalam *List*

*File*: [`contoh/contoh07_daftar_objek.py`](contoh/contoh07_daftar_objek.py)

Objek bisa disimpan di dalam *list*, sama seperti angka atau teks. Berikut isi lengkap *file*-nya, tanpa komentar pembuka:

```python
class Lagu:
    """Satu lagu di playlist."""

    def __init__(self, judul, penyanyi, durasi_detik):
        self.judul = judul
        self.penyanyi = penyanyi
        self.durasi_detik = durasi_detik

    def durasi_teks(self):
        menit = self.durasi_detik // 60
        detik = self.durasi_detik % 60
        return f"{menit}:{detik:02d}"

    def tampilkan(self):
        print(f"- {self.judul} ({self.penyanyi}) {self.durasi_teks()}")


def main():
    playlist = [  # [1] list berisi tiga objek Lagu
        Lagu("Indonesia Pusaka", "Ismail Marzuki", 215),
        Lagu("Ampar-Ampar Pisang", "Lagu Daerah Kalimantan Selatan", 132),
        Lagu("Bengawan Solo", "Gesang", 187),
    ]

    print("=== PLAYLIST BELAJAR ===")
    total = 0
    for lagu in playlist:  # [2] variabel lagu bergantian menunjuk tiap objek
        lagu.tampilkan()
        total = total + lagu.durasi_detik
    print(f"Jumlah lagu : {len(playlist)}")
    print(f"Total durasi: {total // 60} menit {total % 60} detik")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== PLAYLIST BELAJAR ===
- Indonesia Pusaka (Ismail Marzuki) 3:35
- Ampar-Ampar Pisang (Lagu Daerah Kalimantan Selatan) 2:12
- Bengawan Solo (Gesang) 3:07
Jumlah lagu : 3
Total durasi: 8 menit 54 detik
```

Penjelasan:

- **[1]** Objek dibuat langsung di dalam *list*. Kita tidak perlu menyimpannya ke variabel satu per satu.
- **[2]** Pada putaran pertama, `lagu` menunjuk objek "Indonesia Pusaka", lalu "Ampar-Ampar Pisang", lalu "Bengawan Solo". *Method* yang sama (`tampilkan()`) dipanggil untuk setiap objek.
- Kelas `Lagu` menyimpan durasi dalam detik. *Method* `durasi_teks()` mengubahnya menjadi teks berformat menit:detik. Di sana, `//` adalah pembagian bulat dan `%` adalah sisa bagi. Di dalam *f-string*, `{detik:02d}` berarti "tulis `detik` dua digit, tambahkan nol di depan bila perlu". Karena itu, 187 detik tercetak `3:07`, bukan `3:7`.

Pola "*list* berisi objek + perulangan" akan sangat sering kamu pakai. Di KedaiKita nanti, daftar menu dan daftar pesanan disimpan dengan cara ini.

## 8. Anatomi Kelas Python

Berikut rangkuman bagian-bagian sebuah kelas Python. Ini gambaran ringkas, bukan *file* untuk dijalankan; dalam program sungguhan, dua baris terakhir ditulis di dalam `main()`. Simpan gambar ini di kepala.

```text
class Menu:                                  <- kata kunci class + nama kelas (PascalCase)
    """Cetak biru menu."""                   <- docstring: penjelasan kelas

    def __init__(self, nama, harga):         <- konstruktor (otomatis dipanggil)
        self.nama = nama                     <- atribut objek diisi dari parameter
        self.harga = harga

    def hitung_total(self, jumlah):          <- method: parameter pertama selalu self
        return self.harga * jumlah           <- membaca atribut lewat self

kopi = Menu("Kopi Susu Gula Aren", 18000)    <- membuat objek (instansiasi)
total = kopi.hitung_total(2)                 <- memanggil method dengan notasi titik
```

## 9. Studi Kasus KedaiKita

*File*: [`studi-kasus/kedaikita.py`](studi-kasus/kedaikita.py)

Saatnya membangun KedaiKita versi pertama yang memakai kelas. Rancangannya sudah kita bahas di [halaman konsep](../README.md#10-studi-kasus-kedaikita-kelas-menu-pertama).

**Apa yang berubah dibanding Pertemuan 01?**

- Data menu tidak lagi disimpan di tiga *list* terpisah, tetapi di dalam objek `Menu`.
- Perhitungan total tidak lagi memakai fungsi lepas, tetapi *method* `hitung_total()` milik setiap menu.

Berikut isi lengkap *file*-nya, hanya tanpa komentar pembuka:

```python
class Menu:
    """Cetak biru untuk setiap menu di KedaiKita."""

    def __init__(self, nama, harga):  # [1] konstruktor: dipanggil saat objek dibuat
        self.nama = nama  # [2] atribut milik objek
        self.harga = harga

    def tampilkan_info(self):  # [3] method: perilaku objek
        print(f"{self.nama} - Rp{self.harga}")

    def hitung_total(self, jumlah):  # [4] method yang mengembalikan nilai
        return self.harga * jumlah


def main():
    print("=== MENU KEDAIKITA ===")
    kopi = Menu("Kopi Susu Gula Aren", 18000)  # [5] membuat objek
    es_teh = Menu("Es Teh Manis", 8000)
    nasi_goreng = Menu("Nasi Goreng Kampung", 25000)

    kopi.tampilkan_info()  # [6] memanggil method milik objek
    es_teh.tampilkan_info()
    nasi_goreng.tampilkan_info()

    print()
    print("=== PESANAN BUDI ===")
    total_kopi = kopi.hitung_total(2)
    total_nasi = nasi_goreng.hitung_total(1)
    print(f"2 x {kopi.nama} = Rp{total_kopi}")  # [7] membaca atribut objek
    print(f"1 x {nasi_goreng.nama} = Rp{total_nasi}")
    print(f"Total bayar: Rp{total_kopi + total_nasi}")

    print()
    print("=== HARGA ES TEH NAIK ===")
    es_teh.harga = 10000  # [8] mengubah atribut satu objek
    es_teh.tampilkan_info()
    kopi.tampilkan_info()  # objek lain tidak ikut berubah


if __name__ == "__main__":
    main()
```

Cara menjalankan: buka *file* `studi-kasus/kedaikita.py` di VS Code, lalu klik ▷. Lewat terminal, ketik perintah berikut dari folder utama materi:

```bash
cd Pertemuan-02-Kelas-dan-Objek/python/studi-kasus
python kedaikita.py
```

Di macOS/Linux, baris keduanya `python3 kedaikita.py`.

***Output:***

```text
=== MENU KEDAIKITA ===
Kopi Susu Gula Aren - Rp18000
Es Teh Manis - Rp8000
Nasi Goreng Kampung - Rp25000

=== PESANAN BUDI ===
2 x Kopi Susu Gula Aren = Rp36000
1 x Nasi Goreng Kampung = Rp25000
Total bayar: Rp61000

=== HARGA ES TEH NAIK ===
Es Teh Manis - Rp10000
Kopi Susu Gula Aren - Rp18000
```

Penjelasan:

- **[1]** Konstruktor menerima `nama` dan `harga` sehingga tidak ada menu yang lahir tanpa nama atau harga.
- **[2]** Atribut disimpan dengan `self.`, jadi melekat pada objek.
- **[3]** `tampilkan_info()` mencetak data milik objek yang memanggilnya.
- **[4]** `hitung_total(jumlah)` mengembalikan angka sehingga hasilnya bisa dijumlahkan di program utama.
- **[5]** Tiga objek dibuat dari satu kelas.
- **[6]** *Method* yang sama menghasilkan teks berbeda karena `self`-nya berbeda.
- **[7]** Atribut `nama` dibaca langsung dengan notasi titik.
- **[8]** Hanya harga es teh yang berubah. Objek kopi tidak terpengaruh.

> [!NOTE]
> Bagian `if __name__ == "__main__":` di akhir *file* berarti: "jalankan `main()` hanya jika *file* ini dijalankan langsung". Ini adalah "pintu masuk" program, mirip `main` di Java. Untuk sekarang, cukup ingat polanya: tulis program utama di dalam `main()`, lalu tutup *file* dengan dua baris itu. Kita akan memakainya di semua program.

> [!TIP]
> **Coba sendiri:** salin `studi-kasus/kedaikita.py` ke folder `PBO-latihan-saya/pertemuan-02/`. Di akhir fungsi `main()` salinan itu, buat menu keempat, `Mie Goreng Jawa` seharga `23000`, lalu hitung dan cetak total pesanan Siti: 1 mie goreng dan 2 es teh (dengan harga es teh yang sudah naik). Simpan, lalu jalankan. Berapa total yang harus Siti bayar? Bandingkan dengan jawaban di bawah.

<details>
<summary>Lihat jawaban</summary>

Totalnya 1 x 23.000 + 2 x 10.000 = Rp43.000. Salah satu cara menulisnya, ditambahkan di akhir `main()`:

```python
    mie_goreng = Menu("Mie Goreng Jawa", 23000)
    total_siti = mie_goreng.hitung_total(1) + es_teh.hitung_total(2)
    print(f"Total bayar Siti: Rp{total_siti}")
```

Baris terakhir yang tercetak: `Total bayar Siti: Rp43000`.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan *Error*

Pesan *error* Python dibaca **dari bawah ke atas**. Baris paling bawah menyebutkan jenis *error* dan penyebabnya. Baris di atasnya menunjukkan lokasi (nama *file* dan nomor baris).

Setiap kesalahan di bawah ini ditampilkan dalam dua blok: kode yang salah (jangan ditiru) dan pesan *error* yang muncul. Ingin melihatnya sendiri? Buat *file* baru bernama `coba.py` di folder `PBO-latihan-saya/pertemuan-02/` (jangan di dalam folder materi), salin kode yang salah ke sana, lalu jalankan. Potongan Kesalahan 2, 4, dan 5 memakai kelas `Menu` dari studi kasus, jadi salin dulu kelas itu ke bagian atas `coba.py`. Untuk Kesalahan 4 dan 5, tambahkan juga baris `kopi = Menu("Kopi Susu Gula Aren", 18000)` sebelum potongannya.

### Kesalahan 1: Lupa menulis `self` di parameter *method*

Kode yang salah:

```python
class Kucing:
    def bersuara():
        print("Meong!")


oyen = Kucing()
oyen.bersuara()
```

Pesan *error*-nya:

```text
Traceback (most recent call last):
  File "coba.py", line 7, in <module>
    oyen.bersuara()
    ~~~~~~~~~~~~~^^
TypeError: Kucing.bersuara() takes 0 positional arguments but 1 was given
```

**Artinya:** *method* `bersuara` didefinisikan tanpa parameter (0), tetapi Python mengirim 1 argumen, yaitu objek `oyen` sebagai `self`. Baris berisi `~` dan `^` menunjuk bagian kode yang bermasalah; baris ini muncul mulai Python 3.13. **Perbaikan:** tulis `def bersuara(self):`.

### Kesalahan 2: Jumlah argumen tidak sesuai konstruktor

Kode yang salah:

```python
kopi = Menu("Kopi Susu Gula Aren")
```

Baris terakhir pesan *error*-nya:

```text
TypeError: Menu.__init__() missing 1 required positional argument: 'harga'
```

**Artinya:** konstruktor `Menu` membutuhkan `nama` **dan** `harga`, tetapi kita hanya mengirim nama. **Perbaikan:** `Menu("Kopi Susu Gula Aren", 18000)`.

### Kesalahan 3: Lupa `self.` saat menyimpan atribut

Kode yang salah:

```python
class Menu:
    def __init__(self, nama, harga):
        nama = nama
        harga = harga


kopi = Menu("Kopi Susu Gula Aren", 18000)
print(kopi.nama)
```

Baris terakhir pesan *error*-nya:

```text
AttributeError: 'Menu' object has no attribute 'nama'
```

**Artinya:** baris `nama = nama` hanya mengisi variabel lokal, bukan atribut objek. Begitu konstruktor selesai, nilainya hilang. **Perbaikan:** `self.nama = nama`.

### Kesalahan 4: Salah ketik nama atribut

Kode yang salah:

```python
print(kopi.hrga)
```

Baris terakhir pesan *error*-nya:

```text
AttributeError: 'Menu' object has no attribute 'hrga'. Did you mean: 'harga'?
```

**Artinya:** objek tidak punya atribut `hrga`. Mulai Python 3.10, Python bahkan menebak maksudmu (*Did you mean: 'harga'?*). **Perbaikan:** periksa ejaan.

### Kesalahan 5: Lupa tanda kurung saat memanggil *method*

Kode yang salah:

```python
kopi.tampilkan_info
```

Tidak ada *error*, tetapi **tidak ada yang tercetak**. Tanpa `()`, *method* hanya "disebut", tidak dijalankan. Ini termasuk *bug* yang sulit ditemukan karena Python diam saja. **Perbaikan:** `kopi.tampilkan_info()`.

> [!NOTE]
> Pesan di atas diambil dari Python 3.13. Bunyinya bisa sedikit berbeda antarversi Python. Fokuslah pada **jenis *error*** (misalnya `TypeError`, `AttributeError`) dan kata-kata kunci di dalamnya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| Mendefinisikan kelas | `class NamaKelas:` | `class Menu:` |
| Konstruktor | `def __init__(self, ...):` | `def __init__(self, nama, harga):` |
| Mengisi atribut | `self.atribut = nilai` | `self.harga = harga` |
| Mendefinisikan *method* | `def nama_method(self, ...):` | `def hitung_total(self, jumlah):` |
| Mengembalikan nilai | `return nilai` | `return self.harga * jumlah` |
| Membuat objek | `NamaKelas(argumen)` | `kopi = Menu("Kopi", 18000)` |
| Membaca atribut | `objek.atribut` | `kopi.harga` |
| Mengubah atribut | `objek.atribut = nilai` | `kopi.harga = 20000` |
| Memanggil *method* | `objek.method(argumen)` | `kopi.hitung_total(2)` |
| Cek objek yang sama | `a is b` | `oyen is belang` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
