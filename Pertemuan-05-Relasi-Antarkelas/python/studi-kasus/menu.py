"""
Modul menu: kelas Menu (sama seperti Pertemuan 04, kini di file sendiri).

Perubahan kecil: penghitung jumlah menu (atribut kelas) dihapus,
karena sekarang tugas menghitung menu dipegang oleh kelas Kedai.

File ini hanya berisi kelas, jadi tidak mencetak apa-apa jika dijalankan
sendiri. Jalankan main.py dari folder studi-kasus.
"""

from utilitas import format_rupiah


class Menu:
    """Satu menu KedaiKita. Datanya dilindungi dan hanya diubah lewat method."""

    def __init__(self, kode: str, nama: str, harga: int, kategori: str,
                 stok: int = 0):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        self._kode = kode
        self._nama = nama
        self._kategori = kategori
        self._stok = stok
        self.harga = harga  # lewat setter, jadi ikut divalidasi

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def kategori(self) -> str:
        return self._kategori

    @property
    def stok(self) -> int:
        return self._stok

    @property
    def harga(self) -> int:
        return self._harga

    @harga.setter
    def harga(self, nilai: int):
        if nilai <= 0:
            raise ValueError("Harga harus lebih dari 0")
        self._harga = nilai

    def tambah_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self._stok += jumlah

    def kurangi_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        if jumlah > self._stok:
            raise ValueError(f"Stok {self._nama} tidak cukup (sisa {self._stok})")
        self._stok -= jumlah

    def hitung_total(self, jumlah: int) -> int:
        return self._harga * jumlah

    def harga_setelah_diskon(self, persen: int) -> int:
        potongan = self._harga * persen // 100
        return self._harga - potongan

    def stok_cukup(self, jumlah: int) -> bool:
        return self._stok >= jumlah

    def __str__(self) -> str:
        return (f"[{self._kode}] {self._nama} ({self._kategori}) - "
                f"{format_rupiah(self._harga)} | stok {self._stok}")
