"""
Modul pembayaran: kelas induk Pembayaran dan tiga kelas anaknya.

Ketiga kelas anak meng-override method yang SAMA (nama_metode,
hitung_biaya_layanan, proses) dengan perilaku yang BERBEDA.
Pesanan cukup memanggil pembayaran.proses(...) tanpa perlu tahu
jenis pembayarannya. Itulah polimorfisme.
"""

from utilitas import format_rupiah


class Pembayaran:
    """Kelas induk semua metode pembayaran."""

    def nama_metode(self) -> str:
        return "Pembayaran umum"

    def hitung_biaya_layanan(self, total: int) -> int:
        """Biaya tambahan yang dibebankan ke pelanggan. Bawaannya 0."""
        return 0

    def proses(self, total: int) -> bool:
        """Memproses pembayaran. Mengembalikan True jika berhasil."""
        print(f"  Memproses pembayaran {format_rupiah(total)}")
        return True


class PembayaranTunai(Pembayaran):
    """Bayar dengan uang tunai. Bisa menghasilkan kembalian."""

    def __init__(self, uang_diterima: int):
        self._uang_diterima = uang_diterima
        self._kembalian = 0

    @property
    def kembalian(self) -> int:
        return self._kembalian

    def nama_metode(self) -> str:
        return "Tunai"

    def proses(self, total: int) -> bool:
        if self._uang_diterima < total:
            kurang = total - self._uang_diterima
            print(f"  Uang kurang {format_rupiah(kurang)}")
            return False
        self._kembalian = self._uang_diterima - total
        print(f"  Uang diterima {format_rupiah(self._uang_diterima)}, "
              f"kembalian {format_rupiah(self._kembalian)}")
        return True


class PembayaranQRIS(Pembayaran):
    """Simulasi QRIS: saldo e-wallet pelanggan disimpan di objek ini."""

    def __init__(self, saldo_ewallet: int):
        self._saldo = saldo_ewallet

    @property
    def saldo(self) -> int:
        return self._saldo

    def nama_metode(self) -> str:
        return "QRIS"

    def proses(self, total: int) -> bool:
        if self._saldo < total:
            print(f"  Saldo e-wallet tidak cukup "
                  f"(saldo {format_rupiah(self._saldo)})")
            return False
        self._saldo -= total
        print(f"  Saldo e-wallet terpotong {format_rupiah(total)}, "
              f"sisa {format_rupiah(self._saldo)}")
        return True


class PembayaranKartu(Pembayaran):
    """Kartu kredit: pelanggan dikenai biaya layanan 2%."""

    PERSEN_BIAYA = 2

    def __init__(self, nama_bank: str):
        self._nama_bank = nama_bank

    def nama_metode(self) -> str:
        return f"Kartu Kredit {self._nama_bank}"

    def hitung_biaya_layanan(self, total: int) -> int:
        return total * PembayaranKartu.PERSEN_BIAYA // 100

    def proses(self, total: int) -> bool:
        print(f"  Transaksi kartu {self._nama_bank} disetujui "
              f"sebesar {format_rupiah(total)}")
        return True
