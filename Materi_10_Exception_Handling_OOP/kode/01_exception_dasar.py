"""
Kode Praktik - Materi 10: Exception Handling OOP
File: 01_exception_dasar.py
Topik: try/except/else/finally, raise, re-raise, exception chaining

Jalankan: python 01_exception_dasar.py
"""

# ======================================================================
# BAGIAN 1: try / except / else / finally -- Alur Dasar
#           Fokus: memahami kapan setiap blok dijalankan
# ======================================================================
print("=" * 60)
print("BAGIAN 1: try / except / else / finally")
print("=" * 60)


def bagi_nilai(pembilang, penyebut):
    """
    Membagi dua angka dengan penanganan exception lengkap.
    Mendemonstrasikan alur try/except/else/finally.
    """
    print(f"\n  Mencoba: {pembilang} / {penyebut}")
    try:
        hasil = pembilang / penyebut
    except ZeroDivisionError:
        print("  [except] ZeroDivisionError: tidak bisa dibagi nol!")
        return None
    except TypeError as e:
        print(f"  [except] TypeError: {e}")
        return None
    else:
        # Hanya dijalankan jika try BERHASIL tanpa exception
        print(f"  [else]   Berhasil! Hasil = {hasil:.4f}")
        return hasil
    finally:
        # SELALU dijalankan, berhasil atau tidak
        print("  [finally] Proses pembagian selesai (cleanup)")


print("\n-- Kasus 1: Pembagian normal --")
bagi_nilai(100, 4)

print("\n-- Kasus 2: Dibagi nol --")
bagi_nilai(100, 0)

print("\n-- Kasus 3: Tipe data salah --")
bagi_nilai("100", 4)

# ======================================================================
# BAGIAN 2: Tangkap Exception Spesifik vs Umum
#           Fokus: urutan except dan tangkap yang tepat
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 2: Tangkap Spesifik vs Umum")
print("=" * 60)


def akses_data_mahasiswa(daftar_mhs, index, field):
    """
    Mengakses data dari daftar mahasiswa.
    Mendemonstrasikan berbagai tipe exception bawaan.
    """
    print(f"\n  Akses daftar[{index}]['{field}']")
    try:
        mahasiswa = daftar_mhs[index]    # bisa IndexError
        nilai     = mahasiswa[field]     # bisa KeyError
        hasil     = int(nilai)           # bisa ValueError
        return hasil
    except IndexError:
        print(f"  [IndexError] Index {index} di luar batas (max: {len(daftar_mhs)-1})")
    except KeyError:
        print(f"  [KeyError] Field '{field}' tidak ada dalam data mahasiswa")
    except ValueError as e:
        print(f"  [ValueError] Tidak bisa konversi ke int: {e}")
    except Exception as e:
        # Jaring pengaman -- tangkap semua yang tidak dikenali
        print(f"  [Exception] Error tidak terduga: {type(e).__name__}: {e}")
    return None


data = [
    {"nim": "2301001", "nama": "Budi",  "ipk": "3.75"},
    {"nim": "2301042", "nama": "Sari",  "ipk": "tiga koma enam"},   # nilai bermasalah
]

print("\n-- Akses valid --")
akses_data_mahasiswa(data, 0, "nim")

print("\n-- IndexError: index terlalu besar --")
akses_data_mahasiswa(data, 5, "nim")

print("\n-- KeyError: field tidak ada --")
akses_data_mahasiswa(data, 0, "nilai_uts")

print("\n-- ValueError: tidak bisa konversi --")
akses_data_mahasiswa(data, 1, "ipk")

# ======================================================================
# BAGIAN 3: raise dan re-raise
#           Fokus: melempar exception dari kode sendiri
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 3: raise dan re-raise")
print("=" * 60)


def validasi_nim(nim):
    """Memvalidasi format NIM mahasiswa Unmul (7 digit angka)."""
    if not isinstance(nim, str):
        raise TypeError(f"NIM harus berupa string, bukan {type(nim).__name__}")
    if not nim.isdigit():
        raise ValueError(f"NIM hanya boleh berisi angka, bukan '{nim}'")
    if len(nim) != 7:
        raise ValueError(f"NIM harus 7 digit, '{nim}' memiliki {len(nim)} karakter")
    return True


def validasi_ipk(ipk):
    """Memvalidasi nilai IPK (0.00 - 4.00)."""
    if not isinstance(ipk, (int, float)):
        raise TypeError(f"IPK harus berupa angka, bukan {type(ipk).__name__}")
    if not (0.0 <= float(ipk) <= 4.0):
        raise ValueError(f"IPK harus antara 0.00-4.00, bukan {ipk}")
    return True


