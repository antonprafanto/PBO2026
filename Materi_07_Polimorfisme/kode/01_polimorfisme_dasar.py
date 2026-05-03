"""
Kode Praktik - Materi 07: Polimorfisme (Polymorphism)
File: 01_polimorfisme_dasar.py
Topik: Polimorfisme via pewarisan, duck typing, dan ABC dasar

Jalankan: python 01_polimorfisme_dasar.py
"""

# ======================================================================
# BAGIAN 1: Polimorfisme via Pewarisan — Hierarki Kendaraan
#           Fokus: satu antarmuka, banyak perilaku berbeda
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Polimorfisme via Pewarisan — Hierarki Kendaraan")
print("=" * 60)

class Kendaraan:
    """Kelas induk — mendefinisikan antarmuka umum kendaraan."""

    def __init__(self, merk, tahun, harga_per_hari):
        self.merk          = merk
        self.tahun         = tahun
        self.harga_per_hari = harga_per_hari
        self._tersedia     = True

    def hitung_biaya_sewa(self, hari):
        """Implementasi default — kelas anak diharapkan meng-override ini."""
        return self.harga_per_hari * hari

    def deskripsi(self):
        """Kelas anak di-override untuk memberi deskripsi spesifik."""
        return f"{self.merk} ({self.tahun})"

    def info_sewa(self, hari):
        """Method ini TIDAK di-override — tapi memanggil hitung_biaya_sewa()
        yang ter-override. Inilah inti polimorfisme via pewarisan."""
        biaya = self.hitung_biaya_sewa(hari)
        print(f"  {self.deskripsi()}")
        print(f"    Durasi  : {hari} hari")
        print(f"    Biaya   : Rp {biaya:>12,.0f}")

    def __str__(self):
        status = "Tersedia" if self._tersedia else "Tidak Tersedia"
        return f"{self.deskripsi()} [{status}]"


class Mobil(Kendaraan):
    def __init__(self, merk, tahun, harga_per_hari, kapasitas_penumpang):
        super().__init__(merk, tahun, harga_per_hari)
        self.kapasitas_penumpang = kapasitas_penumpang

    def deskripsi(self):
        return f"Mobil {self.merk} ({self.tahun}) — {self.kapasitas_penumpang} penumpang"

    def hitung_biaya_sewa(self, hari):
        # Diskon 10% jika sewa lebih dari 7 hari
        biaya = self.harga_per_hari * hari
        if hari > 7:
            biaya *= 0.90
            print(f"    [Diskon 10% diterapkan untuk sewa > 7 hari]")
        return biaya


class Motor(Kendaraan):
    def __init__(self, merk, tahun, harga_per_hari, jenis):
        super().__init__(merk, tahun, harga_per_hari)
        self.jenis = jenis   # "matic", "sport", "bebek"

    def deskripsi(self):
        return f"Motor {self.merk} {self.jenis.title()} ({self.tahun})"

    def hitung_biaya_sewa(self, hari):
        # Sewa motor: bayar per hari, tapi minimal 2 hari
        hari_bayar = max(hari, 2)
        if hari < 2:
            print(f"    [Minimal sewa 2 hari — ditagih 2 hari]")
        return self.harga_per_hari * hari_bayar


class Truk(Kendaraan):
    def __init__(self, merk, tahun, harga_per_hari, kapasitas_ton,
                 harga_per_km=2000):
        super().__init__(merk, tahun, harga_per_hari)
        self.kapasitas_ton = kapasitas_ton
        self.harga_per_km  = harga_per_km

    def deskripsi(self):
        return f"Truk {self.merk} ({self.tahun}) — {self.kapasitas_ton} ton"

    def hitung_biaya_sewa(self, hari, jarak_km=0):
        biaya_hari = self.harga_per_hari * hari
        biaya_jarak = self.harga_per_km * jarak_km
        if jarak_km > 0:
            print(f"    [Biaya jarak {jarak_km} km: Rp {biaya_jarak:,.0f}]")
        return biaya_hari + biaya_jarak


# --- Polimorfisme dalam aksi ---
print("\n  Daftar kendaraan dan biaya sewa 5 hari:")
print("  " + "-" * 56)

