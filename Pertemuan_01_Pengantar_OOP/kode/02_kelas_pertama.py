"""
==========================================================
    PERTEMUAN 01 — Pengantar OOP
    File: 02_kelas_pertama.py
    Topik: Membuat Kelas dan Objek Pertama
==========================================================

Cara menjalankan:
    python 02_kelas_pertama.py

Setelah file ini, kerjakan: latihan.py
==========================================================
"""

print("=" * 55)
print("     MEMBUAT KELAS DAN OBJEK PERTAMA")
print("=" * 55)

# ──────────────────────────────────────────────────────────
# BAGIAN 1: KELAS PALING SEDERHANA
# ──────────────────────────────────────────────────────────
print("\n📌 1. Kelas Sederhana (tanpa apapun):")
print("-" * 40)

class Hewan:
    pass  # 'pass' = badan kelas kosong, tapi kode tetap valid

# Membuat objek dari kelas kosong
kucing = Hewan()
print(f"  Tipe kucing : {type(kucing)}")
print(f"  Apakah Hewan? {isinstance(kucing, Hewan)}")
# Output:
#   Tipe kucing : <class '__main__.Hewan'>
#   Apakah Hewan? True


# ──────────────────────────────────────────────────────────
# BAGIAN 2: ANATOMI LENGKAP SEBUAH KELAS
# ──────────────────────────────────────────────────────────
print("\n\n📌 2. Anatomi Lengkap Kelas:")
print("-" * 40)

class Motor:
    """
    DOCSTRING — penjelasan kelas ini.
    Kelas Motor merepresentasikan sebuah kendaraan bermotor.
    """

    # ── KONSTRUKTOR (__init__) ──────────────────────────
    def __init__(self, merk, warna, tahun):
        """
        __init__ adalah KONSTRUKTOR:
        - Dijalankan OTOMATIS setiap kali objek baru dibuat
        - 'self' selalu menjadi parameter PERTAMA
        - Fungsi: inisialisasi atribut objek
        """
        self.merk       = merk    # atribut instance
        self.warna      = warna   # atribut instance
        self.tahun      = tahun   # atribut instance
        self.kecepatan  = 0       # atribut dengan nilai default

    # ── METHOD ─────────────────────────────────────────
    def info(self):
        """Menampilkan informasi motor."""
        print(f"  Motor : {self.merk}")
        print(f"  Warna : {self.warna} | Tahun: {self.tahun}")
        print(f"  Kecepatan saat ini: {self.kecepatan} km/jam")

    def gas(self, tambah_kecepatan):
        """Menambah kecepatan motor."""
        self.kecepatan += tambah_kecepatan
        print(f"  ▶ {self.merk} melaju → {self.kecepatan} km/jam")

    def rem(self):
        """Menghentikan motor."""
        self.kecepatan = 0
        print(f"  ■ {self.merk} berhenti.")


# ── Membuat dan menggunakan objek ────────────────────────
motor1 = Motor("Honda Vario", "Merah", 2023)
motor2 = Motor("Yamaha NMAX", "Hitam", 2024)

print("  --- Motor 1 ---")
motor1.info()
motor1.gas(30)
motor1.gas(20)
motor1.rem()

print()
print("  --- Motor 2 ---")
motor2.info()
motor2.gas(50)
# Output:
#   --- Motor 1 ---
#   Motor : Honda Vario
#   Warna : Merah | Tahun: 2023
#   Kecepatan saat ini: 0 km/jam
#   ▶ Honda Vario melaju → 30 km/jam
#   ▶ Honda Vario melaju → 50 km/jam
#   ■ Honda Vario berhenti.
#
#   --- Motor 2 ---
#   Motor : Yamaha NMAX
#   Warna : Hitam | Tahun: 2024
#   Kecepatan saat ini: 0 km/jam
#   ▶ Yamaha NMAX melaju → 50 km/jam


