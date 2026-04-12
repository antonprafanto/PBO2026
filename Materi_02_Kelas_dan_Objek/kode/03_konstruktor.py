"""
==========================================================
    MATERI 02 — Kelas dan Objek
    File: 03_konstruktor.py
    Topik: Pola-Pola Konstruktor __init__
==========================================================

Cara menjalankan:
    python 03_konstruktor.py

Konsep yang dipelajari:
    - Konstruktor dasar
    - Konstruktor dengan nilai default
    - Konstruktor dengan atribut yang dihitung otomatis
    - Konstruktor dengan method privat (_method)
    Note: Validasi dengan raise/try-except dipelajari
          mendalam di Materi 10. Di sini hanya disinggung.
==========================================================
"""

print("=" * 58)
print("       POLA-POLA KONSTRUKTOR __init__")
print("=" * 58)


# ──────────────────────────────────────────────────────────
# BAGIAN 1: KONSTRUKTOR DASAR + VERIFY OTOMATIS BERJALAN
# ──────────────────────────────────────────────────────────
print("\n📌 1. Konstruktor Dasar — Berjalan Otomatis:")
print("-" * 45)

print("""
  Setiap kali Anda menulis: NamaKelas(argumen)
  Python OTOMATIS memanggil __init__ untuk Anda.
  Buktikan dengan print di dalam __init__:
""")

class Titik:
    """Merepresentasikan titik koordinat 2D (x, y)."""

    def __init__(self, x, y):
        print(f"    ⚡ __init__ dipanggil! Membuat Titik({x}, {y})")
        self.x = x
        self.y = y

    def jarak_ke_pusat(self):
        """Hitung jarak ke titik origin (0, 0) dengan Pythagoras."""
        return (self.x**2 + self.y**2) ** 0.5

    def info(self):
        jarak = self.jarak_ke_pusat()
        print(f"  Titik({self.x}, {self.y}) → jarak ke (0,0): {jarak:.2f}")


print("  Membuat 3 objek Titik:")
t1 = Titik(3, 4)    # → jarak = 5.00
t2 = Titik(0, 5)    # → jarak = 5.00
t3 = Titik(6, 8)    # → jarak = 10.00

print()
t1.info()
t2.info()
t3.info()
# Output:
#   ⚡ __init__ dipanggil! Membuat Titik(3, 4)
#   ⚡ __init__ dipanggil! Membuat Titik(0, 5)
#   ⚡ __init__ dipanggil! Membuat Titik(6, 8)
#   Titik(3, 4) → jarak ke (0,0): 5.00
#   Titik(0, 5) → jarak ke (0,0): 5.00
#   Titik(6, 8) → jarak ke (0,0): 10.00


# ──────────────────────────────────────────────────────────
# BAGIAN 2: KONSTRUKTOR DENGAN NILAI DEFAULT
# ──────────────────────────────────────────────────────────
print("\n\n📌 2. Konstruktor dengan Nilai Default:")
print("-" * 45)

class Mahasiswa:
    """Mahasiswa dengan beberapa atribut yang punya nilai default."""

    def __init__(self, nama, nim, semester=1, ipk=0.0, aktif=True):
        """
        Wajib diisi  : nama, nim
        Nilai default: semester=1, ipk=0.0, aktif=True
        """
        self.nama     = nama
        self.nim      = nim
        self.semester = semester
        self.ipk      = ipk
        self.aktif    = aktif

    def info(self):
        status = "Aktif ✅" if self.aktif else "Cuti ⏸️"
        print(f"  {self.nama:<20} | NIM: {self.nim} | "
              f"Sem: {self.semester} | IPK: {self.ipk:.2f} | {status}")


# Berbagai cara membuat objek:
print("  Membuat objek dengan berbagai cara:\n")
mhs1 = Mahasiswa("Andi Rahman",   "2301001")                          # semua default
mhs2 = Mahasiswa("Budi Santoso",  "2301002", semester=3)              # keyword
mhs3 = Mahasiswa("Citra Dewi",    "2301003", 5, 3.75)                 # positional
mhs4 = Mahasiswa("Dono Prasetyo", "2301004", aktif=False)             # hanya aktif
mhs5 = Mahasiswa("Eka Putri",     "2301005", semester=7, ipk=3.90)    # keyword, skip aktif

for mhs in [mhs1, mhs2, mhs3, mhs4, mhs5]:
    mhs.info()
