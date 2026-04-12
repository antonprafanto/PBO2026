"""
============================================================
    MATERI 04 - Enkapsulasi
    File: latihan.py
    Topik: Soal Latihan Mandiri

PETUNJUK:
  - Kerjakan setiap soal di bagian yang sudah disediakan.
  - Jalankan file ini untuk melihat output:
      python latihan.py
  - Jika output sesuai dengan yang diharapkan, jawabanmu BENAR!
============================================================
"""

print("=" * 60)
print("         LATIHAN MANDIRI - MATERI 04")
print("         Enkapsulasi")
print("=" * 60)


# ─────────────────────────────────────────────────────────────
# SOAL 1 - Public, Protected, Private (Tingkat: bintang-1)
# ─────────────────────────────────────────────────────────────
# Buat kelas `Kendaraan` dengan:
#   - Atribut PUBLIC   : `merk`, `warna`
#   - Atribut PROTECTED: `_tahun_produksi`
#   - Atribut PRIVATE  : `__nomor_rangka`
#
#   - Method:
#       info_publik() -> cetak merk dan warna
#       tahun()       -> kembalikan _tahun_produksi (getter biasa)
#       cek_rangka(kode) -> True jika kode == __nomor_rangka
#
# Pastikan __nomor_rangka TIDAK bisa diakses langsung dari luar.
# ─────────────────────────────────────────────────────────────

print("\n--- SOAL 1: Public, Protected, Private ---")


class Kendaraan:
    def __init__(self, merk, warna, tahun_produksi, nomor_rangka):
        # TODO: definisikan atribut dengan tingkat akses yang benar
        pass

    def info_publik(self):
        # TODO: cetak "Merk: [merk] | Warna: [warna]"
        pass

    def tahun(self):
        # TODO: kembalikan _tahun_produksi
        pass

    def cek_rangka(self, kode):
        # TODO: kembalikan True jika kode cocok dengan __nomor_rangka
        pass


# Test Soal 1
mobil = Kendaraan("Honda Jazz", "Merah", 2022, "MHF-123456")
mobil.info_publik()              # Merk: Honda Jazz | Warna: Merah
print(mobil.tahun())             # 2022
print(mobil.cek_rangka("MHF-123456"))   # True
print(mobil.cek_rangka("XYZ-000"))      # False

try:
    _ = mobil.__nomor_rangka     # harus AttributeError
    print("SALAH: seharusnya AttributeError!")
except AttributeError:
    print("Perlindungan private berhasil!")   # ini yang diharapkan
print()


# ─────────────────────────────────────────────────────────────
# SOAL 2 - @property dan @setter dengan Validasi (Tingkat: bintang-2)
# ─────────────────────────────────────────────────────────────
# Buat kelas `Pegawai` dengan property dan validasi:
#
#   Atribut private: __nama, __nip, __gaji
#
#   Property `nama`:
#     - getter: kembalikan nama
#     - setter: harus string, minimal 3 karakter, auto-title-case
#
#   Property `nip`:
#     - getter: kembalikan nip
#     - setter: harus 18 digit angka (standar PNS Indonesia)
#
#   Property `gaji`:
#     - getter: kembalikan gaji
#     - setter: harus antara 2.000.000 dan 50.000.000
#
#   Computed property:
#     - `gaji_bersih`: gaji dikurangi pajak 5% jika gaji > 8.000.000,
#                      jika tidak maka dikurangi 0% (tidak kena pajak)
#     - `golongan`: "Junior" jika gaji < 5jt, "Menengah" 5-15jt,
#                   "Senior" jika > 15jt
#
#   Method: __str__: "[nip] [nama] | Rp [gaji] (bersih: Rp [gaji_bersih]) | [golongan]"
# ─────────────────────────────────────────────────────────────

print("--- SOAL 2: @property dan @setter ---")


class Pegawai:
    def __init__(self, nama, nip, gaji):
        # TODO: Inisialisasi dan gunakan setter untuk validasi
        pass

    @property
    def nama(self):
        pass  # TODO

    @nama.setter
    def nama(self, nilai):
        pass  # TODO: validasi string, min 3 karakter, title-case

    @property
    def nip(self):
        pass  # TODO

    @nip.setter
    def nip(self, nilai):
        pass  # TODO: validasi 18 digit angka

    @property
    def gaji(self):
        pass  # TODO

    @gaji.setter
    def gaji(self, nilai):
        pass  # TODO: validasi 2.000.000 - 50.000.000

    @property
    def gaji_bersih(self):
        pass  # TODO: potong 5% jika gaji > 8jt

    @property
    def golongan(self):
        pass  # TODO: Junior/Menengah/Senior berdasarkan gaji

    def __str__(self):
        pass  # TODO: format lengkap


# Test Soal 2
p1 = Pegawai("  budi santoso  ", "198501012010011001", 12_000_000)
p2 = Pegawai("Sari Dewi",       "199203152015012002",  4_500_000)
print(p1)
# [198501012010011001] Budi Santoso | Rp 12,000,000 (bersih: Rp 11,400,000) | Menengah
print(p2)
# [199203152015012002] Sari Dewi | Rp 4,500,000 (bersih: Rp 4,500,000) | Junior

print("\nUji validasi:")
try:
    p1.gaji = 100_000_000
except ValueError as e:
    print(f"  Gaji terlalu besar: {e}")

try:
    p1.nip = "123"
except ValueError as e:
    print(f"  NIP tidak valid: {e}")

try:
    p1.nama = "Ab"
except ValueError as e:
    print(f"  Nama terlalu pendek: {e}")
print()