armada = [
    Mobil("Toyota Avanza",  2022, 350_000, 7),
    Mobil("Toyota Fortuner",2023, 750_000, 7),
    Motor("Honda Beat",     2021, 100_000, "matic"),
    Motor("Kawasaki Ninja", 2022, 200_000, "sport"),
    Truk("Hino Dutro",      2020, 800_000, 4),
]

# Satu loop — satu method info_sewa() — banyak perilaku berbeda
for kendaraan in armada:
    print()
    kendaraan.info_sewa(5)

# Truk punya parameter tambahan — tapi polimorfisme tetap berjalan
print()
print("  Truk dengan biaya jarak:")
truk = Truk("Mitsubishi Canter", 2021, 600_000, 3, 2500)
truk.hitung_biaya_sewa(3, jarak_km=150)
truk.info_sewa(3)

print()
print("  Sewa Mobil > 7 hari (dapat diskon):")
Mobil("Innova Zenix", 2023, 500_000, 7).info_sewa(10)


# ======================================================================
# BAGIAN 2: Duck Typing — Tanpa Hierarki Pewarisan
#           Fokus: fungsi yang bekerja dengan "tipe apapun" selama
#                  method yang dibutuhkan tersedia
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: Duck Typing — Fungsi Universal")
print("=" * 60)

class Printer:
    """Mencetak dokumen ke kertas (simulasi)."""
    def kirim(self, dokumen):
        print(f"  [Printer] Mencetak: '{dokumen}' ...")
        print(f"  [Printer] Selesai dicetak.")


class EmailSender:
    """Mengirim dokumen via email."""
    def __init__(self, alamat_tujuan):
        self.alamat = alamat_tujuan

    def kirim(self, dokumen):
        print(f"  [Email -> {self.alamat}] Mengirim: '{dokumen}' ...")
        print(f"  [Email] Terkirim.")


class WhatsAppSender:
    """Mengirim dokumen via WhatsApp."""
    def __init__(self, nomor):
        self.nomor = nomor

    def kirim(self, dokumen):
        print(f"  [WA -> {self.nomor}] Mengirim dokumen: '{dokumen}' ...")
        print(f"  [WA] Diterima.")


class CloudStorage:
    """Menyimpan dokumen ke cloud."""
    def __init__(self, bucket):
        self.bucket = bucket

    def kirim(self, dokumen):
        print(f"  [Cloud/{self.bucket}] Mengupload: '{dokumen}' ...")
        print(f"  [Cloud] Upload berhasil. URL: cloud://{self.bucket}/{dokumen}")


def distribusikan_dokumen(dokumen, daftar_pengirim):
    """Distribusikan dokumen ke semua media.

    Tidak peduli apakah pengirim adalah Printer, Email, WA, atau Cloud —
    selama punya method kirim(), fungsi ini berjalan.
    """
    print(f"\n  Mendistribusikan: '{dokumen}'")
    print("  " + "-" * 40)
    for pengirim in daftar_pengirim:
        pengirim.kirim(dokumen)


# Tidak ada pewarisan antar kelas — tapi semuanya bisa dipakai bersama
saluran = [
    Printer(),
    EmailSender("dekan@unmul.ac.id"),
    WhatsAppSender("0812-3456-789"),
    CloudStorage("dok-akademik-2025"),
]

distribusikan_dokumen("Surat_Keputusan_Wisuda.pdf", saluran)
distribusikan_dokumen("Transkrip_Nilai_Budi.pdf",
                      [EmailSender("budi@gmail.com"), CloudStorage("arsip")])


# ======================================================================
# BAGIAN 3: Abstract Base Class (ABC) — Kontrak yang Dipaksakan
#           Fokus: ABC memastikan kelas anak implementasikan method wajib
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: ABC — Kontrak yang Dipaksakan")
print("=" * 60)

from abc import ABC, abstractmethod