# Output:
#   Andi Rahman          | NIM: 2301001 | Sem: 1 | IPK: 0.00 | Aktif ✅
#   Budi Santoso         | NIM: 2301002 | Sem: 3 | IPK: 0.00 | Aktif ✅
#   Citra Dewi           | NIM: 2301003 | Sem: 5 | IPK: 3.75 | Aktif ✅
#   Dono Prasetyo        | NIM: 2301004 | Sem: 1 | IPK: 0.00 | Cuti ⏸️
#   Eka Putri            | NIM: 2301005 | Sem: 7 | IPK: 3.90 | Aktif ✅


# ──────────────────────────────────────────────────────────
# BAGIAN 3: KONSTRUKTOR DENGAN PERHITUNGAN OTOMATIS
# ──────────────────────────────────────────────────────────
print("\n\n📌 3. Konstruktor dengan Perhitungan Otomatis:")
print("-" * 45)
print("""
  Konstruktor tidak hanya menyimpan data!
  Kita bisa melakukan perhitungan di dalamnya,
  sehingga hasilnya langsung tersedia begitu objek dibuat.
""")

class RaporMahasiswa:
    """
    Menghitung nilai akhir dan grade otomatis
    begitu objek dibuat.
    """

    def __init__(self, nama, nilai_tugas, nilai_uts, nilai_uas):
        # Simpan nilai mentah
        self.nama        = nama
        self.nilai_tugas = nilai_tugas
        self.nilai_uts   = nilai_uts
        self.nilai_uas   = nilai_uas

        # Hitung nilai akhir OTOMATIS di konstruktor
        # Rumus: tugas(30%) + uts(30%) + uas(40%)
        self.nilai_akhir = (nilai_tugas * 0.30) + \
                           (nilai_uts   * 0.30) + \
                           (nilai_uas   * 0.40)

        # Tentukan grade OTOMATIS menggunakan method privat
        self.grade = self._tentukan_grade()

    def _tentukan_grade(self):
        """
        Method 'privat' — konvensi underscore (_) di depan nama
        menandakan method ini hanya untuk digunakan di dalam kelas.
        Dipanggil dari konstruktor, bukan dari luar.
        """
        if self.nilai_akhir >= 85: return "A"
        if self.nilai_akhir >= 75: return "B"
        if self.nilai_akhir >= 65: return "C"
        if self.nilai_akhir >= 55: return "D"
        return "E"

    def tampilkan_rapor(self):
        lebar = 42
        print(f"  {'=' * lebar}")
        print(f"  {'RAPOR MAHASISWA':^{lebar}}")
        print(f"  {'=' * lebar}")
        print(f"  Nama         : {self.nama}")
        print(f"  Nilai Tugas  : {self.nilai_tugas}")
        print(f"  Nilai UTS    : {self.nilai_uts}")
        print(f"  Nilai UAS    : {self.nilai_uas}")
        print(f"  {'-' * lebar}")
        print(f"  Nilai Akhir  : {self.nilai_akhir:.1f}")
        print(f"  Grade        : {self.grade}")
        print(f"  {'=' * lebar}")
        print()


# Buat daftar mahasiswa dan tampilkan rapor semua
daftar_mhs = [
    RaporMahasiswa("Andi Rahman",  85, 80, 90),
    RaporMahasiswa("Budi Santoso", 70, 65, 72),
    RaporMahasiswa("Citra Dewi",   90, 95, 88),
    RaporMahasiswa("Dono Prasetyo",55, 50, 48),
]

print()
for mhs in daftar_mhs:
    mhs.tampilkan_rapor()

# Output:
#   ==========================================
#            RAPOR MAHASISWA
#   ==========================================
#   Nama         : Andi Rahman
#   Nilai Tugas  : 85
#   Nilai UTS    : 80
#   Nilai UAS    : 90
#   ------------------------------------------
#   Nilai Akhir  : 85.5
#   Grade        : A
#   ==========================================
#   ... (dan seterusnya untuk setiap mahasiswa)

# Cari mahasiswa dengan nilai akhir tertinggi
terbaik = max(daftar_mhs, key=lambda m: m.nilai_akhir)
print(f"  🏆 Nilai Akhir Tertinggi: {terbaik.nama} ({terbaik.nilai_akhir:.1f}, Grade {terbaik.grade})")

print("\n✅ Selesai! Kerjakan soal di: latihan.py")
