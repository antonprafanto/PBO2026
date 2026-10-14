"""
Contoh 05 - Dependensi: Memakai Sementara
Pertemuan 06 - UML Class Diagram

Diagram (versi Python, sintaks Mermaid):

    Motor ..> SPBU : isi_bensin

- Garis PUTUS-PUTUS dengan panah (..>) berarti Motor BERGANTUNG pada SPBU:
  Motor memakai SPBU hanya selama method isi_bensin() berjalan.
- SPBU datang sebagai PARAMETER dan tidak disimpan sebagai atribut,
  jadi setelah method selesai, motor tidak lagi "mengenal" SPBU itu.

Cara menjalankan:
    python contoh05_dependensi.py
"""


class SPBU:
    """Stasiun pengisian bahan bakar. Harga per liter hanya contoh."""

    def __init__(self, nama: str, harga_per_liter: int):
        self._nama = nama
        self._harga_per_liter = harga_per_liter

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def harga_per_liter(self) -> int:
        return self._harga_per_liter


class Motor:
    """Motor dengan tangki bensin (dalam liter, bilangan bulat)."""

    def __init__(self, plat: str, kapasitas_tangki: int):
        self._plat = plat
        self._kapasitas_tangki = kapasitas_tangki
        self._isi_tangki = 0

    def isi_bensin(self, spbu: SPBU, liter: int) -> int:  # [1] SPBU hanya parameter
        ruang_kosong = self._kapasitas_tangki - self._isi_tangki
        liter_masuk = min(liter, ruang_kosong)  # tangki tidak bisa melebihi kapasitas
        self._isi_tangki += liter_masuk
        biaya = liter_masuk * spbu.harga_per_liter  # [2] memakai data milik SPBU
        print(f"{self._plat} isi {liter_masuk} liter di {spbu.nama}, bayar Rp{biaya}")
        return biaya  # [3] selesai: motor tidak menyimpan SPBU

    def info(self) -> str:
        return f"{self._plat}: tangki {self._isi_tangki}/{self._kapasitas_tangki} liter"


def main():
    spbu_juanda = SPBU("SPBU Jl. Juanda", 10000)
    spbu_pahlawan = SPBU("SPBU Jl. Pahlawan", 12500)
    motor = Motor("KT 3344 XY", 5)

    print("=== ISI BENSIN ===")
    total = 0
    total += motor.isi_bensin(spbu_juanda, 3)  # [4] SPBU dikirim saat dibutuhkan
    total += motor.isi_bensin(spbu_pahlawan, 4)  # hanya muat 2 liter lagi
    print(motor.info())
    print(f"Total biaya: Rp{total}")


if __name__ == "__main__":
    main()
