"""
Contoh 07 - typing.Protocol: Duck Typing yang Diresmikan (khusus Python)
Pertemuan 10 - Abstract Class dan Interface

Dengan ABC, sebuah kelas harus MEWARISI kontraknya secara tertulis:
    class Lampu(BisaDinyalakan): ...
Dengan Protocol, kelas TIDAK perlu mewarisi apa pun. Cukup punya method
dengan nama dan bentuk yang cocok. Ini disebut kontrak struktural.

Yang memeriksa kecocokan Protocol adalah alat pemeriksa tipe seperti mypy
atau Pylance (di VS Code), bukan Python saat program berjalan.
Contoh ini khusus Python. Java tidak punya padanannya (lihat Jembatan).

Cara menjalankan:
    python contoh07_protocol.py
"""

from typing import Protocol, runtime_checkable


@runtime_checkable  # [3] agar Protocol ini boleh dipakai di isinstance()
class BisaBersuara(Protocol):  # [1] kontrak struktural
    """Apa saja yang punya method bersuara() -> str."""

    def bersuara(self) -> str:
        ...


class Kucing:  # [2] TIDAK mewarisi BisaBersuara
    """Kucing peliharaan."""

    def bersuara(self) -> str:
        return "Meong!"


class Kentongan:
    """Kentongan bambu untuk ronda malam."""

    def bersuara(self) -> str:
        return "Tung tung tung!"


class AlarmPonsel:
    """Alarm di ponsel yang berbunyi pada jam tertentu."""

    def __init__(self, jam: str):
        self._jam = jam

    def bersuara(self) -> str:
        return f"Kring! Sudah jam {self._jam}, ayo berangkat kuliah!"


class Batu:
    """Batu tidak punya method bersuara()."""


def bunyikan_semua(daftar: list[BisaBersuara]):  # [4] menerima apa saja yang cocok
    for benda in daftar:
        print(f"{type(benda).__name__:<11}: {benda.bersuara()}")


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    print("=== BUNYIKAN SEMUA ===")
    bunyikan_semua([Kucing(), Kentongan(), AlarmPonsel("07.00")])

    print()
    print("=== CEK DENGAN isinstance() ===")
    for benda in [Kucing(), Kentongan(), Batu()]:
        cocok = ya_tidak(isinstance(benda, BisaBersuara))  # [5]
        print(f"{type(benda).__name__} cocok dengan BisaBersuara? {cocok}")


if __name__ == "__main__":
    main()
