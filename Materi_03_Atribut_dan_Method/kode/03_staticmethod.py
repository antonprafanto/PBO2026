"""
============================================================
    MATERI 03 - Atribut dan Method
    File: 03_staticmethod.py
    Topik: @staticmethod - Cara Kerja dan Kegunaannya
============================================================
"""

# ?????????????????????????????????????????????????????????
# BAGIAN 1: Dasar @staticmethod
# - Tidak menerima self maupun cls
# - Fungsi utilitas yang logisnya 'milik' kelas
# - Bisa dipanggil tanpa membuat objek: Kelas.method()
# ?????????????????????????????????????????????????????????

print("=" * 55)
print("  1. DASAR @staticmethod")
print("=" * 55)


class ValidasiInput:
    """Kelas utilitas untuk validasi berbagai jenis input."""

    @staticmethod
    def adalah_email_valid(email: str) -> bool:
        """Cek apakah string adalah format email yang valid (sederhana)."""
        return "@" in email and "." in email.split("@")[-1]

    @staticmethod
    def adalah_nim_valid(nim: str) -> bool:
        """NIM harus 7 digit angka."""
        return nim.isdigit() and len(nim) == 7

    @staticmethod
    def adalah_ipk_valid(ipk: float) -> bool:
        """IPK harus antara 0.0 dan 4.0."""
        return 0.0 <= ipk <= 4.0

    @staticmethod
    def bersihkan_nama(nama: str) -> str:
        """Normalisasi nama: strip spasi & Title Case."""
        return nama.strip().title()


# Dipanggil langsung via kelas - TIDAK perlu membuat objek
email_test = ["budi@gmail.com", "budi.gmail.com", "test@", "sari@unmul.ac.id"]
print("Validasi Email:")
for e in email_test:
    status = "[OK] valid" if ValidasiInput.adalah_email_valid(e) else "[x] tidak valid"
    print(f"  {e:<25} -> {status}")

print("\nValidasi NIM:")
for nim in ["2301001", "230100", "abc12345", "9999999"]:
    status = "[OK]" if ValidasiInput.adalah_nim_valid(nim) else "[x]"
    print(f"  {nim} -> {status}")

print("\nValidasi IPK:")
for ipk in [3.75, 4.0, -0.1, 4.1, 0.0]:
    status = "[OK]" if ValidasiInput.adalah_ipk_valid(ipk) else "[x]"
    print(f"  {ipk} -> {status}")

print(f"\nBersihkan nama: '  budi santoso  ' -> '{ValidasiInput.bersihkan_nama('  budi santoso  ')}'")


# ?????????????????????????????????????????????????????????
# BAGIAN 2: Static Method sebagai Utilitas Kalkulasi
# ?????????????????????????????????????????????????????????

print("\n" + "=" * 55)
print("  2. STATIC METHOD: Kalkulasi")
print("=" * 55)


class KonversiNilai:
    """Kelas utilitas untuk konversi nilai akademik."""

    SKALA = {
        "A":  4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B":  3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C":  2.0,
        "D":  1.0,
        "E":  0.0,
    }

    @staticmethod
    def angka_ke_huruf(nilai: float) -> str:
        """Konversi nilai 0?100 ke huruf (skala Unmul)."""
        if nilai >= 85: return "A"
        if nilai >= 80: return "A-"
        if nilai >= 75: return "B+"
        if nilai >= 70: return "B"
        if nilai >= 65: return "B-"
        if nilai >= 60: return "C+"
        if nilai >= 55: return "C"
        if nilai >= 40: return "D"
        return "E"

    @staticmethod
    def huruf_ke_bobot(huruf: str) -> float:
        """Konversi nilai huruf ke bobot angka."""
        return KonversiNilai.SKALA.get(huruf.upper(), 0.0)

    @staticmethod
    def hitung_ipk(nilai_list: list[float], sks_list: list[int]) -> float:
        """
        Hitung IPK berdasarkan daftar nilai huruf (0-4) dan SKS.
        nilai_list: list bobot (0-4), sks_list: list jumlah SKS per MK
        """
        if len(nilai_list) != len(sks_list):
            raise ValueError("Panjang nilai_list dan sks_list harus sama!")
        total_bobot_sks = sum(n * s for n, s in zip(nilai_list, sks_list))
        total_sks       = sum(sks_list)
        return round(total_bobot_sks / total_sks, 2) if total_sks > 0 else 0.0

    @staticmethod
    def predikat_ipk(ipk: float) -> str:
        """Tentukan predikat kelulusan dari IPK."""
        if ipk >= 3.51: return "Cum Laude"
        if ipk >= 3.01: return "Sangat Memuaskan"
        if ipk >= 2.76: return "Memuaskan"
        if ipk >= 2.00: return "Cukup"
        return "Tidak Lulus"


