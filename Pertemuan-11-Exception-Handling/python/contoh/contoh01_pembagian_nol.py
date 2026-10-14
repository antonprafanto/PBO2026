"""
Contoh 01 - Exception Pertama: Pembagian dengan Nol
Pertemuan 11 - Exception Handling

Membagi bilangan bulat dengan nol tidak mungkin dilakukan. Python lalu
MELEMPAR exception bernama ZeroDivisionError. Jika tidak ditangkap, program
berhenti mendadak. Dengan try/except, exception itu kita TANGKAP sehingga
program tetap berjalan sampai selesai.

Cara menjalankan:
    python contoh01_pembagian_nol.py
"""


def hitung_patungan(total: int, jumlah_orang: int) -> int:
    """Membagi tagihan sama rata ke semua orang (dibulatkan ke bawah)."""
    return total // jumlah_orang  # [1] gagal jika jumlah_orang = 0


def main():
    print("=== PATUNGAN MAKAN DI WARUNG ===")
    per_orang = hitung_patungan(120000, 4)
    print(f"Rp120000 dibagi 4 orang: Rp{per_orang} per orang")

    print()
    print("=== JIKA JUMLAH ORANG NOL ===")
    try:  # [2] "coba jalankan blok ini"
        print("Menghitung patungan untuk 0 orang...")
        hasil = hitung_patungan(120000, 0)  # [3] exception dilempar di sini
        print(f"Hasil: Rp{hasil} per orang")  # [4] baris ini DILEWATI
    except ZeroDivisionError:  # [5] exception ditangkap di sini
        print("Gagal: jumlah orang tidak boleh nol")
    print("Program tetap berjalan sampai baris terakhir")  # [6]


if __name__ == "__main__":
    main()
