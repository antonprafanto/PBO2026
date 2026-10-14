"""
Contoh 04 - Simple Factory: Membuat Kendaraan dari Pilihan Teks
Pertemuan 14 - Design Pattern Dasar

Aplikasi ojek online menerima pilihan berupa TEKS ("motor", "mobil", ...).
Tanpa factory, setiap bagian program yang butuh kendaraan menulis if/elif
yang sama berulang-ulang. Dengan SIMPLE FACTORY, keputusan "kelas mana yang
dibuat" dikumpulkan di SATU tempat: KendaraanFactory.buat(jenis).

Kode pemanggil cukup mengenal kelas abstrak Kendaraan. Ia tidak perlu tahu
nama kelas Motor, Mobil, atau MobilBesar.

Cara menjalankan:
    python contoh04_simple_factory.py
"""

from abc import ABC, abstractmethod


class Kendaraan(ABC):
    """Produk abstrak: semua kendaraan yang bisa dipesan."""

    @abstractmethod
    def nama(self) -> str:
        """Nama layanan."""

    @abstractmethod
    def kapasitas(self) -> int:
        """Jumlah penumpang maksimal."""

    @abstractmethod
    def tarif_per_km(self) -> int:
        """Tarif dalam rupiah per kilometer."""

    def hitung_ongkos(self, jarak_km: int) -> int:
        return self.tarif_per_km() * jarak_km


class Motor(Kendaraan):
    def nama(self) -> str:
        return "Motor"

    def kapasitas(self) -> int:
        return 1

    def tarif_per_km(self) -> int:
        return 2500


class Mobil(Kendaraan):
    def nama(self) -> str:
        return "Mobil"

    def kapasitas(self) -> int:
        return 4

    def tarif_per_km(self) -> int:
        return 4000


class MobilBesar(Kendaraan):
    def nama(self) -> str:
        return "Mobil Besar"

    def kapasitas(self) -> int:
        return 6

    def tarif_per_km(self) -> int:
        return 5500


class KendaraanFactory:
    """Simple Factory: SATU tempat yang memutuskan kelas mana yang dibuat."""

    @staticmethod
    def buat(jenis: str) -> Kendaraan:  # [1] tipe kembalian: kelas abstrak
        pilihan = jenis.lower()  # [2] "MOBIL" dan "mobil" dianggap sama
        if pilihan == "motor":
            return Motor()
        if pilihan == "mobil":
            return Mobil()
        if pilihan == "mobil besar":
            return MobilBesar()
        raise ValueError(f"Jenis kendaraan tidak dikenal: {jenis}")  # [3]


def main():
    print("=== PESANAN DARI APLIKASI (JARAK 8 KM) ===")
    for pilihan in ["motor", "Mobil", "MOBIL BESAR"]:
        kendaraan = KendaraanFactory.buat(pilihan)  # [4] cukup kirim teks
        ongkos = kendaraan.hitung_ongkos(8)
        print(f"{pilihan:<12} -> {kendaraan.nama():<12} "
              f"maks {kendaraan.kapasitas()} penumpang, Rp{ongkos}")

    print()
    print("=== PILIHAN TIDAK DIKENAL ===")
    try:
        KendaraanFactory.buat("helikopter")
    except ValueError as e:  # [5]
        print(f"Ditolak: {e}")


if __name__ == "__main__":
    main()
