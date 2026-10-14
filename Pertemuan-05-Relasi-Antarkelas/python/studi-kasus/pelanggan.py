"""
Modul pelanggan: kelas Pelanggan (sama seperti Pertemuan 04, kini di file sendiri).

File ini hanya berisi kelas, jadi tidak mencetak apa-apa jika dijalankan
sendiri. Jalankan main.py dari folder studi-kasus.
"""


class Pelanggan:
    """Pelanggan KedaiKita. Poin hanya berubah lewat method resmi."""

    def __init__(self, nama: str, no_hp: str):
        self._nama = nama
        self._no_hp = no_hp
        self._poin = 0

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def no_hp(self) -> str:
        return self._no_hp

    @property
    def poin(self) -> int:
        return self._poin

    def tambah_poin(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Poin yang ditambahkan harus lebih dari 0")
        self._poin += jumlah

    def tukar_poin(self, jumlah: int) -> int:
        """Menukar poin menjadi potongan harga. 1 poin = Rp1.000."""
        if jumlah > self._poin:
            raise ValueError(f"Poin tidak cukup (sisa {self._poin})")
        self._poin -= jumlah
        return jumlah * 1000

    def __str__(self) -> str:
        return f"{self._nama} ({self._no_hp}) - {self._poin} poin"
