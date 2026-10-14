"""
Modul pembayaran: kelas abstrak Pembayaran dan tiga kelas anaknya.

Sejak Pertemuan 11, proses() melempar PembayaranGagalError jika gagal.

Yang baru di Pertemuan 14: PembayaranFactory (pola FACTORY) untuk membuat
objek pembayaran dari pilihan berupa teks, misalnya "tunai" atau "qris".
Kode pemanggil tidak perlu tahu nama-nama kelas konkretnya.
"""

from abc import ABC, abstractmethod

from pengecualian import PembayaranGagalError
from utilitas import format_rupiah


class Pembayaran(ABC):
    """Kelas abstrak: kerangka untuk semua metode pembayaran."""

    @abstractmethod
    def nama_metode(self) -> str:
        """Nama metode pembayaran, misalnya 'Tunai'."""

    @abstractmethod
    def proses(self, total: int):
        """Memproses pembayaran. Melempar PembayaranGagalError jika gagal."""

    def hitung_biaya_layanan(self, total: int) -> int:
        """Biaya tambahan untuk pelanggan. Bawaannya 0 (boleh di-override)."""
        return 0

    def deskripsi(self, total: int) -> str:
        biaya = format_rupiah(self.hitung_biaya_layanan(total))
        return f"{self.nama_metode()} (biaya layanan {biaya})"


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

    def proses(self, total: int):
        if self._uang_diterima < total:
            kurang = total - self._uang_diterima
            raise PembayaranGagalError(self.nama_metode(),
                                       f"uang kurang {format_rupiah(kurang)}")
        self._kembalian = self._uang_diterima - total
        print(f"  Uang diterima {format_rupiah(self._uang_diterima)}, "
              f"kembalian {format_rupiah(self._kembalian)}")


class PembayaranQRIS(Pembayaran):
    """Simulasi QRIS: saldo e-wallet pelanggan disimpan di objek ini."""

    def __init__(self, saldo_ewallet: int):
        self._saldo = saldo_ewallet

    @property
    def saldo(self) -> int:
        return self._saldo

    def nama_metode(self) -> str:
        return "QRIS"

    def proses(self, total: int):
        if self._saldo < total:
            alasan = (f"saldo e-wallet tidak cukup "
                      f"(saldo {format_rupiah(self._saldo)})")
            raise PembayaranGagalError(self.nama_metode(), alasan)
        self._saldo -= total
        print(f"  Saldo e-wallet terpotong {format_rupiah(total)}, "
              f"sisa {format_rupiah(self._saldo)}")


class PembayaranKartu(Pembayaran):
    """Kartu kredit: pelanggan dikenai biaya layanan 2%."""

    PERSEN_BIAYA = 2

    def __init__(self, nama_bank: str):
        self._nama_bank = nama_bank

    def nama_metode(self) -> str:
        return f"Kartu Kredit {self._nama_bank}"

    def hitung_biaya_layanan(self, total: int) -> int:
        return total * PembayaranKartu.PERSEN_BIAYA // 100

    def proses(self, total: int):
        print(f"  Transaksi kartu {self._nama_bank} disetujui "
              f"sebesar {format_rupiah(total)}")


class PembayaranFactory:
    """Factory: membuat objek Pembayaran berdasarkan pilihan (teks)."""

    @staticmethod
    def buat(jenis: str, nominal: int = 0, bank: str = "") -> Pembayaran:
        """nominal = uang diterima (tunai) atau saldo e-wallet (qris)."""
        pilihan = jenis.lower()
        if pilihan == "tunai":
            return PembayaranTunai(nominal)
        if pilihan == "qris":
            return PembayaranQRIS(nominal)
        if pilihan == "kartu":
            return PembayaranKartu(bank)
        raise ValueError(f"Metode pembayaran tidak dikenal: {jenis}")
