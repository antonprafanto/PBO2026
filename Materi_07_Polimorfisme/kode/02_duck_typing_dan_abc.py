"""
Kode Praktik - Materi 07: Polimorfisme (Polymorphism)
File: 02_duck_typing_dan_abc.py
Topik: Duck typing lanjutan, ABC, operator overloading, integrasi built-in

Jalankan: python 02_duck_typing_dan_abc.py
"""

from abc import ABC, abstractmethod
import math

# ======================================================================
# BAGIAN 1: Duck Typing — Sistem Plugin Pembayaran
#           Fokus: kelas-kelas independen yang bisa dipakai seragam
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Duck Typing — Sistem Plugin Pembayaran")
print("=" * 60)

class TransferBank:
    """Pembayaran via transfer bank antar rekening."""

    def __init__(self, bank, nomor_rekening, atas_nama):
        self.bank           = bank
        self.nomor_rekening = nomor_rekening
        self.atas_nama      = atas_nama

    def bayar(self, jumlah, keterangan=""):
        biaya_admin = 6_500
        total       = jumlah + biaya_admin
        print(f"  [Transfer {self.bank}]")
        print(f"    Rekening  : {self.nomor_rekening} a/n {self.atas_nama}")
        print(f"    Jumlah    : Rp {jumlah:>12,.0f}")
        print(f"    Biaya Admin: Rp {biaya_admin:>11,.0f}")
        print(f"    Total     : Rp {total:>12,.0f}")
        if keterangan:
            print(f"    Ket.      : {keterangan}")
        return total

    def nama_metode(self):
        return f"Transfer {self.bank}"


class KartuKredit:
    """Pembayaran via kartu kredit dengan cicilan opsional."""

    def __init__(self, bank_penerbit, jenis="Visa"):
        self.bank_penerbit = bank_penerbit
        self.jenis         = jenis

    def bayar(self, jumlah, keterangan="", cicilan=1):
        biaya_mdr = jumlah * 0.02   # Merchant Discount Rate 2%
        total     = jumlah + biaya_mdr
        print(f"  [Kartu Kredit {self.jenis} — {self.bank_penerbit}]")
        print(f"    Jumlah    : Rp {jumlah:>12,.0f}")
        print(f"    MDR (2%)  : Rp {biaya_mdr:>12,.0f}")
        print(f"    Total     : Rp {total:>12,.0f}")
        if cicilan > 1:
            per_bulan = total / cicilan
            print(f"    Cicilan   : {cicilan}x @ Rp {per_bulan:,.0f}/bln")
        if keterangan:
            print(f"    Ket.      : {keterangan}")
        return total

    def nama_metode(self):
        return f"Kartu Kredit {self.jenis}"


class DompetDigital:
    """Pembayaran via dompet digital (GoPay, OVO, Dana, dll.)."""

    def __init__(self, platform, nomor_akun):
        self.platform   = platform
        self.nomor_akun = nomor_akun
        self._saldo     = 0

    def isi_saldo(self, jumlah):
        self._saldo += jumlah
        print(f"  [{self.platform}] Isi saldo Rp {jumlah:,.0f} — "
              f"Saldo: Rp {self._saldo:,.0f}")

    def bayar(self, jumlah, keterangan=""):
        if self._saldo < jumlah:
            raise ValueError(f"Saldo {self.platform} tidak cukup! "
                             f"Butuh Rp {jumlah:,.0f}, "
                             f"tersedia Rp {self._saldo:,.0f}")
        self._saldo -= jumlah
        print(f"  [{self.platform} — {self.nomor_akun}]")
        print(f"    Jumlah    : Rp {jumlah:>12,.0f}")
        print(f"    Sisa Saldo: Rp {self._saldo:>12,.0f}")
        if keterangan:
            print(f"    Ket.      : {keterangan}")
        return jumlah

    def nama_metode(self):
        return self.platform


