"""
Contoh 03 - Sisi Gelap Singleton: State Global yang Diam-Diam Berubah
Pertemuan 14 - Design Pattern Dasar

Singleton praktis, tetapi isinya adalah STATE GLOBAL: siapa pun bisa
mengubahnya dari mana pun. Akibatnya:
- fungsi yang memakainya punya "ketergantungan tersembunyi" (tidak terlihat
  dari parameternya),
- hasil pengujian bisa bergantung pada URUTAN uji dijalankan.

Solusinya (ingat DIP di Pertemuan 13): kirim kebutuhan lewat parameter atau
konstruktor, sehingga setiap pengujian bisa memakai nilainya sendiri.

Cara menjalankan:
    python contoh03_bahaya_state_global.py
"""


class PengaturanPajak:
    """Singleton: persentase pajak untuk seluruh program."""

    _instance = None

    def __init__(self):
        if PengaturanPajak._instance is not None:
            raise RuntimeError("Gunakan PengaturanPajak.get_instance()")
        self._persen = 10

    @classmethod
    def get_instance(cls) -> "PengaturanPajak":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @property
    def persen(self) -> int:
        return self._persen

    @persen.setter
    def persen(self, nilai: int):
        self._persen = nilai


def harga_akhir(harga: int) -> int:
    # [1] ketergantungan tersembunyi: tidak terlihat dari parameternya
    persen = PengaturanPajak.get_instance().persen
    return harga + harga * persen // 100


def uji_harga_normal() -> str:
    """Rp10000 ditambah pajak 10% harus menjadi Rp11000."""
    hasil = harga_akhir(10000)
    return "LULUS" if hasil == 11000 else f"GAGAL (dapat Rp{hasil})"


def uji_acara_bebas_pajak() -> str:
    """Saat acara bebas pajak, Rp10000 harus tetap Rp10000."""
    PengaturanPajak.get_instance().persen = 0  # [2] mengubah state global...
    hasil = harga_akhir(10000)  # ...dan lupa mengembalikannya
    return "LULUS" if hasil == 10000 else f"GAGAL (dapat Rp{hasil})"


class KalkulatorHarga:
    """[3] Solusi: persen pajak DIKIRIM lewat konstruktor (dependency injection)."""

    def __init__(self, persen_pajak: int):
        self._persen_pajak = persen_pajak

    def harga_akhir(self, harga: int) -> int:
        return harga + harga * self._persen_pajak // 100


def main():
    print("=== PUTARAN 1: DUA UJI DIJALANKAN ===")
    print(f"Uji harga normal      : {uji_harga_normal()}")
    print(f"Uji acara bebas pajak : {uji_acara_bebas_pajak()}")

    print()
    print("=== PUTARAN 2: UJI YANG SAMA DIULANG ===")
    print(f"Uji harga normal      : {uji_harga_normal()}")  # [4] kini gagal!
    print(f"Pajak sekarang {PengaturanPajak.get_instance().persen}%, "
          "sisa perubahan uji sebelumnya")

    print()
    print("=== SOLUSI: KIRIM NILAINYA LEWAT KONSTRUKTOR ===")
    normal = KalkulatorHarga(10)  # [5] setiap uji punya objeknya sendiri
    bebas_pajak = KalkulatorHarga(0)
    print(f"Pajak 10%: Rp10000 -> Rp{normal.harga_akhir(10000)}")
    print(f"Pajak 0% : Rp10000 -> Rp{bebas_pajak.harga_akhir(10000)}")
    print(f"Diulang  : Rp10000 -> Rp{normal.harga_akhir(10000)} (tetap benar)")


if __name__ == "__main__":
    main()
