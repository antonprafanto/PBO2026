"""
Contoh 06 - Strategy: Menukar Cara Menghitung Ongkos Kirim
Pertemuan 14 - Design Pattern Dasar

Satu paket bisa dikirim dengan beberapa layanan: Reguler, Kilat, Hemat.
Setiap layanan punya RUMUS ongkir sendiri. Pola STRATEGY membungkus setiap
rumus menjadi kelas tersendiri (sebuah "strategi"), lalu objek Pengiriman
(context) cukup memanggil strategi yang sedang dipasang.

- Ganti layanan  = tukar objek strategi (bisa saat program berjalan).
- Layanan baru   = kelas strategi baru; kelas Pengiriman tidak diubah (OCP).

Cara menjalankan:
    python contoh06_strategy_ongkir.py
"""

from abc import ABC, abstractmethod


class StrategiOngkir(ABC):
    """Strategy: kontrak semua cara menghitung ongkos kirim."""

    @abstractmethod
    def nama(self) -> str:
        """Nama layanan untuk ditampilkan."""

    @abstractmethod
    def hitung(self, berat_kg: int) -> int:
        """Ongkos kirim dalam rupiah."""


class OngkirReguler(StrategiOngkir):
    def nama(self) -> str:
        return "Reguler (3 hari)"

    def hitung(self, berat_kg: int) -> int:
        return 8000 * berat_kg


class OngkirKilat(StrategiOngkir):
    """Lebih mahal per kg, ditambah biaya tetap Rp5000."""

    def nama(self) -> str:
        return "Kilat (besok tiba)"

    def hitung(self, berat_kg: int) -> int:
        return 15000 * berat_kg + 5000


class OngkirHemat(StrategiOngkir):
    """Murah per kg, tetapi berat minimal dihitung 3 kg."""

    def nama(self) -> str:
        return "Hemat (5 hari)"

    def hitung(self, berat_kg: int) -> int:
        return 5000 * max(berat_kg, 3)


class Pengiriman:
    """Context: memakai strategi ongkir tanpa tahu rumus di dalamnya."""

    def __init__(self, berat_kg: int, strategi: StrategiOngkir):
        self._berat_kg = berat_kg
        self._strategi = strategi  # [1] strategi disimpan sebagai atribut

    def atur_strategi(self, strategi: StrategiOngkir):  # [2] bisa ditukar
        self._strategi = strategi

    def ongkir(self) -> int:
        return self._strategi.hitung(self._berat_kg)  # [3] didelegasikan

    def ringkasan(self) -> str:
        return f"{self._strategi.nama():<20} Rp{self.ongkir()}"


class OngkirAmbilSendiri(StrategiOngkir):
    """Strategi BARU: paket diambil sendiri di gerai, tanpa ongkir."""

    def nama(self) -> str:
        return "Ambil di gerai"

    def hitung(self, berat_kg: int) -> int:
        return 0


def main():
    paket = Pengiriman(2, OngkirReguler())
    print("=== PAKET 2 KG DARI SAMARINDA KE BONTANG ===")
    for strategi in [OngkirReguler(), OngkirKilat(), OngkirHemat()]:
        paket.atur_strategi(strategi)  # [4] tukar saat program berjalan
        print(paket.ringkasan())

    print()
    print("=== STRATEGI BARU, KELAS Pengiriman TIDAK DIUBAH ===")
    paket.atur_strategi(OngkirAmbilSendiri())  # [5]
    print(paket.ringkasan())


if __name__ == "__main__":
    main()
