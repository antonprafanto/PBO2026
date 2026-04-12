"""
============================================================
    MATERI 04 - Enkapsulasi
    File: 03_enkapsulasi_praktis.py
    Topik: Studi Kasus Nyata — RekeningBank & SistemInventori
============================================================
"""

print("=" * 58)
print("  MATERI 04 - Enkapsulasi")
print("  03_enkapsulasi_praktis.py")
print("=" * 58)


# ============================================================
# STUDI KASUS 1: Rekening Bank
# Menunjukkan enkapsulasi pada sistem keuangan nyata
# ============================================================

print("\n" + "=" * 58)
print("  STUDI KASUS 1: Rekening Bank")
print("=" * 58)

from datetime import datetime


class RekeningBank:
    """
    Rekening bank dengan enkapsulasi penuh.
    - Saldo tidak bisa diubah langsung dari luar
    - Setiap transaksi tercatat di riwayat
    - Validasi dijalankan di setiap operasi
    """

    BUNGA_TAHUNAN  = 3.5     # persen
    LIMIT_TARIK    = 10_000_000

    def __init__(self, pemilik, nomor_rekening, saldo_awal=0):
        self.__pemilik         = pemilik.strip().title()
        self.__nomor_rekening  = nomor_rekening
        self.__saldo           = 0.0
        self.__riwayat         = []
        self.__aktif           = True
        if saldo_awal > 0:
            self._catat_transaksi("BUKA REKENING", saldo_awal)
            self.__saldo = saldo_awal

    # ---- Properties (Read-Only untuk data sensitif) ---------
    @property
    def pemilik(self):
        return self.__pemilik

    @property
    def nomor_rekening(self):
        """Sensor nomor rekening — tampilkan hanya 4 digit terakhir."""
        return "****-****-" + self.__nomor_rekening[-4:]

    @property
    def saldo(self):
        return self.__saldo

    @property
    def aktif(self):
        return self.__aktif

    @property
    def riwayat(self):
        """Kembalikan salinan riwayat — bukan referensi aslinya."""
        return self.__riwayat.copy()

    @property
    def bunga_bulanan(self):
        """Computed: estimasi bunga bulan ini."""
        return round(self.__saldo * self.BUNGA_TAHUNAN / 100 / 12, 2)

    # ---- Method untuk Operasi Rekening ----------------------
    def setor(self, jumlah, keterangan="Setoran"):
        self._validasi_aktif()
        if not isinstance(jumlah, (int, float)) or jumlah <= 0:
            raise ValueError("Jumlah setor harus angka positif!")
        self.__saldo += jumlah
        self._catat_transaksi(f"SETOR - {keterangan}", jumlah)
        print(f"  [+] Setor Rp {jumlah:,.0f} | Saldo: Rp {self.__saldo:,.0f}")

    def tarik(self, jumlah, keterangan="Penarikan"):
        self._validasi_aktif()
        if not isinstance(jumlah, (int, float)) or jumlah <= 0:
            raise ValueError("Jumlah tarik harus angka positif!")
        if jumlah > self.__saldo:
            raise ValueError(f"Saldo tidak cukup! Saldo: Rp {self.__saldo:,.0f}")
        if jumlah > self.LIMIT_TARIK:
            raise ValueError(f"Melebihi limit tarik Rp {self.LIMIT_TARIK:,.0f}!")
        self.__saldo -= jumlah
        self._catat_transaksi(f"TARIK - {keterangan}", -jumlah)
        print(f"  [-] Tarik Rp {jumlah:,.0f} | Saldo: Rp {self.__saldo:,.0f}")

    def transfer(self, rekening_tujuan, jumlah):
        self._validasi_aktif()
        if not isinstance(rekening_tujuan, RekeningBank):
            raise TypeError("Tujuan transfer harus objek RekeningBank!")
        
        # Tarik saldo dari rekening sumber
        self.tarik(jumlah, f"Transfer ke {rekening_tujuan.pemilik}")
        
        # Coba transfer ke rekening tujuan dengan mekanisme rollback
        try:
            rekening_tujuan.setor(jumlah, f"Transfer dari {self.__pemilik}")
        except Exception as e:
            # Rollback: jika sektor gagal, kembalikan uang ke rekening sumber
            self.setor(jumlah, f"BATAL - Transfer ke {rekening_tujuan.pemilik} (Gagal: {e})")
            raise RuntimeError(f"Transfer gagal dan telah dibatalkan. Alasan: {e}")

    def tutup(self):
        """Menutup rekening."""
        self._validasi_aktif()
        saldo_akhir   = self.__saldo
        self.__saldo  = 0.0
        self.__aktif  = False
        self._catat_transaksi("TUTUP REKENING", -saldo_akhir)
        print(f"  Rekening {self.nomor_rekening} ditutup.")

    def cetak_mutasi(self):
        """Tampilkan riwayat transaksi."""
        print(f"\n  {'='*48}")
        print(f"  MUTASI REKENING: {self.pemilik}")
        print(f"  No. Rekening: {self.nomor_rekening}")
        print(f"  {'='*48}")
        print(f"  {'Waktu':<22} {'Keterangan':<22} {'Jumlah':>12}")
        print(f"  {'-'*56}")
        for trx in self.__riwayat:
            tanda = "+" if trx['jumlah'] >= 0 else ""
            print(f"  {trx['waktu']:<22} {trx['keterangan']:<22} "
                  f"{tanda}Rp {trx['jumlah']:>10,.0f}")
        print(f"  {'-'*56}")
        print(f"  {'Saldo Akhir':<44} Rp {self.__saldo:>10,.0f}")

    # ---- Method Internal (Protected) ------------------------
    def _catat_transaksi(self, keterangan, jumlah):
        self.__riwayat.append({
            "waktu":      datetime.now().strftime("%Y-%m-%d %H:%M"),
            "keterangan": keterangan,
            "jumlah":     jumlah,
        })

    def _validasi_aktif(self):
        if not self.__aktif:
            raise PermissionError("Rekening sudah ditutup!")

    def __str__(self):
        status = "Aktif" if self.__aktif else "Tutup"
        return (f"Rekening {self.nomor_rekening} | Pemilik: {self.__pemilik} "
                f"| Saldo: Rp {self.__saldo:,.0f} | {status}")


