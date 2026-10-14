"""
Contoh 06 - raise: Melempar dan Melempar Ulang
Pertemuan 11 - Exception Handling

- raise ValueError("pesan") MELEMPAR exception buatan kita sendiri. Kita
  memakainya untuk menolak data yang tidak masuk akal (validasi), seperti
  di Pertemuan 04.
- raise (tanpa apa pun) di dalam blok except MELEMPAR ULANG exception yang
  sedang ditangani. Polanya: "catat dulu, lalu teruskan ke pemanggil".

Cara menjalankan:
    python contoh06_raise_dan_lempar_ulang.py
"""


class AC:
    """AC ruangan dengan batas suhu 16 sampai 30 derajat."""

    SUHU_MIN = 16
    SUHU_MAKS = 30

    def __init__(self, ruangan: str):
        self._ruangan = ruangan
        self._suhu = 25

    @property
    def suhu(self) -> int:
        return self._suhu

    def atur_suhu(self, suhu: int):
        if suhu < AC.SUHU_MIN or suhu > AC.SUHU_MAKS:  # [1] periksa lebih dulu
            raise ValueError(f"Suhu {suhu} di luar batas "
                             f"{AC.SUHU_MIN}-{AC.SUHU_MAKS} derajat")  # [2]
        self._suhu = suhu  # [3] hanya dijalankan jika lolos pemeriksaan


def tekan_remote(ac: AC, suhu: int):
    """Meneruskan perintah ke AC. Penolakan dicatat, lalu dilempar ulang."""
    try:
        ac.atur_suhu(suhu)
    except ValueError:
        print(f"  [log] perintah {suhu} derajat ditolak")  # [4] catat dulu...
        raise  # [5] ...lalu lempar ulang exception yang SAMA ke pemanggil


def main():
    ac = AC("Lab Komputer 2")
    print(f"=== REMOTE AC (suhu awal {ac.suhu} derajat) ===")
    for suhu in [22, 10, 35, 18]:
        try:
            tekan_remote(ac, suhu)
            print(f"Suhu diatur ke {suhu} derajat")
        except ValueError as e:  # [6] pesan dari raise ikut terbawa
            print(f"Layar remote: {e}")
    print(f"Suhu akhir: {ac.suhu} derajat")


if __name__ == "__main__":
    main()
