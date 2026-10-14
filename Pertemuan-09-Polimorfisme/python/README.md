# 🐍 Praktik Python — Pertemuan 09: Polimorfisme

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 09](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Satu Perintah, Banyak Bentuk](#1-satu-perintah-banyak-bentuk)
2. [Koleksi Polimorfik dan Jenis Baru](#2-koleksi-polimorfik-dan-jenis-baru)
3. [Memeriksa Jenis Objek dengan `isinstance()`](#3-memeriksa-jenis-objek-dengan-isinstance)
4. [Polimorfisme dari Dalam Kelas](#4-polimorfisme-dari-dalam-kelas)
5. [Duck Typing: Tanpa Pewarisan pun Bisa](#5-duck-typing-tanpa-pewarisan-pun-bisa)
6. [Python Tidak Punya Overloading](#6-python-tidak-punya-overloading)
7. [Pengganti Overloading: Nilai Bawaan, Argumen Kata Kunci, dan `*args`](#7-pengganti-overloading-nilai-bawaan-argumen-kata-kunci-dan-args)
8. [Studi Kasus KedaiKita](#8-studi-kasus-kedaikita)
9. [Kesalahan Umum dan Cara Membaca Pesan Error](#9-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/          <- 6 contoh, dari polimorfisme dasar sampai pengganti overloading
├── studi-kasus/     <- KedaiKita versi Pertemuan 09 (7 file)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Cara menjalankan sebuah contoh dari terminal:

```bash
cd Pertemuan-09-Polimorfisme/python/contoh
python contoh01_satu_perintah_banyak_bentuk.py
```

Studi kasus terdiri atas beberapa file, jadi jalankan `main.py` **dari dalam** folder `studi-kasus`:

```bash
cd Pertemuan-09-Polimorfisme/python/studi-kasus
python main.py
```

> [!NOTE]
> Di macOS/Linux, gunakan `python3` sebagai ganti `python`. Di VS Code, kamu juga bisa membuka file lalu menekan tombol ▶ (*Run Python File*). Panduan instalasi ada di [00-Persiapan](../../00-Persiapan/README.md).

Seperti sejak Pertemuan 05, kode memakai *type hint* (`nama: str`, `-> int`) dan atribut bergaris bawah (`self._nama`). Ingat, *type hint* hanyalah **keterangan** untuk pembaca dan editor. Python tidak memeriksanya saat program berjalan. Fakta kecil ini ternyata penting di bagian 5.

## 1. Satu Perintah, Banyak Bentuk

File: [`contoh/contoh01_satu_perintah_banyak_bentuk.py`](contoh/contoh01_satu_perintah_banyak_bentuk.py)

Kita mulai dari contoh klasik: hewan-hewan yang bersuara.

```python
class Hewan:
    """Kelas induk semua hewan."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama

    def bersuara(self) -> str:
        return "(diam saja)"  # [1] versi umum milik induk


class Kucing(Hewan):
    def bersuara(self) -> str:  # [2] override: versi khusus kucing
        return "Meong!"
```

`Anjing` (`"Guk guk!"`) dan `Bebek` (`"Kwek kwek!"`) ditulis dengan pola yang sama seperti `Kucing`. Sisanya:

```python
class Ikan(Hewan):
    """Ikan tidak meng-override bersuara(), jadi memakai versi Hewan."""


def suruh_bersuara(hewan: Hewan):  # [3] parameter bertipe kelas induk
    jenis = type(hewan).__name__
    print(f"{hewan.nama} si {jenis}: {hewan.bersuara()}")  # [4]


def main():
    print("=== SATU VARIABEL, BERGANTI OBJEK ===")
    hewan = Kucing("Oyen")  # [5] variabel hewan menunjuk objek Kucing
    print(hewan.bersuara())
    hewan = Anjing("Bruno")  # sekarang menunjuk objek Anjing
    print(hewan.bersuara())  # baris yang sama persis, hasilnya berbeda

    print()
    print("=== SATU PERINTAH UNTUK SEMUA HEWAN ===")
    kebun = [Kucing("Oyen"), Anjing("Bruno"), Bebek("Kuning"), Ikan("Koki")]  # [6]
    for satwa in kebun:
        suruh_bersuara(satwa)
```

**Output:**

```text
=== SATU VARIABEL, BERGANTI OBJEK ===
Meong!
Guk guk!

=== SATU PERINTAH UNTUK SEMUA HEWAN ===
Oyen si Kucing: Meong!
Bruno si Anjing: Guk guk!
Kuning si Bebek: Kwek kwek!
Koki si Ikan: (diam saja)
```

Penjelasan:

- **[1]** `Hewan` menyediakan versi **umum** dari `bersuara()`. Versi ini dipakai oleh kelas anak yang tidak menulis versinya sendiri.
- **[2]** `Kucing`, `Anjing`, dan `Bebek` meng-*override* `bersuara()`: nama sama, parameter sama, isi berbeda.
- **[3]** Parameter `hewan` diberi *type hint* `Hewan`. Artinya, fungsi ini siap menerima **hewan jenis apa pun**, termasuk semua kelas anak `Hewan`.
- **[4]** Inilah inti polimorfisme. Fungsi `suruh_bersuara` tidak tahu dan tidak peduli jenis hewannya. Ia cukup memanggil `hewan.bersuara()`, dan Python yang memilih versi milik objek sebenarnya.
- **[5]** Variabel `hewan` mula-mula menunjuk objek `Kucing`, lalu objek `Anjing`. Baris `print(hewan.bersuara())` ditulis persis sama, tetapi hasilnya berbeda.
- **[6]** List `kebun` berisi empat objek dari empat kelas berbeda. `Ikan` tidak meng-*override*, jadi Python naik ke kelas induk dan memakai `(diam saja)`.

Cara Python memilih versi `bersuara()` untuk setiap objek:

```text
satwa.bersuara()  ->  objeknya Kucing  ->  Kucing punya bersuara()?  ya     ->  "Meong!"
satwa.bersuara()  ->  objeknya Ikan    ->  Ikan punya bersuara()?    tidak  ->  naik ke Hewan  ->  "(diam saja)"
```

> [!TIP]
> **Coba sendiri:** tambahkan kelas `Sapi(Hewan)` yang bersuara `"Mooo!"`, lalu masukkan `Sapi("Belang")` ke list `kebun`. Apakah fungsi `suruh_bersuara` perlu diubah?

<details>
<summary>Lihat jawaban</summary>

Tidak perlu. Muncul baris baru `Belang si Sapi: Mooo!` tanpa menyentuh `suruh_bersuara` sedikit pun. Inilah keuntungan utama polimorfisme yang dibahas di bagian berikutnya.

</details>

## 2. Koleksi Polimorfik dan Jenis Baru

File: [`contoh/contoh02_koleksi_polimorfik.py`](contoh/contoh02_koleksi_polimorfik.py)

Sekarang kita buktikan bahwa jenis baru bisa ditambahkan tanpa mengubah kode pemanggil. Berikut kelas induknya:

```python
class BangunDatar:
    """Kelas induk semua bangun datar."""

    def nama(self) -> str:
        return "Bangun datar"

    def luas(self) -> int:
        return 0  # [1] bangun datar "umum" tidak punya rumus luas
```

Kelas anak `Persegi`, `PersegiPanjang`, dan `Segitiga` masing-masing meng-*override* `nama()` dan `luas()`. Misalnya, `luas()` milik `Segitiga` mengembalikan `self._alas * self._tinggi // 2`. Lalu kelas baru, fungsi laporan, dan program utama:

```python
# ----- Jenis BARU yang ditambahkan belakangan -----
class Trapesium(BangunDatar):  # [2] cukup menulis kelas baru
    def __init__(self, sisi_atas: int, sisi_bawah: int, tinggi: int):
        self._sisi_atas = sisi_atas
        self._sisi_bawah = sisi_bawah
        self._tinggi = tinggi

    def nama(self) -> str:
        return f"Trapesium {self._sisi_atas}/{self._sisi_bawah} tinggi {self._tinggi}"

    def luas(self) -> int:
        return (self._sisi_atas + self._sisi_bawah) * self._tinggi // 2


def cetak_laporan(daftar: list[BangunDatar]):  # [3] tidak kenal kelas anak mana pun
    total = 0
    for bangun in daftar:
        luas = bangun.luas()  # [4] versi luas() milik objek yang sebenarnya
        print(f"{bangun.nama():<30} luas {luas:>4} cm2")
        total += luas
    print(f"Total luas: {total} cm2")


def main():
    print("=== LAPORAN AWAL: TIGA JENIS ===")
    daftar = [Persegi(10), PersegiPanjang(12, 5), Segitiga(8, 6)]  # [5]
    cetak_laporan(daftar)

    print()
    print("=== SETELAH ADA JENIS BARU ===")
    daftar.append(Trapesium(6, 10, 4))  # [6] cetak_laporan() tidak diubah
    daftar.append(BangunDatar())
    cetak_laporan(daftar)
```

**Output:**

```text
=== LAPORAN AWAL: TIGA JENIS ===
Persegi 10x10                  luas  100 cm2
Persegi panjang 12x5           luas   60 cm2
Segitiga alas 8 tinggi 6       luas   24 cm2
Total luas: 184 cm2

=== SETELAH ADA JENIS BARU ===
Persegi 10x10                  luas  100 cm2
Persegi panjang 12x5           luas   60 cm2
Segitiga alas 8 tinggi 6       luas   24 cm2
Trapesium 6/10 tinggi 4        luas   32 cm2
Bangun datar                   luas    0 cm2
Total luas: 216 cm2
```

Penjelasan:

- **[1]** Versi induk mengembalikan 0, karena bangun datar "umum" tidak punya rumus luas.
- **[2]** Menambah jenis baru cukup dengan **menulis kelas baru**. Tidak ada kode lama yang diubah.
- **[3]** *Type hint* `list[BangunDatar]` berarti "list berisi bangun datar jenis apa pun". Perhatikan bahwa isi fungsi ini tidak menyebut `Persegi`, `Segitiga`, atau `Trapesium` sama sekali.
- **[4]** Setiap putaran memanggil `luas()` dan `nama()` milik objek yang sedang diproses.
- **[5]** Satu list menampung tiga jenis objek. Inilah **koleksi polimorfik**.
- **[6]** `Trapesium` ikut dihitung dengan benar, walaupun `cetak_laporan` ditulis sebelum kelas itu ada. Rumus `luas()` disimpan rapi di kelasnya masing-masing.

> [!NOTE]
> Baris `Bangun datar ... luas 0` terasa janggal. Objek `BangunDatar()` memang tidak seharusnya bisa dibuat, karena "bangun datar umum" tidak punya bentuk. Di Pertemuan 10, kita membuat kelas seperti ini menjadi **kelas abstrak**, sehingga Python menolak pembuatan objeknya.

## 3. Memeriksa Jenis Objek dengan `isinstance()`

File: [`contoh/contoh03_cek_jenis_objek.py`](contoh/contoh03_cek_jenis_objek.py)

Kadang sebuah kelas anak punya method **khusus** yang tidak dimiliki saudaranya. Di contoh ini, hanya `Mahasiswa` yang punya `isi_krs()`, dan hanya `Dosen` yang punya `input_nilai()`. Keduanya sama-sama meng-*override* `peran()` dan `menu_utama()` milik `Pengguna`. Berikut method khusus di kelas `Mahasiswa`:

```python
    def isi_krs(self, sks: int) -> str:  # [1] method KHUSUS mahasiswa
        return f"{self._nama} ({self._nim}) mengisi KRS {sks} SKS"
```

Kelas `Dosen` serupa, dengan method khusus `input_nilai(mata_kuliah, nilai)`. Program utamanya:

```python
def main():
    daftar = [
        Mahasiswa("Ayu Lestari", "2409106001"),
        Dosen("Rahmat Hidayat", "198003152005011002"),
        Mahasiswa("Bima Saputra", "2409106002"),
    ]

    print("=== SEMUA PENGGUNA LOGIN ===")
    for pengguna in daftar:  # [2] method bersama: aman untuk semua pengguna
        print(f"{pengguna.nama} [{pengguna.peran()}] menu: {pengguna.menu_utama()}")

    print()
    print("=== FITUR KHUSUS: CEK JENIS DULU ===")
    for pengguna in daftar:
        if isinstance(pengguna, Mahasiswa):  # [3] pastikan dulu jenisnya
            print(pengguna.isi_krs(21))  # [4] baru panggil method khususnya
        elif isinstance(pengguna, Dosen):
            print(pengguna.input_nilai("PBO", "A"))
```

Bagian terakhir `main` memeriksa objek Ayu dengan `isinstance(ayu, Mahasiswa)`, `isinstance(ayu, Pengguna)` (ditandai `# [5]`), dan `isinstance(ayu, Dosen)`.

**Output:**

```text
=== SEMUA PENGGUNA LOGIN ===
Ayu Lestari [Mahasiswa] menu: Profil, KRS, KHS
Rahmat Hidayat [Dosen] menu: Profil, Input Nilai, Jadwal Mengajar
Bima Saputra [Mahasiswa] menu: Profil, KRS, KHS

=== FITUR KHUSUS: CEK JENIS DULU ===
Ayu Lestari (2409106001) mengisi KRS 21 SKS
Rahmat Hidayat menginput nilai PBO: A
Bima Saputra (2409106002) mengisi KRS 21 SKS

=== CEK JENIS IKUT MENGENAL INDUK ===
Ayu termasuk Mahasiswa? ya
Ayu termasuk Pengguna?  ya
Ayu termasuk Dosen?     tidak
```

Penjelasan:

- **[1]** `isi_krs()` hanya ada di `Mahasiswa`. Objek `Dosen` tidak punya method ini.
- **[2]** `peran()` dan `menu_utama()` dimiliki **semua** pengguna, jadi aman dipanggil tanpa pemeriksaan apa pun. Hasilnya polimorfik.
- **[3]** Sebelum memanggil method khusus, kita memastikan jenis objeknya dengan `isinstance(objek, Kelas)`.
- **[4]** Di dalam cabang itu, kita yakin `pengguna` adalah mahasiswa, jadi `isi_krs()` aman dipanggil. Python tidak butuh langkah tambahan seperti *casting* di Java.
- **[5]** `isinstance` juga menjawab "ya" untuk kelas induk, karena setiap mahasiswa **adalah** pengguna.

Tanpa pemeriksaan di **[3]**, memanggil `isi_krs()` pada objek `Dosen` akan menghentikan program dengan `AttributeError`. Pesan lengkapnya ada di [Kesalahan 1](#kesalahan-1-memanggil-method-khusus-tanpa-memeriksa-jenis).

> [!TIP]
> `isinstance` bisa memeriksa beberapa kelas sekaligus dengan tuple: `isinstance(pengguna, (Mahasiswa, Dosen))`. Bedakan juga dengan `type(ayu) is Pengguna`, yang hanya menjawab "ya" jika kelasnya **persis** `Pengguna` (hasilnya `False` untuk Ayu). Untuk polimorfisme, `isinstance` hampir selalu pilihan yang tepat.

> [!WARNING]
> Gunakan `isinstance` hanya untuk method yang benar-benar **khusus**. Untuk perilaku yang dimiliki semua jenis, misalnya teks peran, cukup *override* lalu panggil langsung seperti di **[2]**. Kode yang penuh `if isinstance(...) elif isinstance(...)` adalah tanda rancangan belum memanfaatkan polimorfisme.

## 4. Polimorfisme dari Dalam Kelas

File: [`contoh/contoh04_polimorfisme_dari_dalam_kelas.py`](contoh/contoh04_polimorfisme_dari_dalam_kelas.py)

Method `tulis()` hanya ditulis sekali, di kelas induk. Namun hasilnya berbeda untuk setiap jenis kartu.

```python
class KartuUcapan:
    """Kartu ucapan umum. Kerangka tulis() sama untuk semua jenis kartu."""

    def __init__(self, penerima: str, pengirim: str):
        self._penerima = penerima
        self._pengirim = pengirim

    def salam(self) -> str:
        return f"Halo, {self._penerima}!"

    def isi(self) -> str:
        return "Semoga harimu menyenangkan."

    def tulis(self):  # [1] method induk yang memanggil method lain lewat self
        print("-" * 40)
        print(self.salam())  # [2] versi siapa? tergantung objek self
        print(self.isi())
        print(f"Salam hangat, {self._pengirim}")
        print("-" * 40)
```

`KartuUlangTahun` menyimpan `_umur` dan hanya meng-*override* `isi()` (ditandai `# [3]`). Kelas ketiga:

```python
class KartuWisuda(KartuUcapan):
    def salam(self) -> str:  # [4] salam() dan isi() sama-sama di-override
        return f"Selamat, {self._penerima}, S.Kom.!"

    def isi(self) -> str:
        return "Perjuanganmu terbayar lunas. " + super().isi()  # [5]
```

Program utamanya membuat tiga kartu (umum, ulang tahun, dan wisuda) di dalam list, lalu memanggil `kartu.tulis()` untuk masing-masing.

**Output:**

```text
=== Kartu 1: KartuUcapan ===
----------------------------------------
Halo, Siti!
Semoga harimu menyenangkan.
Salam hangat, Budi
----------------------------------------

=== Kartu 2: KartuUlangTahun ===
----------------------------------------
Halo, Rina!
Selamat ulang tahun yang ke-20!
Salam hangat, Ayu
----------------------------------------

=== Kartu 3: KartuWisuda ===
----------------------------------------
Selamat, Dimas, S.Kom.!
Perjuanganmu terbayar lunas. Semoga harimu menyenangkan.
Salam hangat, Keluarga di Samarinda
----------------------------------------
```

Penjelasan:

- **[1]** `tulis()` adalah **kerangka** yang sama untuk semua kartu: garis, salam, isi, pengirim, garis.
- **[2]** `self.salam()` dan `self.isi()` dipanggil lewat `self`. Saat `kartu_wisuda.tulis()` berjalan, `self` adalah objek `KartuWisuda`, jadi yang dipanggil adalah versi `KartuWisuda`.
- **[3]** (di `KartuUlangTahun`) Hanya `isi()` yang di-*override*. Salamnya tetap versi induk (`Halo, Rina!`).
- **[4]** `KartuWisuda` meng-*override* keduanya. Kelas ini tidak menulis `__init__`, jadi konstruktor induk dipakai apa adanya.
- **[5]** Gaya "memperluas" dari Pertemuan 07: versi anak menambahkan kalimat, lalu memakai versi induk lewat `super().isi()`.
- **[6]** (di `main`) Program utama hanya memanggil `tulis()`. Ia tidak tahu bahwa di dalamnya terjadi polimorfisme.

Jejak eksekusi untuk kartu ketiga:

```text
kartu.tulis()                      -> tulis() milik KartuUcapan (KartuWisuda tidak punya tulis)
  self.salam()                     -> self adalah KartuWisuda -> "Selamat, Dimas, S.Kom.!"
  self.isi()                       -> self adalah KartuWisuda -> isi() milik KartuWisuda
    super().isi()                  -> isi() milik KartuUcapan -> "Semoga harimu menyenangkan."
```

## 5. Duck Typing: Tanpa Pewarisan pun Bisa

File: [`contoh/contoh05_duck_typing.py`](contoh/contoh05_duck_typing.py)

Di Python, polimorfisme bahkan tidak membutuhkan pewarisan.

```python
class AyamJago:  # [1] tidak mewarisi kelas apa pun (selain object)
    def bunyikan(self) -> str:
        return "Kukuruyuuuk!"


class AlarmPonsel:
    def __init__(self, jam: str):
        self._jam = jam

    def bunyikan(self) -> str:
        return f"Kriiing! Sudah pukul {self._jam}"


class Kentongan:
    def bunyikan(self) -> str:
        return "Tung tung tung!"


class BelSekolah:  # [2] kelas baru, juga tanpa induk bersama
    def bunyikan(self) -> str:
        return "Teeet! Waktunya masuk kelas"


def bangunkan_semua(daftar: list):  # [3] tidak menyebut tipe khusus apa pun
    for benda in daftar:
        nama = type(benda).__name__
        print(f"{nama:<12}: {benda.bunyikan()}")  # [4] cukup punya bunyikan()


def main():
    print("=== PAGI DI ASRAMA ===")
    bangunkan_semua([AyamJago(), AlarmPonsel("05.00"), Kentongan()])

    print()
    print("=== PAGI DI SEKOLAH ===")
    bangunkan_semua([BelSekolah(), AlarmPonsel("06.45")])
```

**Output:**

```text
=== PAGI DI ASRAMA ===
AyamJago    : Kukuruyuuuk!
AlarmPonsel : Kriiing! Sudah pukul 05.00
Kentongan   : Tung tung tung!

=== PAGI DI SEKOLAH ===
BelSekolah  : Teeet! Waktunya masuk kelas
AlarmPonsel : Kriiing! Sudah pukul 06.45
```

Penjelasan:

- **[1]** `AyamJago`, `AlarmPonsel`, `Kentongan`, dan `BelSekolah` tidak punya induk bersama. Induk mereka hanya kelas akar `object`, yang tidak punya `bunyikan()`.
- **[2]** Kelas baru pun cukup punya `bunyikan()` untuk ikut diproses.
- **[3]** *Type hint* parameter hanya `list`. Tidak ada kelas induk yang bisa disebut, dan Python tidak membutuhkannya.
- **[4]** Saat `benda.bunyikan()` dijalankan, Python hanya mencari method bernama `bunyikan` di objek itu. Python tidak bertanya "kamu kelas apa?", melainkan "kamu bisa `bunyikan()` atau tidak?".

Kelemahannya: kesalahan baru ketahuan saat program **berjalan**. Jika ada objek yang tidak punya `bunyikan()`, misalnya objek `Batu`, beginilah yang terjadi:

```python
class AyamJago:
    def bunyikan(self):
        return "Kukuruyuuuk!"


class Batu:
    pass


for benda in [AyamJago(), Batu()]:
    print(benda.bunyikan())
```

Hasilnya:

```text
Kukuruyuuuk!
Traceback (most recent call last):
  File "contoh.py", line 11, in <module>
    print(benda.bunyikan())
          ^^^^^^^^^^^^^^
AttributeError: 'Batu' object has no attribute 'bunyikan'
```

Objek pertama berhasil berbunyi, lalu program berhenti di objek kedua. Pesan `'Batu' object has no attribute 'bunyikan'` berarti objek `Batu` tidak punya method `bunyikan`.

> [!NOTE]
> Jalur Java punya contoh 05 dengan output yang sama persis, tetapi semua kelasnya **wajib** mewarisi kelas induk bersama. Java tidak mengenal *duck typing*: *compiler* harus yakin setiap objek punya `bunyikan()` sebelum program dijalankan. Perbandingannya ada di [Jembatan Python ↔ Java](../jembatan-python-java.md).

## 6. Python Tidak Punya Overloading

Di Java, satu kelas boleh punya beberapa method bernama sama dengan daftar parameter berbeda. Teknik ini disebut ***overloading***. Bagaimana jika kita mencobanya di Python?

```python
class Penyapa:
    def sapa(self):
        return "Halo!"

    def sapa(self, nama):
        return f"Halo, {nama}!"


p = Penyapa()
print(p.sapa("Budi"))
print(p.sapa())
```

Hasilnya:

```text
Halo, Budi!
Traceback (most recent call last):
  File "contoh.py", line 11, in <module>
    print(p.sapa())
          ~~~~~~^^
TypeError: Penyapa.sapa() missing 1 required positional argument: 'nama'
```

Penjelasannya:

- Saat kelas dibaca, Python menjalankan isi kelas dari atas ke bawah. `def sapa(self)` membuat method bernama `sapa`.
- `def sapa(self, nama)` membuat method **baru** dengan nama yang sama. Nama `sapa` kini menunjuk method kedua, dan method pertama **hilang**.
- Tidak ada pesan error saat kelas ditulis. Pemanggilan `p.sapa("Budi")` bahkan berhasil, karena cocok dengan method kedua.
- Error baru muncul saat `p.sapa()` dipanggil tanpa argumen. Versi tanpa parameter itu sudah tidak ada.

Ibaratnya menyimpan kontak "Ibu" dua kali di ponsel yang tidak mengizinkan nama kembar. Nomor kedua menimpa nomor pertama tanpa bertanya.

> [!IMPORTANT]
> Di Python, satu nama method dalam satu kelas hanya punya **satu** isi. `def` kedua dengan nama sama selalu **menimpa** `def` pertama, diam-diam. Beberapa editor memberi garis peringatan, tetapi Python sendiri tidak.

Lalu bagaimana membuat satu method yang bisa dipanggil dengan banyak cara? Jawabannya di bagian berikut.

## 7. Pengganti Overloading: Nilai Bawaan, Argumen Kata Kunci, dan `*args`

File: [`contoh/contoh06_pengganti_overloading.py`](contoh/contoh06_pengganti_overloading.py)

Contoh ini adalah perpustakaan sederhana. Kelas `Buku` menyimpan judul, penulis, dan tahun. Bagian pentingnya ada di kelas `Perpustakaan`:

```python
class Perpustakaan:
    """Perpustakaan sederhana yang bisa menyimpan dan mencari buku."""

    def __init__(self, nama: str = "Perpustakaan Kampus"):  # [1] nilai bawaan
        self._nama = nama
        self._koleksi: list[Buku] = []
        print(f"{self._nama} dibuka")

    def tambah_buku(self, *daftar_buku: Buku):  # [2] *args: berapa pun jumlahnya
        for buku in daftar_buku:  # daftar_buku berupa tuple berisi semua argumen
            self._koleksi.append(buku)
        print(f"{self._nama}: {len(daftar_buku)} buku ditambahkan")

    def cari(self, kata_kunci: str = "", tahun: int = 0) -> list[Buku]:  # [3]
        """Cari berdasarkan judul, tahun, atau keduanya (tahun 0 = bebas)."""
        hasil = []
        for buku in self._koleksi:
            cocok_judul = kata_kunci in buku.judul  # teks kosong selalu cocok
            cocok_tahun = tahun == 0 or buku.tahun == tahun
            if cocok_judul and cocok_tahun:
                hasil.append(buku)
        return hasil
```

Program utamanya:

```python
def main():
    print("=== KONSTRUKTOR DENGAN NILAI BAWAAN ===")
    pusat = Perpustakaan()  # [4] nama tidak diisi -> nilai bawaan dipakai
    pojok = Perpustakaan("Pojok Baca Informatika")

    print()
    print("=== SATU METHOD, JUMLAH ARGUMEN BEBAS ===")
    pusat.tambah_buku(Buku("Laskar Pelangi", "Andrea Hirata", 2005))  # [5] 1 buku
    pusat.tambah_buku(
        Buku("Sang Pemimpi", "Andrea Hirata", 2006),
        Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980),
        Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    )  # 3 buku sekaligus
    pojok.tambah_buku()  # 0 buku pun boleh

    print()
    print("=== SATU NAMA METHOD, BANYAK CARA CARI ===")
    tampilkan("Judul memuat 'Pe'", pusat.cari("Pe"))  # [6]
    tampilkan("Tahun 1980", pusat.cari(tahun=1980))  # [7] argumen kata kunci
    tampilkan("Judul memuat 'a', tahun 2006", pusat.cari("a", 2006))  # [8]
    tampilkan("Judul memuat 'Kancil'", pusat.cari("Kancil"))
```

**Output:**

```text
=== KONSTRUKTOR DENGAN NILAI BAWAAN ===
Perpustakaan Kampus dibuka
Pojok Baca Informatika dibuka

=== SATU METHOD, JUMLAH ARGUMEN BEBAS ===
Perpustakaan Kampus: 1 buku ditambahkan
Perpustakaan Kampus: 3 buku ditambahkan
Pojok Baca Informatika: 0 buku ditambahkan

=== SATU NAMA METHOD, BANYAK CARA CARI ===
Judul memuat 'Pe'           : Laskar Pelangi (2005), Sang Pemimpi (2006)
Tahun 1980                  : Bumi Manusia (1980)
Judul memuat 'a', tahun 2006: Sang Pemimpi (2006)
Judul memuat 'Kancil'       : (tidak ada)
```

Penjelasan:

- **[1]** **Nilai bawaan** (*default*): jika `nama` tidak diisi, Python memakai `"Perpustakaan Kampus"`. Di Java, hal yang sama dikerjakan dengan dua konstruktor (overloading). Teknik ini sudah kamu kenal sejak Pertemuan 03.
- **[2]** Tanda bintang pada `*daftar_buku` membuat method menerima argumen **berapa pun jumlahnya**. Semua argumen dikumpulkan menjadi sebuah *tuple*. Nama umumnya `*args`, tetapi boleh diberi nama yang lebih jelas.
- **[3]** Satu method `cari` dengan **dua** nilai bawaan menggantikan tiga versi overloading di Java: cari judul, cari tahun, dan cari keduanya.
- **[4]** `Perpustakaan()` tanpa argumen memakai nama bawaan.
- **[5]** `tambah_buku` dipanggil dengan satu buku, lalu tiga buku, lalu tanpa buku sama sekali. Method-nya tetap satu.
- **[6]** `cari("Pe")` hanya mengisi `kata_kunci`. `tahun` memakai nilai bawaan 0 (bebas).
- **[7]** **Argumen kata kunci** (*keyword argument*): `tahun=1980` mengisi parameter `tahun` secara langsung dan melewati `kata_kunci`, yang tetap memakai nilai bawaan `""`.
- **[8]** Kedua parameter diisi berurutan seperti biasa.

| Cara memanggil | Isi parameter |
|---|---|
| `cari("Pe")` | `kata_kunci="Pe"`, `tahun=0` |
| `cari(tahun=1980)` | `kata_kunci=""`, `tahun=1980` |
| `cari("a", 2006)` | `kata_kunci="a"`, `tahun=2006` |

> [!WARNING]
> Jangan memakai list atau dict sebagai nilai bawaan, misalnya `def tambah(self, daftar=[])`. Nilai bawaan dibuat **sekali** saat `def` dibaca, sehingga list yang sama ikut terbawa ke setiap pemanggilan. Pakai `None` sebagai nilai bawaan, lalu buat list baru di dalam method.

> [!NOTE]
> Jalur Java punya satu contoh tambahan, yaitu contoh 07, tentang aturan "*overload* dipilih saat kompilasi, *override* dipilih saat berjalan". Contoh itu **khusus Java**, karena Python tidak punya overloading. Ringkasannya ada di [Jembatan Python ↔ Java](../jembatan-python-java.md).

## 8. Studi Kasus KedaiKita

File: [`studi-kasus/pembayaran.py`](studi-kasus/pembayaran.py), [`studi-kasus/pesanan.py`](studi-kasus/pesanan.py), dan [`studi-kasus/main.py`](studi-kasus/main.py)

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#10-studi-kasus-kedaikita-banyak-cara-bayar).

**Apa yang berubah dibanding Pertemuan 07?**

- **File baru `pembayaran.py`** berisi kelas induk `Pembayaran` dan tiga kelas anak: `PembayaranTunai`, `PembayaranQRIS`, dan `PembayaranKartu`.
- **`pesanan.py`**: `Pesanan` punya atribut `_status` (`"BARU"` lalu `"LUNAS"`), *property* `status`, method baru `bayar(pembayaran)`, dan `tambah_item(menu, jumlah=1)` kini punya nilai bawaan. Struk ikut menampilkan status.
- **`main.py`**: menambah bagian "SATU PANGGILAN, BANYAK BENTUK", pembayaran Budi dan Siti, serta "MEMERIKSA JENIS PEMBAYARAN".
- `menu.py`, `kedai.py`, `pelanggan.py`, dan `utilitas.py` **tidak berubah**.

Berikut isi `pembayaran.py` (tanpa *docstring* modul di baris paling atas):

```python
from utilitas import format_rupiah


class Pembayaran:
    """Kelas induk semua metode pembayaran."""

    def nama_metode(self) -> str:
        return "Pembayaran umum"

    def hitung_biaya_layanan(self, total: int) -> int:
        """Biaya tambahan yang dibebankan ke pelanggan. Bawaannya 0."""
        return 0

    def proses(self, total: int) -> bool:
        """Memproses pembayaran. Mengembalikan True jika berhasil."""
        print(f"  Memproses pembayaran {format_rupiah(total)}")
        return True


class PembayaranTunai(Pembayaran):
    """Bayar dengan uang tunai. Bisa menghasilkan kembalian."""

    def __init__(self, uang_diterima: int):
        self._uang_diterima = uang_diterima
        self._kembalian = 0

    @property
    def kembalian(self) -> int:
        return self._kembalian

    def nama_metode(self) -> str:
        return "Tunai"

    def proses(self, total: int) -> bool:
        if self._uang_diterima < total:
            kurang = total - self._uang_diterima
            print(f"  Uang kurang {format_rupiah(kurang)}")
            return False
        self._kembalian = self._uang_diterima - total
        print(f"  Uang diterima {format_rupiah(self._uang_diterima)}, "
              f"kembalian {format_rupiah(self._kembalian)}")
        return True
```

`PembayaranQRIS` ditulis dengan pola yang sama seperti tunai, tetapi menyimpan `_saldo` e-wallet dan memotongnya di `proses()`. Kelas anak terakhir:

```python
class PembayaranKartu(Pembayaran):
    """Kartu kredit: pelanggan dikenai biaya layanan 2%."""

    PERSEN_BIAYA = 2

    def __init__(self, nama_bank: str):
        self._nama_bank = nama_bank

    def nama_metode(self) -> str:
        return f"Kartu Kredit {self._nama_bank}"

    def hitung_biaya_layanan(self, total: int) -> int:
        return total * PembayaranKartu.PERSEN_BIAYA // 100

    def proses(self, total: int) -> bool:
        print(f"  Transaksi kartu {self._nama_bank} disetujui "
              f"sebesar {format_rupiah(total)}")
        return True
```

- **`Pembayaran`** menetapkan tiga method yang dimiliki **semua** jenis pembayaran. `hitung_biaya_layanan` bawaannya 0, jadi hanya kelas yang punya biaya tambahan yang perlu meng-*override*-nya.
- **Setiap kelas anak meng-*override* yang perlu saja.** Tunai dan QRIS tidak menulis `hitung_biaya_layanan`, sehingga biayanya 0 (warisan induk). Kartu kredit meng-*override* ketiganya.
- **Setiap kelas menyimpan datanya sendiri:** tunai menyimpan uang yang diterima dan kembalian, QRIS menyimpan saldo, kartu menyimpan nama bank. Data khusus ini hanya dipakai oleh `proses()` milik kelas itu sendiri.
- **Kelas `Pembayaran` "umum" terasa janggal.** Tidak ada pelanggan yang membayar dengan "Pembayaran umum". Di Pertemuan 10, kelas ini dijadikan kelas abstrak.

Di `pesanan.py`, inilah dua method yang berubah atau baru:

```python
    def tambah_item(self, menu: Menu, jumlah: int = 1):
        item = ItemPesanan(menu, jumlah)  # objek item dibuat OLEH pesanan
        menu.kurangi_stok(jumlah)  # gagal (ValueError) jika stok kurang
        self._daftar_item.append(item)
```

```python
    def bayar(self, pembayaran: Pembayaran) -> bool:
        """Membayar pesanan dengan metode pembayaran apa pun."""
        total = self.hitung_total()
        biaya = pembayaran.hitung_biaya_layanan(total)  # polimorfisme
        total_bayar = total + biaya
        print(f"Pembayaran pesanan {self._nomor} ({self._pelanggan.nama})")
        print(f"  Metode       : {pembayaran.nama_metode()}")  # polimorfisme
        if biaya > 0:
            print(f"  Biaya layanan: {format_rupiah(biaya)}")
        print(f"  Total bayar  : {format_rupiah(total_bayar)}")
        berhasil = pembayaran.proses(total_bayar)  # polimorfisme
        if berhasil:
            self._status = "LUNAS"
            poin = total // 10000
            if poin > 0:
                self._pelanggan.tambah_poin(poin)
            print(f"  Status       : LUNAS (+{poin} poin)")
        else:
            print("  Status       : GAGAL, silakan pilih metode lain")
        return berhasil
```

- **`jumlah: int = 1`** membuat `tambah_item(menu)` berarti satu porsi. Java memakai overloading untuk hal yang sama, yaitu method `tambahItem(Menu)` tambahan.
- **`bayar()` tidak punya satu pun `if isinstance(...)`.** Tiga baris bertanda `# polimorfisme` memanggil method milik objek pembayaran yang sebenarnya.
- **Poin dihitung dari total pesanan** (sebelum biaya layanan): 1 poin per Rp10.000.

Di `main.py`, bagian "SATU PANGGILAN, BANYAK BENTUK" memproses list `daftar_metode` berisi tiga jenis pembayaran dengan satu perulangan. Berikut pembayaran Siti dan pemeriksaan jenis pembayaran:

```python
    pesanan_siti = kedai.buat_pesanan(siti)
    pesanan_siti.tambah_item(kedai.cari_menu("M02"), 2)
    pesanan_siti.tambah_item(kedai.cari_menu("M05"))
    pesanan_siti.cetak_struk()
    berhasil = pesanan_siti.bayar(PembayaranQRIS(20000))
    if not berhasil:
        print()
        pesanan_siti.bayar(PembayaranKartu("BNI"))
    print()

    print("=== MEMERIKSA JENIS PEMBAYARAN ===")
    for pembayaran in [pembayaran_budi, PembayaranKartu("Mandiri")]:
        if isinstance(pembayaran, PembayaranTunai):
            kembalian = format_rupiah(pembayaran.kembalian)
            print(f"{pembayaran.nama_metode()}: kembalian {kembalian}")
        else:
            print(f"{pembayaran.nama_metode()}: tidak ada kembalian")
    print()
```

- **`bayar()` mengembalikan `True`/`False`.** Jika QRIS gagal, program mencoba metode lain. Pesanan yang sama dibayar dengan objek pembayaran berbeda, tanpa mengubah `bayar()`.
- **`isinstance` dipakai hanya untuk fitur khusus.** *Property* `kembalian` hanya dimiliki `PembayaranTunai`, jadi jenisnya diperiksa dulu.

Jalankan `python main.py` dari dalam folder `studi-kasus` (lihat [Persiapan](#persiapan)).

Daftar menu di awal output sama persis dengan Pertemuan 07. Sesudahnya:

**Output:**

```text
=== SATU PANGGILAN, BANYAK BENTUK ===
Tunai                biaya layanan untuk Rp100.000: Rp0
QRIS                 biaya layanan untuk Rp100.000: Rp0
Kartu Kredit BNI     biaya layanan untuk Rp100.000: Rp2.000

========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P001
Pelanggan   : Budi Santoso
Status      : BARU
----------------------------------------
2 x Kopi Susu Gula Aren         Rp36.000
1 x Nasi Goreng Kampung         Rp25.000
----------------------------------------
TOTAL                           Rp61.000
========================================
Pembayaran pesanan P001 (Budi Santoso)
  Metode       : Tunai
  Total bayar  : Rp61.000
  Uang diterima Rp100.000, kembalian Rp39.000
  Status       : LUNAS (+6 poin)

========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P002
Pelanggan   : Siti Aminah
Status      : BARU
----------------------------------------
2 x Es Teh Manis                Rp16.000
1 x Pisang Goreng Keju          Rp15.000
----------------------------------------
TOTAL                           Rp31.000
========================================
Pembayaran pesanan P002 (Siti Aminah)
  Metode       : QRIS
  Total bayar  : Rp31.000
  Saldo e-wallet tidak cukup (saldo Rp20.000)
  Status       : GAGAL, silakan pilih metode lain

Pembayaran pesanan P002 (Siti Aminah)
  Metode       : Kartu Kredit BNI
  Biaya layanan: Rp620
  Total bayar  : Rp31.620
  Transaksi kartu BNI disetujui sebesar Rp31.620
  Status       : LUNAS (+3 poin)

=== MEMERIKSA JENIS PEMBAYARAN ===
Tunai: kembalian Rp39.000
Kartu Kredit Mandiri: tidak ada kembalian

=== STATUS AKHIR ===
P001: LUNAS
P002: LUNAS
Budi Santoso (081234567890) - 6 poin
Siti Aminah (082198765432) - 3 poin
```

Perhatikan pembayaran Siti. Method `bayar()` yang **sama** dipanggil dua kali pada pesanan yang **sama**. Yang berbeda hanya objek pembayarannya, dan itulah yang menentukan seluruh perilakunya: ada atau tidaknya baris biaya layanan, cara memproses, dan berhasil atau tidaknya pembayaran.

> [!TIP]
> **Coba sendiri:**
> 1. Ubah saldo QRIS Siti dari `20000` menjadi `50000`. Apa yang tercetak pada pembayaran Siti?
> 2. Di bagian "SATU PANGGILAN, BANYAK BENTUK", tambahkan `Pembayaran()` ke `daftar_metode`. Baris apa yang muncul, dan mengapa terasa janggal?

<details>
<summary>Lihat jawaban</summary>

1. Pembayaran QRIS langsung berhasil. Tercetak `Saldo e-wallet terpotong Rp31.000, sisa Rp19.000` lalu `Status       : LUNAS (+3 poin)`, sehingga percobaan kartu kredit tidak dijalankan.

2. Muncul baris `Pembayaran umum      biaya layanan untuk Rp100.000: Rp0`. Janggal, karena "pembayaran umum" bukan metode bayar sungguhan. Objek seperti ini seharusnya tidak bisa dibuat. Pertemuan 10 akan memperbaikinya dengan kelas abstrak.

</details>

## 9. Kesalahan Umum dan Cara Membaca Pesan Error

Ingat, pesan error Python dibaca **dari bawah ke atas**. Baris paling bawah menyebut jenis error dan penyebabnya. Baris di atasnya menunjukkan lokasinya. Dua kesalahan lain sudah dibahas di bagian sebelumnya: objek tanpa method yang dibutuhkan *duck typing* ([bagian 5](#5-duck-typing-tanpa-pewarisan-pun-bisa)) dan `def` kedua yang menimpa `def` pertama ([bagian 6](#6-python-tidak-punya-overloading)).

### Kesalahan 1: Memanggil method khusus tanpa memeriksa jenis

Misalkan kelas `Mahasiswa` punya `isi_krs()`, sedangkan `Dosen` tidak, seperti di contoh 03:

```python
daftar = [Mahasiswa("Ayu"), Dosen("Rahmat")]
for pengguna in daftar:
    print(pengguna.isi_krs(21))
```

```text
Ayu mengisi KRS 21 SKS
Traceback (most recent call last):
  File "contoh.py", line 17, in <module>
    print(pengguna.isi_krs(21))
          ^^^^^^^^^^^^^^^^
AttributeError: 'Dosen' object has no attribute 'isi_krs'
```

**Artinya:** putaran pertama berhasil, tetapi objek kedua adalah `Dosen`, yang tidak punya `isi_krs`. **Perbaikan:** periksa dulu dengan `if isinstance(pengguna, Mahasiswa):` seperti di [bagian 3](#3-memeriksa-jenis-objek-dengan-isinstance), atau jika perilakunya dibutuhkan semua jenis, jadikan method di kelas induk lalu *override*.

### Kesalahan 2: Parameter versi anak berbeda dengan versi induk

Kelas `BangunDatar` dan `Persegi` ditulis seperti contoh 02 (`luas()` tanpa parameter). Lalu `Segitiga` menambahkan parameter:

```python
class Segitiga(BangunDatar):
    def __init__(self, alas, tinggi):
        self._alas = alas
        self._tinggi = tinggi

    def luas(self, satuan):
        return f"{self._alas * self._tinggi // 2} {satuan}"


for bangun in [Persegi(10), Segitiga(8, 6)]:
    print(bangun.luas())
```

```text
100
Traceback (most recent call last):
  File "contoh.py", line 24, in <module>
    print(bangun.luas())
          ~~~~~~~~~~~^^
TypeError: Segitiga.luas() missing 1 required positional argument: 'satuan'
```

**Artinya:** `Segitiga.luas()` meminta parameter `satuan`, padahal pemanggil polimorfik memanggil `luas()` tanpa argumen, sesuai "janji" kelas induk. Python tidak memeriksa kecocokan parameter saat kelas ditulis, jadi kesalahan baru ketahuan saat program berjalan. **Perbaikan:** samakan daftar parameter dengan versi induk. Jika butuh data tambahan, simpan sebagai atribut lewat konstruktor.

### Kesalahan 3: Versi anak mencetak, padahal versi induk mengembalikan

```python
class Hewan:
    def bersuara(self):
        return "(diam saja)"


class Kucing(Hewan):
    def bersuara(self):
        print("Meong!")


for hewan in [Hewan(), Kucing()]:
    print(f"Suaranya: {hewan.bersuara()}")
```

Tidak ada pesan error, tetapi hasilnya aneh:

```text
Suaranya: (diam saja)
Meong!
Suaranya: None
```

**Artinya:** `Kucing.bersuara()` mencetak `Meong!` lalu selesai tanpa `return`, sehingga nilai kembaliannya `None`. Pemanggil mengharapkan teks, seperti yang dijanjikan versi induk. **Perbaikan:** versi anak harus mengembalikan jenis nilai yang sama dengan versi induk: `return "Meong!"`.

### Kesalahan 4: Salah ketik nama method saat override

Jika `Kucing` menulis `def bersuar(self)` (kurang satu huruf), Python menganggapnya method **baru**. Tidak ada error sama sekali, tetapi kucing akan "diam saja", karena `bersuara()` milik induk yang dipakai. Kesalahan ini sudah dibahas di Pertemuan 07, dan dampaknya makin terasa pada polimorfisme: satu jenis objek diam-diam berperilaku seperti induknya. **Perbaikan:** periksa ejaan dengan teliti, dan uji setiap kelas anak.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi Python. Misalnya, baris bertanda `^^^^` atau `~~~^^` hanya muncul di Python 3.11 ke atas. Fokuslah pada **jenis error** (`AttributeError`, `TypeError`) dan kata kuncinya, seperti `has no attribute` dan `missing 1 required positional argument`.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| Override (dasar polimorfisme) | `def` dengan nama dan parameter sama di kelas anak | `def bersuara(self) -> str:` |
| Pemanggilan polimorfik | `objek.method()` | `hewan.bersuara()` |
| Parameter bertipe induk | *type hint* kelas induk | `def suruh_bersuara(hewan: Hewan):` |
| Koleksi polimorfik | list berisi objek berbagai kelas anak | `[Persegi(10), Segitiga(8, 6)]` |
| Memeriksa jenis objek | `isinstance(objek, Kelas)` | `isinstance(pengguna, Mahasiswa)` |
| Memeriksa beberapa jenis | `isinstance(objek, (A, B))` | `isinstance(p, (Mahasiswa, Dosen))` |
| Polimorfisme dari dalam kelas | `self.method()` di method induk | `print(self.isi())` |
| *Duck typing* | panggil method tanpa memeriksa kelas | `benda.bunyikan()` |
| Nilai bawaan | `param=nilai` | `def cari(self, kata_kunci="", tahun=0):` |
| Argumen kata kunci | `nama_param=nilai` saat memanggil | `pusat.cari(tahun=1980)` |
| Jumlah argumen bebas | `*nama` | `def tambah_buku(self, *daftar_buku):` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
