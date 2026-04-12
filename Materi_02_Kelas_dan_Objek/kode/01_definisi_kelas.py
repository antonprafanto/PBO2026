"""
==========================================================
    MATERI 02 — Kelas dan Objek
    File: 01_definisi_kelas.py
    Topik: Sintaks Lengkap Mendefinisikan Kelas
==========================================================
"""

print("=" * 55)
print("      DEFINISI KELAS — SINTAKS LENGKAP")
print("=" * 55)

# ──────────────────────────────────────────────────────────
# BAGIAN 1: KELAS DENGAN KONSTRUKTOR WAJIB
# ──────────────────────────────────────────────────────────
print("\n📌 1. Kelas dengan Konstruktor Wajib:")
print("-" * 40)

class MataKuliah:
    """Merepresentasikan sebuah mata kuliah di universitas."""

    def __init__(self, kode, nama, sks, dosen):
        """
        Parameter:
            kode  (str): Kode mata kuliah, contoh: 'IF301'
            nama  (str): Nama mata kuliah
            sks   (int): Jumlah SKS
            dosen (str): Nama dosen pengampu
        """
        self.kode  = kode
        self.nama  = nama
        self.sks   = sks
        self.dosen = dosen

    def info(self):
        """Menampilkan informasi lengkap mata kuliah."""
        print(f"  [{self.kode}] {self.nama}")
        print(f"        SKS   : {self.sks}")
        print(f"        Dosen : {self.dosen}")

mk1 = MataKuliah("IF301", "Pemrograman Berorientasi Objek", 3, "Anton Prafanto, M.Kom")
mk2 = MataKuliah("IF302", "Basis Data", 3, "Dr. Siti Rahayu")
mk3 = MataKuliah("IF303", "Jaringan Komputer", 2, "Andi Wijaya, M.T")

for mk in [mk1, mk2, mk3]:
    mk.info()
    print()


# ──────────────────────────────────────────────────────────
# BAGIAN 2: KONSTRUKTOR DENGAN NILAI DEFAULT
# ──────────────────────────────────────────────────────────
print("\n📌 2. Konstruktor dengan Nilai Default:")
print("-" * 40)

class Mahasiswa:
    """Merepresentasikan mahasiswa dengan nilai default tertentu."""
    
    def __init__(self, nama, nim, semester=1, aktif=True):
        """
        'semester' dan 'aktif' memiliki nilai default,
        sehingga tidak wajib diisi saat membuat objek.
        """
        self.nama     = nama
        self.nim      = nim
        self.semester = semester
        self.aktif    = aktif
        self.ipk      = 0.0  # IPK awal selalu 0

    def info(self):
        status = "✅ Aktif" if self.aktif else "❌ Tidak Aktif"
        print(f"  {self.nama} ({self.nim}) | Sem: {self.semester} | {status} | IPK: {self.ipk:.2f}")

# Berbagai cara membuat objek
mhs1 = Mahasiswa("Andi Rahman",  "2301001")              # pakai semua default
mhs2 = Mahasiswa("Budi Santoso", "2301002", semester=3)  # semester diisi
mhs3 = Mahasiswa("Citra Dewi",   "2301003", 5, True)     # semua diisi
mhs4 = Mahasiswa("Dono Prasetyo","2301004", aktif=False) # hanya aktif diubah

for mhs in [mhs1, mhs2, mhs3, mhs4]:
    mhs.info()


# ──────────────────────────────────────────────────────────
# BAGIAN 3: MENGAKSES DAN MENGUBAH ATRIBUT
# ──────────────────────────────────────────────────────────
print("\n\n📌 3. Mengakses dan Mengubah Atribut:")
print("-" * 40)

mhs = Mahasiswa("Eko Prasetyo", "2301005", 4)
print(f"  Sebelum: {mhs.nama} | Semester: {mhs.semester} | IPK: {mhs.ipk}")

# Mengubah atribut langsung
mhs.ipk      = 3.75    # update IPK setelah ujian
mhs.semester = 5        # naik semester
print(f"  Sesudah: {mhs.nama} | Semester: {mhs.semester} | IPK: {mhs.ipk}")


# ──────────────────────────────────────────────────────────
# BAGIAN 4: OBJEK SEBAGAI PARAMETER DAN RETURN VALUE
# ──────────────────────────────────────────────────────────
print("\n\n📌 4. Objek sebagai Parameter dan Return Value:")
print("-" * 40)

def bandingkan_ipk(mhs_a, mhs_b):
    """Menerima dua objek Mahasiswa dan membandingkan IPK-nya."""
    if mhs_a.ipk > mhs_b.ipk:
        return mhs_a
    elif mhs_b.ipk > mhs_a.ipk:
        return mhs_b
    else:
        return None  # seri

def buat_mahasiswa_baru(nama, nim):
    """Membuat dan mengembalikan objek Mahasiswa baru."""
    return Mahasiswa(nama, nim)  # return objek!

a = buat_mahasiswa_baru("Fatma", "2301006")
b = buat_mahasiswa_baru("Galih", "2301007")
a.ipk = 3.85
b.ipk = 3.60

terbaik = bandingkan_ipk(a, b)
print(f"  IPK tertinggi: {terbaik.nama} dengan IPK {terbaik.ipk}")

print("\n✅ Selesai! Lanjut ke: 02_banyak_objek.py")
