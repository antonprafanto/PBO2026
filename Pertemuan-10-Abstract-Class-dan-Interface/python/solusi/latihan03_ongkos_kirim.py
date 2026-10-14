"""
Solusi Latihan 03 - Ongkos Kirim dengan Template Method
Pertemuan 10 - Abstract Class dan Interface

Ide penyelesaian:
- Pengiriman adalah kelas abstrak. Rumus ongkir ditulis SEKALI di
  hitung_ongkir() (template method):
      ongkir = berat x tarif_per_kg() + biaya_tambahan(berat)
- tarif_per_kg() dan nama_layanan() abstrak: wajib diisi kelas anak.
- biaya_tambahan() adalah hook: bawaannya 0, di-override oleh layanan
  yang punya aturan khusus (Kilat dan Kargo).

Cara menjalankan:
    python latihan03_ongkos_kirim.py
"""

from abc import ABC, abstractmethod


def format_rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


class Pengiriman(ABC):
    """Kelas abstrak: kerangka perhitungan ongkos kirim."""

    @abstractmethod
    def nama_layanan(self) -> str:
        """Nama layanan pengiriman."""

    @abstractmethod
    def tarif_per_kg(self) -> int:
        """Tarif dasar per kilogram."""

    def biaya_tambahan(self, berat_kg: int) -> int:
        """Hook: biaya tambahan. Bawaannya 0."""
        return 0

    def hitung_ongkir(self, berat_kg: int) -> int:
        """Template method: rumusnya sama untuk semua layanan."""
        return berat_kg * self.tarif_per_kg() + self.biaya_tambahan(berat_kg)

    def rincian(self, berat_kg: int) -> str:
        tarif = format_rupiah(self.tarif_per_kg())
        tambahan = format_rupiah(self.biaya_tambahan(berat_kg))
        total = format_rupiah(self.hitung_ongkir(berat_kg))
        return (f"{self.nama_layanan():<8}: {berat_kg} kg x {tarif} "
                f"+ tambahan {tambahan} = {total}")


class KirimReguler(Pengiriman):
    """Layanan biasa tanpa biaya tambahan."""

    def nama_layanan(self) -> str:
        return "Reguler"

    def tarif_per_kg(self) -> int:
        return 8000


class KirimKilat(Pengiriman):
    """Layanan cepat: ada biaya prioritas tetap Rp5.000."""

    def nama_layanan(self) -> str:
        return "Kilat"

    def tarif_per_kg(self) -> int:
        return 15000

    def biaya_tambahan(self, berat_kg: int) -> int:
        return 5000


class KirimKargo(Pengiriman):
    """Murah untuk barang berat, tetapi dihitung minimal 10 kg."""

    BERAT_MINIMUM = 10

    def nama_layanan(self) -> str:
        return "Kargo"

    def tarif_per_kg(self) -> int:
        return 5000

    def biaya_tambahan(self, berat_kg: int) -> int:
        if berat_kg < KirimKargo.BERAT_MINIMUM:
            return (KirimKargo.BERAT_MINIMUM - berat_kg) * self.tarif_per_kg()
        return 0


def termurah(daftar: list[Pengiriman], berat_kg: int) -> Pengiriman:
    pilihan = daftar[0]
    for layanan in daftar:
        if layanan.hitung_ongkir(berat_kg) < pilihan.hitung_ongkir(berat_kg):
            pilihan = layanan
    return pilihan


def bandingkan(daftar: list[Pengiriman], berat_kg: int):
    print(f"=== ONGKOS KIRIM PAKET {berat_kg} KG ===")
    for layanan in daftar:
        print(layanan.rincian(berat_kg))
    pilihan = termurah(daftar, berat_kg)
    ongkir = format_rupiah(pilihan.hitung_ongkir(berat_kg))
    print(f"Termurah: {pilihan.nama_layanan()} ({ongkir})")


def main():
    daftar: list[Pengiriman] = [KirimReguler(), KirimKilat(), KirimKargo()]
    bandingkan(daftar, 3)
    print()
    bandingkan(daftar, 12)


if __name__ == "__main__":
    main()
