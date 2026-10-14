# 🐍 Praktik Python — Pertemuan 05: Relasi Antar Kelas

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 05](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Dependensi: Objek sebagai Parameter](#1-dependensi-objek-sebagai-parameter)
2. [Asosiasi: Atribut Berisi Objek Lain](#2-asosiasi-atribut-berisi-objek-lain)
3. [Agregasi: List Berisi Objek dari Luar](#3-agregasi-list-berisi-objek-dari-luar)
4. [Komposisi: Bagian Dibuat di Dalam](#4-komposisi-bagian-dibuat-di-dalam)
5. [Multiplisitas dan Pencarian yang Bisa Gagal](#5-multiplisitas-dan-pencarian-yang-bisa-gagal)
6. [Mengembalikan Salinan List](#6-mengembalikan-salinan-list)
7. [Objek Saling Mengirim Pesan](#7-objek-saling-mengirim-pesan)
8. [Program Multi-File dengan import](#8-program-multi-file-dengan-import)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan Error](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/                     <- 8 contoh, dari yang paling sederhana
│   └── contoh08_multi_file/    <- contoh 08 terdiri atas 3 file
├── studi-kasus/                <- KedaiKita versi Pertemuan 05 (6 file)
└── solusi/                     <- solusi latihan (buka setelah mencoba sendiri!)
```

Contoh 01 sampai 07 masing-masing berupa satu file. Cara menjalankannya sama seperti pertemuan sebelumnya:

```bash
cd Pertemuan-05-Relasi-Antar-Kelas/python/contoh
python contoh01_dependensi.py
```

Contoh 08 dan studi kasus terdiri atas **beberapa file**. Untuk keduanya, kamu harus masuk dulu ke foldernya masing-masing, seperti dijelaskan di bagian 8 dan 9.

> [!NOTE]
> Di macOS/Linux, gunakan `python3` sebagai ganti `python`. Jika kamu memakai VS Code, buka file `.py`-nya lalu klik tombol ▶ (*Run Python File*) di pojok kanan atas. Panduan instalasi lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

### Kenalan dengan petunjuk tipe (*type hints*)

Mulai pertemuan ini, kode Python kita memakai **petunjuk tipe** (*type hints*), yaitu keterangan tipe data pada parameter dan nilai kembalian. Contohnya:

```python
    def antar(self, tujuan: str, jarak_km: int) -> int:
```

| Penulisan | Artinya |
|---|---|
| `tujuan: str` | parameter `tujuan` diharapkan berupa teks |
| `jarak_km: int` | parameter `jarak_km` diharapkan berupa bilangan bulat |
| `-> int` | method ini mengembalikan bilangan bulat |
| `ojek: Ojek` | parameter `ojek` diharapkan berupa objek kelas `Ojek` |
| `list[Pemain]` | list yang isinya objek-objek `Pemain` |
| `Peserta \| None` | objek `Peserta`, **atau** `None` jika tidak ada |

Atribut juga boleh diberi petunjuk tipe saat pertama kali diisi, misalnya `self._daftar_pemain: list[Pemain] = []`. Method yang tidak mengembalikan apa-apa tidak kita beri `-> None` agar ringkas.

> [!IMPORTANT]
> Petunjuk tipe hanyalah **keterangan**. Python tidak memeriksanya saat program berjalan, jadi mengirim teks ke parameter bertipe `int` tetap tidak dicegah. Manfaatnya: kode lebih mudah dibaca, dan editor seperti VS Code bisa memberi saran serta peringatan lebih awal. Penulisan `Peserta | None` membutuhkan Python 3.10 atau lebih baru.

## 1. Dependensi: Objek sebagai Parameter

File: [`contoh/contoh01_dependensi.py`](contoh/contoh01_dependensi.py)

Kita mulai dari hubungan paling longgar. Kelas `Ojek` menyimpan nama pengemudi, plat nomor, dan tarif per km. Method `antar(tujuan, jarak_km)` mencetak siapa yang mengantar, lalu mengembalikan ongkosnya. Yang menarik adalah kelas `Penumpang`:

```python
class Penumpang:
    """Penumpang yang memesan ojek. Ia TIDAK menyimpan objek Ojek."""

    def __init__(self, nama: str):
        self._nama = nama
        self._jumlah_perjalanan = 0  # [1] yang diingat hanya angka-angka ini
        self._total_ongkos = 0
```

Setelah dua property untuk membaca angka-angka itu (`jumlah_perjalanan` dan `total_ongkos`), ada method utamanya:

```python
    def pesan_ojek(self, ojek: Ojek, tujuan: str, jarak_km: int):  # [2]
        print(f"{self._nama} memesan ojek, jarak {jarak_km} km")
        ongkos = ojek.antar(tujuan, jarak_km)  # [3] memakai objek Ojek
        self._jumlah_perjalanan += 1
        self._total_ongkos += ongkos
        print(f"  Ongkos: Rp{ongkos}")
        # [4] method selesai: parameter ojek dilepas, tidak disimpan di self
```

Program utamanya membuat penumpang Ayu dan dua objek ojek, `ojek_rudi` dan `ojek_dedi`, lalu:

```python
    print("=== PERJALANAN 1 ===")
    ayu.pesan_ojek(ojek_rudi, "Kampus Gunung Kelua", 4)  # [5]

    print()
    print("=== PERJALANAN 2 ===")
    ayu.pesan_ojek(ojek_dedi, "Tepian Mahakam", 6)  # ojek lain pun bisa
```

**Output:**

```text
=== PERJALANAN 1 ===
Ayu memesan ojek, jarak 4 km
  Pak Rudi (KT 4521 AB) mengantar ke Kampus Gunung Kelua
  Ongkos: Rp10000

=== PERJALANAN 2 ===
Ayu memesan ojek, jarak 6 km
  Bang Dedi (KT 3317 CD) mengantar ke Tepian Mahakam
  Ongkos: Rp15000

=== RINGKASAN ===
Ayu sudah 2 kali naik ojek
Total ongkos: Rp25000
```

Penjelasan:

- **[1]** Atribut milik `Penumpang` hanya nama, jumlah perjalanan, dan total ongkos. **Tidak ada** atribut yang menyimpan objek `Ojek`.
- **[2]** Objek `Ojek` masuk lewat **parameter** `ojek`. Petunjuk tipe `ojek: Ojek` memberi tahu pembaca bahwa yang diharapkan adalah objek kelas `Ojek`.
- **[3]** Di sinilah objek penumpang **mengirim pesan** ke objek ojek: "antar aku, lalu beri tahu ongkosnya".
- **[4]** Begitu method selesai, parameter `ojek` ikut hilang. Penumpang tidak lagi memegang ojek mana pun. Inilah ciri khas **dependensi**.
- **[5]** Setiap perjalanan boleh memakai ojek yang berbeda, karena penumpang tidak terikat pada satu ojek. Objek ojek bahkan boleh dibuat langsung di dalam pemanggilan, misalnya `ayu.pesan_ojek(Ojek("Mas Eko", "KT 7788 EF", 3000), "Bandara APT Pranoto", 20)`. Objek seperti itu tidak dipegang siapa pun setelah method selesai.

## 2. Asosiasi: Atribut Berisi Objek Lain

File: [`contoh/contoh02_asosiasi.py`](contoh/contoh02_asosiasi.py)

Kelas `DosenWali` di file ini sederhana: punya `nama`, `ruangan`, dan method `pindah_ruangan()`. Yang menarik adalah kelas `Mahasiswa`, karena salah satu atributnya berisi **objek lain**.

```python
class Mahasiswa:
    """Mahasiswa yang mengenal dosen walinya."""

    def __init__(self, nama: str):
        self._nama = nama
        self._dosen_wali: DosenWali | None = None  # [1] awalnya belum ada

    def atur_dosen_wali(self, dosen: DosenWali):
        self._dosen_wali = dosen  # [2] menyimpan REFERENSI, bukan salinan

    def info_perwalian(self) -> str:
        if self._dosen_wali is None:  # [3] periksa dulu sebelum dipakai
            return f"{self._nama}: belum punya dosen wali"
        dosen = self._dosen_wali
        return f"{self._nama}: dosen wali {dosen.nama}, ruang {dosen.ruangan}"  # [4]
```

Program utamanya membuat objek `bu_rina` (ruang C-201) serta tiga mahasiswa: Ayu, Bima, dan Citra. Hanya Ayu dan Bima yang diberi dosen wali:

```python
    ayu.atur_dosen_wali(bu_rina)  # [5] dua mahasiswa mengenal objek yang SAMA
    bima.atur_dosen_wali(bu_rina)
```

Setelah info perwalian ketiganya dicetak, Bu Rina pindah ruangan:

```python
    bu_rina.pindah_ruangan("D-105")  # [6] diubah di satu tempat saja
    print(ayu.info_perwalian())
    print(bima.info_perwalian())
```

**Output:**

```text
=== SEBELUM PERWALIAN ===
Ayu: belum punya dosen wali

=== SETELAH PERWALIAN ===
Ayu: dosen wali Bu Rina, ruang C-201
Bima: dosen wali Bu Rina, ruang C-201
Citra: belum punya dosen wali

=== BU RINA PINDAH RUANGAN ===
Ayu: dosen wali Bu Rina, ruang D-105
Bima: dosen wali Bu Rina, ruang D-105
```

Penjelasan:

- **[1]** Atribut `_dosen_wali` awalnya `None`, artinya "belum menunjuk objek apa pun". Petunjuk tipe `DosenWali | None` menegaskan multiplisitas `0..1`: boleh ada satu dosen wali, boleh juga belum ada.
- **[2]** Yang disimpan adalah **referensi** ke objek dosen, bukan salinan datanya. Inilah ciri **asosiasi**: objek lain disimpan sebagai atribut, sehingga bisa dipakai kapan saja.
- **[3]** Sebelum memakai atribut yang boleh kosong, periksa dulu dengan `is None`. Tanpa pemeriksaan ini, membaca `.nama` milik `None` akan error untuk Citra.
- **[4]** Mahasiswa "berjalan" ke objek dosen untuk membaca nama dan ruangannya. Arahnya satu: mahasiswa tahu dosennya, tetapi dosen tidak menyimpan daftar mahasiswa.
- **[5]** Ayu dan Bima memegang referensi ke objek `bu_rina` yang **sama**.
- **[6]** Karena objeknya sama, pindah ruangan cukup dilakukan sekali. Ayu dan Bima langsung melihat ruangan yang baru, sedangkan atribut `_dosen_wali` milik Citra tetap `None`.

> [!TIP]
> **Coba sendiri:** di akhir `main()`, tambahkan `citra.atur_dosen_wali(DosenWali("Bu Rina", "D-105"))`, lalu `bu_rina.pindah_ruangan("E-301")`, lalu cetak `ayu.info_perwalian()` dan `citra.info_perwalian()`. Apakah ruangan dosen wali Citra ikut berubah?

<details>
<summary>Lihat jawaban</summary>

Tidak. Ayu melihat `ruang E-301`, tetapi Citra tetap `ruang D-105`. Citra dihubungkan ke objek `DosenWali` **baru** yang kebetulan bernama sama. Dua objek dengan data sama tetaplah dua objek berbeda.

</details>

## 3. Agregasi: List Berisi Objek dari Luar

File: [`contoh/contoh03_agregasi.py`](contoh/contoh03_agregasi.py)

Tim futsal mengumpulkan pemain-pemain yang **sudah ada**. Kelas `Pemain` hanya berisi `nama`, `posisi`, dan `__str__`.

```python
class Tim:
    """Tim futsal yang mengumpulkan pemain-pemain yang sudah ada."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_pemain: list[Pemain] = []  # [1] list kosong: 0 pemain

    def rekrut(self, pemain: Pemain):  # [2] menerima OBJEK yang sudah jadi
        self._daftar_pemain.append(pemain)
        print(f"{pemain.nama} bergabung dengan {self._nama}")

    def jumlah_pemain(self) -> int:
        return len(self._daftar_pemain)

    def tampilkan(self):
        print(f"{self._nama} ({self.jumlah_pemain()} pemain):")
        for nomor, pemain in enumerate(self._daftar_pemain, start=1):  # [3]
            print(f"  {nomor}. {pemain}")


def main():
    andi = Pemain("Andi", "kiper")  # [4] pemain lahir lebih dulu, tanpa tim
    bayu = Pemain("Bayu", "anchor")
    candra = Pemain("Candra", "pivot")
    tim_kelas = Tim("Tim Kelas TI-A")
    tim_fakultas = Tim("Tim Fakultas")

    print("=== MEMBENTUK TIM ===")
    tim_kelas.rekrut(andi)
    tim_kelas.rekrut(bayu)
    tim_kelas.rekrut(candra)
    tim_fakultas.rekrut(bayu)  # [5] satu pemain boleh ikut dua tim
```

Setelah kedua tim ditampilkan, tim kelas dibubarkan:

```python
    tim_kelas = None  # [6] objek tim dilepas, pemain tidak ikut hilang
    print(f"Pemain tetap ada: {andi}, {bayu}, {candra}")
    tim_fakultas.tampilkan()
```

**Output:**

```text
=== MEMBENTUK TIM ===
Andi bergabung dengan Tim Kelas TI-A
Bayu bergabung dengan Tim Kelas TI-A
Candra bergabung dengan Tim Kelas TI-A
Bayu bergabung dengan Tim Fakultas

Tim Kelas TI-A (3 pemain):
  1. Andi (kiper)
  2. Bayu (anchor)
  3. Candra (pivot)
Tim Fakultas (1 pemain):
  1. Bayu (anchor)

=== TIM KELAS DIBUBARKAN ===
Pemain tetap ada: Andi (kiper), Bayu (anchor), Candra (pivot)
Tim Fakultas (1 pemain):
  1. Bayu (anchor)
```

Penjelasan:

- **[1]** Tim baru dimulai dengan list kosong. Multiplisitasnya `*`: boleh nol, boleh banyak.
- **[2]** Method `rekrut()` menerima **objek** `Pemain` yang sudah jadi, lalu menyimpannya ke list. Inilah ciri **agregasi**: bagian dibuat di luar, lalu dikumpulkan.
- **[3]** `enumerate(..., start=1)` memberi nomor urut mulai dari 1 sambil membaca isi list. Setiap putaran menghasilkan pasangan nomor dan pemain.
- **[4]** Ketiga pemain sudah ada **sebelum** tim mana pun dibentuk.
- **[5]** Objek `bayu` yang sama tersimpan di dua list sekaligus. Hal ini wajar pada agregasi.
- **[6]** Variabel `tim_kelas` tidak lagi menunjuk objek tim, dan objek tim yang tidak dipegang siapa pun akan dibersihkan otomatis oleh Python. Para pemain tetap ada, karena mereka masih dipegang oleh variabel `andi`, `bayu`, `candra`, dan oleh list milik `tim_fakultas`.

## 4. Komposisi: Bagian Dibuat di Dalam

File: [`contoh/contoh04_komposisi.py`](contoh/contoh04_komposisi.py)

Kelas `Ruangan` menyimpan nama, panjang, dan lebar, serta punya method `luas()`. Perhatikan **siapa** yang membuat objek `Ruangan`.

```python
class Rumah:
    """Rumah yang membuat dan memiliki ruangan-ruangannya sendiri."""

    def __init__(self, pemilik: str):
        self._pemilik = pemilik
        self._daftar_ruangan: list[Ruangan] = []

    def bangun_ruangan(self, nama: str, panjang: int, lebar: int):  # [1]
        ruangan = Ruangan(nama, panjang, lebar)  # [2] dibuat DI DALAM rumah
        self._daftar_ruangan.append(ruangan)

    def luas_total(self) -> int:
        total = 0
        for ruangan in self._daftar_ruangan:
            total += ruangan.luas()  # [3] rumah bertanya ke setiap ruangan
        return total
```

Setelah method `tampilkan()`, program utamanya:

```python
def main():
    print("=== MEMBANGUN RUMAH ===")
    rumah = Rumah("Pak Hasan")
    rumah.bangun_ruangan("Ruang tamu", 4, 3)  # [4] hanya mengirim data
    rumah.bangun_ruangan("Kamar tidur", 3, 3)
    rumah.bangun_ruangan("Dapur", 3, 2)
    rumah.tampilkan()

    print()
    print("=== RUMAH DIROBOHKAN ===")
    rumah = None  # [5] satu-satunya pemegang ruangan dilepas
    print("Rumah dirobohkan. Tidak ada variabel lain yang memegang ruangannya,")
    print("jadi ruangan-ruangan itu ikut hilang bersama rumahnya.")
```

**Output:**

```text
=== MEMBANGUN RUMAH ===
Rumah Pak Hasan:
- Ruang tamu 4x3 m = 12 m2
- Kamar tidur 3x3 m = 9 m2
- Dapur 3x2 m = 6 m2
Luas total: 27 m2

=== RUMAH DIROBOHKAN ===
Rumah dirobohkan. Tidak ada variabel lain yang memegang ruangannya,
jadi ruangan-ruangan itu ikut hilang bersama rumahnya.
```

Penjelasan:

- **[1]** Method `bangun_ruangan()` menerima **data** (nama dan ukuran), bukan objek `Ruangan`.
- **[2]** Objek `Ruangan` dibuat **di dalam** method milik rumah, dan hanya rumah yang memegang referensinya. Inilah ciri **komposisi**.
- **[3]** Rumah menghitung luas totalnya dengan bertanya ke setiap ruangan.
- **[4]** Di `main()`, tidak ada satu baris pun yang menulis `Ruangan(...)`. Kode luar tidak pernah memegang objek ruangan.
- **[5]** Begitu rumah dilepas, ruangannya pun tidak dipegang siapa-siapa lagi, sehingga ikut dibersihkan bersama rumahnya.

Bandingkan dengan contoh 03: `tim.rekrut(pemain)` menerima **objek jadi** yang dibuat di luar (agregasi), sedangkan `rumah.bangun_ruangan(nama, panjang, lebar)` menerima **data** dan membuat objeknya sendiri (komposisi).

> [!TIP]
> **Coba sendiri:** mengapa kelas `Rumah` sengaja **tidak** punya method `tambah_ruangan(ruangan: Ruangan)`? Pikirkan apa yang bisa terjadi jika method itu ada.

<details>
<summary>Lihat jawaban</summary>

Jika ada method yang menerima objek `Ruangan` jadi, kode luar bisa membuat satu ruangan lalu memasukkannya ke **dua** rumah sekaligus. Satu dapur dimiliki dua rumah? Itu melanggar makna komposisi. Dengan hanya menerima data, rumah memastikan setiap ruangannya dibuat sendiri dan tidak dibagi.

</details>

## 5. Multiplisitas dan Pencarian yang Bisa Gagal

File: [`contoh/contoh05_multiplisitas.py`](contoh/contoh05_multiplisitas.py)

Sebuah grup belajar punya aturan: **tepat satu** ketua (multiplisitas `1`) dan **minimal satu** anggota (multiplisitas `1..*`). Kelas `Peserta` berisi `nim` dan `nama`. Kelas `GrupBelajar` yang menjaga aturannya:

```python
class GrupBelajar:
    """Grup belajar: tepat 1 ketua dan minimal 1 anggota."""

    def __init__(self, nama: str, ketua: Peserta):
        if ketua is None:  # [1] multiplisitas 1: ketua wajib ada
            raise ValueError("Grup wajib punya ketua")
        self._nama = nama
        self._ketua = ketua
        self._daftar_anggota: list[Peserta] = [ketua]  # [2] 1..*: sudah 1 anggota

    def tambah_anggota(self, peserta: Peserta):
        self._daftar_anggota.append(peserta)

    def cari_anggota(self, nim: str) -> Peserta | None:  # [3]
        for peserta in self._daftar_anggota:
            if peserta.nim == nim:
                return peserta
        return None  # [4] sudah diperiksa semua, tidak ketemu

    def keluarkan(self, nim: str):
        peserta = self.cari_anggota(nim)
        if peserta is None:  # [5] periksa None sebelum memakai hasilnya
            print(f"Gagal: NIM {nim} bukan anggota {self._nama}")
        elif peserta is self._ketua:  # [6] ketua tidak boleh keluar
            print(f"Gagal: {peserta.nama} adalah ketua, tidak bisa dikeluarkan")
        else:
            self._daftar_anggota.remove(peserta)
            print(f"{peserta.nama} keluar dari {self._nama}")
```

Program utamanya membuat grup dengan Ayu sebagai ketua, mencoba membuat grup tanpa ketua (`GrupBelajar("Grup Hantu", None)` di dalam `try`/`except`), menambah Bima dan Citra, mencari dua NIM, lalu mencoba mengeluarkan tiga orang.

**Output:**

```text
=== GRUP BARU ===
Grup PBO - ketua: Ayu
Anggota (1 orang):
- Ayu (2409106001)

=== GRUP TANPA KETUA ===
Gagal membuat grup: Grup wajib punya ketua

=== MENAMBAH ANGGOTA ===
Grup PBO - ketua: Ayu
Anggota (3 orang):
- Ayu (2409106001)
- Bima (2409106002)
- Citra (2409106003)

=== MENCARI ANGGOTA ===
Cari 2409106002: Bima (2409106002)
Cari 2409106099: tidak ditemukan

=== MENGELUARKAN ANGGOTA ===
Gagal: NIM 2409106099 bukan anggota Grup PBO
Gagal: Ayu adalah ketua, tidak bisa dikeluarkan
Citra keluar dari Grup PBO
Grup PBO - ketua: Ayu
Anggota (2 orang):
- Ayu (2409106001)
- Bima (2409106002)
```

Penjelasan:

- **[1]** Petunjuk tipe `ketua: Peserta` tidak mencegah siapa pun mengirim `None`. Karena itu, konstruktor memeriksanya sendiri dan menolak dengan `ValueError`, seperti validasi di Pertemuan 04.
- **[2]** List anggota langsung berisi ketua. Sejak lahir, grup sudah punya satu anggota, sehingga aturan `1..*` terpenuhi.
- **[3]** Petunjuk tipe `-> Peserta | None` memberi tahu pemanggil: "hasilnya bisa objek `Peserta`, bisa juga `None`".
- **[4]** `return None` baru dijalankan setelah perulangan selesai tanpa menemukan NIM yang dicari. Jika ketemu, `return peserta` di dalam perulangan langsung mengakhiri method.
- **[5]** Hasil pencarian **selalu** diperiksa dulu dengan `is None` sebelum dipakai. Programmer Python menulis `is None`, bukan `== None`, karena yang ditanyakan adalah "apakah ini objek `None` itu?".
- **[6]** Operator `is` memeriksa apakah dua variabel menunjuk objek yang **sama** (materi Pertemuan 03). Karena ketua tidak boleh keluar, list anggota tidak akan pernah kosong.

## 6. Mengembalikan Salinan List

File: [`contoh/contoh06_salinan_list.py`](contoh/contoh06_salinan_list.py)

Kelas `GarasiBocor` dan `GarasiAman` hampir identik. Konstruktor, method `parkir()` yang menolak motor saat garasi penuh, dan method `tampilkan()` keduanya sama persis. Bedanya hanya pada property `daftar_motor`.

Di kelas `GarasiBocor`:

```python
    @property
    def daftar_motor(self) -> list[Motor]:
        return self._daftar_motor  # [1] list ASLI diserahkan ke luar
```

Di kelas `GarasiAman`:

```python
    @property
    def daftar_motor(self) -> list[Motor]:
        return list(self._daftar_motor)  # [2] yang diserahkan hanya SALINAN
```

Di `main()`, setiap garasi berkapasitas 2 dicoba diisi tiga motor, dan motor ketiga ditolak. Lalu kode luar mencoba menyelinapkan motor ketiga lewat list yang didapat dari property. Untuk garasi bocor:

```python
    daftar = bocor.daftar_motor  # [3] kode luar memegang list ASLI
    daftar.append(Motor("KT 3333 CC"))  # [4] menyelinap, kapasitas dilewati
```

Untuk garasi aman, caranya sama persis:

```python
    daftar = aman.daftar_motor  # [5] kode luar hanya memegang salinan
    daftar.append(Motor("KT 3333 CC"))  # yang bertambah hanya salinannya
```

**Output:**

```text
=== GARASI BOCOR ===
KT 1111 AA masuk garasi
KT 2222 BB masuk garasi
Ditolak: garasi penuh, KT 3333 CC tidak bisa masuk
Isi garasi (3/2):
- KT 1111 AA
- KT 2222 BB
- KT 3333 CC

=== GARASI AMAN ===
KT 1111 AA masuk garasi
KT 2222 BB masuk garasi
Ditolak: garasi penuh, KT 3333 CC tidak bisa masuk
Isi garasi (2/2):
- KT 1111 AA
- KT 2222 BB
Isi salinan di luar: 3 motor
```

Penjelasan:

- **[1]** Property ini mengembalikan list yang **sama** dengan yang dipakai garasi di dalam.
- **[2]** `list(...)` membuat **list baru** yang isinya sama. Garasi menyerahkan "fotokopi", bukan aslinya.
- **[3]** Variabel `daftar` kini menunjuk list asli milik garasi bocor.
- **[4]** Menambah ke list itu berarti menambah ke garasi **tanpa lewat** `parkir()`. Hasilnya `3/2`: aturan kapasitas jebol.
- **[5]** Pada garasi aman, yang bertambah hanya salinannya (3 motor). Isi garasi tetap `2/2`.

> [!NOTE]
> Selain `list(x)`, salinan list juga bisa dibuat dengan `x.copy()` atau `x[:]`. Ketiganya hanya menyalin **list-nya**. Objek `Motor` di dalam salinan tetap objek yang sama dengan yang di dalam garasi.

## 7. Objek Saling Mengirim Pesan

File: [`contoh/contoh07_kirim_pesan.py`](contoh/contoh07_kirim_pesan.py)

Tiga objek bekerja sama saat Ayu menarik uang tunai. Kelas `Rekening` menyimpan saldo, dan method `tarik(jumlah)`-nya mengembalikan `True` jika berhasil atau `False` jika saldo tidak cukup. Dua kelas lainnya:

```python
class KartuAtm:
    """Kartu ATM yang MENGENAL rekeningnya (asosiasi)."""

    def __init__(self, pin: str, rekening: Rekening):
        self._pin = pin
        self._rekening = rekening  # [1] kartu menyimpan referensi rekening

    def otorisasi(self, pin: str, jumlah: int) -> bool:
        if pin != self._pin:
            print("  [KartuAtm] PIN salah")
            return False
        print("  [KartuAtm] PIN cocok, teruskan ke rekening")
        return self._rekening.tarik(jumlah)  # [2] pesan diteruskan ke Rekening
```

```python
    def tarik_tunai(self, kartu: KartuAtm, pin: str, jumlah: int):  # [3]
        print(f"[MesinAtm] permintaan tarik Rp{jumlah}")
        if jumlah > self._uang_tersedia:
            print("[MesinAtm] uang di mesin tidak cukup")
            return
        if kartu.otorisasi(pin, jumlah):  # [4] pesan dikirim ke KartuAtm
            self._uang_tersedia -= jumlah
            print(f"[MesinAtm] silakan ambil uang Rp{jumlah}")
        else:
            print("[MesinAtm] transaksi dibatalkan")
```

Program utamanya membuat rekening Ayu (saldo 500000), kartunya dengan PIN `123456`, dan mesin berisi uang 1000000, lalu mencoba tiga transaksi. Transaksi pertama:

```python
    mesin.tarik_tunai(kartu_ayu, "123456", 200000)  # [5]
```

**Output:**

```text
=== TRANSAKSI 1: BERHASIL ===
[MesinAtm] permintaan tarik Rp200000
  [KartuAtm] PIN cocok, teruskan ke rekening
    [Rekening] saldo Ayu kini Rp300000
[MesinAtm] silakan ambil uang Rp200000

=== TRANSAKSI 2: PIN SALAH ===
[MesinAtm] permintaan tarik Rp100000
  [KartuAtm] PIN salah
[MesinAtm] transaksi dibatalkan

=== TRANSAKSI 3: SALDO TIDAK CUKUP ===
[MesinAtm] permintaan tarik Rp400000
  [KartuAtm] PIN cocok, teruskan ke rekening
    [Rekening] saldo tidak cukup (sisa Rp300000)
[MesinAtm] transaksi dibatalkan

=== SETELAH TRANSAKSI ===
Saldo rekening Ayu: Rp300000
Uang di mesin     : Rp800000
```

Penjelasan:

- **[1]** Kartu menyimpan referensi rekeningnya sebagai atribut: **asosiasi** dari `KartuAtm` ke `Rekening`.
- **[2]** Kartu tidak mengubah saldo sendiri. Ia **meneruskan pesan** ke rekening, dan rekening yang memutuskan berhasil atau tidak.
- **[3]** Mesin hanya memakai kartu selama transaksi dan tidak menyimpannya: **dependensi** dari `MesinAtm` ke `KartuAtm`.
- **[4]** Mesin hanya peduli jawaban akhirnya (`True` atau `False`). Ia tidak perlu tahu bagaimana kartu dan rekening bekerja di dalamnya.
- **[5]** Satu pemanggilan dari `main()` memicu pesan berantai: mesin ke kartu, lalu kartu ke rekening. Jawabannya kembali dengan urutan terbalik. Indentasi pada output menunjukkan kedalaman rantai itu.

## 8. Program Multi-File dengan import

Folder: `contoh/contoh08_multi_file/`, berisi tiga file: [`ikan.py`](contoh/contoh08_multi_file/ikan.py), [`akuarium.py`](contoh/contoh08_multi_file/akuarium.py), dan [`main.py`](contoh/contoh08_multi_file/main.py).

Di Python, setiap file `.py` adalah sebuah **modul** (*module*). Kelas yang ditulis di satu modul bisa dipakai modul lain lewat perintah `import`. File `ikan.py` hanya berisi kelas `Ikan` (atribut `nama` dan `jenis`, serta `__str__`). File `akuarium.py` memakai kelas itu:

```python
from ikan import Ikan  # [1] ambil kelas Ikan dari file ikan.py
```

Di bawah baris itu ada kelas `Akuarium` yang menampung beberapa ikan (agregasi) dengan kapasitas tertentu. File `main.py` menjadi pintu masuk program:

```python
from akuarium import Akuarium  # [2] ambil kelas dari file akuarium.py
from ikan import Ikan


def main():
    print("=== AKUARIUM DI MEJA BELAJAR ===")
    akuarium = Akuarium(2)
    akuarium.masukkan(Ikan("Oren", "cupang"))  # [3] objek dari modul lain
    akuarium.masukkan(Ikan("Belang", "koi"))
    akuarium.masukkan(Ikan("Si Biru", "guppy"))
    akuarium.tampilkan()


if __name__ == "__main__":  # [4] main() hanya jalan jika file ini dijalankan langsung
    main()
```

Cara menjalankan: masuk ke folder contoh 08, lalu jalankan `main.py`.

```bash
cd Pertemuan-05-Relasi-Antar-Kelas/python/contoh/contoh08_multi_file
python main.py
```

**Output:**

```text
=== AKUARIUM DI MEJA BELAJAR ===
Oren masuk akuarium
Belang masuk akuarium
Gagal: akuarium penuh, Si Biru tidak muat
Isi akuarium (2/2):
- Oren (ikan cupang)
- Belang (ikan koi)
```

Penjelasan:

- **[1]** `from ikan import Ikan` dibaca: "dari modul `ikan` (file `ikan.py`), ambil kelas `Ikan`". Nama modul adalah nama file **tanpa** `.py`.
- **[2]** `main.py` mengambil kelas `Akuarium` dan `Ikan`. Setiap file wajib meng-`import` sendiri apa yang dipakainya.
- **[3]** Setelah di-import, kelas `Ikan` dipakai seperti biasa, seolah-olah ditulis di file yang sama.
- **[4]** Saat sebuah modul di-import, Python menjalankan isi file itu dari atas ke bawah. Karena itu, `ikan.py` dan `akuarium.py` hanya berisi definisi kelas. Bagian `if __name__ == "__main__":` memastikan `main()` hanya berjalan saat `main.py` dijalankan langsung, bukan saat di-import.

Ada dua gaya menulis `import`:

| Gaya | Cara memakai kelasnya | Kapan dipakai |
|---|---|---|
| `from ikan import Ikan` | `Ikan("Oren", "cupang")` | paling sering; nama kelas langsung bisa dipakai |
| `import ikan` | `ikan.Ikan("Oren", "cupang")` | jika ingin asal-usul kelas terlihat jelas |

**Di mana Python mencari modul?** Saat kamu menjalankan `python main.py`, Python mencari modul `akuarium` dan `ikan` di **folder tempat `main.py` berada**, lalu di folder pustaka bawaan Python. Karena itu, semua file program kita harus berada di folder yang sama.

> [!NOTE]
> Setelah program dijalankan, mungkin muncul folder baru bernama `__pycache__`. Isinya adalah versi terkompilasi dari modul-modul yang di-import, agar program berikutnya berjalan sedikit lebih cepat. Folder itu aman dihapus dan sudah diabaikan oleh Git.

> [!TIP]
> **Coba sendiri:** tambahkan baris `print("ikan.py sedang dibaca")` di baris paling atas `ikan.py` (di luar kelas), lalu jalankan `main.py`. Berapa kali pesan itu muncul, dan di mana posisinya? Padahal `ikan` di-import oleh **dua** file.

<details>
<summary>Lihat jawaban</summary>

Pesan itu muncul **satu kali**, di baris paling awal, sebelum `=== AKUARIUM DI MEJA BELAJAR ===`. Saat `main.py` meng-import `akuarium`, file `akuarium.py` meng-import `ikan`, sehingga `ikan.py` dijalankan. Saat `main.py` meng-import `ikan` lagi, Python memakai modul yang sudah dimuat. Setiap modul hanya dijalankan sekali dalam satu kali program berjalan. Jangan lupa hapus lagi baris percobaan itu.

</details>

## 9. Studi Kasus KedaiKita

Folder: `studi-kasus/`, berisi [`utilitas.py`](studi-kasus/utilitas.py), [`menu.py`](studi-kasus/menu.py), [`pelanggan.py`](studi-kasus/pelanggan.py), [`pesanan.py`](studi-kasus/pesanan.py), [`kedai.py`](studi-kasus/kedai.py), dan [`main.py`](studi-kasus/main.py).

Saatnya KedaiKita mencatat siapa memesan apa. Rancangan dan alasan pemilihan setiap relasi sudah dibahas di [halaman konsep](../README.md#12-studi-kasus-kedaikita-kedai-pesanan-dan-item).

**Apa yang berubah dibanding Pertemuan 04?**

| Bagian | Pertemuan 04 | Pertemuan 05 |
|---|---|---|
| Susunan file | satu file `kedaikita.py` | enam file, satu tugas per file |
| `format_rupiah()` | di `kedaikita.py` | dipindah ke `utilitas.py` |
| Kelas `Menu` dan `Pelanggan` | di `kedaikita.py` | di `menu.py` dan `pelanggan.py`, isinya hampir sama |
| Penghitung menu | `Menu._jumlah_menu` + `Menu.jumlah_menu()` | dihapus; diganti `kedai.jumlah_menu()` |
| Petunjuk tipe | belum ada | parameter dan nilai kembalian diberi petunjuk tipe |
| Pesanan | belum ada | kelas baru `ItemPesanan` dan `Pesanan` di `pesanan.py` |
| Daftar menu | variabel lepas di `main()` | disimpan dan dikelola objek `Kedai` di `kedai.py` |

Kelas `Menu` di `menu.py` sama dengan Pertemuan 04, ditambah petunjuk tipe dan tanpa penghitung `_jumlah_menu`. Karena `__str__`-nya memakai `format_rupiah()`, file itu diawali `from utilitas import format_rupiah`. Kelas `Pelanggan` di `pelanggan.py` juga sama, hanya pindah file.

**Kelas `ItemPesanan`** (di `pesanan.py`) mewakili satu baris pesanan:

```python
class ItemPesanan:
    """Satu baris pesanan: menu apa dan berapa porsi."""

    def __init__(self, menu: Menu, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self._menu = menu  # menyimpan REFERENSI ke objek Menu
        self._jumlah = jumlah
```

```python
    def hitung_subtotal(self) -> int:
        return self._menu.harga * self._jumlah

    def __str__(self) -> str:
        return f"{self._jumlah} x {self._menu.nama}"
```

- Item menyimpan **referensi** ke objek `Menu`: asosiasi dari `ItemPesanan` ke `Menu`. Di antara kedua potongan di atas ada property `menu` dan `jumlah`.
- `hitung_subtotal()` bertanya harga ke menunya **saat itu juga**, bukan menyimpan salinan harga.

**Kelas `Pesanan`** (juga di `pesanan.py`) memegang pelanggan pemiliknya dan daftar item:

```python
class Pesanan:
    """Satu pesanan milik seorang pelanggan, berisi beberapa ItemPesanan."""

    _nomor_terakhir = 0  # atribut kelas untuk membuat nomor otomatis

    def __init__(self, pelanggan: Pelanggan):
        Pesanan._nomor_terakhir += 1
        self._nomor = f"P{Pesanan._nomor_terakhir:03d}"  # P001, P002, ...
        self._pelanggan = pelanggan
        self._daftar_item: list[ItemPesanan] = []
```

Setelah property `nomor` dan `pelanggan`, ada tiga method penting:

```python
    @property
    def daftar_item(self) -> list[ItemPesanan]:
        """Mengembalikan SALINAN list, agar isi asli tidak diubah dari luar."""
        return list(self._daftar_item)

    def tambah_item(self, menu: Menu, jumlah: int):
        item = ItemPesanan(menu, jumlah)  # objek item dibuat OLEH pesanan
        menu.kurangi_stok(jumlah)  # gagal (ValueError) jika stok kurang
        self._daftar_item.append(item)

    def hitung_total(self) -> int:
        total = 0
        for item in self._daftar_item:
            total += item.hitung_subtotal()
        return total
```

- Atribut kelas `_nomor_terakhir` (materi Pertemuan 03) membuat nomor otomatis. `f"P{n:03d}"` menulis angka selebar 3 digit dengan nol di depan: `P001`, `P002`, dan seterusnya.
- `self._pelanggan` menyimpan referensi pelanggan: asosiasi dengan multiplisitas `1`, karena pelanggan wajib diberikan saat pesanan dibuat.
- `daftar_item` mengembalikan **salinan**, persis seperti garasi aman di contoh 06.
- `tambah_item()` menerima menu dan jumlah, lalu membuat objek `ItemPesanan` sendiri: **komposisi**. Urutannya penting: item dibuat dulu (jumlah divalidasi), lalu stok dikurangi, baru item dimasukkan ke list. Jika `kurangi_stok()` menolak, baris `append` tidak pernah dijalankan, sehingga item yang gagal tidak masuk ke pesanan.
- `hitung_total()` bertanya ke setiap item, dan setiap item bertanya ke menunya. Inilah pesan berantai: `Pesanan -> ItemPesanan -> Menu`.

Method `cetak_struk()` mencetak struk selebar 40 karakter (konstanta `LEBAR_STRUK`). Setiap baris item dicetak dengan `f"{str(item):<30}{subtotal:>10}"`: format `:<30` berarti "rata kiri, selebar 30 karakter", dan `:>10` berarti "rata kanan, selebar 10 karakter", sehingga kolom subtotal selalu lurus.

**Kelas `Kedai`** (di `kedai.py`) menyiapkan dua list kosong di konstruktornya, `_daftar_menu` dan `_daftar_pesanan`. Method-method utamanya:

```python
    def tambah_menu(self, menu: Menu):
        self._daftar_menu.append(menu)

    def cari_menu(self, kode: str) -> Menu | None:
        """Mengembalikan objek Menu dengan kode tertentu, atau None jika tidak ada."""
        for menu in self._daftar_menu:
            if menu.kode == kode:
                return menu
        return None

    def jumlah_menu(self) -> int:
        return len(self._daftar_menu)

    def buat_pesanan(self, pelanggan: Pelanggan) -> Pesanan:
        pesanan = Pesanan(pelanggan)
        self._daftar_pesanan.append(pesanan)
        return pesanan
```

- `tambah_menu(menu)` menerima objek menu yang dibuat di luar: **agregasi**.
- `cari_menu()` mengembalikan objek `Menu` atau `None`, sama polanya dengan `cari_anggota()` di contoh 05.
- `jumlah_menu()` menggantikan penghitung milik kelas `Menu` dari Pertemuan 04.
- `buat_pesanan()` membuat pesanan, mencatatnya, lalu **mengembalikannya** ke pemanggil agar bisa diisi. Parameter `pelanggan` hanya diteruskan ke pesanan, tidak disimpan oleh kedai: **dependensi**.
- Sisanya, `jumlah_pesanan()` dan `tampilkan_menu()`, bentuknya sederhana.

**Program utama** (`main.py`) diawali `from kedai import Kedai`, `from menu import Menu`, dan `from pelanggan import Pelanggan`. Berikut potongan pesanan Siti, termasuk item yang gagal:

```python
    # Pesanan kedua: Siti (salah satu item gagal karena stok kurang)
    pesanan_siti = kedai.buat_pesanan(siti)
    pesanan_siti.tambah_item(kedai.cari_menu("M02"), 2)
    pesanan_siti.tambah_item(kedai.cari_menu("M05"), 1)
    try:
        pesanan_siti.tambah_item(kedai.cari_menu("M04"), 20)
    except ValueError as e:
        print(f"Gagal menambah item: {e}")
    pesanan_siti.cetak_struk()
```

Hasil `kedai.cari_menu("M02")` di sini langsung dipakai tanpa diperiksa, karena kode `M01` sampai `M05` pasti ada. Untuk kode yang datang dari luar program, misalnya diketik pengguna, selalu periksa `None` dulu, seperti bagian `=== MENCARI MENU ===` di file yang sama.

Cara menjalankan (masuk dulu ke folder `studi-kasus`):

```bash
cd Pertemuan-05-Relasi-Antar-Kelas/python/studi-kasus
python main.py
```

Bagian awal output, yaitu daftar menu dan struk Budi, sama persis dengan yang tercantum di [halaman konsep](../README.md#12-studi-kasus-kedaikita-kedai-pesanan-dan-item). Lanjutannya:

**Output:**

```text
Gagal menambah item: Stok Mie Goreng Jawa tidak cukup (sisa 10)
========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P002
Pelanggan   : Siti Aminah
----------------------------------------
2 x Es Teh Manis                Rp16.000
1 x Pisang Goreng Keju          Rp15.000
----------------------------------------
TOTAL                           Rp31.000
========================================

=== MENCARI MENU ===
Cari M02: [M02] Es Teh Manis (Minuman) - Rp8.000 | stok 28
Cari M99: tidak ditemukan

=== SETELAH TRANSAKSI ===
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 18
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 28
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 14
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 11
Jumlah pesanan tercatat: 2
```

Stok di menu milik kedai ikut berkurang, karena objek `Menu` yang dikurangi stoknya oleh `tambah_item()` adalah objek yang **sama** dengan yang tersimpan di daftar menu kedai. `cari_menu()` mengembalikan referensinya, bukan salinannya.

> [!IMPORTANT]
> Jalankan `main.py`, bukan file lain. File seperti `menu.py` atau `pesanan.py` hanya berisi kelas, jadi jika dijalankan sendiri tidak menampilkan apa-apa.

> [!TIP]
> **Coba sendiri:** tepat setelah `pesanan_budi.cetak_struk()`, tambahkan tiga baris ini: `print(len(pesanan_budi.daftar_item))`, lalu `pesanan_budi.daftar_item.clear()`, lalu `print(len(pesanan_budi.daftar_item))`. Angka berapa saja yang tercetak, dan mengapa?

<details>
<summary>Lihat jawaban</summary>

Tercetak `2`, lalu `2` lagi. Setiap kali `pesanan_budi.daftar_item` dibaca, property itu membuat **salinan baru**. Perintah `clear()` hanya mengosongkan salinan yang langsung dibuang, sedangkan list asli di dalam pesanan tetap berisi dua item.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan Error

Pesan error Python dibaca **dari bawah ke atas**. Baris paling bawah menyebutkan jenis error dan penyebabnya, dan baris di atasnya menunjukkan lokasinya. Jalur folder yang panjang di pesan error berikut disingkat menjadi nama file atau `...`.

Untuk mencoba kesalahan 2 sampai 4, buat file `coba.py` di dalam folder `studi-kasus/`, isi dengan kode yang ditunjukkan, lalu jalankan `python coba.py`. Hapus lagi file itu setelah selesai.

### Kesalahan 1: Menjalankan dari folder yang salah

Misalkan terminalmu masih berada di folder `python/`, bukan di `python/studi-kasus/`, lalu kamu mengetik `python main.py`:

```text
python: can't open file '.../python/main.py': [Errno 2] No such file or directory
```

**Artinya:** di folder aktif tidak ada file `main.py`. **Perbaikan:** masuk dulu ke foldernya dengan `cd studi-kasus`, lalu jalankan lagi.

Kesalahan lain muncul jika kamu membuat file baru **di luar** folder `studi-kasus`, misalnya `python/coba.py`, lalu menulis `from menu import Menu` di dalamnya:

```text
Traceback (most recent call last):
  File "coba.py", line 1, in <module>
    from menu import Menu
ModuleNotFoundError: No module named 'menu'
```

**Artinya:** Python mencari modul di folder tempat file yang dijalankan berada, yaitu folder `python/`, dan file `menu.py` tidak ada di sana. **Perbaikan:** letakkan file barumu di folder yang sama dengan modul yang ingin di-import.

> [!NOTE]
> Perintah `python studi-kasus/main.py` yang diketik dari folder `python/` justru **berhasil**, karena Python mencari modul di folder milik `main.py`, bukan di folder aktif terminal. Meski begitu, biasakan masuk ke folder `studi-kasus` dulu: cara ini selalu berhasil, sama dengan cara menjalankan program Java, dan nanti dibutuhkan di Pertemuan 15 saat program membaca file data.

### Kesalahan 2: Salah menulis nama modul atau nama kelas

```python
from Menu import Menu
```

```text
Traceback (most recent call last):
  File "coba.py", line 1, in <module>
    from Menu import Menu
ModuleNotFoundError: No module named 'Menu'
```

**Artinya:** tidak ada file bernama `Menu.py`. Nama modul adalah nama **file**, yaitu `menu.py` dengan huruf kecil. Aturan huruf besar-kecil ini berlaku juga di Windows. Kebalikannya, salah menulis nama **kelas**, juga sering terjadi:

```python
from menu import menu
```

```text
Traceback (most recent call last):
  File "coba.py", line 1, in <module>
    from menu import menu
ImportError: cannot import name 'menu' from 'menu' (.../studi-kasus/menu.py). Did you mean: 'Menu'?
```

**Artinya:** modul `menu` ditemukan, tetapi di dalamnya tidak ada sesuatu bernama `menu` (huruf kecil). **Perbaikan:** ingat polanya, `from nama_file import NamaKelas`, sehingga yang benar adalah `from menu import Menu`.

### Kesalahan 3: Memakai `import modul`, tetapi menulis nama kelas langsung

Jika file diawali `import menu`, lalu kamu menulis `kopi = Menu("M01", ...)`, Python berhenti dengan `NameError: name 'Menu' is not defined. Did you mean: 'menu'?`. **Artinya:** `import menu` hanya memperkenalkan nama **modul** `menu`, bukan nama kelas `Menu`. **Perbaikan:** tulis `menu.Menu(...)`, atau ganti import-nya menjadi `from menu import Menu`.

### Kesalahan 4: Memakai hasil pencarian tanpa memeriksa `None`

```python
from main import siapkan_kedai
from pelanggan import Pelanggan

kedai = siapkan_kedai()
pesanan = kedai.buat_pesanan(Pelanggan("Budi Santoso", "081234567890"))
pesanan.tambah_item(kedai.cari_menu("M10"), 1)
```

```text
Traceback (most recent call last):
  File "coba.py", line 6, in <module>
    pesanan.tambah_item(kedai.cari_menu("M10"), 1)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "pesanan.py", line 69, in tambah_item
    menu.kurangi_stok(jumlah)  # gagal (ValueError) jika stok kurang
    ^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'kurangi_stok'
```

**Artinya:** baca dari bawah. Ada sesuatu bertipe `NoneType` (yaitu `None`) yang disuruh `kurangi_stok`. Lokasinya di `pesanan.py` baris 69, yang dipanggil dari baris 6 file kita. Menu `M10` tidak ada, sehingga `cari_menu()` mengembalikan `None`, dan `None` itu dikirim ke `tambah_item()`. **Perbaikan:** simpan dulu hasil pencarian ke variabel, periksa dengan `if menu is None:`, lalu panggil `tambah_item()` hanya jika menunya ada.

Baris `from main import siapkan_kedai` meminjam fungsi dari `main.py` tanpa menjalankan program utamanya, berkat `if __name__ == "__main__":`.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi Python. Tanda `^^^^` dan `~~~~` di bawah baris kode baru muncul sejak Python 3.11, dan saran *Did you mean* pada `ImportError` baru ada di versi yang lebih baru lagi. Fokuslah pada **jenis error** (`ModuleNotFoundError`, `ImportError`, `NameError`, `AttributeError`) dan kata-kata kunci di dalamnya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| Petunjuk tipe | `def nama(self, x: Tipe) -> Tipe:` | `def antar(self, tujuan: str, jarak_km: int) -> int:` |
| Dependensi | objek sebagai parameter, tidak disimpan | `def pesan_ojek(self, ojek: Ojek, ...):` |
| Asosiasi | atribut berisi objek lain | `self._dosen_wali = dosen` |
| Atribut boleh kosong (`0..1`) | awalnya `None` | `self._dosen_wali: DosenWali \| None = None` |
| Agregasi | list berisi objek dari luar | `self._daftar_pemain.append(pemain)` |
| Komposisi | objek bagian dibuat di dalam | `ruangan = Ruangan(nama, panjang, lebar)` |
| Pencarian yang bisa gagal | `-> Tipe \| None` dan `return None` | `def cari_menu(self, kode: str) -> Menu \| None:` |
| Memeriksa hasil kosong | `is None` / `is not None` | `if menu is None:` |
| Objek yang sama? | `a is b` | `peserta is self._ketua` |
| Salinan list | `list(x)`, `x.copy()`, `x[:]` | `return list(self._daftar_item)` |
| Nomor urut dalam perulangan | `enumerate(daftar, start=1)` | `for nomor, pemain in enumerate(...)` |
| Import kelas dari file lain | `from nama_file import NamaKelas` | `from menu import Menu` |
| Import modul | `import nama_file` | `import menu` lalu `menu.Menu(...)` |
| Menjalankan program multi-file | masuk ke foldernya, lalu jalankan `main.py` | `cd studi-kasus` lalu `python main.py` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
