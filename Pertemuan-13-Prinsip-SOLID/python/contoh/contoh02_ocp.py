"""
Contoh 02 - OCP: Terbuka untuk Ditambah, Tertutup untuk Diubah
Pertemuan 13 - Prinsip SOLID

Versi MELANGGAR: KalkulatorOngkirKaku memilih rumus dengan rantai if/elif.
Layanan baru (Same Day) belum dikenal, dan satu-satunya cara menambahkannya
adalah MEMBONGKAR method hitung() yang sudah berjalan.

Versi SESUAI OCP: setiap layanan adalah kelas turunan LayananKirim.
Layanan Same Day ditambahkan sebagai kelas BARU; KalkulatorOngkir dan
layanan lama tidak disentuh sama sekali.

Cara menjalankan:
    python contoh02_ocp.py
"""

from abc import ABC, abstractmethod


def format_rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


# ------------------------------------------------------------ MELANGGAR OCP
class KalkulatorOngkirKaku:
    """Setiap layanan baru memaksa method hitung() dibongkar."""

    def hitung(self, layanan: str, berat_kg: int) -> int:
        if layanan == "reguler":
            return 9000 * berat_kg
        elif layanan == "kilat":
            return 15000 * berat_kg
        return 0  # [1] layanan lain belum dikenal: diam-diam dianggap gratis!


# -------------------------------------------------------------- SESUAI OCP
class LayananKirim(ABC):
    """Kontrak semua layanan pengiriman."""

    @abstractmethod
    def nama(self) -> str:
        """Nama layanan untuk ditampilkan."""

    @abstractmethod
    def ongkir(self, berat_kg: int) -> int:
        """Ongkos kirim dalam rupiah untuk berat tertentu."""


class LayananReguler(LayananKirim):
    def nama(self) -> str:
        return "Reguler"

    def ongkir(self, berat_kg: int) -> int:
        return 9000 * berat_kg


class LayananKilat(LayananKirim):
    def nama(self) -> str:
        return "Kilat"

    def ongkir(self, berat_kg: int) -> int:
        return 15000 * berat_kg


class LayananSameDay(LayananKirim):  # [2] layanan BARU = kelas baru, kode lama aman
    def nama(self) -> str:
        return "Same Day"

    def ongkir(self, berat_kg: int) -> int:
        return 25000 + 5000 * berat_kg


class KalkulatorOngkir:
    """Tidak pernah menyebut nama layanan apa pun, jadi tidak perlu diubah."""

    def hitung(self, layanan: LayananKirim, berat_kg: int) -> int:
        if berat_kg < 1:  # aturan umum: berat dihitung minimal 1 kg
            berat_kg = 1
        return layanan.ongkir(berat_kg)  # [3] polimorfisme bekerja di sini


def main():
    berat = 3

    print("=== VERSI MELANGGAR OCP (rantai percabangan) ===")
    kaku = KalkulatorOngkirKaku()
    for layanan in ["reguler", "kilat", "sameday"]:
        print(f"{layanan:<9}{berat} kg: {format_rupiah(kaku.hitung(layanan, berat))}")
    print("Layanan baru dianggap gratis! Method hitung() harus dibongkar dulu.")

    print()
    print("=== VERSI SESUAI OCP (satu kelas per layanan) ===")
    kalkulator = KalkulatorOngkir()
    daftar_layanan = [LayananReguler(), LayananKilat(), LayananSameDay()]
    for layanan in daftar_layanan:
        ongkir = kalkulator.hitung(layanan, berat)
        print(f"{layanan.nama():<9}{berat} kg: {format_rupiah(ongkir)}")
    print("Layanan Same Day cukup ditambahkan sebagai kelas baru.")


if __name__ == "__main__":
    main()
