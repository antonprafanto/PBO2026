"""
============================================================
    MATERI 03 - Atribut dan Method
    File: latihan.py
    Topik: Soal Latihan Mandiri
============================================================

PETUNJUK:
  - Kerjakan setiap soal di bagian yang sudah disediakan.
  - Jalankan file ini untuk melihat hasilnya:
      python latihan.py
  - Setiap soal memiliki test sederhana di bawahnya.
    Jika output cocok, berarti jawabanmu benar! [OK]
============================================================
"""

print("=" * 60)
print("         LATIHAN MANDIRI - MATERI 03")
print("         Atribut dan Method")
print("=" * 60)


# ─────────────────────────────────────────────────────────
# SOAL 1 - Atribut Kelas vs Instance (★☆☆)
# ─────────────────────────────────────────────────────────
# Lengkapi kelas `Buku` di bawah ini:
#   - Atribut KELAS: `penerbit` = "Penerbit Nusantara"
#                   `jumlah_buku` = 0 (counter)
#   - Atribut INSTANCE: `judul`, `penulis`, `harga`
#   - Setiap kali objek dibuat, `jumlah_buku` bertambah 1
#   - Method instance: `info()` -> cetak: "[judul] oleh [penulis] - Rp [harga]"
#   - Class method: `total_koleksi()` -> cetak jumlah_buku
# ─────────────────────────────────────────────────────────

print("\n--- SOAL 1: Atribut Kelas vs Instance ---")


class Buku:
    # TODO: Tambahkan atribut kelas di sini
    # penerbit     = ...
    # jumlah_buku  = ...

    def __init__(self, judul, penulis, harga):
        # TODO: Definisikan atribut instance
        pass

    def info(self):
        # TODO: Cetak: "[judul] oleh [penulis] - Rp [harga:,.0f]"
        pass

    @classmethod
    def total_koleksi(cls):
        # TODO: Cetak: "Total koleksi: [jumlah_buku] buku"
        pass


# Test Soal 1
b1 = Buku("Pemrograman Python", "Anton Prafanto", 125_000)
b2 = Buku("Clean Code", "Robert C. Martin", 210_000)
b3 = Buku("Design Patterns", "Gang of Four", 195_000)
b1.info()           # [Pemrograman Python] oleh Anton Prafanto - Rp 125,000
b2.info()           # [Clean Code] oleh Robert C. Martin - Rp 210,000
Buku.total_koleksi()  # Total koleksi: 3 buku
print()


# ─────────────────────────────────────────────────────────
# SOAL 2 - Factory Method dengan @classmethod (★★☆)
# ─────────────────────────────────────────────────────────
# Buat kelas `Pegawai` dengan:
#   - Atribut instance: `nama`, `departemen`, `gaji`
#   - Method: `info()` -> cetak: "[nama] | [departemen] | Rp [gaji]"
#   - @classmethod `dari_teks(cls, teks)`:
#       Format teks: "nama:departemen:gaji" (pisah oleh ":")
#       Contoh: "Budi:IT:8000000"
#   - @classmethod `pegawai_magang(cls, nama)`:
#       departemen = "Magang", gaji = 2_000_000
# ─────────────────────────────────────────────────────────

print("--- SOAL 2: Factory Method ---")


class Pegawai:
    def __init__(self, nama, departemen, gaji):
        # TODO: Definisikan atribut instance
        pass

    def info(self):
        # TODO: Cetak: "[nama] | [departemen] | Rp [gaji:,.0f]"
        pass

    @classmethod
    def dari_teks(cls, teks):
        # TODO: Parsing teks "nama:departemen:gaji"
        pass

    @classmethod
    def pegawai_magang(cls, nama):
        # TODO: Buat pegawai magang dengan nilai default
        pass


# Test Soal 2
p1 = Pegawai("Anton", "Engineering", 12_000_000)
p2 = Pegawai.dari_teks("Budi:Marketing:7500000")
p3 = Pegawai.pegawai_magang("Citra")
p1.info()   # Anton | Engineering | Rp 12,000,000
p2.info()   # Budi | Marketing | Rp 7,500,000
p3.info()   # Citra | Magang | Rp 2,000,000
print()


