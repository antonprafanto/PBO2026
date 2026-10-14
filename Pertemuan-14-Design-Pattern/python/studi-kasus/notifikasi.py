"""
Modul notifikasi: dua pengamat (observer) konkret untuk Pesanan.

- LayarDapur          : menampilkan pesanan yang harus disiapkan dapur
- NotifikasiPelanggan : mengirim pesan (simulasi SMS) ke pelanggan
"""

from pengamat import PengamatPesanan
from pesanan import Pesanan


class LayarDapur(PengamatPesanan):
    """Layar di dapur yang menampilkan pesanan masuk."""

    def perbarui(self, pesanan: Pesanan):
        if pesanan.status == "LUNAS":
            daftar = ", ".join(str(item) for item in pesanan.daftar_item)
            print(f"  [DAPUR] Pesanan baru {pesanan.nomor}: {daftar}")
        else:
            print(f"  [DAPUR] {pesanan.nomor} -> {pesanan.status}")


class NotifikasiPelanggan(PengamatPesanan):
    """Mengirim kabar status pesanan ke nomor HP pelanggan (simulasi)."""

    def perbarui(self, pesanan: Pesanan):
        pelanggan = pesanan.pelanggan
        print(f"  [SMS ke {pelanggan.no_hp}] Halo {pelanggan.nama}, "
              f"status pesanan {pesanan.nomor}: {pesanan.status}")
