"""
Contoh 01 - Dependensi: Memakai Objek Lain Sebentar
Pertemuan 05 - Relasi Antar Kelas

Penumpang MEMAKAI objek Ojek hanya selama method pesan_ojek() berjalan.
Objek Ojek datang lewat parameter dan TIDAK disimpan sebagai atribut.
Hubungan "memakai sebentar" seperti ini disebut dependensi.

Cara menjalankan:
    python contoh01_dependensi.py
"""


class Ojek:
    """Ojek daring yang bisa mengantar penumpang."""

    def __init__(self, pengemudi: str, plat: str, tarif_per_km: int):
        self._pengemudi = pengemudi
        self._plat = plat
        self._tarif_per_km = tarif_per_km

    def antar(self, tujuan: str, jarak_km: int) -> int:
        """Mengantar penumpang, lalu mengembalikan ongkosnya."""
        print(f"  {self._pengemudi} ({self._plat}) mengantar ke {tujuan}")
        return jarak_km * self._tarif_per_km


class Penumpang:
    """Penumpang yang memesan ojek. Ia TIDAK menyimpan objek Ojek."""

    def __init__(self, nama: str):
        self._nama = nama
        self._jumlah_perjalanan = 0  # [1] yang diingat hanya angka-angka ini
        self._total_ongkos = 0

    @property
    def jumlah_perjalanan(self) -> int:
        return self._jumlah_perjalanan

    @property
    def total_ongkos(self) -> int:
        return self._total_ongkos

    def pesan_ojek(self, ojek: Ojek, tujuan: str, jarak_km: int):  # [2]
        print(f"{self._nama} memesan ojek, jarak {jarak_km} km")
        ongkos = ojek.antar(tujuan, jarak_km)  # [3] memakai objek Ojek
        self._jumlah_perjalanan += 1
        self._total_ongkos += ongkos
        print(f"  Ongkos: Rp{ongkos}")
        # [4] method selesai: parameter ojek dilepas, tidak disimpan di self


def main():
    ayu = Penumpang("Ayu")
    ojek_rudi = Ojek("Pak Rudi", "KT 4521 AB", 2500)
    ojek_dedi = Ojek("Bang Dedi", "KT 3317 CD", 2500)

    print("=== PERJALANAN 1 ===")
    ayu.pesan_ojek(ojek_rudi, "Kampus Gunung Kelua", 4)  # [5]

    print()
    print("=== PERJALANAN 2 ===")
    ayu.pesan_ojek(ojek_dedi, "Tepian Mahakam", 6)  # ojek lain pun bisa

    print()
    print("=== RINGKASAN ===")
    print(f"Ayu sudah {ayu.jumlah_perjalanan} kali naik ojek")
    print(f"Total ongkos: Rp{ayu.total_ongkos}")


if __name__ == "__main__":
    main()
