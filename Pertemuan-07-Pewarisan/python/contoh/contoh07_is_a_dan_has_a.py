"""
Contoh 07 - is-a atau has-a? Kapan TIDAK Memakai Pewarisan
Pertemuan 07 - Pewarisan (Inheritance)

Dua rancangan untuk "mobil dan mesinnya":
- KELIRU : MobilKeliru mewarisi Mesin  -> "mobil ADALAH mesin" (janggal).
- TEPAT  : MobilTepat menyimpan objek Mesin sebagai atribut
           -> "mobil PUNYA mesin" (has-a, seperti relasi di Pertemuan 05).

Cara menjalankan:
    python contoh07_is_a_dan_has_a.py
"""


class Mesin:
    """Mesin kendaraan dengan kapasitas tertentu (cc)."""

    def __init__(self, cc: int):
        self._cc = cc

    def hidupkan(self) -> str:
        return f"Mesin {self._cc} cc menyala"


class MobilKeliru(Mesin):  # [1] KELIRU: mobil dianggap "adalah" mesin
    """Rancangan keliru: mobil mewarisi mesin hanya demi memakai hidupkan()."""

    def __init__(self, nama: str, cc: int):
        super().__init__(cc)
        self._nama = nama

    def jalan(self) -> str:
        return f"{self._nama}: {self.hidupkan()}"


class MobilTepat:  # [2] TEPAT: mobil "punya" mesin
    """Rancangan tepat: mobil MENYIMPAN objek Mesin sebagai atribut."""

    def __init__(self, nama: str, mesin: Mesin):
        self._nama = nama
        self._mesin = mesin  # [3] has-a: atribut berisi objek lain

    def jalan(self) -> str:
        return f"{self._nama}: {self._mesin.hidupkan()}"  # [4] tugas diteruskan

    def ganti_mesin(self, mesin_baru: Mesin):  # [5] bagiannya bisa diganti
        self._mesin = mesin_baru


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    print("=== RANCANGAN KELIRU: MOBIL MEWARISI MESIN ===")
    avanza = MobilKeliru("Avanza", 1300)
    print(avanza.jalan())
    print(f"Avanza adalah Mesin? {ya_tidak(isinstance(avanza, Mesin))} (janggal!)")

    print()
    print("=== RANCANGAN TEPAT: MOBIL PUNYA MESIN ===")
    xenia = MobilTepat("Xenia", Mesin(1300))
    print(xenia.jalan())
    xenia.ganti_mesin(Mesin(1500))
    print(f"Setelah ganti mesin -> {xenia.jalan()}")


if __name__ == "__main__":
    main()
