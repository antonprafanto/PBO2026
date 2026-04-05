"""
==========================================================
    PERTEMUAN 01 — Pengantar OOP
    File: 01_prosedural_vs_oop.py
    Topik: Perbandingan Paradigma Prosedural vs OOP
==========================================================
"""

print("=" * 55)
print("   PERBANDINGAN PARADIGMA PROSEDURAL vs OOP")
print("=" * 55)

# ──────────────────────────────────────────────────────────
# BAGIAN 1: CARA PROSEDURAL
# ──────────────────────────────────────────────────────────
print("\n🔴 CARA PROSEDURAL:")
print("-" * 40)

# Data mahasiswa — tersebar sebagai variabel biasa
nama1  = "Budi Santoso"
nim1   = "2301001"
ipk1   = 3.75
aktif1 = True

nama2  = "Sari Dewi"
nim2   = "2301002"
ipk2   = 2.90
aktif2 = True

# Fungsi terpisah dari data
def tampilkan_info_prosedural(nama, nim, ipk, aktif):
    status = "Aktif" if aktif else "Tidak Aktif"
    print(f"  Nama : {nama}")
    print(f"  NIM  : {nim}")
    print(f"  IPK  : {ipk}")
    print(f"  Status: {status}")

def hitung_predikat_prosedural(ipk):
    if ipk >= 3.50:
        return "Cum Laude"
    elif ipk >= 3.00:
        return "Sangat Memuaskan"
    elif ipk >= 2.50:
        return "Memuaskan"
    else:
        return "Cukup"

# Masalah: kalau ada 100 mahasiswa → 100 variabel!
# Semakin banyak data, semakin kacau kode kita.

tampilkan_info_prosedural(nama1, nim1, ipk1, aktif1)
predikat1 = hitung_predikat_prosedural(ipk1)
print(f"  Predikat: {predikat1}")

print()
tampilkan_info_prosedural(nama2, nim2, ipk2, aktif2)
predikat2 = hitung_predikat_prosedural(ipk2)
print(f"  Predikat: {predikat2}")


# ──────────────────────────────────────────────────────────
# BAGIAN 2: CARA OOP
# ──────────────────────────────────────────────────────────
print("\n\n🟢 CARA OOP:")
print("-" * 40)

class Mahasiswa:
    """
    Kelas yang merepresentasikan seorang Mahasiswa.
    Data dan fungsi dikemas dalam satu unit yang rapi.
    """

    def __init__(self, nama, nim, ipk, aktif=True):
        """Konstruktor: dijalankan otomatis saat objek dibuat."""
        self.nama  = nama
        self.nim   = nim
        self.ipk   = ipk
        self.aktif = aktif

    def tampilkan_info(self):
        """Menampilkan informasi lengkap mahasiswa."""
        status = "Aktif" if self.aktif else "Tidak Aktif"
        print(f"  Nama  : {self.nama}")
        print(f"  NIM   : {self.nim}")
        print(f"  IPK   : {self.ipk}")
        print(f"  Status: {status}")

    def hitung_predikat(self):
        """Menghitung predikat kelulusan berdasarkan IPK."""
        if self.ipk >= 3.50:
            return "Cum Laude"
        elif self.ipk >= 3.00:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.50:
            return "Memuaskan"
        else:
            return "Cukup"


# Membuat objek — bersih dan mudah!
mhs1 = Mahasiswa("Budi Santoso", "2301001", 3.75)
mhs2 = Mahasiswa("Sari Dewi",    "2301002", 2.90)
mhs3 = Mahasiswa("Andi Rahman",  "2301003", 3.10)

# Memanggil method — cara yang elegan
for mhs in [mhs1, mhs2, mhs3]:
    mhs.tampilkan_info()
    print(f"  Predikat: {mhs.hitung_predikat()}")
    print()


# ──────────────────────────────────────────────────────────
# BAGIAN 3: KEUNGGULAN OOP
# ──────────────────────────────────────────────────────────
print("\n📊 RINGKASAN PERBANDINGAN:")
print("-" * 55)
print(f"  {'Aspek':<20} {'Prosedural':<15} {'OOP':<15}")
print(f"  {'-'*20} {'-'*15} {'-'*15}")
print(f"  {'Organisasi Data':<20} {'Tersebar':<15} {'Terstruktur':<15}")
print(f"  {'Skalabilitas':<20} {'Sulit':<15} {'Mudah':<15}")
print(f"  {'Reuse Kode':<20} {'Tidak mudah':<15} {'Sangat mudah':<15}")
print(f"  {'Kolaborasi Tim':<20} {'Sulit':<15} {'Mudah':<15}")
print(f"  {'Maintenance':<20} {'Rumit':<15} {'Mudah':<15}")

print("\n✅ Selesai! Lanjut ke file berikutnya: 02_kelas_pertama.py")
