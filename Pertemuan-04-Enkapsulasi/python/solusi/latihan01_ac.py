"""
Solusi Latihan 01 - Pengatur Suhu AC
Pertemuan 04 - Enkapsulasi

Ide penyelesaian:
- Simpan data di atribut bergaris bawah: _ruangan dan _suhu.
- ruangan cukup punya getter (@property tanpa setter), jadi read-only.
- suhu punya getter dan setter. Setter menolak suhu di luar batas dengan
  raise ValueError.
- Konstruktor mengisi suhu LEWAT setter (self.suhu = suhu), sehingga AC
  dengan suhu awal yang salah juga ditolak.
- Batas suhu disimpan sebagai konstanta kelas (huruf besar semua).

Cara menjalankan:
    python latihan01_ac.py
"""


class AC:
    """Pendingin ruangan yang suhunya hanya bisa diatur 16-30 derajat."""

    SUHU_MIN = 16  # konstanta: huruf besar = "jangan diubah"
    SUHU_MAKS = 30

    def __init__(self, ruangan, suhu):
        self._ruangan = ruangan
        self.suhu = suhu  # lewat setter, jadi ikut diperiksa

    @property
    def ruangan(self):
        return self._ruangan

    @property
    def suhu(self):
        return self._suhu

    @suhu.setter
    def suhu(self, nilai):
        if nilai < AC.SUHU_MIN or nilai > AC.SUHU_MAKS:
            raise ValueError(
                f"Suhu harus {AC.SUHU_MIN}-{AC.SUHU_MAKS} derajat, bukan {nilai}")
        self._suhu = nilai


def main():
    ac = AC("Ruang Dosen", 24)
    print("=== AC RUANG DOSEN ===")
    print(f"Suhu awal: {ac.suhu} derajat")
    ac.suhu = 20
    print(f"Suhu diatur ke {ac.suhu} derajat")
    try:
        ac.suhu = 10
    except ValueError as e:
        print(f"Ditolak: {e}")
    try:
        ac.suhu = 35
    except ValueError as e:
        print(f"Ditolak: {e}")
    print(f"Suhu sekarang: {ac.suhu} derajat")

    print()
    print("=== MEMASANG AC BARU ===")
    try:
        lab = AC("Lab Komputer", 40)
        print(f"AC {lab.ruangan} terpasang")
    except ValueError as e:
        print(f"Gagal memasang AC: {e}")


if __name__ == "__main__":
    main()
