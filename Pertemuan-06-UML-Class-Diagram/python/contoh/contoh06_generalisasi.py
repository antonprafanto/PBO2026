"""
Contoh 06 - Generalisasi: Pratinjau Pewarisan
Pertemuan 06 - UML Class Diagram

Diagram (versi Python, sintaks Mermaid):

    Karyawan <|-- Barista
    Karyawan <|-- Kasir

- Segitiga KOSONG menunjuk ke kelas INDUK (Karyawan).
- Barista dan Kasir mewarisi isi Karyawan, sehingga di diagram kotak
  kelas anak hanya berisi anggota yang BARU.
- Sintaks pewarisan selengkapnya (super(), override, dan lainnya)
  dipelajari di Pertemuan 07. Di sini kita cukup melihat wujud panahnya.

Cara menjalankan:
    python contoh06_generalisasi.py
"""


class Karyawan:
    """Data dan perilaku yang dimiliki SEMUA karyawan kafe."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama

    def absen(self) -> str:
        return f"{self._nama} sudah absen masuk"


class Barista(Karyawan):  # [1] Barista ADALAH Karyawan: panah menunjuk ke induk
    """Karyawan yang meracik minuman."""

    def racik(self, minuman: str) -> str:  # [2] anggota baru milik Barista
        return f"{self.nama} meracik {minuman}"


class Kasir(Karyawan):
    """Karyawan yang menerima pembayaran."""

    def terima_uang(self, jumlah: int) -> str:
        return f"{self.nama} menerima uang Rp{jumlah}"


def main():
    dimas = Barista("Dimas")
    sari = Kasir("Sari")

    print("=== SHIFT PAGI ===")
    print(dimas.absen())  # [3] method warisan dari Karyawan
    print(sari.absen())
    print(dimas.racik("Kopi Susu Gula Aren"))
    print(sari.terima_uang(50000))

    print()
    print("=== PANAH GENERALISASI DI DALAM PROGRAM ===")
    print(f"Induk Barista: {Barista.__bases__[0].__name__}")  # [4]
    print(f"Induk Kasir  : {Kasir.__bases__[0].__name__}")


if __name__ == "__main__":
    main()