def proses_transaksi(item, harga, metode_bayar):
    """Proses transaksi apapun dengan metode pembayaran apapun.

    Duck typing: selama metode_bayar punya .bayar() dan .nama_metode(),
    fungsi ini bekerja — tidak perlu pewarisan.
    """
    print(f"\n  Transaksi: {item} — Rp {harga:,.0f}")
    print(f"  Metode   : {metode_bayar.nama_metode()}")
    print("  " + "-" * 40)
    total = metode_bayar.bayar(harga, keterangan=item)
    print(f"  [OK] Pembayaran berhasil. Total: Rp {total:,.0f}")
    return total


# Demo — berbagai metode pembayaran dipakai dengan fungsi yang sama
gopay  = DompetDigital("GoPay",  "0812-xxxx")
gopay.isi_saldo(5_000_000)

transaksi = [
    ("SPP Semester Genap 2025",  3_500_000,
     TransferBank("BNI", "0123456789", "Bendahara UNMUL")),
    ("Buku PBO Python",            185_000,
     KartuKredit("BCA", "Mastercard")),
    ("Fotokopi + Jilid Skripsi",   75_000,
     gopay),
]

total_semua = 0
for item, harga, metode in transaksi:
    total_semua += proses_transaksi(item, harga, metode)

print(f"\n  Total semua transaksi: Rp {total_semua:,.0f}")


# ======================================================================
# BAGIAN 2: ABC — Kontrak Formal dengan @abstractmethod
#           Fokus: ABC memaksa implementasi & menyediakan template method
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: ABC — Kontrak Formal Pembayaran SPP")
print("=" * 60)

class MetodePembayaranSPP(ABC):
    """ABC — mendefinisikan kontrak wajib untuk metode pembayaran SPP."""

    @abstractmethod
    def validasi(self, jumlah):
        """Validasi apakah pembayaran dapat dilakukan. Return True/False."""
        pass

    @abstractmethod
    def proses(self, jumlah):
        """Proses pembayaran. Return (sukses: bool, pesan: str)."""
        pass

    @abstractmethod
    def nama(self):
        """Return nama metode sebagai string."""
        pass

    def bayar_spp(self, nim, nama_mhs, jumlah):
        """Template method — alur pembayaran selalu konsisten."""
        print(f"\n  Pembayaran SPP: {nama_mhs} ({nim})")
        print(f"  Metode        : {self.nama()}")
        print(f"  Jumlah        : Rp {jumlah:,.0f}")
        print("  " + "-" * 45)

        if not self.validasi(jumlah):
            print("  [GAGAL] Validasi tidak lolos.")
            return False

        sukses, pesan = self.proses(jumlah)
        if sukses:
            print(f"  [OK] {pesan}")
            print(f"  Bukti: SPP-{nim}-{jumlah}")
        else:
            print(f"  [GAGAL] {pesan}")
        return sukses


class SPPTransfer(MetodePembayaranSPP):
    def __init__(self, rekening_tujuan):
        self.rekening = rekening_tujuan
        self._transaksi_terakhir = None

    def validasi(self, jumlah):
        if jumlah <= 0:
            return False
        if jumlah > 50_000_000:   # batas transfer harian
            print(f"  [Validasi] Jumlah melebihi batas transfer harian!")
            return False
        return True

    def proses(self, jumlah):
        self._transaksi_terakhir = jumlah
        return True, f"Transfer Rp {jumlah:,.0f} ke {self.rekening} berhasil."

    def nama(self):
        return f"Transfer Bank ({self.rekening})"


class SPPQris(MetodePembayaranSPP):
    def __init__(self, merchant_id):
        self.merchant_id = merchant_id
        self._limit_qris  = 10_000_000   # limit QRIS Bank Indonesia

    def validasi(self, jumlah):
        if jumlah > self._limit_qris:
            print(f"  [Validasi] Melebihi limit QRIS Rp {self._limit_qris:,.0f}!")
            return False
        return True

    def proses(self, jumlah):
        return True, f"QRIS scan berhasil. Merchant: {self.merchant_id}"

    def nama(self):
        return f"QRIS ({self.merchant_id})"


