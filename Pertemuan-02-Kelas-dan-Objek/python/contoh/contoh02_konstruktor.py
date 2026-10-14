"""
Contoh 02 - Konstruktor: Mengisi Data Saat Objek Dibuat
Pertemuan 02 - Kelas dan Objek

Method khusus __init__ adalah konstruktor. Ia dipanggil OTOMATIS setiap kali
objek baru dibuat, sehingga setiap objek langsung lahir dengan data lengkap.

Cara menjalankan:
    python contoh02_konstruktor.py
"""


class Mobil:
    """Cetak biru mobil: setiap mobil punya merek, warna, dan tahun."""

    def __init__(self, merek, warna, tahun):  # [1] konstruktor
        print(f"  (konstruktor dipanggil untuk mobil {merek})")  # [2]
        self.merek = merek  # [3] simpan parameter ke atribut objek
        self.warna = warna
        self.tahun = tahun


def main():
    print("=== MEMBUAT TIGA OBJEK MOBIL ===")
    mobil_budi = Mobil("Avanza", "hitam", 2019)  # [4] argumen dikirim ke __init__
    mobil_siti = Mobil("Brio", "merah", 2022)
    mobil_rina = Mobil("Xpander", "putih", 2021)

    print()
    print("=== DATA SETIAP MOBIL ===")
    print(f"Mobil Budi: {mobil_budi.merek} {mobil_budi.warna} ({mobil_budi.tahun})")
    print(f"Mobil Siti: {mobil_siti.merek} {mobil_siti.warna} ({mobil_siti.tahun})")
    print(f"Mobil Rina: {mobil_rina.merek} {mobil_rina.warna} ({mobil_rina.tahun})")


if __name__ == "__main__":
    main()