# Simulasi transkrip nilai
mata_kuliah = [
    ("Pemrograman Berorientasi Objek", 3, 88),
    ("Basis Data",                     3, 76),
    ("Jaringan Komputer",              3, 65),
    ("Kalkulus",                       2, 55),
    ("Bahasa Inggris",                 2, 80),
]

print(f"{'Mata Kuliah':<38} {'SKS':>4} {'Nilai':>6} {'Huruf':>6} {'Bobot':>6}")
print("-" * 68)

nilai_list, sks_list = [], []
for mk, sks, nilai in mata_kuliah:
    huruf = KonversiNilai.angka_ke_huruf(nilai)
    bobot = KonversiNilai.huruf_ke_bobot(huruf)
    nilai_list.append(bobot)
    sks_list.append(sks)
    print(f"{mk:<38} {sks:>4} {nilai:>6} {huruf:>6} {bobot:>6.1f}")

ipk = KonversiNilai.hitung_ipk(nilai_list, sks_list)
print("-" * 68)
print(f"IPK     : {ipk}")
print(f"Predikat: {KonversiNilai.predikat_ipk(ipk)}")


# ?????????????????????????????????????????????????????????
# BAGIAN 3: Perbandingan Ketiga Jenis Method dalam Satu Kelas
# ?????????????????????????????????????????????????????????

print("\n" + "=" * 55)
print("  3. PERBANDINGAN INSTANCE vs CLASS vs STATIC METHOD")
print("=" * 55)


class Karyawan:
    perusahaan   = "PT Nusantara Digital"
    gaji_minimum = 3_000_000

    def __init__(self, nama, jabatan, gaji):
        self.nama    = nama
        self.jabatan = jabatan
        self.gaji    = gaji

    # INSTANCE METHOD - akses self (data per objek)
    def info(self):
        print(f"  Instance  -> {self.nama} | {self.jabatan} | Rp {self.gaji:,.0f}")

    def gaji_bersih(self, potongan=10):
        return self.gaji * (1 - potongan / 100)

    # CLASS METHOD - akses cls (data kelas)
    @classmethod
    def info_perusahaan(cls):
        print(f"  Class     -> Perusahaan: {cls.perusahaan} | Gaji Min: Rp {cls.gaji_minimum:,.0f}")

    @classmethod
    def naik_gaji_minimum(cls, nominal):
        cls.gaji_minimum += nominal
        print(f"  Class     -> Gaji minimum baru: Rp {cls.gaji_minimum:,.0f}")

    # STATIC METHOD - tidak akses self/cls
    @staticmethod
    def format_rupiah(nominal):
        return f"Rp {nominal:,.0f}"

    @staticmethod
    def hitung_potongan(gaji, persen):
        return gaji * persen / 100


k = Karyawan("Anton", "Senior Dev", 9_000_000)

# Instance method - harus via objek
k.info()

# Class method - via kelas atau objek (tapi via kelas lebih jelas)
Karyawan.info_perusahaan()
Karyawan.naik_gaji_minimum(500_000)

# Static method - via kelas (tidak perlu objek)
print(f"  Static    -> {Karyawan.format_rupiah(9_000_000)}")
print(f"  Static    -> Potongan 10%: {Karyawan.format_rupiah(Karyawan.hitung_potongan(9_000_000, 10))}")


print("\n[OK] Selesai: 03_staticmethod.py")
