"""
Solusi Latihan 04 - Rekap Nilai Kuis dengan Fungsi
Pertemuan 01 - Pengenalan PBO

Ide penyelesaian:
- Setiap tugas dibuat menjadi satu fungsi kecil yang MENGEMBALIKAN hasilnya.
  main() cukup memanggil fungsi-fungsi itu lalu mencetak hasilnya.
- hitung_rata_rata: jumlahkan semua nilai, lalu bagi bulat (//) dengan banyak data.
- cari_tertinggi: anggap elemen pertama yang tertinggi, lalu bandingkan satu per satu.
- hitung_lulus: hitung berapa nilai yang >= batas.
- huruf_mutu: periksa dari batas tertinggi dulu (if-elif-else).

Cara menjalankan:
    python latihan04_rekap_nilai.py
"""


def hitung_rata_rata(daftar_nilai):
    total = 0
    for n in daftar_nilai:
        total = total + n
    return total // len(daftar_nilai)


def cari_tertinggi(daftar_nilai):
    tertinggi = daftar_nilai[0]
    for n in daftar_nilai:
        if n > tertinggi:
            tertinggi = n
    return tertinggi


def hitung_lulus(daftar_nilai, batas):
    jumlah = 0
    for n in daftar_nilai:
        if n >= batas:
            jumlah = jumlah + 1
    return jumlah


def huruf_mutu(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"


def main():
    nilai_kuis = [85, 72, 58, 91, 66, 47]

    print("=== NILAI KUIS PBO ===")
    for i in range(len(nilai_kuis)):
        nilai = nilai_kuis[i]
        print(f"Mahasiswa {i + 1}: {nilai} ({huruf_mutu(nilai)})")

    print()
    print("=== REKAP ===")
    print(f"Rata-rata : {hitung_rata_rata(nilai_kuis)}")
    print(f"Tertinggi : {cari_tertinggi(nilai_kuis)}")
    jumlah_lulus = hitung_lulus(nilai_kuis, 60)
    print(f"Lulus     : {jumlah_lulus} dari {len(nilai_kuis)} mahasiswa")


if __name__ == "__main__":
    main()