# ──────────────────────────────────────────────────────────
# BAGIAN 3: MEMAHAMI 'self' SECARA MENDALAM
# ──────────────────────────────────────────────────────────
print("\n\n📌 3. Memahami 'self' — Dibuktikan dengan Kode:")
print("-" * 40)

# Penjelasan konsep:
print("""
  'self' merujuk ke objek yang SEDANG memanggil method.
  
  Ketika kita tulis:  motor1.info()
  Python sebenarnya:  Motor.info(motor1)
                                  ▲
                          inilah 'self' di dalam method!
""")

# BUKTI NYATA — kedua baris ini menghasilkan output yang SAMA PERSIS:
print("  [Cara 1 - normal]    motor1.info():")
motor1.info()

print("\n  [Cara 2 - eksplisit] Motor.info(motor1):")
Motor.info(motor1)
# Kedua cara ini identik! Python menerjemahkan cara 1 → cara 2

# Mengapa perlu self? Karena ada BANYAK objek dari 1 kelas:
print("\n  Mengapa perlu 'self'? Karena ada banyak objek:")
print(f"    motor1.merk = {motor1.merk}")   # Merah → milik motor1
print(f"    motor2.merk = {motor2.merk}")   # Hitam → milik motor2
# 'self' memastikan setiap objek mengakses DATA MILIKNYA SENDIRI


# ──────────────────────────────────────────────────────────
# BAGIAN 4: SETIAP OBJEK BERDIRI SENDIRI (INDEPENDEN)
# ──────────────────────────────────────────────────────────
print("\n\n📌 4. Setiap Objek Berdiri Sendiri (Independen):")
print("-" * 40)

class Mahasiswa:
    """Kelas untuk mahasiswa — digunakan sebagai contoh independensi."""

    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim  = nim
        self.ipk  = ipk

    def info(self):
        print(f"  {self.nama} ({self.nim}) → IPK: {self.ipk:.2f}")

mhs_a = Mahasiswa("Andi Prasetyo", "2301001", 3.80)
mhs_b = Mahasiswa("Budi Santoso",  "2301002", 3.20)
mhs_c = Mahasiswa("Citra Dewi",    "2301003", 3.55)

print("  Sebelum perubahan:")
for mhs in [mhs_a, mhs_b, mhs_c]:
    mhs.info()

# Ubah IPK mhs_a — TIDAK mempengaruhi mhs_b dan mhs_c
mhs_a.ipk = 3.95

print("\n  Setelah mhs_a.ipk diubah menjadi 3.95:")
for mhs in [mhs_a, mhs_b, mhs_c]:
    mhs.info()
# Output: hanya mhs_a yang berubah, lainnya tetap

print(f"\n  Apakah mhs_a dan mhs_b objek yang sama? {mhs_a is mhs_b}")
# Output: False → masing-masing punya ruang memori sendiri


# ──────────────────────────────────────────────────────────
# BAGIAN 5: MENGECEK TIPE DAN IDENTITAS OBJEK
# ──────────────────────────────────────────────────────────
print("\n\n📌 5. Mengecek Tipe dan Identitas Objek:")
print("-" * 40)

print(f"  type(mhs_a)                     = {type(mhs_a)}")
print(f"  isinstance(mhs_a, Mahasiswa)    = {isinstance(mhs_a, Mahasiswa)}")
print(f"  isinstance(mhs_a, Motor)        = {isinstance(mhs_a, Motor)}")
print(f"  id(mhs_a)                       = {id(mhs_a)}  ← alamat memori")
print(f"  id(mhs_b)                       = {id(mhs_b)}  ← alamat berbeda!")
# Output:
#   type(mhs_a)                     = <class '__main__.Mahasiswa'>
#   isinstance(mhs_a, Mahasiswa)    = True
#   isinstance(mhs_a, Motor)        = False
#   id(mhs_a)                       = 2093819... ← (angka bervariasi)
#   id(mhs_b)                       = 2093819... ← (beda dengan mhs_a)

print("\n✅ Selesai! Lanjut kerjakan soal di: latihan.py")
