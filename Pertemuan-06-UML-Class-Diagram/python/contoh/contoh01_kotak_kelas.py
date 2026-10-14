"""
Contoh 01 - Dari Diagram ke Kode: Kotak Kelas Lengkap
Pertemuan 06 - UML Class Diagram

Kelas Paket di bawah ini adalah wujud kode dari kotak kelas berikut
(versi Python, ditulis dengan sintaks Mermaid):

    class Paket {
        +TARIF_PER_KG : int = 8000$
        -_penghitung : int = 0$
        -_resi : str
        -_tujuan : str
        -_berat_gram : int
        +resi : str
        +tujuan : str
        +Paket(tujuan: str, berat_gram: int)
        -_berat_kg() int
        +hitung_ongkir() int
        +jumlah_paket() int$
    }

Tanda $ berarti static (milik kelas). Di diagram UML, anggota static
digambar dengan garis bawah.

Cara menjalankan:
    python contoh01_kotak_kelas.py
"""


class Paket:
    """Paket kiriman di sebuah jasa ekspedisi."""

    TARIF_PER_KG = 8000  # [1] +TARIF_PER_KG : int = 8000$ (publik, milik kelas)
    _penghitung = 0  # [2] -_penghitung : int = 0$ (privat, milik kelas)

    def __init__(self, tujuan: str, berat_gram: int):  # [3] +Paket(...)
        Paket._penghitung += 1
        self._resi = f"KRM{Paket._penghitung:03d}"  # [4] -_resi : str
        self._tujuan = tujuan
        self._berat_gram = berat_gram

    @property
    def resi(self) -> str:  # [5] +resi : str (property hanya-baca)
        return self._resi

    @property
    def tujuan(self) -> str:
        return self._tujuan

    def _berat_kg(self) -> int:  # [6] -_berat_kg() int (method privat)
        """Berat dibulatkan ke atas per kilogram: 1200 gram dihitung 2 kg."""
        return (self._berat_gram + 999) // 1000

    def hitung_ongkir(self) -> int:  # [7] +hitung_ongkir() int
        return self._berat_kg() * Paket.TARIF_PER_KG

    @classmethod
    def jumlah_paket(cls) -> int:  # [8] +jumlah_paket() int$ (milik kelas)
        return cls._penghitung


def main():
    print("=== PAKET MASUK ===")
    daftar_paket = [
        Paket("Samarinda", 1200),
        Paket("Balikpapan", 500),
        Paket("Bontang", 3000),
    ]
    for paket in daftar_paket:
        print(f"{paket.resi} ke {paket.tujuan}: ongkir Rp{paket.hitung_ongkir()}")

    print()
    print("=== DATA MILIK KELAS ===")
    print(f"Tarif per kg : Rp{Paket.TARIF_PER_KG}")  # [9] static dibaca lewat kelas
    print(f"Jumlah paket : {Paket.jumlah_paket()}")


if __name__ == "__main__":
    main()
