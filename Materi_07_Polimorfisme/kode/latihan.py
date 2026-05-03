"""
Latihan Mandiri - Materi 07: Polimorfisme (Polymorphism)
File: latihan.py

Petunjuk:
- Kerjakan setiap soal di bawah ini.
- Hapus perintah `pass` dan ganti dengan implementasi Anda.
- Jalankan file ini untuk menguji jawaban: python latihan.py
- Output yang diharapkan tersedia sebagai komentar di tiap soal.
"""

from abc import ABC, abstractmethod
import math

print("=" * 60)
print("LATIHAN MATERI 07 - POLIMORFISME (POLYMORPHISM)")
print("=" * 60)


# ==================================================================
# SOAL 1 (* Mudah) — Polimorfisme via Pewarisan: Hierarki Pegawai
#
# Buat hierarki kelas berikut:
#
#   Pegawai (induk)
#     |-- PegawaiTetap     (gaji_pokok, tunjangan)
#     |-- PegawaiKontrak   (upah_per_jam, jam_kerja)
#     `-- PegawaiMagang    (uang_saku_per_bulan)
#
# Semua kelas WAJIB mengimplementasikan:
#   - hitung_gaji()   -> kembalikan total penghasilan bulanan
#   - jenis_pegawai() -> kembalikan string jenis pegawai
#
# Pegawai (induk) harus memiliki:
#   - Atribut: nama, nip
#   - Method cetak_slip() yang memanggil hitung_gaji() dan jenis_pegawai()
#     (method ini TIDAK boleh di-override — biarkan polimorfisme bekerja)
#
# Detail perhitungan:
#   - PegawaiTetap   : gaji_pokok + tunjangan
#   - PegawaiKontrak : upah_per_jam * jam_kerja (max 200 jam/bulan)
#   - PegawaiMagang  : uang_saku_per_bulan (tetap, tidak berubah)
# ==================================================================
print("\n" + "-" * 50)
print("SOAL 1: Hierarki Pegawai")
print("-" * 50)


class Pegawai:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip  = nip

    def hitung_gaji(self):
        raise NotImplementedError("Subkelas harus mengimplementasikan hitung_gaji()")

    def jenis_pegawai(self):
        raise NotImplementedError("Subkelas harus mengimplementasikan jenis_pegawai()")

    def cetak_slip(self):
        gaji = self.hitung_gaji()
        print(f"  ---- Slip Gaji ----")
        print(f"  Nama  : {self.nama}")
        print(f"  NIP   : {self.nip}")
        print(f"  Jenis : {self.jenis_pegawai()}")
        print(f"  Gaji  : Rp {gaji:,.0f}")
        print(f"  -------------------")


class PegawaiTetap(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, tunjangan):
        pass   # TODO: panggil super().__init__ dan simpan atribut

    def hitung_gaji(self):
        pass   # TODO: gaji_pokok + tunjangan

    def jenis_pegawai(self):
        pass   # TODO: return "Pegawai Tetap"


class PegawaiKontrak(Pegawai):
    def __init__(self, nama, nip, upah_per_jam, jam_kerja):
        pass   # TODO

    def hitung_gaji(self):
        pass   # TODO: upah_per_jam * min(jam_kerja, 200)

    def jenis_pegawai(self):
        pass   # TODO: return "Pegawai Kontrak"


class PegawaiMagang(Pegawai):
    def __init__(self, nama, nip, uang_saku_per_bulan):
        pass   # TODO

    def hitung_gaji(self):
        pass   # TODO: return uang_saku_per_bulan

    def jenis_pegawai(self):
        pass   # TODO: return "Pegawai Magang"


# Uji Soal 1
# Hapus tanda '#' pada blok di bawah setelah implementasi selesai
"""
daftar_pegawai = [
    PegawaiTetap("Andi Kurniawan",   "T001", 8_000_000, 2_500_000),
    PegawaiKontrak("Budi Santoso",   "K001", 75_000,    160),
    PegawaiMagang("Sari Dewi",       "M001", 1_500_000),
    PegawaiKontrak("Rudi Hartono",   "K002", 80_000,    220),  # jam > 200!
]

total_pengeluaran = 0
for p in daftar_pegawai:
    p.cetak_slip()
    total_pengeluaran += p.hitung_gaji()
    print()

print(f"  Total pengeluaran gaji: Rp {total_pengeluaran:,.0f}")

# Output yang diharapkan:
#   ---- Slip Gaji ----
#   Nama  : Andi Kurniawan
#   NIP   : T001
#   Jenis : Pegawai Tetap
#   Gaji  : Rp 10,500,000
#   -------------------
#
#   ---- Slip Gaji ----
#   Nama  : Budi Santoso
#   NIP   : K001
#   Jenis : Pegawai Kontrak
#   Gaji  : Rp 12,000,000      <- 75.000 * 160
#   -------------------
#
#   ---- Slip Gaji ----
#   Nama  : Sari Dewi
#   NIP   : M001
#   Jenis : Pegawai Magang
#   Gaji  : Rp 1,500,000
#   -------------------
#
#   ---- Slip Gaji ----
#   Nama  : Rudi Hartono
#   NIP   : K002
#   Jenis : Pegawai Kontrak
#   Gaji  : Rp 16,000,000      <- 80.000 * 200 (bukan 220!)
#   -------------------
#
#   Total pengeluaran gaji: Rp 40,000,000
"""
print("  [TODO] Soal 1 belum dikerjakan.")


