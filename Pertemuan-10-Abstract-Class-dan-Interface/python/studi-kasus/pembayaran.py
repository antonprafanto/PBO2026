"""
Modul pembayaran: kelas ABSTRAK Pembayaran dan tiga kelas anaknya.

Yang baru di Pertemuan 10:
- Pembayaran kini kelas abstrak (turunan ABC). Objeknya TIDAK BISA dibuat
  langsung karena "pembayaran umum" memang tidak ada di dunia nyata.
- nama_metode() dan proses() menjadi method abstrak: setiap kelas anak
  WAJIB meng-override keduanya.
- hitung_biaya_layanan() tetap method biasa (konkret), dan deskripsi()
  adalah method konkret baru. Keduanya langsung diwarisi kelas anak.
"""

from abc import ABC, abstractmethod

from utilitas import format_rupiah


class Pembayaran(ABC):
    """Kelas abstrak: kerangka untuk semua metode pembayaran."""

    @abstractmethod
    def nama_metode(self) -> str:
        """Nama metode pembayaran, misalnya 'Tunai'."""

    @abstractmethod
    def proses(self, total: int) -> bool:
        """Memproses pembayaran. Mengembalikan True jika berhasil."""

    def hitung_biaya_layanan(self, total: int) -> int:
        """Biaya tambahan untuk pelanggan. Bawaannya 0 (boleh di-override)."""
        return 0

    def deskripsi(self, total: int) -> str:
        """Method konkret yang memanggil method abstrak."""
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
