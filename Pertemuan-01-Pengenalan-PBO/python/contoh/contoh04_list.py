"""
Contoh 04 - List: Menyimpan Banyak Data dalam Satu Variabel
Pertemuan 01 - Pengenalan PBO

- List ditulis dengan kurung siku [ ], elemennya dipisah koma.
- Indeks (nomor urut) elemen dimulai dari 0, bukan 1.
- len(list) memberi tahu banyaknya elemen.
- list.sort() mengurutkan isi list (angka dari kecil, teks sesuai abjad).

Cara menjalankan:
    python contoh04_list.py
"""


def main():
    nilai = [78, 92, 65, 88, 70]  # [1] list berisi lima nilai kuis

    print("=== NILAI KUIS ===")
    print(f"Banyak data    : {len(nilai)}")  # [2] len() menghitung jumlah elemen
    print(f"Nilai pertama  : {nilai[0]}")  # [3] indeks pertama adalah 0
    print(f"Nilai terakhir : {nilai[len(nilai) - 1]}")  # indeks terakhir = len - 1

    print()
    print("=== SEMUA NILAI ===")
    for i in range(len(nilai)):  # [4] perulangan dengan indeks: i = 0, 1, 2, 3, 4
        print(f"Mahasiswa ke-{i + 1}: {nilai[i]}")

    total = 0
    tertinggi = nilai[0]
    for n in nilai:  # [5] perulangan langsung: n berisi setiap elemen bergantian
        total = total + n
        if n > tertinggi:
            tertinggi = n
    print(f"Total          : {total}")
    print(f"Rata-rata      : {total // len(nilai)}")  # dibulatkan ke bawah
    print(f"Tertinggi      : {tertinggi}")

    print()
    print("=== MENGUBAH DAN MENGURUTKAN ===")
    nilai[2] = 75  # [6] mengganti elemen di indeks 2 (elemen ketiga)
    print(f"Setelah nilai ke-3 diperbaiki: {nilai}")  # [7] mencetak seluruh list
    nilai.sort()  # [8] mengurutkan dari kecil ke besar
    print(f"Setelah diurutkan            : {nilai}")

    kota = ["Samarinda", "Balikpapan", "Bontang"]
    kota.sort()  # teks diurutkan sesuai abjad
    daftar_kota = ", ".join(kota)  # [9] menggabungkan isi list menjadi satu teks
    print(f"Kota urut abjad: {daftar_kota}")


if __name__ == "__main__":
    main()
