"""
============================================================
    MATERI 04 - Enkapsulasi
    File: 02_property.py
    Topik: @property, @setter, @deleter secara Lengkap
============================================================
"""

print("=" * 58)
print("  MATERI 04 - Enkapsulasi")
print("  02_property.py")
print("=" * 58)


# ------------------------------------------------------------
# BAGIAN 1: @property dasar (getter read-only)
# ------------------------------------------------------------

print("\n--- 1. @property Dasar (Read-Only) ---")


class Suhu:
    """Kelas yang menyimpan suhu dalam Celsius dan otomatis
    mengkonversi ke Fahrenheit dan Kelvin via property."""

    def __init__(self, celsius):
        self.celsius = celsius   # akan melalui setter

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, nilai):
        if nilai < -273.15:
            raise ValueError(f"Suhu tidak bisa di bawah nol mutlak! Dapat: {nilai}")
        self.__celsius = nilai

    # Computed properties - selalu sinkron dengan celsius
    @property
    def fahrenheit(self):
        return self.__celsius * 9 / 5 + 32

    @property
    def kelvin(self):
        return self.__celsius + 273.15

    @property
    def deskripsi(self):
        if self.__celsius < 0:    return "Beku"
        if self.__celsius < 20:   return "Dingin"
        if self.__celsius < 30:   return "Sejuk"
        if self.__celsius < 37:   return "Hangat"
        return "Panas"

    def __str__(self):
        return (f"{self.__celsius:.1f}C = {self.fahrenheit:.1f}F "
                f"= {self.kelvin:.2f}K ({self.deskripsi})")


suhu_ruang  = Suhu(25)
suhu_beku   = Suhu(0)
suhu_tubuh  = Suhu(36.6)

for s in [suhu_ruang, suhu_beku, suhu_tubuh]:
    print(f"  {s}")

# Ubah celsius - fahrenheit/kelvin otomatis update
suhu_ruang.celsius = 40
print(f"\nSetelah diubah ke 40C: {suhu_ruang}")

# Validasi
try:
    suhu_ruang.celsius = -300
except ValueError as e:
    print(f"Error: {e}")


# ------------------------------------------------------------
# BAGIAN 2: @property + @setter dengan Validasi Lengkap
# ------------------------------------------------------------

print("\n--- 2. @property + @setter dengan Validasi ---")


class Mahasiswa:
    """Mahasiswa dengan enkapsulasi penuh pada semua atribut."""

    def __init__(self, nama, nim, ipk, semester):
        # Panggil setter agar validasi berjalan dari konstruktor
        self.__nama     = ""
        self.__nim      = ""
        self.__ipk      = 0.0
        self.__semester = 0
        self.nama       = nama
        self.nim        = nim
        self.ipk        = ipk
        self.semester   = semester

    # ---- NAMA -----------------------------------------------
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nilai):
        if not isinstance(nilai, str):
            raise TypeError("Nama harus berupa string!")
        nilai = nilai.strip().title()
        if len(nilai) < 2:
            raise ValueError("Nama minimal 2 karakter!")
        self.__nama = nilai

    # ---- NIM ------------------------------------------------
    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, nilai):
        nilai = str(nilai).strip()
        if not nilai.isdigit() or len(nilai) != 7:
            raise ValueError(f"NIM harus 7 digit angka! Dapat: '{nilai}'")
        self.__nim = nilai

    # ---- IPK ------------------------------------------------
    @property
    def ipk(self):
        return self.__ipk

    @ipk.setter
    def ipk(self, nilai):
        if not isinstance(nilai, (int, float)):
            raise TypeError("IPK harus angka!")
        if not 0.0 <= nilai <= 4.0:
            raise ValueError(f"IPK harus 0.0-4.0! Dapat: {nilai}")
        self.__ipk = round(float(nilai), 2)

    # ---- SEMESTER -------------------------------------------
    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, nilai):
        if not isinstance(nilai, int) or not 1 <= nilai <= 14:
            raise ValueError(f"Semester harus 1-14! Dapat: {nilai}")
        self.__semester = nilai

    # ---- Computed Properties --------------------------------
    @property
    def predikat(self):
        if self.__ipk >= 3.51: return "Cum Laude"
        if self.__ipk >= 3.01: return "Sangat Memuaskan"
        if self.__ipk >= 2.76: return "Memuaskan"
        if self.__ipk >= 2.00: return "Cukup"
        return "Di Bawah Standar"

    @property
    def tahun_masuk(self):
        """Estimasi tahun masuk dari NIM (2 digit pertama = angkatan)."""
        return 2000 + int(self.__nim[:2])

    def __str__(self):
        return (f"[{self.nim}] {self.nama} | "
                f"Sem {self.semester} | IPK {self.ipk:.2f} ({self.predikat})")