# ---- Demo Rekening Bank -----
print("\nMembuka rekening...")
rek_budi = RekeningBank("budi santoso", "1234567890123456", saldo_awal=5_000_000)
rek_sari = RekeningBank("sari dewi",    "9876543210987654", saldo_awal=2_000_000)

print(f"\n{rek_budi}")
print(f"{rek_sari}")

print("\nTransaksi:")
rek_budi.setor(1_500_000, "Gaji Maret")
rek_budi.tarik(500_000,   "Bayar Kos")
rek_budi.transfer(rek_sari, 1_000_000)

print(f"\nBunga bulanan Budi: Rp {rek_budi.bunga_bulanan:,.0f}")

rek_budi.cetak_mutasi()

# Uji validasi
print("\nUji perlindungan enkapsulasi:")
try:
    rek_budi.tarik(50_000_000)
except ValueError as e:
    print(f"  Tarik melebihi saldo: {e}")

try:
    rek_budi.__saldo = 999_999_999
except AttributeError:
    print("  __saldo tidak bisa diakses langsung dari luar: Terlindungi!")

# Verifikasi bahwa saldo tidak berubah
print(f"  Saldo tetap aman: Rp {rek_budi.saldo:,.0f}")


# ============================================================
# STUDI KASUS 2: Sistem Inventori Produk
# ============================================================

print("\n" + "=" * 58)
print("  STUDI KASUS 2: Inventori Produk")
print("=" * 58)


class Produk:
    """Produk dalam sistem inventori dengan enkapsulasi stok."""

    def __init__(self, kode, nama, harga, stok_awal=0):
        self.__kode         = kode.upper()
        self.__nama         = nama.strip()
        self.__harga        = 0.0
        self.__stok         = 0
        self.__terjual      = 0
        self.__log          = []
        # gunakan setter
        self.harga  = harga
        if stok_awal > 0:
            self.tambah_stok(stok_awal, "Stok Awal")

    @property
    def kode(self):
        return self.__kode

    @property
    def nama(self):
        return self.__nama

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai):
        if not isinstance(nilai, (int, float)) or nilai < 0:
            raise ValueError("Harga harus >= 0!")
        self.__harga = float(nilai)

    @property
    def stok(self):
        return self.__stok

    @property
    def terjual(self):
        return self.__terjual

    @property
    def nilai_inventori(self):
        return self.__stok * self.__harga

    @property
    def status(self):
        if self.__stok == 0:   return "HABIS"
        if self.__stok <= 5:   return "KRITIS"
        if self.__stok <= 20:  return "RENDAH"
        return "TERSEDIA"

    def tambah_stok(self, jumlah, keterangan="Restock"):
        if jumlah <= 0:
            raise ValueError("Jumlah tambah stok harus positif!")
        self.__stok += jumlah
        self.__log.append(f"+{jumlah} ({keterangan})")

    def jual(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah jual harus positif!")
        if jumlah > self.__stok:
            raise ValueError(f"Stok tidak cukup! Stok: {self.__stok}")
        self.__stok    -= jumlah
        self.__terjual += jumlah
        self.__log.append(f"-{jumlah} (Penjualan)")
        return jumlah * self.__harga   # kembalikan total harga

    @property
    def log(self):
        return self.__log.copy()

    def __str__(self):
        return (f"[{self.__kode}] {self.__nama} | "
                f"Rp {self.__harga:,.0f} | Stok: {self.__stok} [{self.status}]")


# Demo Inventori
print()
laptop  = Produk("LPT-001", "Laptop ASUS VivoBook", 8_500_000, stok_awal=15)
mouse   = Produk("MSE-001", "Mouse Logitech M330",    150_000, stok_awal=50)
kboard  = Produk("KBD-001", "Keyboard Mechanical",    350_000, stok_awal=8)

produk_list = [laptop, mouse, kboard]
for p in produk_list:
    print(f"  {p}")

print("\nTransaksi penjualan:")
total_rev = 0
total_rev += laptop.jual(3)
print(f"  Jual 3 Laptop  -> Pendapatan: Rp {laptop.harga * 3:,.0f}")
total_rev += mouse.jual(10)
print(f"  Jual 10 Mouse  -> Pendapatan: Rp {mouse.harga * 10:,.0f}")
total_rev += kboard.jual(7)
print(f"  Jual 7 Keyboard -> Pendapatan: Rp {kboard.harga * 7:,.0f}")

print(f"\nTotal Pendapatan: Rp {total_rev:,.0f}")

print("\nStatus stok setelah penjualan:")
for p in produk_list:
    print(f"  {p} | Terjual: {p.terjual} | Nilai Inventori: Rp {p.nilai_inventori:,.0f}")

print("\nUji proteksi stok:")
try:
    mouse.jual(999)
except ValueError as e:
    print(f"  Jual lebih dari stok: {e}")

try:
    laptop.harga = -1000
except ValueError as e:
    print(f"  Harga negatif: {e}")


print("\n[OK] Selesai: 03_enkapsulasi_praktis.py")