# ─────────────────────────────────────────────────────────────
# SOAL 3 - Read-Only Property & Computed Value (Tingkat: bintang-2)
# ─────────────────────────────────────────────────────────────
# Buat kelas `Lingkaran` dengan:
#   - Atribut private: __jari_jari
#   - Property `jari_jari` dengan setter (harus > 0)
#   - Computed properties (READ-ONLY, tidak ada setter):
#       * `diameter`:   2 * jari_jari
#       * `keliling`:   2 * pi * jari_jari
#       * `luas`:       pi * jari_jari^2
#       * `kategori`:   "Kecil" jika r<=5, "Sedang" 5<r<=20, "Besar" jika >20
#   - Method __str__: tampilkan semua ukuran dalam 2 desimal
#
# PETUNJUK: gunakan import math dan math.pi
# ─────────────────────────────────────────────────────────────

print("--- SOAL 3: Read-Only Computed Property ---")
import math


class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari   # gunakan setter

    @property
    def jari_jari(self):
        pass  # TODO

    @jari_jari.setter
    def jari_jari(self, nilai):
        pass  # TODO: validasi harus > 0

    @property
    def diameter(self):
        pass  # TODO

    @property
    def keliling(self):
        pass  # TODO

    @property
    def luas(self):
        pass  # TODO

    @property
    def kategori(self):
        pass  # TODO

    def __str__(self):
        pass  # TODO


# Test Soal 3
l1 = Lingkaran(7)
l2 = Lingkaran(25)
print(l1)
# r=7 | d=14.00 | keliling=43.98 | luas=153.94 | Sedang
print(l2)
# r=25 | d=50.00 | keliling=157.08 | luas=1963.50 | Besar

l1.jari_jari = 3
print(f"Setelah ubah r=3: {l1}")
# r=3 | d=6.00 | keliling=18.85 | luas=28.27 | Kecil

# Pastikan computed property tidak bisa diubah langsung
try:
    l1.luas = 100   # harus AttributeError
    print("SALAH: seharusnya AttributeError!")
except AttributeError:
    print("Read-only property terlindungi!")
print()


# ─────────────────────────────────────────────────────────────
# SOAL 4 - Enkapsulasi Penuh: Sistem Nilai Akademik (Tingkat: bintang-3)
# ─────────────────────────────────────────────────────────────
# Buat kelas `NilaiMataKuliah` yang menyimpan nilai UTS, UAS, Tugas:
#
#   Atribut private: __uts, __uas, __tugas, __nama_mk, __sks
#
#   Property dengan setter dan validasi untuk MASING-MASING:
#     - `uts`, `uas`, `tugas` : nilai 0-100 (float/int)
#     - `nama_mk`             : string, tidak boleh kosong
#     - `sks`                 : integer, 1-4
#
#   Computed properties (READ-ONLY):
#     - `nilai_akhir`: (UTS*30% + UAS*40% + Tugas*30%)
#     - `nilai_huruf`: A(>=85), B+(>=80), B(>=75), B-(>=70),
#                      C+(>=65), C(>=55), D(>=40), E(<40)
#     - `bobot`:       A=4.0, B+=3.3, B=3.0, B-=2.7, C+=2.3,
#                      C=2.0, D=1.0, E=0.0
#     - `lulus`:       True jika nilai_huruf bukan D atau E
#
#   Method:
#     - __str__: "[nama_mk] ([sks] SKS) | UTS:[uts] UAS:[uas] Tgs:[tugas]
#                 -> [nilai_akhir:.1f] [nilai_huruf] ([bobot]) - [LULUS/TIDAK LULUS]"
# ─────────────────────────────────────────────────────────────

print("--- SOAL 4: Sistem Nilai Akademik ---")


class NilaiMataKuliah:
    _SKALA_HURUF = [
        (85, "A",  4.0),
        (80, "B+", 3.3),
        (75, "B",  3.0),
        (70, "B-", 2.7),
        (65, "C+", 2.3),
        (55, "C",  2.0),
        (40, "D",  1.0),
        (0,  "E",  0.0),
    ]

    def __init__(self, nama_mk, sks, uts, uas, tugas):
        # TODO: Inisialisasi dan gunakan setter
        pass

    # TODO: Implementasi semua property dan method


# Test Soal 4
mk1 = NilaiMataKuliah("Pemrograman Berorientasi Objek", 3, 85, 88, 90)
mk2 = NilaiMataKuliah("Kalkulus",                       2, 40, 45, 50)
mk3 = NilaiMataKuliah("Basis Data",                     3, 70, 75, 80)

for mk in [mk1, mk2, mk3]:
    print(f"  {mk}")
# Pemrograman Berorientasi Objek (3 SKS) | UTS:85 UAS:88 Tgs:90 -> 87.7 A (4.0) - LULUS
# Kalkulus (2 SKS) | UTS:40 UAS:45 Tgs:50 -> 45.0 D (1.0) - TIDAK LULUS
# Basis Data (3 SKS) | UTS:70 UAS:75 Tgs:80 -> 75.5 B+ (3.3) - LULUS

# Hitung IPK dari daftar mata kuliah (bonus)
mk_list = [mk1, mk2, mk3]
total_bobot_sks = sum(mk.bobot * mk.sks for mk in mk_list)
total_sks       = sum(mk.sks for mk in mk_list)
ipk             = total_bobot_sks / total_sks
print(f"\n  IPK dari ketiga mata kuliah: {ipk:.2f}")

# Uji validasi
print("\n  Uji validasi:")
try:
    mk1.uts = 101
except ValueError as e:
    print(f"  Nilai >100: {e}")

try:
    mk1.sks = 5
except ValueError as e:
    print(f"  SKS >4: {e}")
print()


print("\n" + "=" * 60)
print("  Selesai mengerjakan latihan!")
print("  Cocokkan outputmu dengan komentar di setiap soal.")
print("=" * 60)