# Penggunaan normal
mhs1 = Mahasiswa("budi santoso", "2301001", 3.80, 5)
mhs2 = Mahasiswa("  sari dewi  ", "2301002", 3.20, 3)

print(f"{mhs1}")
print(f"{mhs2}")
print(f"Tahun masuk mhs1: {mhs1.tahun_masuk}")   # 2023

# Perubahan via setter
mhs1.ipk = 3.95
print(f"\nSetelah naik IPK: {mhs1}")

# Uji validasi
print("\nUji validasi:")
kasus = [
    ("ipk",      5.0,   "IPK terlalu tinggi"),
    ("ipk",      -1,    "IPK negatif"),
    ("semester", 0,     "Semester nol"),
    ("semester", 15,    "Semester terlalu besar"),
    ("nim",      "abc", "NIM bukan angka"),
    ("nama",     "X",   "Nama terlalu pendek"),
]
for attr, nilai, deskripsi in kasus:
    try:
        setattr(mhs1, attr, nilai)
        print(f"  {deskripsi}: LOLOS (harusnya error!)")
    except (ValueError, TypeError) as e:
        print(f"  {deskripsi}: Tertangkap -> {e}")


# ------------------------------------------------------------
# BAGIAN 3: @deleter
# ------------------------------------------------------------

print("\n--- 3. @deleter ---")


class Sesi:
    """Mengelola sesi login pengguna."""

    def __init__(self, username):
        self.__username   = username
        self.__token      = self._buat_token()
        self.__aktif      = True

    def _buat_token(self):
        import random
        return f"TKN-{random.randint(100000, 999999)}"

    @property
    def username(self):
        return self.__username

    @property
    def token(self):
        if not self.__aktif:
            return None
        return self.__token

    @property
    def aktif(self):
        return self.__aktif

    @token.deleter
    def token(self):
        """Logout: hapus token dan tandai sesi tidak aktif."""
        print(f"Sesi {self.__username} diakhiri. Token dicabut.")
        self.__token  = None
        self.__aktif  = False

    def __str__(self):
        status = "AKTIF" if self.__aktif else "TIDAK AKTIF"
        return f"Sesi [{self.__username}] | {status} | Token: {self.token}"


sesi = Sesi("budi_admin")
print(f"Login  : {sesi}")

del sesi.token   # logout

print(f"Logout : {sesi}")
print(f"Token  : {sesi.token}")   # None


# ------------------------------------------------------------
# BAGIAN 4: Property dengan Caching (Optimasi)
# ------------------------------------------------------------

print("\n--- 4. Property dengan Caching ---")


class Dokumen:
    """Dokumen teks dengan word-count yang dihitung sekali dan di-cache."""

    def __init__(self, judul, isi):
        self.__judul      = judul
        self.__isi        = isi
        self.__cache_wc   = None   # cache word count

    @property
    def judul(self):
        return self.__judul

    @property
    def isi(self):
        return self.__isi

    @isi.setter
    def isi(self, teks_baru):
        self.__isi      = teks_baru
        self.__cache_wc = None   # invalidate cache saat isi berubah

    @property
    def jumlah_kata(self):
        """Hitung kata hanya jika belum di-cache atau isi berubah."""
        if self.__cache_wc is None:
            print("  [Menghitung word count...]")
            self.__cache_wc = len(self.__isi.split())
        return self.__cache_wc

    @property
    def ringkasan(self):
        kata = self.__isi.split()
        return " ".join(kata[:10]) + ("..." if len(kata) > 10 else "")


isi_teks = ("Python adalah bahasa pemrograman tingkat tinggi yang dirancang "
            "dengan filosofi keterbacaan kode. Python mendukung berbagai "
            "paradigma pemrograman termasuk OOP dan fungsional.")

dok = Dokumen("Pengantar Python", isi_teks)

print(f"Judul: {dok.judul}")
print(f"Akses pertama  jumlah_kata: {dok.jumlah_kata}")  # akan hitung
print(f"Akses kedua    jumlah_kata: {dok.jumlah_kata}")  # dari cache
print(f"Ringkasan: {dok.ringkasan}")

dok.isi = "Isi dokumen baru yang lebih pendek."
print(f"Setelah isi berubah jumlah_kata: {dok.jumlah_kata}")  # hitung ulang


print("\n[OK] Selesai: 02_property.py")