# ==================================================================
# SOAL 2 (** Menengah) — Duck Typing + ABC: Plugin Ekspor Dokumen
#
# Sebuah sistem akademik perlu mengekspor data ke berbagai format.
# Implementasikan sistem berikut:
#
# (a) Buat ABC FormatEkspor dengan:
#     - @abstractmethod ekspor(data, nama_file)
#       (cetak isi dokumen ke stdout sesuai format — tidak perlu return)
#     - @abstractmethod ekstensi() -> str
#       (return ekstensi file, misal ".csv")
#     - Method simpan(data, nama_file) yang:
#       1. Memanggil ekspor(data, nama_file)  <- mencetak isi dokumen
#       2. Mencetak "Disimpan: {nama_file}{ekstensi()}"
#
# (b) Implementasikan tiga kelas:
#
#   EksporCSV:
#     - ekspor: cetak setiap baris data sebagai "kolom1,kolom2,..."
#     - ekstensi: return ".csv"
#
#   EksporMarkdown:
#     - ekspor: cetak sebagai tabel Markdown
#       (baris pertama = header, sisanya = data)
#     - ekstensi: return ".md"
#
#   EksporJSON:
#     - ekspor: cetak sebagai format JSON sederhana
#       (list of dict, key dari baris pertama)
#     - ekstensi: return ".json"
#
# Format data input selalu: list of list, baris pertama adalah header.
# Contoh:
#   data = [
#       ["NIM",       "Nama",          "IPK"],
#       ["2301001",   "Budi Santoso",  "3.85"],
#       ["2301002",   "Sari Dewi",     "3.92"],
#   ]
# ==================================================================
print("\n" + "-" * 50)
print("SOAL 2: Plugin Ekspor Dokumen")
print("-" * 50)


class FormatEkspor(ABC):
    @abstractmethod
    def ekspor(self, data, nama_file):
        pass

    @abstractmethod
    def ekstensi(self):
        pass

    def simpan(self, data, nama_file):
        pass   # TODO: panggil ekspor(), lalu cetak "Disimpan: ..."


class EksporCSV(FormatEkspor):
    def ekspor(self, data, nama_file):
        pass   # TODO: cetak setiap baris sebagai "a,b,c"

    def ekstensi(self):
        pass   # TODO: return ".csv"


class EksporMarkdown(FormatEkspor):
    def ekspor(self, data, nama_file):
        pass   # TODO: cetak tabel Markdown
        # Header:  | NIM | Nama | IPK |
        # Separator: |---|---|---|
        # Baris:   | 2301001 | Budi | 3.85 |

    def ekstensi(self):
        pass   # TODO: return ".md"


class EksporJSON(FormatEkspor):
    def ekspor(self, data, nama_file):
        pass   # TODO: cetak sebagai JSON
        # [
        #   {"NIM": "2301001", "Nama": "Budi Santoso", "IPK": "3.85"},
        #   ...
        # ]

    def ekstensi(self):
        pass   # TODO: return ".json"


