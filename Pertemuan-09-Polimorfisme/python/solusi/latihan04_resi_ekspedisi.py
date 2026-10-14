"""
Solusi Latihan 04 - Resi Ekspedisi
Pertemuan 09 - Polimorfisme

Ide penyelesaian:
- ongkir() dan cetak_resi() ditulis SEKALI di kelas induk Pengiriman.
  Di dalamnya, keduanya memanggil self.nama_layanan(), self.tarif_per_kg(),
  dan self.berat_ditagih(). Kelas anak cukup meng-override method kecil itu
  (polimorfisme dari dalam kelas).
- Kargo meng-override berat_ditagih(): minimal 10 kg.
- SameDay (jenis baru) meng-override ongkir() dengan gaya "memperluas":
  ongkir versi induk + biaya kurir.
- cetak_manifest() tidak menyebut kelas anak mana pun, jadi tidak perlu
  diubah saat SameDay ditambahkan.

Cara menjalankan:
    python latihan04_resi_ekspedisi.py
"""


class Pengiriman:
    """Kelas induk semua layanan pengiriman. Berat dalam kg (bilangan bulat)."""

    def __init__(self, kode: str, kota_tujuan: str, berat_kg: int):
        self._kode = kode
        self._kota_tujuan = kota_tujuan
        self._berat_kg = berat_kg

    def nama_layanan(self) -> str:
        return "Umum"

    def tarif_per_kg(self) -> int:
        return 10000

    def berat_ditagih(self) -> int:
        return self._berat_kg

    def ongkir(self) -> int:
        return self.berat_ditagih() * self.tarif_per_kg()  # memanggil versi anak

    def cetak_resi(self):
        print(f"[{self._kode}] {self.nama_layanan():<8} {self._kota_tujuan:<11}"
              f"{self._berat_kg:>3} kg  Rp{self.ongkir()}")


class Reguler(Pengiriman):
    def nama_layanan(self) -> str:
        return "Reguler"

    def tarif_per_kg(self) -> int:
        return 9000


class Kilat(Pengiriman):
    def nama_layanan(self) -> str:
        return "Kilat"

    def tarif_per_kg(self) -> int:
        return 15000


class Kargo(Pengiriman):
    BERAT_MINIMUM = 10

    def nama_layanan(self) -> str:
        return "Kargo"

    def tarif_per_kg(self) -> int:
        return 6000

    def berat_ditagih(self) -> int:
        return max(self._berat_kg, Kargo.BERAT_MINIMUM)


# ----- Jenis BARU (bagian 2 soal) -----
class SameDay(Pengiriman):
    BIAYA_KURIR = 10000

    def nama_layanan(self) -> str:
        return "SameDay"

    def tarif_per_kg(self) -> int:
        return 20000

    def ongkir(self) -> int:
        return super().ongkir() + SameDay.BIAYA_KURIR  # memperluas versi induk


def cetak_manifest(daftar: list[Pengiriman]):
    total = 0
    for kiriman in daftar:
        kiriman.cetak_resi()
        total += kiriman.ongkir()
    print(f"Total ongkir: Rp{total}")


def main():
    print("=== MANIFEST PAGI ===")
    pagi = [
        Reguler("KK001", "Balikpapan", 2),
        Kilat("KK002", "Bontang", 3),
        Kargo("KK003", "Tenggarong", 4),
        Kargo("KK004", "Sangatta", 25),
    ]
    cetak_manifest(pagi)

    print()
    print("=== MANIFEST SORE (ADA LAYANAN BARU) ===")
    sore = [
        SameDay("KK005", "Samarinda", 1),
        Reguler("KK006", "Balikpapan", 5),
        SameDay("KK007", "Samarinda", 3),
    ]
    cetak_manifest(sore)


if __name__ == "__main__":
    main()
