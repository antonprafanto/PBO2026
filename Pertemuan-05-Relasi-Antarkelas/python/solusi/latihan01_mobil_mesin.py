"""
Solusi Latihan 01 - Mobil dan Mesin (Komposisi)
Pertemuan 05 - Relasi Antarkelas

Ide penyelesaian:
- Mesin dibuat DI DALAM konstruktor Mobil. Setiap mobil punya mesinnya
  sendiri, dan kode di luar kelas tidak pernah menulis Mesin(...).
- Mobil meneruskan perintah nyalakan/matikan ke mesinnya (mengirim pesan).
- jalan(km) hanya berhasil jika mesin sedang menyala.

Cara menjalankan:
    python latihan01_mobil_mesin.py
"""


class Mesin:
    """Mesin mobil dengan kapasitas tertentu (cc)."""

    def __init__(self, kapasitas_cc: int):
        self._kapasitas_cc = kapasitas_cc
        self._menyala = False

    @property
    def menyala(self) -> bool:
        return self._menyala

    def hidupkan(self):
        self._menyala = True
        print(f"Mesin {self._kapasitas_cc} cc dihidupkan")

    def matikan(self):
        self._menyala = False
        print(f"Mesin {self._kapasitas_cc} cc dimatikan")

    def __str__(self) -> str:
        if self._menyala:
            status = "menyala"
        else:
            status = "mati"
        return f"mesin {self._kapasitas_cc} cc ({status})"


class Mobil:
    """Mobil yang membuat dan memiliki mesinnya sendiri (komposisi)."""

    def __init__(self, merek: str, kapasitas_cc: int):
        self._merek = merek
        self._mesin = Mesin(kapasitas_cc)  # mesin lahir bersama mobilnya
        self._odometer = 0

    def nyalakan(self):
        self._mesin.hidupkan()  # perintah diteruskan ke mesin

    def matikan(self):
        self._mesin.matikan()

    def jalan(self, km: int):
        if not self._mesin.menyala:  # mobil bertanya ke mesinnya
            print(f"{self._merek} belum bisa jalan: mesin masih mati")
            return
        self._odometer += km
        print(f"{self._merek} melaju {km} km")

    def __str__(self) -> str:
        return f"{self._merek}, {self._mesin}, odometer {self._odometer} km"


def main():
    mobil = Mobil("Avanza", 1300)  # tidak ada Mesin(...) di sini
    print("=== MOBIL BARU ===")
    print(mobil)

    print()
    print("=== PERJALANAN ===")
    mobil.jalan(5)
    mobil.nyalakan()
    mobil.jalan(12)
    mobil.jalan(5)
    mobil.matikan()

    print()
    print("=== SETELAH PERJALANAN ===")
    print(mobil)


if __name__ == "__main__":
    main()
