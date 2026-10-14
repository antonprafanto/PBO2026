# 🐍 Praktik Python — Pertemuan 11: Exception Handling

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 11](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Exception Pertama: Pembagian dengan Nol](#1-exception-pertama-pembagian-dengan-nol)
2. [Mengubah Teks Menjadi Angka](#2-mengubah-teks-menjadi-angka)
3. [Indeks di Luar Batas dan Exception yang Merambat](#3-indeks-di-luar-batas-dan-exception-yang-merambat)
4. [Banyak `except` dan Urutannya](#4-banyak-except-dan-urutannya)
5. [`else` dan `finally`](#5-else-dan-finally)
6. [`raise`: Melempar dan Melempar Ulang](#6-raise-melempar-dan-melempar-ulang)
7. [Exception Buatan Sendiri dan Chaining](#7-exception-buatan-sendiri-dan-chaining)
8. [Hierarki Exception Python](#8-hierarki-exception-python)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan Error](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/          <- 7 contoh, dari pembagian dengan nol sampai exception buatan sendiri
├── studi-kasus/     <- KedaiKita versi Pertemuan 11 (9 file, baru: pengecualian.py)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Cara menjalankan sebuah contoh dari terminal:

```bash
cd Pertemuan-11-Exception-Handling/python/contoh
python contoh01_pembagian_nol.py
```

Studi kasus terdiri atas beberapa file, jadi jalankan `main.py` **dari dalam** folder `studi-kasus`:

```bash
cd Pertemuan-11-Exception-Handling/python/studi-kasus
python main.py
```

> [!NOTE]
> Di macOS/Linux, gunakan `python3` sebagai ganti `python`. Di VS Code, kamu juga bisa membuka file lalu menekan tombol ▶ (*Run Python File*). Panduan instalasi ada di [00-Persiapan](../../00-Persiapan/README.md).

> [!NOTE]
> Halaman ini banyak menampilkan **pesan error asli** dari potongan kode yang sengaja dibuat salah. Jalur folder sudah dipendekkan menjadi nama file. Bunyinya bisa sedikit berbeda antarversi Python: misalnya, Python 3.11 ke atas menambahkan garis penanda seperti `~~~~^^`, sedangkan Python 3.10 tidak. Fokuslah pada **jenis** exception, **pesannya**, dan **nomor barisnya**.

## 1. Exception Pertama: Pembagian dengan Nol

File: [`contoh/contoh01_pembagian_nol.py`](contoh/contoh01_pembagian_nol.py)

### Tanpa penanganan: program berhenti mendadak

Kita mulai dari program yang **belum** menangani exception. Simpan sebagai `patungan.py`, lalu jalankan:

```python
def hitung_patungan(total: int, jumlah_orang: int) -> int:
    return total // jumlah_orang


def main():
    print("Menghitung patungan...")
    hasil = hitung_patungan(120000, 0)
    print(f"Hasil: Rp{hasil}")


main()
```

Hasilnya:

```text
Menghitung patungan...
Traceback (most recent call last):
  File "patungan.py", line 11, in <module>
    main()
    ~~~~^^
  File "patungan.py", line 7, in main
    hasil = hitung_patungan(120000, 0)
  File "patungan.py", line 2, in hitung_patungan
    return total // jumlah_orang
           ~~~~~~^^~~~~~~~~~~~~~
ZeroDivisionError: integer division or modulo by zero
```

Baca *traceback* **dari bawah ke atas** (*most recent call last*):

- Baris terakhir menyebut **jenis** exception (`ZeroDivisionError`) dan **pesannya**.
- Blok `File ...` tepat di atasnya adalah **tempat exception lahir**: baris 2, di dalam `hitung_patungan`. Blok-blok di atasnya menunjukkan siapa memanggil siapa, sampai ke titik awal program (baris 11).
- `Hasil: Rp...` tidak pernah tercetak. Begitu exception dilempar, sisa program tidak dijalankan.

### Dengan `try`/`except`: program tetap berjalan

```python
def hitung_patungan(total: int, jumlah_orang: int) -> int:
    """Membagi tagihan sama rata ke semua orang (dibulatkan ke bawah)."""
    return total // jumlah_orang  # [1] gagal jika jumlah_orang = 0


def main():
    print("=== PATUNGAN MAKAN DI WARUNG ===")
    per_orang = hitung_patungan(120000, 4)
    print(f"Rp120000 dibagi 4 orang: Rp{per_orang} per orang")

    print()
    print("=== JIKA JUMLAH ORANG NOL ===")
    try:  # [2] "coba jalankan blok ini"
        print("Menghitung patungan untuk 0 orang...")
        hasil = hitung_patungan(120000, 0)  # [3] exception dilempar di sini
        print(f"Hasil: Rp{hasil} per orang")  # [4] baris ini DILEWATI
    except ZeroDivisionError:  # [5] exception ditangkap di sini
        print("Gagal: jumlah orang tidak boleh nol")
    print("Program tetap berjalan sampai baris terakhir")  # [6]
```

**Output:**

```text
=== PATUNGAN MAKAN DI WARUNG ===
Rp120000 dibagi 4 orang: Rp30000 per orang

=== JIKA JUMLAH ORANG NOL ===
Menghitung patungan untuk 0 orang...
Gagal: jumlah orang tidak boleh nol
Program tetap berjalan sampai baris terakhir
```

Penjelasan:

- **[1]** Operator `//` (pembagian bilangan bulat) melempar `ZeroDivisionError` jika pembaginya 0. Fungsi ini tidak menangkapnya, jadi exception merambat ke pemanggil.
- **[2]** `try:` diikuti blok berindentasi berisi kode yang **mungkin** gagal.
- **[3]** Di sinilah exception dilempar. Python langsung berhenti menjalankan blok `try`.
- **[4]** Baris ini **dilewati**, karena ada di blok `try` setelah baris yang gagal.
- **[5]** `except ZeroDivisionError:` hanya menangkap exception berjenis `ZeroDivisionError` (atau turunannya). Isinya dijalankan sebagai pengganti.
- **[6]** Setelah blok `except` selesai, program melanjutkan ke baris **setelah** struktur `try`, bukan kembali ke baris yang gagal.

> [!TIP]
> **Coba sendiri:** ganti `except ZeroDivisionError:` menjadi `except ValueError:`, lalu jalankan. Tebak dulu: apakah exception-nya masih tertangkap?

<details>
<summary>Lihat jawaban</summary>

Tidak. `ValueError` bukan jenis yang cocok, jadi exception lolos. Program berhenti dengan *traceback* yang berakhir `ZeroDivisionError: integer division or modulo by zero`, dan baris "Program tetap berjalan..." tidak pernah tercetak. Penangkap hanya bekerja untuk jenis yang **cocok**. Kembalikan menjadi `ZeroDivisionError`.

</details>

## 2. Mengubah Teks Menjadi Angka

File: [`contoh/contoh02_konversi_teks.py`](contoh/contoh02_konversi_teks.py)

Data dari formulir, file, atau jaringan selalu datang sebagai **teks**. Saat teks diubah dengan `int()`, teks yang bukan bilangan bulat membuat Python melempar `ValueError`.

```python
def main():
    # [1] isian jumlah porsi dari formulir pesanan online (semuanya teks)
    isian_formulir = ["3", "dua", "5", "2.5", "", "4"]
    total = 0
    jumlah_salah = 0

    print("=== REKAP JUMLAH PORSI ===")
    for teks in isian_formulir:
        try:
            porsi = int(teks)  # [2] bisa melempar ValueError
            total += porsi  # [3] hanya dijalankan jika int() berhasil
            print(f"'{teks}' -> {porsi} porsi")
        except ValueError:  # [4] isian ini dilewati, perulangan lanjut
            jumlah_salah += 1
            print(f"'{teks}' -> bukan bilangan bulat, dilewati")

    print()
    print(f"Total porsi     : {total}")
    print(f"Isian yang salah: {jumlah_salah}")
```

**Output:**

```text
=== REKAP JUMLAH PORSI ===
'3' -> 3 porsi
'dua' -> bukan bilangan bulat, dilewati
'5' -> 5 porsi
'2.5' -> bukan bilangan bulat, dilewati
'' -> bukan bilangan bulat, dilewati
'4' -> 4 porsi

Total porsi     : 12
Isian yang salah: 3
```

Penjelasan:

- **[1]** Data ditulis langsung di program (bukan dari `input()`), supaya hasilnya selalu sama. Bayangkan ini isian dari formulir pesanan online.
- **[2]** `int("dua")`, `int("2.5")`, dan `int("")` sama-sama melempar `ValueError`.
- **[3]** Penjumlahan ada **setelah** `int()` di dalam blok `try`. Jika `int()` gagal, baris ini ikut dilewati, sehingga total tidak pernah tercemar data yang salah.
- **[4]** Karena `try` berada **di dalam** perulangan, satu isian yang salah tidak menghentikan perulangan. Isian berikutnya tetap diproses.

> [!TIP]
> **Coba sendiri:** exception adalah objek, dan `except ValueError as e:` menyimpannya ke variabel `e`. Ubah baris `except` menjadi bentuk itu, lalu tambahkan `print(f"  pesan asli: {e}")` di dalam bloknya. Pesan apa yang muncul untuk `'dua'`, `'2.5'`, dan `''`?

<details>
<summary>Lihat jawaban</summary>

```text
  pesan asli: invalid literal for int() with base 10: 'dua'
  pesan asli: invalid literal for int() with base 10: '2.5'
  pesan asli: invalid literal for int() with base 10: ''
```

Pesan bawaan ini berguna untuk programmer, tetapi kurang ramah untuk pengguna. Karena itu, program kita menulis pesannya sendiri: `bukan bilangan bulat, dilewati`.

</details>

> [!NOTE]
> `int(" 7 ")` di Python **berhasil** menghasilkan 7, karena spasi di tepi teks diabaikan. Di Java, `Integer.parseInt(" 7 ")` justru gagal. Perbedaan kecil seperti ini dibahas di [Jembatan Python ↔ Java](../jembatan-python-java.md).

## 3. Indeks di Luar Batas dan Exception yang Merambat

File: [`contoh/contoh03_indeks_dan_merambat.py`](contoh/contoh03_indeks_dan_merambat.py)

Meminta elemen list di posisi yang tidak ada membuat Python melempar `IndexError`. Contoh ini juga memperlihatkan **perjalanan** exception melewati beberapa fungsi.

```python
def ambil_kelompok(jadwal: list[str], giliran: int) -> str:
    """Mengembalikan nama kelompok pada giliran tertentu (mulai dari 1)."""
    print(f"    [ambil kelompok] mencari giliran {giliran}")
    return jadwal[giliran - 1]  # [1] IndexError jika giliran terlalu besar


def umumkan(jadwal: list[str], giliran: int):
    print(f"  [umumkan] giliran {giliran}")
    kelompok = ambil_kelompok(jadwal, giliran)  # [2] tidak ada try di sini
    print(f"  Giliran {giliran}: {kelompok}")  # [3] dilewati jika ada error


def main():
    jadwal = ["Kelompok Pesut", "Kelompok Enggang", "Kelompok Bekantan"]
    print("=== JADWAL PRESENTASI ===")
    for giliran in [1, 3, 5]:
        try:
            umumkan(jadwal, giliran)  # [4]
        except IndexError:  # [5] exception merambat sampai ke sini
            print(f"  -> Giliran {giliran} tidak ada. "
                  f"Hanya ada {len(jadwal)} kelompok.")
```

**Output:**

```text
=== JADWAL PRESENTASI ===
  [umumkan] giliran 1
    [ambil kelompok] mencari giliran 1
  Giliran 1: Kelompok Pesut
  [umumkan] giliran 3
    [ambil kelompok] mencari giliran 3
  Giliran 3: Kelompok Bekantan
  [umumkan] giliran 5
    [ambil kelompok] mencari giliran 5
  -> Giliran 5 tidak ada. Hanya ada 3 kelompok.
```

Penjelasan:

- **[1]** Giliran 5 berarti indeks 4, padahal list hanya punya indeks 0 sampai 2. Python melempar `IndexError: list index out of range`.
- **[2]** `umumkan()` tidak punya `try`, jadi exception dari `ambil_kelompok()` **merambat** melewatinya.
- **[3]** Akibatnya baris ini tidak pernah dijalankan untuk giliran 5. Bandingkan dengan giliran 1 dan 3 di output.
- **[4]** dan **[5]** Exception baru tertangkap di `main()`. Inilah tempat yang tepat, karena `main()` tahu harus berkata apa kepada pengguna.

> [!WARNING]
> Python mengizinkan **indeks negatif**: `jadwal[-1]` berarti elemen terakhir. Jika `umumkan(jadwal, 0)` dipanggil, indeksnya menjadi -1 dan **tidak ada error**. Program dengan tenang mencetak `Giliran 0: Kelompok Bekantan`, padahal giliran 0 tidak ada. Untuk kasus seperti ini, jangan menunggu exception bawaan. Periksa sendiri lebih awal, misalnya `if giliran < 1: raise ValueError(...)`. Caranya dibahas di bagian 6.

## 4. Banyak `except` dan Urutannya

File: [`contoh/contoh04_banyak_except.py`](contoh/contoh04_banyak_except.py)

Setiap baris data berformat `nama;total_nilai;jumlah_tugas`. Satu baris bisa gagal dengan beberapa cara, dan setiap cara ditangani berbeda.

```python
def hitung_rata_rata(baris: str) -> int:
    """Menghitung rata-rata nilai tugas dari satu baris data."""
    bagian = baris.split(";")
    total = int(bagian[1])  # [1] IndexError atau ValueError
    jumlah_tugas = int(bagian[2])
    return total // jumlah_tugas  # [2] ZeroDivisionError jika belum ada tugas


def main():
    data = [
        "Ayu;255;3",
        "Bima;sembilan puluh;1",  # nilai bukan angka
        "Citra;160",  # kolom jumlah_tugas tidak ada
        "Dimas;0;0",  # belum ada tugas yang dinilai
        None,  # data kosong dari sistem lama
        "Eka;176;2",
    ]
    print("=== RATA-RATA NILAI TUGAS ===")
    for nomor, baris in enumerate(data, start=1):
        try:
            rata = hitung_rata_rata(baris)
            nama = baris.split(";")[0]
            print(f"Baris {nomor} ({nama}): rata-rata {rata}")
        except (ValueError, IndexError):  # [3] dua jenis, satu penanganan
            print(f"Baris {nomor}: format salah, dilewati")
        except ZeroDivisionError:  # [4]
            print(f"Baris {nomor}: belum ada tugas yang dinilai")
        except Exception:  # [5] jaring pengaman: PALING UMUM, PALING BAWAH
            print(f"Baris {nomor}: data tidak terbaca, dilewati")
```

**Output:**

```text
=== RATA-RATA NILAI TUGAS ===
Baris 1 (Ayu): rata-rata 85
Baris 2: format salah, dilewati
Baris 3: format salah, dilewati
Baris 4: belum ada tugas yang dinilai
Baris 5: data tidak terbaca, dilewati
Baris 6 (Eka): rata-rata 88
```

Penjelasan:

- **[1]** `"Citra;160".split(";")` hanya menghasilkan dua bagian, jadi `bagian[2]` melempar `IndexError`. `int("sembilan puluh")` melempar `ValueError`.
- **[2]** Dimas belum punya tugas yang dinilai, jadi `0 // 0` melempar `ZeroDivisionError`.
- **[3]** Tuple `(ValueError, IndexError)` berarti "tangkap salah satu dari keduanya". Cocok jika penanganannya sama.
- **[4]** Penangkap khusus untuk pembagian dengan nol, dengan pesan yang berbeda.
- **[5]** `Exception` menangkap hampir semua exception lain. Di sini ia menangkap baris 5: `None.split(";")` melempar `AttributeError`, jenis yang tidak kita duga. Karena paling umum, ia **wajib** ditulis paling bawah.

### Jika urutannya salah

Apa jadinya jika penangkap umum ditulis lebih dulu?

```python
try:
    hasil = 120000 // 0
except Exception:
    print("Terjadi kesalahan umum")
except ZeroDivisionError:
    print("Gagal: jumlah orang tidak boleh nol")
```

Hasilnya:

```text
Terjadi kesalahan umum
```

Tidak ada error, tetapi pesan khusus kita **tidak pernah** muncul. `ZeroDivisionError` adalah turunan `Exception`, jadi penangkap pertama sudah cocok, dan penangkap di bawahnya dilewati. Python tidak memperingatkan apa pun, jadi kamu yang harus teliti. (Java menolak mengompilasi kode seperti ini.)

## 5. `else` dan `finally`

File: [`contoh/contoh05_else_dan_finally.py`](contoh/contoh05_else_dan_finally.py)

Proyektor di ruang kelas harus **selalu** dimatikan setelah presentasi, apa pun yang terjadi. Method `tampilkan()` milik kelas `Proyektor` bisa gagal dengan dua cara:

```python
    def tampilkan(self, nama_file: str):
        if self._lampu_putus:
            raise RuntimeError("lampu proyektor putus")
        if not nama_file.endswith(".pdf"):
            raise ValueError(f"file {nama_file} bukan PDF")
        print(f"  Menampilkan {nama_file}")
```

Fungsi `presentasi()` memakai bentuk `try` yang lengkap:

```python
def presentasi(proyektor: Proyektor, nama_file: str):
    proyektor.nyalakan()
    try:
        proyektor.tampilkan(nama_file)  # [1] bisa gagal
    except ValueError as e:  # [2] hanya menangani ValueError
        print(f"  Gagal presentasi: {e}")
    else:  # [3] hanya jika blok try berhasil tanpa error
        print("  Presentasi lancar, terima kasih!")
    finally:  # [4] SELALU dijalankan
        proyektor.matikan()


def main():
    proyektor = Proyektor("R301")

    print("=== PRESENTASI 1: LANCAR ===")
    presentasi(proyektor, "laporan-akhir.pdf")

    print()
    print("=== PRESENTASI 2: FILE SALAH ===")
    presentasi(proyektor, "laporan-akhir.docx")

    print()
    print("=== PRESENTASI 3: LAMPU PUTUS ===")
    proyektor.rusakkan_lampu()
    try:
        presentasi(proyektor, "laporan-akhir.pdf")  # [5]
    except RuntimeError as e:  # [6] ditangkap oleh pemanggil
        print(f"Ditangani di main: {e}")
```

**Output:**

```text
=== PRESENTASI 1: LANCAR ===
  Proyektor R301 menyala
  Menampilkan laporan-akhir.pdf
  Presentasi lancar, terima kasih!
  Proyektor R301 dimatikan

=== PRESENTASI 2: FILE SALAH ===
  Proyektor R301 menyala
  Gagal presentasi: file laporan-akhir.docx bukan PDF
  Proyektor R301 dimatikan

=== PRESENTASI 3: LAMPU PUTUS ===
  Proyektor R301 menyala
  Proyektor R301 dimatikan
Ditangani di main: lampu proyektor putus
```

Penjelasan:

- **[1]** Hanya baris yang **mungkin gagal** yang ditaruh di blok `try`. Blok `try` yang pendek membuat jelas exception datang dari mana.
- **[2]** `except ValueError as e:` menangani file yang bukan PDF. Pesan dari `raise` dibaca lewat `e`.
- **[3]** `else` hanya berjalan jika blok `try` selesai **tanpa** exception (presentasi 1). Kode di `else` tidak ikut "dijaga" oleh `except`, sehingga error lain di sana tidak tertangkap secara tidak sengaja.
- **[4]** `finally` berjalan di **ketiga** presentasi. Proyektor tidak pernah lupa dimatikan.
- **[5]** dan **[6]** Pada presentasi 3, `RuntimeError` tidak cocok dengan `except ValueError`. Exception merambat ke `main()`, tetapi **sebelum** itu `finally` tetap mematikan proyektor. Perhatikan urutan di output: "dimatikan" muncul sebelum "Ditangani di main".

> [!NOTE]
> **Pratinjau Pertemuan 15:** untuk file, Python punya pernyataan `with`, misalnya `with open("data/menu_awal.csv", encoding="utf-8") as berkas:`. Setelah blok `with` selesai, file **pasti** tertutup walaupun terjadi exception di dalamnya, seperti `finally` yang ditulis untukmu.

## 6. `raise`: Melempar dan Melempar Ulang

File: [`contoh/contoh06_raise_dan_lempar_ulang.py`](contoh/contoh06_raise_dan_lempar_ulang.py)

Di Pertemuan 04 kita sudah memakai `raise ValueError(...)` untuk menolak data. Contoh ini mengulangnya, lalu menambah satu pola baru: **melempar ulang**. Kelas `AC` menyimpan suhu (awalnya 25) dan konstanta batas `SUHU_MIN = 16` serta `SUHU_MAKS = 30`. Method pengaturnya:

```python
    def atur_suhu(self, suhu: int):
        if suhu < AC.SUHU_MIN or suhu > AC.SUHU_MAKS:  # [1] periksa lebih dulu
            raise ValueError(f"Suhu {suhu} di luar batas "
                             f"{AC.SUHU_MIN}-{AC.SUHU_MAKS} derajat")  # [2]
        self._suhu = suhu  # [3] hanya dijalankan jika lolos pemeriksaan
```

Fungsi perantara dan program utamanya:

```python
def tekan_remote(ac: AC, suhu: int):
    """Meneruskan perintah ke AC. Penolakan dicatat, lalu dilempar ulang."""
    try:
        ac.atur_suhu(suhu)
    except ValueError:
        print(f"  [log] perintah {suhu} derajat ditolak")  # [4] catat dulu...
        raise  # [5] ...lalu lempar ulang exception yang SAMA ke pemanggil


def main():
    ac = AC("Lab Komputer 2")
    print(f"=== REMOTE AC (suhu awal {ac.suhu} derajat) ===")
    for suhu in [22, 10, 35, 18]:
        try:
            tekan_remote(ac, suhu)
            print(f"Suhu diatur ke {suhu} derajat")
        except ValueError as e:  # [6] pesan dari raise ikut terbawa
            print(f"Layar remote: {e}")
    print(f"Suhu akhir: {ac.suhu} derajat")
```

**Output:**

```text
=== REMOTE AC (suhu awal 25 derajat) ===
Suhu diatur ke 22 derajat
  [log] perintah 10 derajat ditolak
Layar remote: Suhu 10 di luar batas 16-30 derajat
  [log] perintah 35 derajat ditolak
Layar remote: Suhu 35 di luar batas 16-30 derajat
Suhu diatur ke 18 derajat
Suhu akhir: 18 derajat
```

Penjelasan:

- **[1]**, **[2]**, dan **[3]** Validasi lebih awal: data diperiksa **sebelum** atribut diubah. `raise` membuat objek `ValueError` berisi pesan, lalu melemparnya, sehingga method langsung berhenti dan suhu lama tetap utuh.
- **[4]** `tekan_remote()` ingin mencatat setiap penolakan, tetapi tidak tahu harus menampilkan apa ke pengguna.
- **[5]** `raise` **tanpa apa pun** di dalam `except` melempar ulang exception yang sedang ditangani, lengkap dengan pesan dan jejak aslinya.
- **[6]** `main()` menerima exception yang sama, lalu menampilkan pesannya. Perhatikan urutan di output: log dulu, baru "Layar remote".

> [!TIP]
> **Coba sendiri:** ganti baris `raise` di `tekan_remote()` dengan `pass`, lalu jalankan. Apa yang salah dari output-nya?

<details>
<summary>Lihat jawaban</summary>

```text
=== REMOTE AC (suhu awal 25 derajat) ===
Suhu diatur ke 22 derajat
  [log] perintah 10 derajat ditolak
Suhu diatur ke 10 derajat
  [log] perintah 35 derajat ditolak
Suhu diatur ke 35 derajat
Suhu diatur ke 18 derajat
Suhu akhir: 18 derajat
```

Program **berbohong**: tertulis "Suhu diatur ke 10 derajat", padahal AC menolaknya. Exception sudah "ditelan" oleh `tekan_remote()`, jadi `main()` mengira semuanya berhasil. Inilah bahayanya menangkap exception tanpa meneruskannya.

</details>

## 7. Exception Buatan Sendiri dan Chaining

File: [`contoh/contoh07_exception_buatan_sendiri.py`](contoh/contoh07_exception_buatan_sendiri.py)

Exception hanyalah **kelas**, jadi kita bisa membuat jenis baru dengan pewarisan. Contoh ini membuat hierarki kecil untuk rekening tabungan: `RekeningError` sebagai induk, dengan dua anak, `SaldoTidakCukupError` (membawa data saldo dan jumlah yang diminta) dan `TransferGagalError`.

```python
class RekeningError(Exception):  # [1] turunan Exception
    """Induk semua error yang berhubungan dengan rekening."""


class SaldoTidakCukupError(RekeningError):  # [2] turunan RekeningError
    """Dilempar saat saldo tidak cukup untuk penarikan."""

    def __init__(self, saldo: int, diminta: int):
        super().__init__(f"Saldo tidak cukup: saldo Rp{saldo}, "
                         f"diminta Rp{diminta}")  # [3] pesan untuk str(e)
        self.saldo = saldo  # [4] data tambahan untuk penangkap
        self.diminta = diminta

    @property
    def kekurangan(self) -> int:
        return self.diminta - self.saldo


class TransferGagalError(RekeningError):
    """Dilempar saat transfer tidak bisa diselesaikan."""
```

Method `tarik()` milik kelas `Rekening` melempar `raise SaldoTidakCukupError(self._saldo, jumlah)` **[5]** jika saldo kurang. Fungsi `transfer()` lalu membungkusnya menjadi `TransferGagalError`:

```python
def transfer(asal: Rekening, tujuan: Rekening, jumlah: int):
    try:
        asal.tarik(jumlah)
    except SaldoTidakCukupError as e:
        pesan = f"Transfer {asal.pemilik} ke {tujuan.pemilik} gagal"
        raise TransferGagalError(pesan) from e  # [6] simpan penyebab aslinya
    tujuan.setor(jumlah)
    print(f"Transfer Rp{jumlah} dari {asal.pemilik} ke {tujuan.pemilik} berhasil")
```

Program utamanya:

```python
    print("=== TARIK TUNAI ===")
    for jumlah in [200000, 400000]:
        try:
            budi.tarik(jumlah)
            print(f"Tarik Rp{jumlah} berhasil, sisa saldo Rp{budi.saldo}")
        except SaldoTidakCukupError as e:  # [7] tangkap yang spesifik
            print(f"Gagal: {e}")
            print(f"  Kurang Rp{e.kekurangan}. Coba tarik paling banyak "
                  f"Rp{e.saldo}.")  # [8] memakai data tambahan

    print()
    print("=== TRANSFER ===")
    for asal, tujuan, jumlah in [(budi, siti, 50000), (siti, budi, 250000)]:
        try:
            transfer(asal, tujuan, jumlah)
        except RekeningError as e:  # [9] tangkap induknya: semua error rekening
            print(f"Gagal: {e}")
            print(f"  Penyebab: {e.__cause__}")  # [10] exception lama tersimpan
```

**Output:**

```text
=== TARIK TUNAI ===
Tarik Rp200000 berhasil, sisa saldo Rp300000
Gagal: Saldo tidak cukup: saldo Rp300000, diminta Rp400000
  Kurang Rp100000. Coba tarik paling banyak Rp300000.

=== TRANSFER ===
Transfer Rp50000 dari Budi ke Siti berhasil
Gagal: Transfer Siti ke Budi gagal
  Penyebab: Saldo tidak cukup: saldo Rp150000, diminta Rp250000

Saldo akhir: Budi Rp250000, Siti Rp150000
```

Penjelasan:

- **[1]** dan **[2]** Exception buatan sendiri **wajib** mewarisi `Exception`, langsung atau tidak langsung. Badan kelas boleh hanya berisi *docstring*. `SaldoTidakCukupError` **adalah** `RekeningError`, dan juga **adalah** `Exception`.
- **[3]** dan **[4]** Pesan dikirim ke konstruktor induk dengan `super().__init__(...)`; pesan inilah yang muncul saat `print(e)`. Data tambahan disimpan sebagai atribut, persis seperti objek biasa.
- **[5]** Yang dilempar adalah **objek** baru dari kelas exception kita.
- **[6]** `raise ... from e` melempar exception baru dan menyimpan `e` sebagai penyebabnya (*exception chaining*).
- **[7]** dan **[8]** Penangkap spesifik bisa memakai data tambahan (`e.kekurangan`, `e.saldo`) untuk memberi saran.
- **[9]** Penangkap induk `RekeningError` menangkap `TransferGagalError` karena relasi *is-a*.
- **[10]** `e.__cause__` berisi exception lama (`SaldoTidakCukupError`). Penyebab aslinya tidak hilang.

### Jika exception bersambung tidak ditangkap

Tambahkan baris `transfer(siti, budi, 250000)` di akhir `main()`, di luar `try`. *Traceback*-nya memuat **dua** bagian:

```text
Traceback (most recent call last):
  File "contoh07_exception_buatan_sendiri.py", line 70, in transfer
    asal.tarik(jumlah)
    ~~~~~~~~~~^^^^^^^^
  File "contoh07_exception_buatan_sendiri.py", line 61, in tarik
    raise SaldoTidakCukupError(self._saldo, jumlah)  # [5]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SaldoTidakCukupError: Saldo tidak cukup: saldo Rp150000, diminta Rp250000

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "contoh07_exception_buatan_sendiri.py", line 107, in <module>
    main()
    ~~~~^^
  File "contoh07_exception_buatan_sendiri.py", line 103, in main
    transfer(siti, budi, 250000)
    ~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "contoh07_exception_buatan_sendiri.py", line 73, in transfer
    raise TransferGagalError(pesan) from e  # [6] simpan penyebab aslinya
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TransferGagalError: Transfer Siti ke Budi gagal
```

Bagian atas adalah **penyebab** (saldo kurang), bagian bawah adalah exception yang akhirnya lolos (transfer gagal). Kalimat *The above exception was the direct cause of the following exception* menghubungkan keduanya.

> [!NOTE]
> Jika kamu melempar exception baru di dalam `except` **tanpa** `from e`, Python tetap mencatat exception lama, tetapi dengan kalimat lain: *During handling of the above exception, another exception occurred*. Artinya "terjadi exception lain saat sedang menangani exception pertama", yang biasanya menandakan kecelakaan. Tulis `from e` untuk menegaskan bahwa pembungkusan itu **disengaja**.

## 8. Hierarki Exception Python

Semua exception bawaan Python tersusun dalam pohon pewarisan (diagramnya ada di [halaman konsep](../README.md#8-hierarki-exception)). Di puncaknya ada `BaseException`, dengan tiga anak penting: `Exception` (induk semua exception "biasa"), `KeyboardInterrupt` (pengguna menekan Ctrl+C), dan `SystemExit` (program diminta berhenti).

Kamu bisa memeriksa leluhur sebuah kelas exception dengan atribut `__mro__` (urutan pencarian method, Pertemuan 07). Misalnya `print(ZeroDivisionError.__mro__)` menghasilkan:

```text
(<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
```

Akibatnya:

- `except ArithmeticError:` ikut menangkap `ZeroDivisionError`, dan `except LookupError:` ikut menangkap `IndexError` maupun `KeyError`.
- `except Exception:` menangkap hampir semua kesalahan, tetapi **tidak** menangkap `KeyboardInterrupt` dan `SystemExit`. Itu memang disengaja: Ctrl+C harus tetap bisa menghentikan program.
- `except:` **tanpa** nama jenis menangkap **segalanya**, termasuk Ctrl+C. Hindari bentuk ini. Jika benar-benar butuh jaring pengaman, tulis `except Exception:`.

> [!IMPORTANT]
> Exception buatan sendiri selalu mewarisi `Exception`, **bukan** `BaseException`. Dengan begitu, ia ikut tertangkap oleh `except Exception:` seperti exception biasa lainnya.

## 9. Studi Kasus KedaiKita

File: [`studi-kasus/main.py`](studi-kasus/main.py) dan file baru [`studi-kasus/pengecualian.py`](studi-kasus/pengecualian.py), ditambah perubahan kecil di `kedai.py`, `menu.py`, `pembayaran.py`, dan `pesanan.py`.

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#12-studi-kasus-kedaikita-kesalahan-yang-jelas-dan-bisa-ditangkap).

**Apa yang berubah dibanding Pertemuan 10?**

- **File baru `pengecualian.py`** berisi `KedaiError` dan tiga turunannya.
- `kedai.py`: `cari_menu()` melempar `MenuTidakDitemukanError`, tidak lagi mengembalikan `None`.
- `menu.py`: `kurangi_stok()` melempar `StokTidakCukupError` (sebelumnya `ValueError` biasa).
- `pembayaran.py`: `proses()` tidak lagi mengembalikan `True`/`False`. Jika gagal, ia melempar `PembayaranGagalError`.
- `pesanan.py`: `tambah_item()` dan `bayar()` menolak pesanan yang sudah LUNAS dengan `KedaiError`. `bayar()` tidak lagi mengembalikan nilai.
- `main.py`: skenarionya baru, memakai `try`/`except`/`else`/`finally`. Fungsi `cetak_semua()` dari Pertemuan 10 tidak dipakai lagi.
- `utilitas.py`, `pelanggan.py`, dan `dapat_dicetak.py` **tidak berubah**.

### Exception khusus KedaiKita

Isi `pengecualian.py` (setelah *docstring* modulnya):

```python
class KedaiError(Exception):
    """Induk semua error khusus KedaiKita."""


class StokTidakCukupError(KedaiError):
    """Dilempar saat jumlah yang dipesan melebihi stok."""

    def __init__(self, nama_menu: str, diminta: int, tersedia: int):
        super().__init__(f"Stok {nama_menu} tidak cukup: "
                         f"diminta {diminta}, tersedia {tersedia}")
        self.nama_menu = nama_menu
        self.diminta = diminta
        self.tersedia = tersedia


class MenuTidakDitemukanError(KedaiError):
    """Dilempar saat kode menu tidak terdaftar."""

    def __init__(self, kode: str):
        super().__init__(f"Menu dengan kode {kode} tidak ditemukan")
        self.kode = kode


class PembayaranGagalError(KedaiError):
    """Dilempar saat pembayaran tidak bisa diselesaikan."""

    def __init__(self, metode: str, alasan: str):
        super().__init__(f"Pembayaran {metode} gagal: {alasan}")
        self.metode = metode
        self.alasan = alasan
```

- Semuanya turunan `KedaiError`, jadi `except KedaiError:` menangkap ketiganya sekaligus.
- Setiap konstruktor menyusun **pesan** yang lengkap, lalu menyimpan data mentahnya sebagai atribut. `main.py` nanti memakai `e.tersedia` untuk memberi saran.

### Siapa melempar apa

- `kedai.py`: `cari_menu()` kini diakhiri `raise MenuTidakDitemukanError(kode)` setelah perulangan selesai tanpa hasil. Tipe kembaliannya berubah dari `Menu | None` menjadi `Menu`, jadi pemanggil tidak perlu lagi memeriksa `None`.
- `menu.py`: `kurangi_stok()` menulis `raise StokTidakCukupError(self._nama, jumlah, self._stok)` saat stok kurang. Jumlah yang tidak positif tetap ditolak dengan `ValueError`, karena itu kesalahan input biasa, bukan aturan bisnis kedai.
- `pembayaran.py`: `proses()` tidak lagi mengembalikan `True`/`False`. `PembayaranTunai` dan `PembayaranQRIS` melempar `PembayaranGagalError` jika uang atau saldonya kurang. `PembayaranKartu` tidak pernah melempar, karena di simulasi ini transaksi kartu selalu disetujui.

Perubahan paling menarik ada di `bayar()` milik `pesanan.py`. Bagian awalnya menolak pesanan yang sudah LUNAS:

```python
    def bayar(self, pembayaran: Pembayaran):
        """Membayar pesanan. Melempar KedaiError jika gagal."""
        if self._status == "LUNAS":
            raise KedaiError(f"Pesanan {self._nomor} sudah lunas")
```

Bagian tengahnya memanggil `proses()` **tanpa** `try`:

```python
        pembayaran.proses(total_bayar)  # jika gagal, baris di bawah tidak dijalankan
        self._status = "LUNAS"
```

- Pesanan yang sudah LUNAS ditolak dengan `KedaiError` (induknya), karena kesalahan ini tidak butuh jenis khusus. `tambah_item()` melakukan pemeriksaan yang sama.
- `bayar()` sengaja **tidak menangkap** `PembayaranGagalError`. Exception itu merambat ke `main.py`, dan karena baris `self._status = "LUNAS"` ikut dilewati, **status tetap BARU**. Tidak ada lagi `if berhasil:` seperti di Pertemuan 10.

### Program utama

Bagian pertama memproses lima permintaan Budi. Setiap jenis kegagalan punya penangkapnya sendiri:

```python
    print("=== PESANAN BUDI: MENAMBAH ITEM ===")
    pesanan_budi = kedai.buat_pesanan(budi)
    permintaan = [("M01", 2), ("M03", 1), ("M99", 1), ("M04", 50), ("M02", 0)]
    for kode, jumlah in permintaan:
        try:
            menu = kedai.cari_menu(kode)
            pesanan_budi.tambah_item(menu, jumlah)
        except MenuTidakDitemukanError as e:
            print(f"  [GAGAL] {e}")
        except StokTidakCukupError as e:
            print(f"  [GAGAL] {e}")
            print(f"          Saran: pesan paling banyak {e.tersedia} porsi")
        except KedaiError as e:  # error kedai lain (misalnya pesanan sudah lunas)
            print(f"  [GAGAL] {e}")
        except ValueError as e:
            print(f"  [GAGAL] {kode}: {e}")
        else:
            print(f"  [OK] {jumlah} x {menu.nama}")
    print()
```

- Dua penangkap spesifik ditulis **di atas** penangkap induknya, `KedaiError`. Jika urutannya terbalik, `KedaiError` akan menangkap semuanya dan saran "pesan paling banyak ..." tidak pernah muncul.
- `ValueError` menangkap permintaan 0 porsi, yang ditolak oleh `ItemPesanan`.
- `else` mencetak `[OK]` hanya jika kedua baris di blok `try` berhasil.

Bagian kedua memperlihatkan **rencana cadangan** dan `finally`:

```python
    print("=== PESANAN SITI: BAYAR GAGAL, LALU COBA LAGI ===")
    pesanan_siti = kedai.buat_pesanan(siti)
    try:
        pesanan_siti.tambah_item(kedai.cari_menu("M02"), 2)
        pesanan_siti.tambah_item(kedai.cari_menu("M05"))
        pesanan_siti.bayar(PembayaranQRIS(20000))
    except PembayaranGagalError as e:
        print(f"  [GAGAL] {e}")
        print("  Mencoba kartu kredit...")
        try:
            pesanan_siti.bayar(PembayaranKartu("BNI"))
        except KedaiError as e2:
            print(f"  [GAGAL LAGI] {e2}")
    except KedaiError as e:
        print(f"  [GAGAL] {e}")
    finally:
        print("  [log] proses pesanan Siti selesai")
    print()
```

- Di dalam blok `except` boleh ada `try` lagi. Pembayaran cadangan juga bisa gagal, jadi ia dijaga sendiri dengan nama variabel `e2`.
- `finally` mencatat log setelah semuanya selesai, berhasil maupun gagal.

Bagian ketiga (pesanan Rina) cukup memakai **satu** penangkap, `except KedaiError as e:`, untuk semua jenis error kedai: kode M77 yang tidak ada, stok yang kurang, serta membayar ulang dan mengubah pesanan Budi yang sudah LUNAS. Bagian terakhir mencetak ringkasan status dan daftar menu.

Jalankan `python main.py` dari dalam folder `studi-kasus` (lihat [Persiapan](#persiapan)).

**Output:**

```text
=== PESANAN BUDI: MENAMBAH ITEM ===
  [OK] 2 x Kopi Susu Gula Aren
  [OK] 1 x Nasi Goreng Kampung
  [GAGAL] Menu dengan kode M99 tidak ditemukan
  [GAGAL] Stok Mie Goreng Jawa tidak cukup: diminta 50, tersedia 10
          Saran: pesan paling banyak 10 porsi
  [GAGAL] M02: Jumlah harus lebih dari 0

Pembayaran pesanan P001 (Budi Santoso)
  Metode       : Tunai
  Total bayar  : Rp61.000
  Uang diterima Rp100.000, kembalian Rp39.000
  Status       : LUNAS (+6 poin)

=== PESANAN SITI: BAYAR GAGAL, LALU COBA LAGI ===
Pembayaran pesanan P002 (Siti Aminah)
  Metode       : QRIS
  Total bayar  : Rp31.000
  [GAGAL] Pembayaran QRIS gagal: saldo e-wallet tidak cukup (saldo Rp20.000)
  Mencoba kartu kredit...
Pembayaran pesanan P002 (Siti Aminah)
  Metode       : Kartu Kredit BNI
  Biaya layanan: Rp620
  Total bayar  : Rp31.620
  Transaksi kartu BNI disetujui sebesar Rp31.620
  Status       : LUNAS (+3 poin)
  [log] proses pesanan Siti selesai

=== SATU PENANGKAP UNTUK SEMUA ERROR KEDAI ===
  Ditolak: Menu dengan kode M77 tidak ditemukan
  Ditolak: Stok Mie Goreng Jawa tidak cukup: diminta 99, tersedia 10
  Ditolak: Pesanan P001 sudah lunas
  Ditolak: Pesanan P001 sudah lunas, tidak bisa diubah

=== RINGKASAN ===
P001 (Budi Santoso): LUNAS
P002 (Siti Aminah): LUNAS
P003 (Rina Marlina): BARU, 0 item
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 18 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 28 | dingin
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 14 | pedas level 2
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10 | pedas level 1
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 11 | pedas level 0
```

Perhatikan pembayaran QRIS Siti: baris `Status : LUNAS` tidak muncul setelah kegagalan pertama, karena `proses()` melempar exception sebelum status diubah. Pesanan Rina tetap kosong (0 item), dan stok Mie Goreng Jawa tetap 10.

> [!TIP]
> **Coba sendiri:** tambahkan baris `kedai.cari_menu("M99")` tepat setelah `kedai = siapkan_kedai()` di `main()`, di luar `try` mana pun. Tebak dulu apa yang terjadi.

<details>
<summary>Lihat jawaban</summary>

Python tidak memprotes apa pun sebelum program berjalan. Exception baru meledak saat baris itu dijalankan. Bagian akhir *traceback*-nya:

```text
  File "main.py", line 36, in main
    kedai.cari_menu("M99")
    ~~~~~~~~~~~~~~~^^^^^^^
  File "kedai.py", line 43, in cari_menu
    raise MenuTidakDitemukanError(kode)
pengecualian.MenuTidakDitemukanError: Menu dengan kode M99 tidak ditemukan
```

Nama jenisnya ditulis lengkap dengan nama modulnya (`pengecualian.`), karena kelas itu didefinisikan di file `pengecualian.py`. Bandingkan dengan Pertemuan 10: dulu kesalahan yang sama meledak sebagai `AttributeError` di dalam `tambah_item()`, jauh dari penyebabnya. Sekarang pesannya langsung menyebut masalah yang sebenarnya. Hapus lagi baris tadi setelah mencoba.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan Error

Kesalahan yang paling sering, yaitu **menelan exception diam-diam** dengan `except ...: pass`, sudah kamu lihat di "Coba sendiri" bagian 6: program tidak error, tetapi berbohong. Berikut kesalahan lain yang perlu diwaspadai. Sebagian di antaranya juga **tidak** memunculkan pesan error sama sekali.

### Kesalahan 1: Lupa menulis `raise`

```python
    def atur_suhu(self, suhu: int):
        if suhu < 16 or suhu > 30:
            ValueError(f"Suhu {suhu} di luar batas 16-30 derajat")
        self.suhu = suhu
```

Hasilnya, setelah `ac.atur_suhu(10)`:

```text
Suhu AC sekarang: 10 derajat
```

**Artinya:** baris `ValueError(...)` hanya **membuat** objek exception, lalu membuangnya. Tanpa `raise`, objek itu tidak pernah dilempar, sehingga suhu 10 lolos. **Perbaikan:** `raise ValueError(...)`.

### Kesalahan 2: Exception buatan sendiri tanpa `super().__init__(pesan)`

```python
class StokTidakCukupError(KedaiError):
    def __init__(self, nama_menu: str, diminta: int, tersedia: int):
        self.nama_menu = nama_menu
        self.diminta = diminta
        self.tersedia = tersedia


try:
    raise StokTidakCukupError("Mie Goreng Jawa", 50, 10)
except KedaiError as e:
    print(f"[GAGAL] {e}")
```

Hasilnya:

```text
[GAGAL] ('Mie Goreng Jawa', 50, 10)
```

**Artinya:** karena pesan tidak pernah dikirim ke kelas induk, Python menampilkan argumen mentahnya sebagai pesan. **Perbaikan:** panggil `super().__init__(f"Stok {nama_menu} tidak cukup: ...")` di baris pertama konstruktor.

### Kesalahan 3: Memakai variabel dari blok `try` yang gagal

```python
def baca_porsi(teks: str) -> int:
    try:
        porsi = int(teks)
    except ValueError:
        print(f"'{teks}' bukan angka")
    return porsi


print(baca_porsi("3"))
print(baca_porsi("dua"))
```

```text
3
'dua' bukan angka
Traceback (most recent call last):
  File "variabel_try.py", line 10, in <module>
    print(baca_porsi("dua"))
          ~~~~~~~~~~^^^^^^^
  File "variabel_try.py", line 6, in baca_porsi
    return porsi
           ^^^^^
UnboundLocalError: cannot access local variable 'porsi' where it is not associated with a value
```

**Artinya:** saat `int("dua")` gagal, baris `porsi = ...` tidak pernah selesai, jadi variabel `porsi` tidak pernah diisi. Setelah `except` selesai, `return porsi` mencoba membaca variabel yang kosong. **Perbaikan:** kembalikan nilai cadangan di dalam `except` (misalnya `return 0`), atau lempar ulang exception-nya.

> [!NOTE]
> Yang boleh dilempar hanyalah objek exception. `raise "Stok habis"` ditolak dengan `TypeError: exceptions must derive from BaseException`. Tulis `raise ValueError("Stok habis")`, atau lebih baik lagi exception buatan sendiri.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi Python. Misalnya, pesan `UnboundLocalError` di Python 3.10 berbeda kalimatnya, tetapi jenis exception-nya tetap sama.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| Menangkap | `try:` ... `except Jenis:` | `except ZeroDivisionError:` |
| Menyimpan objek exception | `except Jenis as e:` | `print(f"Gagal: {e}")` |
| Beberapa jenis, satu penanganan | `except (A, B):` | `except (ValueError, IndexError):` |
| Jika tidak ada exception | `else:` | `else: print("[OK]")` |
| Selalu dijalankan | `finally:` | `finally: proyektor.matikan()` |
| Melempar | `raise Jenis("pesan")` | `raise ValueError("Suhu di luar batas")` |
| Melempar ulang | `raise` (di dalam `except`) | `raise` |
| *Exception chaining* + membaca penyebab | `raise Baru(...) from e`, lalu `e.__cause__` | `raise TransferGagalError(pesan) from e` |
| Exception buatan sendiri | `class NamaError(Induk):` | `class KedaiError(Exception):` |
| Pesan exception buatan sendiri | `super().__init__(pesan)` | `super().__init__(f"Menu {kode} tidak ditemukan")` |
| Data tambahan | atribut biasa | `self.tersedia = tersedia` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