class LaporanAkademik(ABC):
    """Kelas abstrak untuk semua jenis laporan akademik."""

    def __init__(self, judul, periode):
        self.judul   = judul
        self.periode = periode

    @abstractmethod
    def kumpulkan_data(self):
        """Kumpulkan data yang dibutuhkan laporan. WAJIB diimplementasikan."""
        pass

    @abstractmethod
    def format_output(self):
        """Format data menjadi string laporan. WAJIB diimplementasikan."""
        pass

    def generate(self):
        """Template method — urutan pembuatan laporan selalu sama."""
        print(f"\n  Membuat: {self.judul} [{self.periode}]")
        self.kumpulkan_data()
        output = self.format_output()
        print(output)
        print(f"  Laporan selesai dibuat.")

    def simpan(self, nama_file):
        """Method konkret — bisa langsung dipakai kelas anak."""
        print(f"  [Simpan] {nama_file} tersimpan.")


class LaporanIPK(LaporanAkademik):
    def __init__(self, periode, data_mahasiswa):
        super().__init__("Laporan Rekap IPK Mahasiswa", periode)
        self._data = data_mahasiswa   # list of (nama, ipk)

    def kumpulkan_data(self):
        print(f"  [Data] Mengambil data {len(self._data)} mahasiswa...")

    def format_output(self):
        lines = [f"  {'Nama':<25} {'IPK':>5}  {'Predikat':<20}"]
        lines.append("  " + "-" * 55)
        for nama, ipk in sorted(self._data, key=lambda x: -x[1]):
            if   ipk >= 3.51: predikat = "Cum Laude"
            elif ipk >= 3.01: predikat = "Sangat Memuaskan"
            elif ipk >= 2.76: predikat = "Memuaskan"
            else:              predikat = "Cukup"
            lines.append(f"  {nama:<25} {ipk:>5.2f}  {predikat}")
        rata = sum(i for _, i in self._data) / len(self._data)
        lines.append("  " + "-" * 55)
        lines.append(f"  Rata-rata IPK Angkatan: {rata:.2f}")
        return "\n".join(lines)


class LaporanKehadiran(LaporanAkademik):
    def __init__(self, periode, matkul, data_hadir):
        super().__init__(f"Laporan Kehadiran: {matkul}", periode)
        self.matkul    = matkul
        self._data     = data_hadir   # list of (nama, hadir, total)

    def kumpulkan_data(self):
        print(f"  [Data] Mengambil data kehadiran {self.matkul}...")

    def format_output(self):
        lines = [f"  {'Nama':<25} {'Hadir':>6} {'Total':>6} {'%':>6}  Status"]
        lines.append("  " + "-" * 55)
        for nama, hadir, total in self._data:
            persen = (hadir / total) * 100
            status = "OK" if persen >= 75 else "KURANG"
            lines.append(f"  {nama:<25} {hadir:>6} {total:>6} "
                         f"{persen:>5.1f}%  {status}")
        return "\n".join(lines)


# Uji ABC: instansiasi kelas abstrak langsung akan error
print("\n  Uji: instansiasi kelas abstrak")
try:
    lap = LaporanAkademik("Test", "2025")
except TypeError as e:
    print(f"  [Error ditangkap] {e}")

# Kelas konkret berjalan normal
data_mhs = [
    ("Budi Santoso",   3.85),
    ("Sari Dewi",      3.50),
    ("Rudi Hartono",   2.90),
    ("Ayu Lestari",    3.72),
    ("Doni Prasetyo",  2.65),
]

laporan_ipk = LaporanIPK("Semester Genap 2024/2025", data_mhs)
laporan_ipk.generate()
laporan_ipk.simpan("rekap_ipk_genap_2025.pdf")

data_hadir = [
    ("Budi Santoso",  13, 14),
    ("Sari Dewi",     14, 14),
    ("Rudi Hartono",  10, 14),
    ("Ayu Lestari",   11, 14),
    ("Doni Prasetyo",  9, 14),
]

laporan_hadir = LaporanKehadiran("Semester Genap 2024/2025", "PBO", data_hadir)
laporan_hadir.generate()

# Polimorfisme: dua laporan berbeda, satu antarmuka yang sama
print("\n  Polimorfisme: generate semua laporan sekaligus")
print("  " + "-" * 40)
semua_laporan = [laporan_ipk, laporan_hadir]
for lap in semua_laporan:
    print(f"  -> {lap.judul}")

print()
