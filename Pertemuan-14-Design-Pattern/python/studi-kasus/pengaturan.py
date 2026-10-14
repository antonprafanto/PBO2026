"""
Modul pengaturan: kelas PengaturanKedai dengan pola SINGLETON.

Singleton menjamin hanya ada SATU objek pengaturan di seluruh program.
Bagian program yang membutuhkannya (pesanan dan struk) membaca nama kedai,
alamat, dan persentase pajak dari objek yang sama sehingga tidak mungkin berbeda.

Cara memakainya:
    pengaturan = PengaturanKedai.get_instance()
"""


class PengaturanKedai:
    """Pengaturan global KedaiKita (Singleton)."""

    _instance = None  # tempat menyimpan satu-satunya objek

    def __init__(self):
        if PengaturanKedai._instance is not None:
            raise RuntimeError("PengaturanKedai adalah Singleton. "
                               "Gunakan PengaturanKedai.get_instance()")
        self._nama_kedai = "KedaiKita"
        self._alamat = "Jl. Pramuka No. 10, Samarinda"
        self._pajak_persen = 10  # Pajak Barang dan Jasa Tertentu (PBJT) 10%

    @classmethod
    def get_instance(cls) -> "PengaturanKedai":
        """Mengembalikan satu-satunya objek; dibuat saat pertama kali diminta."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def nama_kedai(self) -> str:
        return self._nama_kedai

    @property
    def alamat(self) -> str:
        return self._alamat

    @property
    def pajak_persen(self) -> int:
        return self._pajak_persen

    @pajak_persen.setter
    def pajak_persen(self, nilai: int):
        if nilai < 0 or nilai > 100:
            raise ValueError("Pajak harus 0 sampai 100 persen")
        self._pajak_persen = nilai