class SPPBeasiswa(MetodePembayaranSPP):
    """Pembayaran SPP via pemotongan beasiswa — selalu gratis."""

    def __init__(self, jenis_beasiswa, nilai_beasiswa):
        self.jenis       = jenis_beasiswa
        self.nilai       = nilai_beasiswa
        self._sisa       = nilai_beasiswa

    def validasi(self, jumlah):
        if self._sisa < jumlah:
            print(f"  [Validasi] Sisa beasiswa Rp {self._sisa:,.0f} "
                  f"tidak mencukupi SPP Rp {jumlah:,.0f}!")
            return False
        return True

    def proses(self, jumlah):
        self._sisa -= jumlah
        return (True,
                f"Beasiswa {self.jenis} dipotong Rp {jumlah:,.0f}. "
                f"Sisa: Rp {self._sisa:,.0f}")

    def nama(self):
        return f"Beasiswa {self.jenis}"


# Polimorfisme ABC: semua metode punya .bayar_spp() yang sama
metode_list = [
    ("2301001", "Budi Santoso",   3_500_000, SPPTransfer("BNI-1234567890")),
    ("2301002", "Sari Dewi",      3_500_000, SPPQris("UNMUL-QRIS-001")),
    ("2301003", "Rudi Hartono",   3_500_000,
     SPPBeasiswa("KIP-Kuliah", 10_000_000)),
]

for nim, nama, jumlah, metode in metode_list:
    metode.bayar_spp(nim, nama, jumlah)

# Uji validasi gagal
print("\n  Uji kasus gagal:")
qris_kecil = SPPQris("KOPERASI-001")
qris_kecil.bayar_spp("2301099", "Test Gagal", 15_000_000)


# ======================================================================
# BAGIAN 3: Operator Overloading
#           Fokus: __add__, __sub__, __eq__, __lt__, __len__, dan lainnya
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: Operator Overloading")
print("=" * 60)

class NilaiMahasiswa:
    """Merepresentasikan nilai akhir seorang mahasiswa."""

    _PREDIKAT = [
        (87, "A"), (82, "A-"), (78, "B+"), (75, "B"),
        (71, "B-"), (67, "C+"), (64, "C"), (56, "D"), (0, "E"),
    ]

    def __init__(self, nama, nilai):
        if not (0 <= nilai <= 100):
            raise ValueError(f"Nilai harus 0-100, dapat: {nilai}")
        self.nama  = nama
        self.nilai = float(nilai)

    @property
    def huruf(self):
        for batas, h in self._PREDIKAT:
            if self.nilai >= batas:
                return h
        return "E"

    def __add__(self, other):
        """Rata-rata dua nilai — berguna untuk menggabungkan komponen nilai."""
        if isinstance(other, NilaiMahasiswa):
            return NilaiMahasiswa(f"{self.nama}+{other.nama}",
                                  (self.nilai + other.nilai) / 2)
        # Skalar: dijepit ke rentang 0-100 agar tidak melebihi batas valid
        return NilaiMahasiswa(self.nama, max(0.0, min(100.0, self.nilai + other)))

    def __sub__(self, other):
        """Selisih nilai — berguna untuk melihat peningkatan/penurunan."""
        if isinstance(other, NilaiMahasiswa):
            return self.nilai - other.nilai
        return self.nilai - other

    def __eq__(self, other):
        if isinstance(other, NilaiMahasiswa):
            return self.nilai == other.nilai
        return self.nilai == other

    def __lt__(self, other):
        if isinstance(other, NilaiMahasiswa):
            return self.nilai < other.nilai
        return self.nilai < other

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        if isinstance(other, NilaiMahasiswa):
            return self.nilai > other.nilai
        return self.nilai > other

    def __ge__(self, other):
        return self == other or self > other

    def __float__(self):
        return self.nilai

    def __str__(self):
        return f"{self.nama}: {self.nilai:.1f} ({self.huruf})"

    def __repr__(self):
        return f"NilaiMahasiswa('{self.nama}', {self.nilai})"


print("\n  Demo NilaiMahasiswa:")
n1 = NilaiMahasiswa("Budi",  88.5)
n2 = NilaiMahasiswa("Sari",  92.0)
n3 = NilaiMahasiswa("Rudi",  75.0)

