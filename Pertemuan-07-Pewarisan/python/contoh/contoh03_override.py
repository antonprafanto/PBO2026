"""
Contoh 03 - Override: Menimpa Method Induk (dan Tetap Memakai Versi Induk)
Pertemuan 07 - Pewarisan (Inheritance)

TiketVIP mewarisi Tiket, lalu MENIMPA (override) dua method: info() dan
hitung_bayar(). Di dalam versi barunya, TiketVIP tetap memakai hasil versi
induk lewat super().nama_method(), sehingga tidak perlu menulis ulang rumusnya.

Cara menjalankan:
    python contoh03_override.py
"""

BIAYA_LAYANAN_VIP = 25000  # biaya layanan VIP per orang, dalam Rupiah


class Tiket:
    """Tiket reguler sebuah acara."""

    def __init__(self, acara: str, harga: int):
        self._acara = acara
        self._harga = harga

    @property
    def acara(self) -> str:
        return self._acara

    def info(self) -> str:
        return f"Tiket {self._acara} - Rp{self._harga}"

    def hitung_bayar(self, jumlah: int) -> int:
        return self._harga * jumlah


class TiketVIP(Tiket):
    """Tiket VIP: punya fasilitas dan ada biaya layanan per orang."""

    def __init__(self, acara: str, harga: int, fasilitas: str):
        super().__init__(acara, harga)
        self._fasilitas = fasilitas

    def info(self) -> str:  # [1] override: nama dan parameter sama dengan induk
        return f"{super().info()} | VIP: {self._fasilitas}"  # [2] induk + tambahan

    def hitung_bayar(self, jumlah: int) -> int:  # [3] override kedua
        harga_dasar = super().hitung_bayar(jumlah)  # [4] hitungan versi induk
        return harga_dasar + BIAYA_LAYANAN_VIP * jumlah


def main():
    reguler = Tiket("Festival Musik Kampus", 50000)
    vip = TiketVIP("Festival Musik Kampus", 120000, "kursi depan dan kaus")

    print("=== INFO TIKET ===")
    print(reguler.info())  # [5] objek Tiket -> versi Tiket
    print(vip.info())  # [5] objek TiketVIP -> versi TiketVIP

    print()
    print("=== BAYAR UNTUK 3 ORANG ===")
    print(f"Reguler: Rp{reguler.hitung_bayar(3)}")
    print(f"VIP    : Rp{vip.hitung_bayar(3)}")
    print(f"Acara  : {vip.acara}")  # [6] property yang tidak di-override tetap warisan


if __name__ == "__main__":
    main()