def daftar_mahasiswa_baru(nim, nama, ipk):
    """
    Mendaftarkan mahasiswa baru.
    Mendemonstrasikan penggunaan raise dan re-raise.
    """
    print(f"\n  Mendaftarkan: NIM={nim}, Nama={nama}, IPK={ipk}")
    try:
        validasi_nim(nim)
        validasi_ipk(ipk)
        print(f"  [OK] Mahasiswa '{nama}' berhasil didaftarkan")
        return {"nim": nim, "nama": nama, "ipk": ipk}
    except (TypeError, ValueError) as e:
        print(f"  [GAGAL] Validasi gagal: {e}")
        # Re-raise: log dulu, baru teruskan
        print(f"  [LOG] Exception diteruskan ke pemanggil")
        raise


# --- Demo raise ---
print("\n-- NIM valid dan IPK valid --")
try:
    daftar_mahasiswa_baru("2301001", "Budi Santoso", 3.75)
except (TypeError, ValueError):
    pass

print("\n-- NIM terlalu pendek --")
try:
    daftar_mahasiswa_baru("230", "Sari Dewi", 3.50)
except ValueError as e:
    print(f"  [Tertangkap di luar] {e}")

print("\n-- IPK melebihi batas --")
try:
    daftar_mahasiswa_baru("2301099", "Ahmad", 4.5)
except ValueError as e:
    print(f"  [Tertangkap di luar] {e}")

print("\n-- NIM bukan string --")
try:
    daftar_mahasiswa_baru(2301001, "Budi", 3.75)   # int bukan string
except TypeError as e:
    print(f"  [Tertangkap di luar] {e}")

# ======================================================================
# BAGIAN 4: Exception Chaining -- raise E from original
#           Fokus: memberikan konteks penuh saat exception terjadi
#                  akibat exception lain
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 4: Exception Chaining")
print("=" * 60)


class KonfigurasiError(Exception):
    """Exception untuk masalah konfigurasi sistem."""
    pass


def muat_konfigurasi(path):
    """Memuat konfigurasi dari file. Simulasi: file tidak ada."""
    try:
        # Simulasi: kita anggap FileNotFoundError terjadi
        raise FileNotFoundError(f"File '{path}' tidak ditemukan")
    except FileNotFoundError as e:
        # Bungkus dalam exception domain kita, tapi simpan konteks aslinya
        raise KonfigurasiError(
            f"Gagal memuat konfigurasi dari '{path}'"
        ) from e


def inisialisasi_sistem():
    """Menginisialisasi sistem akademik."""
    try:
        muat_konfigurasi("config/akademik.json")
    except KonfigurasiError as e:
        # Exception chaining memungkinkan kita lihat KEDUA exception
        raise RuntimeError("Sistem akademik tidak bisa diinisialisasi") from e


print("\n-- Demo exception chaining --")
try:
    inisialisasi_sistem()
except RuntimeError as e:
    print(f"  [RuntimeError] {e}")
    # Akses exception asal via __cause__
    if e.__cause__:
        print(f"  [Penyebab] {type(e.__cause__).__name__}: {e.__cause__}")
    if e.__cause__ and e.__cause__.__cause__:
        print(f"  [Asal]     {type(e.__cause__.__cause__).__name__}: "
              f"{e.__cause__.__cause__}")

# ======================================================================
# BAGIAN 5: finally dalam Manajemen Resource
#           Fokus: memastikan cleanup selalu berjalan
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 5: finally untuk Manajemen Resource")
print("=" * 60)


class SimulasiKoneksiDB:
    """Simulasi koneksi database untuk demo finally."""

    def __init__(self, nama):
        self.nama    = nama
        self.terbuka = False

    def buka(self):
        self.terbuka = True
        print(f"  [DB] Koneksi ke '{self.nama}' dibuka")

    def tutup(self):
        self.terbuka = False
        print(f"  [DB] Koneksi ke '{self.nama}' ditutup")

    def query(self, sql):
        if not self.terbuka:
            raise RuntimeError("Koneksi belum dibuka!")
        if "DROP" in sql.upper():
            raise PermissionError(f"Query '{sql}' tidak diizinkan!")
        print(f"  [DB] Query dieksekusi: {sql}")
        return [{"nim": "2301001", "nama": "Budi"}]


def jalankan_query(sql):
    """Menjalankan query dengan jaminan koneksi selalu ditutup."""
    db = SimulasiKoneksiDB("akademik.db")
    db.buka()
    try:
        hasil = db.query(sql)
        return hasil
    except PermissionError as e:
        print(f"  [GAGAL] {e}")
        return None
    finally:
        db.tutup()   # SELALU ditutup, meski ada exception


print("\n-- Query normal --")
hasil = jalankan_query("SELECT * FROM mahasiswa")
print(f"  Hasil: {hasil}")

print("\n-- Query berbahaya (PermissionError) --")
hasil = jalankan_query("DROP TABLE mahasiswa")
print(f"  Hasil: {hasil}")

print()
print("Selesai! Semua bagian dijalankan tanpa error.")