# Uji Soal 2
"""
data_mahasiswa = [
    ["NIM",       "Nama",            "IPK",  "Prodi"],
    ["2301001",   "Budi Santoso",    "3.85", "Informatika"],
    ["2301002",   "Sari Dewi",       "3.92", "Informatika"],
    ["2301003",   "Rudi Hartono",    "3.20", "Sistem Informasi"],
]

# Duck typing: semua format bisa diproses dengan fungsi yang sama
def ekspor_ke_semua_format(data, nama_file, daftar_format):
    print(f"  Mengekspor '{nama_file}' ke {len(daftar_format)} format...")
    for fmt in daftar_format:
        print(f"\n  --- {fmt.ekstensi().upper()} ---")
        fmt.simpan(data, nama_file)

ekspor_ke_semua_format(
    data_mahasiswa,
    "rekap_mahasiswa",
    [EksporCSV(), EksporMarkdown(), EksporJSON()]
)

# Output CSV yang diharapkan:
#   NIM,Nama,IPK,Prodi
#   2301001,Budi Santoso,3.85,Informatika
#   2301002,Sari Dewi,3.92,Informatika
#   2301003,Rudi Hartono,3.20,Sistem Informasi
#   Disimpan: rekap_mahasiswa.csv

# Output Markdown yang diharapkan:
#   | NIM | Nama | IPK | Prodi |
#   |---|---|---|---|
#   | 2301001 | Budi Santoso | 3.85 | Informatika |
#   ...
#   Disimpan: rekap_mahasiswa.md

# Output JSON yang diharapkan:
#   [
#     {"NIM": "2301001", "Nama": "Budi Santoso", "IPK": "3.85", ...},
#     ...
#   ]
#   Disimpan: rekap_mahasiswa.json
"""
print("  [TODO] Soal 2 belum dikerjakan.")


# ==================================================================
# SOAL 3 (*** Menantang) — Operator Overloading: Kelas Matriks
#
# Implementasikan kelas Matriks2D yang mendukung:
#
# Atribut:
#   - baris x kolom (int x int)
#   - data: list of list (nilai)
#
# Method wajib:
#   __init__(self, data)    -> simpan data matriks
#   __add__(self, other)    -> penjumlahan dua matriks (dimensi sama)
#   __sub__(self, other)    -> pengurangan dua matriks (dimensi sama)
#   __mul__(self, other)    -> perkalian:
#                              - jika other adalah Matriks2D: perkalian matriks
#                              - jika other adalah int/float: perkalian skalar
#   __eq__(self, other)     -> True jika semua elemen sama
#   __str__(self)           -> cetak matriks dalam format grid rapi
#   __repr__(self)          -> Matriks2D([[...], [...]])
#   transpose(self)         -> kembalikan Matriks2D baru hasil transpos
#
# Validasi:
#   - Penjumlahan/pengurangan: dimensi harus sama
#   - Perkalian matriks: kolom A harus sama dengan baris B
#   - Angkat ValueError jika dimensi tidak cocok
#
# Tips:
#   Untuk perkalian matriks AxB:
#     hasil[i][j] = sum(A[i][k] * B[k][j] for k in range(kol_A))
# ==================================================================
print("\n" + "-" * 50)
print("SOAL 3: Kelas Matriks2D dengan Operator Overloading")
print("-" * 50)


class Matriks2D:
    def __init__(self, data):
        pass   # TODO: simpan data, hitung self.baris dan self.kolom

    def __add__(self, other):
        pass   # TODO: tambah elemen-per-elemen, raise ValueError jika dimensi beda

    def __sub__(self, other):
        pass   # TODO: kurang elemen-per-elemen, raise ValueError jika dimensi beda

    def __mul__(self, other):
        pass   # TODO: perkalian matriks ATAU perkalian skalar

    def __eq__(self, other):
        pass   # TODO: True jika semua elemen dan dimensi sama

    def __str__(self):
        pass   # TODO: tampilkan sebagai grid, tiap elemen lebar 6 karakter

    def __repr__(self):
        pass   # TODO: Matriks2D([[...], [...]])

    def transpose(self):
        pass   # TODO: tukar baris dan kolom


# Uji Soal 3
"""
A = Matriks2D([[1, 2, 3],
               [4, 5, 6]])

B = Matriks2D([[7,  8,  9],
               [10, 11, 12]])

C = Matriks2D([[1, 4],
               [2, 5],
               [3, 6]])

print("Matriks A:")
print(A)
print("Matriks B:")
print(B)

print("A + B:")
print(A + B)
# [[8, 10, 12], [14, 16, 18]]

print("A - B:")
print(A - B)
# [[-6, -6, -6], [-6, -6, -6]]

print("A * 2 (skalar):")
print(A * 2)
# [[2, 4, 6], [8, 10, 12]]

print("A * C (perkalian matriks 2x3 * 3x2 = 2x2):")
print(A * C)
# [[14, 32], [32, 77]]

print("A == B:", A == B)   # False
print("A == A:", A == A)   # True

print("Transpos A:")
print(A.transpose())
# [[1, 4], [2, 5], [3, 6]]

# Uji error dimensi tidak cocok
try:
    hasil = A + C
except ValueError as e:
    print(f"Error: {e}")
# Error: Dimensi matriks tidak sama: (2, 3) vs (3, 2)
"""
print("  [TODO] Soal 3 belum dikerjakan.")


print("\n" + "=" * 60)
print("Selesai! Kerjakan semua soal di atas.")
print("Hapus tanda # pada blok pengujian setelah implementasi selesai.")
print("=" * 60)
