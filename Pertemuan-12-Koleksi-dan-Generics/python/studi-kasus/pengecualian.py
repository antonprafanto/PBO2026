"""
Modul pengecualian: exception khusus milik KedaiKita.

Hierarki:
    Exception                  (bawaan Python)
    +-- KedaiError             (induk semua error KedaiKita)
        +-- StokTidakCukupError
        +-- MenuTidakDitemukanError
        +-- PembayaranGagalError

Karena semuanya turunan KedaiError, kita bisa menangkapnya satu per satu
ATAU sekaligus dengan "except KedaiError".
"""


class KedaiError(Exception):
    """Induk semua error khusus KedaiKita."""


class StokTidakCukupError(KedaiError):
    """Dilempar saat jumlah yang dipesan melebihi stok."""

    def __init__(self, nama_menu: str, diminta: int, tersedia: int):
        super().__init__(f"Stok {nama_menu} tidak cukup: "
                         f"diminta {diminta}, tersedia {tersedia}")
        self.nama_menu = nama_menu
        self.diminta = diminta
        self.tersedia = tersedia


class MenuTidakDitemukanError(KedaiError):
    """Dilempar saat kode menu tidak terdaftar."""

    def __init__(self, kode: str):
        super().__init__(f"Menu dengan kode {kode} tidak ditemukan")
        self.kode = kode


class PembayaranGagalError(KedaiError):
    """Dilempar saat pembayaran tidak bisa diselesaikan."""

    def __init__(self, metode: str, alasan: str):
        super().__init__(f"Pembayaran {metode} gagal: {alasan}")
        self.metode = metode
        self.alasan = alasan
