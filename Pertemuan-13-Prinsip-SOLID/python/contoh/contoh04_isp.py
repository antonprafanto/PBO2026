"""
Contoh 04 - ISP: Interface Kecil Lebih Baik daripada Interface Gemuk
Pertemuan 13 - Prinsip SOLID

Versi MELANGGAR: kontrak PerangkatKasir "gemuk" (tiga kemampuan sekaligus).
PrinterBluetooth hanya bisa mencetak, tetapi dipaksa menulis dua method
palsu yang melempar exception.

Versi SESUAI ISP: kontrak dipecah menjadi PencetakStruk, PemindaiBarcode,
dan LaciUang. Setiap perangkat hanya memenuhi kontrak yang benar-benar
sesuai kemampuannya. KasirLengkap memenuhi ketiganya sekaligus.

Cara menjalankan:
    python contoh04_isp.py
"""

from abc import ABC, abstractmethod


# ------------------------------------------------------------ MELANGGAR ISP
class PerangkatKasir(ABC):
    """Kontrak GEMUK: siapa pun yang memenuhinya wajib bisa tiga hal."""

    @abstractmethod
    def cetak_struk(self, teks: str):
        """Mencetak teks struk."""

    @abstractmethod
    def pindai_barcode(self) -> str:
        """Membaca kode barcode barang."""

    @abstractmethod
    def buka_laci(self):
        """Membuka laci uang."""


class MesinKasirLengkap(PerangkatKasir):
    def cetak_struk(self, teks: str):
        print(f"[Mesin Kasir] mencetak: {teks}")

    def pindai_barcode(self) -> str:
        return "8991234567890"

    def buka_laci(self):
        print("[Mesin Kasir] laci terbuka")


class PrinterBluetooth(PerangkatKasir):
    def cetak_struk(self, teks: str):
        print(f"[Printer Bluetooth] mencetak: {teks}")

    def pindai_barcode(self) -> str:  # [1] method palsu: dipaksa ada
        raise NotImplementedError("Printer Bluetooth tidak punya pemindai barcode")

    def buka_laci(self):  # method palsu kedua
        raise NotImplementedError("Printer Bluetooth tidak punya laci uang")


# -------------------------------------------------------------- SESUAI ISP
class PencetakStruk(ABC):  # [2] tiga kontrak kecil, masing-masing satu kemampuan
    @abstractmethod
    def cetak_struk(self, teks: str):
        """Mencetak teks struk."""


class PemindaiBarcode(ABC):
    @abstractmethod
    def pindai_barcode(self) -> str:
        """Membaca kode barcode barang."""


class LaciUang(ABC):
    @abstractmethod
    def buka_laci(self):
        """Membuka laci uang."""


class KasirLengkap(PencetakStruk, PemindaiBarcode, LaciUang):  # [3]
    def cetak_struk(self, teks: str):
        print(f"[Mesin Kasir] mencetak: {teks}")

    def pindai_barcode(self) -> str:
        return "8991234567890"

    def buka_laci(self):
        print("[Mesin Kasir] laci terbuka")


class PrinterThermal(PencetakStruk):  # [4] cukup satu kontrak, tanpa method palsu
    def cetak_struk(self, teks: str):
        print(f"[Printer Thermal] mencetak: {teks}")


class PemindaiGenggam(PemindaiBarcode):
    def pindai_barcode(self) -> str:
        return "8997654321098"


def main():
    print("=== VERSI MELANGGAR ISP (interface gemuk) ===")
    perangkat_lama: list[PerangkatKasir] = [MesinKasirLengkap(), PrinterBluetooth()]
    for perangkat in perangkat_lama:
        perangkat.cetak_struk("Terima kasih!")
        try:
            print(f"Hasil pindai: {perangkat.pindai_barcode()}")
        except NotImplementedError as e:
            print(f"[KEJUTAN] {e}")

    print()
    print("=== VERSI SESUAI ISP (interface kecil) ===")
    kasir = KasirLengkap()
    pencetak: list[PencetakStruk] = [kasir, PrinterThermal()]  # [5]
    pemindai: list[PemindaiBarcode] = [kasir, PemindaiGenggam()]
    print("-- semua PencetakStruk --")
    for alat in pencetak:
        alat.cetak_struk("Terima kasih!")
    print("-- semua PemindaiBarcode --")
    for alat in pemindai:
        print(f"Hasil pindai: {alat.pindai_barcode()}")
    print("Setiap perangkat hanya berjanji sebanyak kemampuannya.")


if __name__ == "__main__":
    main()
