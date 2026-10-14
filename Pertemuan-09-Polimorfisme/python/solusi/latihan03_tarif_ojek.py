"""
Solusi Latihan 03 - Tarif Ojek Online
Pertemuan 09 - Polimorfisme

Ide penyelesaian:
- Python tidak punya overloading. Jika kita menulis tiga def hitung_tarif,
  hanya def TERAKHIR yang tersisa. Sebagai gantinya, SATU method diberi
  nilai bawaan: hitung_tarif(jarak_km, jam_sibuk=False, kode_promo="").
- Konstruktor juga memakai nilai bawaan: tarif_per_km=2500.
- Pemanggil boleh mengisi sebagian argumen saja, dan boleh memakai argumen
  kata kunci, misalnya hitung_tarif(5, kode_promo="HEMAT10").
- Semua perhitungan memakai bilangan bulat (persen: nilai * persen // 100).

Cara menjalankan:
    python latihan03_tarif_ojek.py
"""

TARIF_MINIMUM = 10000
PERSEN_JAM_SIBUK = 20
PERSEN_PROMO = 10
KODE_PROMO_BERLAKU = "HEMAT10"


class Ojek:
    """Driver ojek online beserta tarifnya."""

    def __init__(self, nama_driver: str, tarif_per_km: int = 2500):
        self._nama_driver = nama_driver
        self._tarif_per_km = tarif_per_km

    @property
    def nama_driver(self) -> str:
        return self._nama_driver

    def info(self) -> str:
        return f"{self._nama_driver} (Rp{self._tarif_per_km}/km)"

    def hitung_tarif(self, jarak_km: int, jam_sibuk: bool = False,
                     kode_promo: str = "") -> int:
        tarif = jarak_km * self._tarif_per_km
        if tarif < TARIF_MINIMUM:
            tarif = TARIF_MINIMUM
        if jam_sibuk:
            tarif += tarif * PERSEN_JAM_SIBUK // 100
        if kode_promo == KODE_PROMO_BERLAKU:
            tarif -= tarif * PERSEN_PROMO // 100
        return tarif


def cetak(keterangan: str, tarif: int):
    print(f"{keterangan:<36}: Rp{tarif}")


def main():
    darto = Ojek("Pak Darto")  # tarif per km memakai nilai bawaan
    yuni = Ojek("Mbak Yuni", 3000)

    print("=== DRIVER ===")
    print(darto.info())
    print(yuni.info())

    print()
    print("=== HITUNG TARIF ===")
    cetak("Pak Darto, 3 km", darto.hitung_tarif(3))
    cetak("Pak Darto, 8 km", darto.hitung_tarif(8))
    cetak("Pak Darto, 8 km, jam sibuk", darto.hitung_tarif(8, True))
    cetak("Pak Darto, 8 km, jam sibuk, HEMAT10", darto.hitung_tarif(8, True, "HEMAT10"))
    cetak("Mbak Yuni, 5 km, HEMAT10", yuni.hitung_tarif(5, kode_promo="HEMAT10"))
    cetak("Mbak Yuni, 5 km, kode SALAH", yuni.hitung_tarif(5, kode_promo="SALAH"))


if __name__ == "__main__":
    main()
