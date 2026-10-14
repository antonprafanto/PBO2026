"""
Contoh 04 - Urutan Konstruktor dan Pewarisan Bertingkat (Multilevel)
Pertemuan 07 - Pewarisan (Inheritance)

Tiga tingkat: Perangkat -> Komputer -> Laptop.
Setiap konstruktor mencetak pesan SETELAH memanggil konstruktor induknya,
sehingga kita bisa melihat urutannya: bagian induk selalu selesai lebih dulu.
Laptop juga bisa memakai method dari SEMUA tingkat di atasnya.

Cara menjalankan:
    python contoh04_urutan_konstruktor.py
"""


class Perangkat:
    """Tingkat 1: semua perangkat elektronik."""

    def __init__(self, merek: str):
        self._merek = merek
        print(f"  Bagian Perangkat selesai: merek {merek}")  # [1]

    def nyalakan(self) -> str:
        return f"{self._merek} dinyalakan"


class Komputer(Perangkat):
    """Tingkat 2: Komputer adalah Perangkat."""

    def __init__(self, merek: str, ram_gb: int):
        super().__init__(merek)  # [2] minta induk menyiapkan bagiannya dulu
        self._ram_gb = ram_gb
        print(f"  Bagian Komputer selesai: RAM {ram_gb} GB")

    def jalankan(self, program: str) -> str:
        return f"{program} berjalan dengan RAM {self._ram_gb} GB"


class Laptop(Komputer):
    """Tingkat 3: Laptop adalah Komputer, dan karena itu juga Perangkat."""

    def __init__(self, merek: str, ram_gb: int, baterai_jam: int):
        super().__init__(merek, ram_gb)  # [3] induk langsung Laptop adalah Komputer
        self._baterai_jam = baterai_jam
        print(f"  Bagian Laptop selesai: baterai {baterai_jam} jam")

    def cek_baterai(self) -> str:
        return f"Baterai tahan {self._baterai_jam} jam"


def main():
    print("=== MEMBUAT LAPTOP (3 TINGKAT) ===")
    laptop = Laptop("Lenovo", 16, 8)  # [4]

    print()
    print("=== MEMBUAT KOMPUTER (2 TINGKAT) ===")
    Komputer("Dell", 32)  # [5] hanya dua bagian yang disiapkan

    print()
    print("=== METHOD DARI SETIAP TINGKAT ===")
    print(laptop.nyalakan())  # [6] warisan dari "kakek" (Perangkat)
    print(laptop.jalankan("VS Code"))  # warisan dari induk (Komputer)
    print(laptop.cek_baterai())  # milik Laptop sendiri


if __name__ == "__main__":
    main()
