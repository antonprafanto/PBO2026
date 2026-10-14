"""
Contoh 07 - Objek Saling Mengirim Pesan
Pertemuan 05 - Relasi Antarkelas

Menarik uang tunai melibatkan tiga objek yang bekerja sama:
    MesinAtm -> KartuAtm -> Rekening   (arah pesan)
Setiap objek hanya mengerjakan bagiannya sendiri, lalu meneruskan pesan
ke objek yang ia kenal. Baris berawalan [NamaKelas] menunjukkan objek
mana yang sedang bekerja.

Cara menjalankan:
    python contoh07_kirim_pesan.py
"""


class Rekening:
    """Rekening bank yang menjaga saldonya sendiri."""

    def __init__(self, pemilik: str, saldo: int):
        self._pemilik = pemilik
        self._saldo = saldo

    @property
    def saldo(self) -> int:
        return self._saldo

    def tarik(self, jumlah: int) -> bool:
        if jumlah > self._saldo:
            print(f"    [Rekening] saldo tidak cukup (sisa Rp{self._saldo})")
            return False
        self._saldo -= jumlah
        print(f"    [Rekening] saldo {self._pemilik} kini Rp{self._saldo}")
        return True


class KartuAtm:
    """Kartu ATM yang MENGENAL rekeningnya (asosiasi)."""

    def __init__(self, pin: str, rekening: Rekening):
        self._pin = pin
        self._rekening = rekening  # [1] kartu menyimpan referensi rekening

    def otorisasi(self, pin: str, jumlah: int) -> bool:
        if pin != self._pin:
            print("  [KartuAtm] PIN salah")
            return False
        print("  [KartuAtm] PIN cocok, teruskan ke rekening")
        return self._rekening.tarik(jumlah)  # [2] pesan diteruskan ke Rekening


class MesinAtm:
    """Mesin ATM yang MEMAKAI kartu selama transaksi (dependensi)."""

    def __init__(self, uang_tersedia: int):
        self._uang_tersedia = uang_tersedia

    @property
    def uang_tersedia(self) -> int:
        return self._uang_tersedia

    def tarik_tunai(self, kartu: KartuAtm, pin: str, jumlah: int):  # [3]
        print(f"[MesinAtm] permintaan tarik Rp{jumlah}")
        if jumlah > self._uang_tersedia:
            print("[MesinAtm] uang di mesin tidak cukup")
            return
        if kartu.otorisasi(pin, jumlah):  # [4] pesan dikirim ke KartuAtm
            self._uang_tersedia -= jumlah
            print(f"[MesinAtm] silakan ambil uang Rp{jumlah}")
        else:
            print("[MesinAtm] transaksi dibatalkan")


def main():
    rekening_ayu = Rekening("Ayu", 500000)
    kartu_ayu = KartuAtm("123456", rekening_ayu)
    mesin = MesinAtm(1000000)

    print("=== TRANSAKSI 1: BERHASIL ===")
    mesin.tarik_tunai(kartu_ayu, "123456", 200000)  # [5]

    print()
    print("=== TRANSAKSI 2: PIN SALAH ===")
    mesin.tarik_tunai(kartu_ayu, "111111", 100000)

    print()
    print("=== TRANSAKSI 3: SALDO TIDAK CUKUP ===")
    mesin.tarik_tunai(kartu_ayu, "123456", 400000)

    print()
    print("=== SETELAH TRANSAKSI ===")
    print(f"Saldo rekening Ayu: Rp{rekening_ayu.saldo}")
    print(f"Uang di mesin     : Rp{mesin.uang_tersedia}")


if __name__ == "__main__":
    main()