print(f"  n1 = {n1}")
print(f"  n2 = {n2}")
print(f"  n3 = {n3}")

print(f"\n  n1 + n2 (rata-rata) = {n1 + n2}")
print(f"  n2 - n1 (selisih)   = {n2 - n1:.1f}")
print(f"  n1 > n3?            = {n1 > n3}")
print(f"  n1 == n3?           = {n1 == n3}")

# sorted() otomatis pakai __lt__
nilai_kelas = [
    NilaiMahasiswa("Budi",  88.5),
    NilaiMahasiswa("Sari",  92.0),
    NilaiMahasiswa("Rudi",  75.0),
    NilaiMahasiswa("Ayu",   85.0),
    NilaiMahasiswa("Doni",  68.5),
]

print("\n  Peringkat kelas (tertinggi ke terendah):")
for rank, nilai in enumerate(sorted(nilai_kelas, reverse=True), 1):
    print(f"    {rank}. {nilai}")

# max() dan min() juga bekerja otomatis
print(f"\n  Nilai tertinggi: {max(nilai_kelas)}")
print(f"  Nilai terendah : {min(nilai_kelas)}")


# ======================================================================
# BAGIAN 4: Integrasi dengan Built-in Python via Magic Methods
#           Fokus: __len__, __contains__, __iter__, __getitem__
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 4: Kelas yang Kompatibel dengan Built-in Python")
print("=" * 60)

class DaftarMahasiswa:
    """Koleksi mahasiswa yang kompatibel dengan built-in Python."""

    def __init__(self, nama_kelas):
        self.nama_kelas = nama_kelas
        self._data      = []   # list of (nim, nama, ipk)

    def tambah(self, nim, nama, ipk):
        self._data.append((nim, nama, float(ipk)))

    def __len__(self):
        """Mendukung len(daftar)."""
        return len(self._data)

    def __contains__(self, nim):
        """Mendukung 'NIM in daftar'."""
        return any(d[0] == nim for d in self._data)

    def __iter__(self):
        """Mendukung 'for mhs in daftar'."""
        return iter(self._data)

    def __getitem__(self, index):
        """Mendukung daftar[0], daftar[1:3], dll."""
        return self._data[index]

    def __str__(self):
        return f"DaftarMahasiswa({self.nama_kelas}, {len(self)} orang)"

    def rata_rata_ipk(self):
        if not self._data:
            return 0.0
        return sum(ipk for _, _, ipk in self._data) / len(self)


# Buat daftar kelas
kelas_a = DaftarMahasiswa("Informatika A 2023")
for nim, nama, ipk in [
    ("2301001", "Budi Santoso",   3.85),
    ("2301002", "Sari Dewi",      3.92),
    ("2301003", "Rudi Hartono",   3.20),
    ("2301004", "Ayu Lestari",    3.75),
    ("2301005", "Doni Prasetyo",  2.85),
]:
    kelas_a.tambah(nim, nama, ipk)

print(f"\n  Kelas: {kelas_a}")
print(f"  Jumlah mahasiswa: {len(kelas_a)}")           # __len__
print(f"  '2301002' ada?   : {'2301002' in kelas_a}")   # __contains__
print(f"  '2301099' ada?   : {'2301099' in kelas_a}")

print(f"\n  Iterasi (for loop):")                        # __iter__
for nim, nama, ipk in kelas_a:
    bintang = "*" * int(ipk * 10 / 4)
    print(f"    {nim} | {nama:<20} | {ipk:.2f} {bintang}")

print(f"\n  Mahasiswa pertama: {kelas_a[0]}")            # __getitem__
print(f"  Dua terakhir     : {kelas_a[-2:]}")

print(f"\n  Rata-rata IPK kelas: {kelas_a.rata_rata_ipk():.2f}")

# sorted() bekerja dengan kelas ini juga (via __iter__)
print(f"\n  Diurutkan berdasarkan IPK:")
for nim, nama, ipk in sorted(kelas_a, key=lambda x: -x[2]):
    print(f"    {nama:<22} {ipk:.2f}")

print()
