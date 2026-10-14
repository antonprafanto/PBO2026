"""
Modul menu: kelas induk Menu dan dua kelas anaknya, Makanan dan Minuman.

Hierarki pewarisan:
        Menu            <- kelas induk (superclass)
       /    \\
  Makanan  Minuman      <- kelas anak (subclass)

Makanan dan Minuman MEWARISI semua atribut dan method Menu, lalu:
- menambah atribut khusus (level_pedas / dingin),
- meng-override __str__ agar informasinya lebih lengkap.
"""

from utilitas import format_rupiah


class Menu:
    """Kelas induk: data dan perilaku yang dimiliki SEMUA jenis menu."""

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


class Makanan(Menu):
    """Menu kategori makanan. Tambahan: level pedas 0 sampai 5."""

    def __init__(self, kode: str, nama: str, harga: int, stok: int = 0,
                 level_pedas: int = 0):
        # Panggil konstruktor induk. Kategori diisi otomatis "Makanan".
        super().__init__(kode, nama, harga, "Makanan", stok)
        self.level_pedas = level_pedas  # lewat setter, jadi ikut divalidasi

    @property
    def level_pedas(self) -> int:
        return self._level_pedas

    @level_pedas.setter
    def level_pedas(self, nilai: int):
        if nilai < 0 or nilai > 5:
            raise ValueError("Level pedas harus 0 sampai 5")
        self._level_pedas = nilai

    def __str__(self) -> str:
        # Override: pakai teks dari induk, lalu tambahkan info pedas
        return f"{super().__str__()} | pedas level {self._level_pedas}"


class Minuman(Menu):
    """Menu kategori minuman. Tambahan: disajikan dingin atau panas."""

    def __init__(self, kode: str, nama: str, harga: int, stok: int = 0,
                 dingin: bool = True):
        super().__init__(kode, nama, harga, "Minuman", stok)
        self._dingin = dingin

    @property
    def dingin(self) -> bool:
        return self._dingin

    def __str__(self) -> str:
        suhu = "dingin" if self._dingin else "panas"
        return f"{super().__str__()} | {suhu}"
