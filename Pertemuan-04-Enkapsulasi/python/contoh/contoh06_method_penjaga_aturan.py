"""
Contoh 06 - Method sebagai Penjaga Aturan
Pertemuan 04 - Enkapsulasi

Jumlah motor di parkiran TIDAK diberi setter. Jumlah itu hanya berubah
lewat method masuk() dan keluar(), yang menjaga aturan:
- jumlah motor yang masuk/keluar harus lebih dari 0,
- motor tidak boleh masuk melebihi sisa tempat,
- motor yang keluar tidak boleh lebih banyak dari motor yang ada.

Prinsip "tell, don't ask": SURUH objek bekerja (parkiran.masuk(3)),
jangan TANYA datanya lalu mengubahnya sendiri dari luar kelas.

Cara menjalankan:
    python contoh06_method_penjaga_aturan.py
"""


class Parkiran:
    """Parkiran motor dengan kapasitas terbatas."""

    def __init__(self, nama, kapasitas):
        if kapasitas <= 0:
            raise ValueError("Kapasitas harus lebih dari 0")
        self._nama = nama
        self._kapasitas = kapasitas
        self._terisi = 0  # [1] tanpa setter: hanya berubah lewat masuk()/keluar()

    @property
    def nama(self):
        return self._nama

    @property
    def kapasitas(self):
        return self._kapasitas

    @property
    def terisi(self):
        return self._terisi

    @property
    def sisa(self):  # [2] dihitung saat dibaca, tidak disimpan di atribut
        return self._kapasitas - self._terisi

    @property
    def penuh(self):  # [3] property bernilai True/False
        return self._terisi == self._kapasitas

    def masuk(self, jumlah):  # [4] pintu resmi untuk menambah jumlah motor
        if jumlah <= 0:
            raise ValueError("Jumlah motor harus lebih dari 0")
        if jumlah > self.sisa:
            raise ValueError(
                f"Tempat tidak cukup untuk {jumlah} motor (sisa {self.sisa})")
        self._terisi += jumlah

    def keluar(self, jumlah):  # [5] pintu resmi untuk mengurangi jumlah motor
        if jumlah <= 0:
            raise ValueError("Jumlah motor harus lebih dari 0")
        if jumlah > self._terisi:
            raise ValueError(f"Hanya ada {self._terisi} motor di parkiran")
        self._terisi -= jumlah


def ya_tidak(kondisi):
    """Mengubah True/False menjadi teks 'ya' atau 'tidak'."""
    if kondisi:
        return "ya"
    return "tidak"


def tampilkan(parkiran):
    print(f"  {parkiran.nama}: terisi {parkiran.terisi}/{parkiran.kapasitas}, "
          f"sisa {parkiran.sisa}, penuh: {ya_tidak(parkiran.penuh)}")


def main():
    parkiran = Parkiran("Parkiran Gedung C", 5)

    print("=== PAGI: MOTOR BERDATANGAN ===")
    tampilkan(parkiran)
    parkiran.masuk(3)  # [6] "tell": suruh parkiran mencatat motor yang masuk
    print("3 motor masuk")
    parkiran.masuk(2)
    print("2 motor masuk")
    tampilkan(parkiran)
    try:
        parkiran.masuk(1)
        print("1 motor masuk")
    except ValueError as e:
        print(f"Ditolak: {e}")

    print()
    print("=== SORE: MOTOR PULANG ===")
    parkiran.keluar(4)
    print("4 motor keluar")
    tampilkan(parkiran)
    try:
        parkiran.keluar(2)
    except ValueError as e:
        print(f"Ditolak: {e}")
    try:
        parkiran.masuk(-2)  # [7] trik curang: "masuk" dengan angka negatif
    except ValueError as e:
        print(f"Ditolak: {e}")


if __name__ == "__main__":
    main()