# ─────────────────────────────────────────────────────────
# SOAL 3 - Utilitas dengan @staticmethod (★★☆)
# ─────────────────────────────────────────────────────────
# Buat kelas `UtilitasString` dengan static method:
#   a) `hitung_kata(teks)` -> kembalikan jumlah kata dalam teks
#   b) `balik_kata(teks)` -> kembalikan teks dengan urutan kata dibalik
#      Contoh: "Saya suka Python" -> "Python suka Saya"
#   c) `is_palindrom(kata)` -> True jika kata palindrom (baca sama dr kiri/kanan)
#      Contoh: "radar" -> True, "python" -> False
#   d) `kapital_setiap_kata(teks)` -> Title Case
#      Contoh: "pemrograman berorientasi objek" -> "Pemrograman Berorientasi Objek"
# ─────────────────────────────────────────────────────────

print("--- SOAL 3: Static Method Utilitas ---")


class UtilitasString:
    @staticmethod
    def hitung_kata(teks):
        # TODO
        pass

    @staticmethod
    def balik_kata(teks):
        # TODO
        pass

    @staticmethod
    def is_palindrom(kata):
        # TODO (petunjuk: bandingkan kata dengan versi terbaliknya)
        pass

    @staticmethod
    def kapital_setiap_kata(teks):
        # TODO
        pass


# Test Soal 3
print(UtilitasString.hitung_kata("Saya suka belajar Python"))  # 4
print(UtilitasString.balik_kata("Saya suka Python"))           # Python suka Saya
print(UtilitasString.is_palindrom("radar"))                    # True
print(UtilitasString.is_palindrom("python"))                   # False
print(UtilitasString.kapital_setiap_kata("pemrograman berorientasi objek"))
# Pemrograman Berorientasi Objek
print()


# ─────────────────────────────────────────────────────────
# SOAL 4 - Kelas Komprehensif (★★★)
# ─────────────────────────────────────────────────────────
# Buat kelas `AkunBank` yang menggabungkan semuanya:
#
# Atribut KELAS:
#   - `nama_bank` = "Bank Nusantara"
#   - `bunga_tahunan` = 3.5  (persen)
#   - `jumlah_akun` = 0
#
# Atribut INSTANCE: `pemilik`, `nomor_rekening`, `saldo`
#
# Instance Methods:
#   - `setor(jumlah)` -> tambah saldo, cetak konfirmasi
#   - `tarik(jumlah)` -> kurangi saldo (cek cukup!), cetak konfirmasi
#   - `info()` -> cetak ringkasan akun
#
# Class Methods:
#   - `dari_dict(cls, data)` -> factory dari dict {"pemilik", "norek", "saldo"}
#   - `info_bank(cls)` -> cetak nama bank & bunga
#
# Static Methods:
#   - `format_norek(norek)` -> format: "XXXX-XXXX-XXXX" (setiap 4 digit pisah -)
#     Contoh: "123456789012" -> "1234-5678-9012"
#   - `hitung_bunga(saldo, tahun)` -> kembalikan bunga (saldo * bunga% * tahun)
# ─────────────────────────────────────────────────────────

print("--- SOAL 4: Kelas Komprehensif AkunBank ---")


class AkunBank:
    # TODO: Implementasi lengkap di sini
    pass


# Test Soal 4
akun1 = AkunBank("Budi Santoso", "123456789012", 5_000_000)
akun2 = AkunBank.dari_dict({
    "pemilik": "Sari Dewi",
    "norek":   "987654321098",
    "saldo":   10_000_000
})

akun1.info()
# Bank Nusantara | 1234-5678-9012 | Pemilik: Budi Santoso | Saldo: Rp 5,000,000

akun1.setor(2_000_000)
# Setor Rp 2,000,000. Saldo: Rp 7,000,000

akun1.tarik(1_000_000)
# Tarik Rp 1,000,000. Saldo: Rp 6,000,000

AkunBank.info_bank()
# Bank Nusantara | Bunga: 3.5% per tahun

print(AkunBank.format_norek("123456789012"))   # 1234-5678-9012
print(f"Bunga 2 tahun: Rp {AkunBank.hitung_bunga(6_000_000, 2):,.0f}")
# Bunga 2 tahun: Rp 420,000

akun2.info()
print(f"Total akun: {AkunBank.jumlah_akun}")   # Total akun: 2


print("\n" + "=" * 60)
print("  Selesai mengerjakan latihan!")
print("  Jika output sesuai harapan, kamu berhasil! [OK]")
print("=" * 60)
