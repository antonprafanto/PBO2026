"""
Contoh 06 - Mengembalikan Salinan List
Pertemuan 05 - Relasi Antarkelas

Dua garasi berkapasitas 2 motor. GarasiBocor menyerahkan list ASLI-nya
ke luar, sehingga aturan kapasitas bisa dilewati. GarasiAman hanya
menyerahkan SALINAN list, sehingga isi garasi tetap terjaga.

Cara menjalankan:
    python contoh06_salinan_list.py
"""


class Motor:
    """Motor dengan nomor plat."""

    def __init__(self, plat: str):
        self._plat = plat

    @property
    def plat(self) -> str:
        return self._plat


class GarasiBocor:
    """Garasi yang membocorkan list aslinya."""

    def __init__(self, kapasitas: int):
        self._kapasitas = kapasitas
        self._daftar_motor: list[Motor] = []

    def parkir(self, motor: Motor):
        if len(self._daftar_motor) >= self._kapasitas:
            print(f"Ditolak: garasi penuh, {motor.plat} tidak bisa masuk")
            return
        self._daftar_motor.append(motor)
        print(f"{motor.plat} masuk garasi")

    @property
    def daftar_motor(self) -> list[Motor]:
        return self._daftar_motor  # [1] list ASLI diserahkan ke luar

    def tampilkan(self):
        print(f"Isi garasi ({len(self._daftar_motor)}/{self._kapasitas}):")
        for motor in self._daftar_motor:
            print(f"- {motor.plat}")


class GarasiAman:
    """Garasi yang hanya menyerahkan salinan list."""

    def __init__(self, kapasitas: int):
        self._kapasitas = kapasitas
        self._daftar_motor: list[Motor] = []

    def parkir(self, motor: Motor):
        if len(self._daftar_motor) >= self._kapasitas:
            print(f"Ditolak: garasi penuh, {motor.plat} tidak bisa masuk")
            return
        self._daftar_motor.append(motor)
        print(f"{motor.plat} masuk garasi")

    @property
    def daftar_motor(self) -> list[Motor]:
        return list(self._daftar_motor)  # [2] yang diserahkan hanya SALINAN

    def tampilkan(self):
        print(f"Isi garasi ({len(self._daftar_motor)}/{self._kapasitas}):")
        for motor in self._daftar_motor:
            print(f"- {motor.plat}")


def main():
    print("=== GARASI BOCOR ===")
    bocor = GarasiBocor(2)
    bocor.parkir(Motor("KT 1111 AA"))
    bocor.parkir(Motor("KT 2222 BB"))
    bocor.parkir(Motor("KT 3333 CC"))
    daftar = bocor.daftar_motor  # [3] kode luar memegang list ASLI
    daftar.append(Motor("KT 3333 CC"))  # [4] menyelinap, kapasitas dilewati
    bocor.tampilkan()

    print()
    print("=== GARASI AMAN ===")
    aman = GarasiAman(2)
    aman.parkir(Motor("KT 1111 AA"))
    aman.parkir(Motor("KT 2222 BB"))
    aman.parkir(Motor("KT 3333 CC"))
    daftar = aman.daftar_motor  # [5] kode luar hanya memegang salinan
    daftar.append(Motor("KT 3333 CC"))  # yang bertambah hanya salinannya
    aman.tampilkan()
    print(f"Isi salinan di luar: {len(daftar)} motor")


if __name__ == "__main__":
    main()
