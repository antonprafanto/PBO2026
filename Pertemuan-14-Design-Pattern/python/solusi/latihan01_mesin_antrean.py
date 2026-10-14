"""
Solusi Latihan 01 - Mesin Antrean (Singleton)
Pertemuan 14 - Design Pattern Dasar

Ide penyelesaian:
- MesinAntrean adalah Singleton: hanya ada SATU mesin pembagi nomor, sehingga
  nomor dari pintu mana pun tidak pernah kembar.
- TombolAntrean di setiap pintu TIDAK menyimpan mesin sendiri. Setiap kali
  ditekan, ia meminta mesin lewat MesinAntrean.get_instance().
- Nomor dibuat dengan format A001, A002, ... memakai f"A{n:03d}".

Cara menjalankan:
    python latihan01_mesin_antrean.py
"""


class MesinAntrean:
    """Singleton: satu-satunya mesin pembagi nomor antrean."""

    _instance = None

    def __init__(self):
        if MesinAntrean._instance is not None:
            raise RuntimeError("Gunakan MesinAntrean.get_instance()")
        self._nomor_terakhir = 0

    @classmethod
    def get_instance(cls) -> "MesinAntrean":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def ambil_nomor(self) -> str:
        self._nomor_terakhir += 1
        return f"A{self._nomor_terakhir:03d}"

    def jumlah_dibagikan(self) -> int:
        return self._nomor_terakhir


class TombolAntrean:
    """Tombol pengambil nomor yang dipasang di sebuah pintu masuk."""

    def __init__(self, lokasi: str):
        self._lokasi = lokasi

    def tekan(self):
        nomor = MesinAntrean.get_instance().ambil_nomor()  # selalu mesin yang sama
        print(f"{self._lokasi:<14}: nomor {nomor}")


def main():
    utara = TombolAntrean("Pintu Utara")
    selatan = TombolAntrean("Pintu Selatan")

    print("=== PENGUNJUNG MENGAMBIL NOMOR ===")
    utara.tekan()
    utara.tekan()
    selatan.tekan()
    utara.tekan()
    selatan.tekan()

    print()
    print("=== RINGKASAN ===")
    mesin_1 = MesinAntrean.get_instance()
    mesin_2 = MesinAntrean.get_instance()
    print(f"Mesin yang sama? {'ya' if mesin_1 is mesin_2 else 'tidak'}")
    print(f"Total nomor dibagikan: {mesin_1.jumlah_dibagikan()}")


if __name__ == "__main__":
    main()
