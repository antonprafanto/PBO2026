"""
Contoh 04 - Menjelajahi Isi Dict dan Menjaga Urutan
Pertemuan 12 - Koleksi dan Generics

- Menghitung kemunculan dengan dict: hitung[k] = hitung.get(k, 0) + 1
- Tiga cara menjelajah: kunci saja, nilai saja, atau pasangan kunci-nilai.
- dict Python MENJAGA urutan saat kunci pertama kali dimasukkan
  (dijamin sejak Python 3.7). Untuk urutan abjad, urutkan dulu dengan sorted().
- dict comprehension: membuat dict baru dari dict lama dalam satu baris.

Cara menjalankan:
    python contoh04_iterasi_dict.py
"""


def main():
    suara = ["Bima", "Ayu", "Bima", "Citra", "Ayu", "Bima"]  # [1] isi kotak suara
    hitung: dict[str, int] = {}
    for nama in suara:
        hitung[nama] = hitung.get(nama, 0) + 1  # [2] belum ada -> mulai dari 0

    print("=== HASIL PEMILIHAN KETUA HIMPUNAN ===")
    print(f"Kandidat   : {', '.join(hitung.keys())}")  # [3] kunci saja
    total = sum(hitung.values())  # [4] nilai saja
    print(f"Total suara: {total}")
    for nama, jumlah in hitung.items():  # [5] pasangan kunci-nilai
        print(f"{nama}: {jumlah} suara")

    print()
    print("=== URUT NAMA KANDIDAT (A-Z) ===")
    for nama, jumlah in sorted(hitung.items()):  # [6] urutkan berdasarkan kunci
        print(f"{nama}: {jumlah} suara")

    print()
    print("=== PERSENTASE (dibulatkan ke bawah) ===")
    persen = {nama: jumlah * 100 // total for nama, jumlah in hitung.items()}  # [7]
    for nama, nilai in persen.items():
        print(f"{nama}: {nilai}%")


if __name__ == "__main__":
    main()
