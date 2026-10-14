"""
Contoh 02 - Variabel dan Tipe Data
Pertemuan 01 - Pengenalan PBO

- Variabel adalah "kotak bernama" untuk menyimpan sebuah nilai.
- Di Python, tipe variabel mengikuti nilai yang disimpan di dalamnya:
  str (teks), int (bilangan bulat), float (bilangan pecahan).
- f-string (teks yang diawali huruf f) menyisipkan nilai variabel ke dalam teks.

Cara menjalankan:
    python contoh02_variabel_dan_tipe.py
"""


def main():
    # [1] variabel dibuat saat pertama kali diisi; tipenya mengikuti nilainya
    nama = "Ayu Lestari"  # str: teks, diapit tanda kutip
    inisial = "A"  # str juga (Python tidak punya tipe khusus untuk satu huruf)
    semester = 3  # int: bilangan bulat
    ipk = 3.75  # float: bilangan pecahan, memakai TITIK desimal

    print("=== DATA MAHASISWA ===")
    print(f"Nama     : {nama}")  # [2] f-string: nilai di dalam {} ikut dicetak
    print(f"Inisial  : {inisial}")
    print(f"Semester : {semester}")
    print(f"IPK      : {ipk}")

    print()
    print("=== HITUNG UANG JAJAN ===")
    uang_saku = 50000
    harga_kopi = 18000
    jumlah_cup = uang_saku // harga_kopi  # [3] // pembagian bulat (sisanya dibuang)
    sisa_uang = uang_saku % harga_kopi  # [4] % sisa hasil bagi
    print(f"Uang saku     : Rp{uang_saku}")
    print(f"Harga kopi    : Rp{harga_kopi}")
    print(f"Bisa beli     : {jumlah_cup} cup")
    print(f"Total belanja : Rp{jumlah_cup * harga_kopi}")  # [5] boleh berisi hitungan
    print(f"Sisa uang     : Rp{sisa_uang}")

    print()
    print("=== MENGUBAH NILAI VARIABEL ===")
    semester = semester + 1  # [6] nilai lama diganti dengan nilai baru
    print(f"Semester depan {nama} masuk semester {semester}")


if __name__ == "__main__":
    main()
