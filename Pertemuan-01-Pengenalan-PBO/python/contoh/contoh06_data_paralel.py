"""
Contoh 06 - Data Paralel: Rapi di Awal, Rapuh Saat Program Membesar
Pertemuan 01 - Pengenalan PBO

Data satu mahasiswa disimpan di BEBERAPA list (nama, nim, nilai).
Indeks yang sama = mahasiswa yang sama. Agar data tidak tertukar, setiap
fungsi yang memindahkan data wajib memindahkan SEMUA list bersama-sama.

Ceritanya: fungsi urutkan_berdasarkan_nilai() ditulis ketika datanya baru
nama dan nilai. Belakangan, list nim ditambahkan, tetapi fungsi itu lupa
diperbarui. Perhatikan apa yang terjadi pada NIM setelah pengurutan!

Cara menjalankan:
    python contoh06_data_paralel.py
"""


def tampilkan(nama, nim, nilai):
    for i in range(len(nama)):
        print(f"{i + 1}. {nim[i]} {nama[i]} - nilai {nilai[i]}")


def urutkan_berdasarkan_nilai(nama, nilai):  # [1] fungsi lama: hanya kenal 2 list
    """Bubble sort: bandingkan dua tetangga, tukar jika urutannya salah."""
    n = len(nilai)
    for putaran in range(n - 1):
        for i in range(n - 1 - putaran):
            if nilai[i] > nilai[i + 1]:
                # [2] tukar nilai, lalu tukar nama di posisi yang sama
                nilai[i], nilai[i + 1] = nilai[i + 1], nilai[i]
                nama[i], nama[i + 1] = nama[i + 1], nama[i]


def main():
    # [3] tiga list paralel: indeks yang sama = mahasiswa yang sama
    nama = ["Ayu", "Bima", "Citra", "Dimas"]
    nim = ["2409106001", "2409106002", "2409106003", "2409106004"]
    nilai = [90, 55, 78, 62]

    print("=== DATA AWAL ===")
    tampilkan(nama, nim, nilai)

    print()
    print("=== DIURUTKAN DARI NILAI TERKECIL ===")
    urutkan_berdasarkan_nilai(nama, nilai)  # [4] list nim tidak ikut dikirim!
    tampilkan(nama, nim, nilai)

    print()
    print("Nama dan nilai pindah bersama, tetapi NIM tertinggal di tempatnya.")
    print(f"Sekarang NIM {nim[0]} milik Ayu tercatat bersama {nama[0]}!")


if __name__ == "__main__":
    main()
