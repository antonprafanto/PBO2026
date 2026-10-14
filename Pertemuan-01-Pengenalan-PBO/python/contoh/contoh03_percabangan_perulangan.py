"""
Contoh 03 - Percabangan dan Perulangan
Pertemuan 01 - Pengenalan PBO

- if / elif / else memilih perintah mana yang dijalankan.
- for mengulang untuk setiap nilai dalam suatu rentang.
- while mengulang SELAMA kondisinya masih benar.
- Blok perintah ditandai dengan titik dua (:) dan INDENTASI 4 spasi.

Cara menjalankan:
    python contoh03_percabangan_perulangan.py
"""


def main():
    print("=== PERCABANGAN: DISKON TOKO ALAT TULIS ===")
    total_belanja = 120000
    member = True  # [1] bool: hanya bernilai True atau False

    if total_belanja >= 100000:  # [2] diperiksa dari atas; yang pertama benar dipilih
        persen_diskon = 10
    elif total_belanja >= 50000:
        persen_diskon = 5
    else:
        persen_diskon = 0

    if member:  # [3] kondisi berupa variabel bool
        persen_diskon = persen_diskon + 5

    potongan = total_belanja * persen_diskon // 100
    print(f"Total belanja : Rp{total_belanja}")
    print(f"Diskon        : {persen_diskon}%")
    print(f"Potongan      : Rp{potongan}")
    print(f"Harus dibayar : Rp{total_belanja - potongan}")

    hari = "Sabtu"
    if hari == "Sabtu" or hari == "Minggu":  # [4] or: cukup salah satu yang benar
        print(f"Hari {hari}: toko tutup pukul 15.00")
    else:
        print(f"Hari {hari}: toko tutup pukul 21.00")

    print()
    print("=== PERULANGAN FOR: DAFTAR HARGA FOTOKOPI ===")
    harga_per_lembar = 500
    for lembar in range(1, 6):  # [5] range(1, 6) menghasilkan 1, 2, 3, 4, 5
        print(f"{lembar} lembar = Rp{lembar * harga_per_lembar}")

    print()
    print("=== PERULANGAN WHILE: MENABUNG UNTUK BUKU ===")
    target = 100000
    tabungan = 0
    minggu = 0
    while tabungan < target:  # [6] diulang SELAMA kondisinya benar
        tabungan = tabungan + 30000
        minggu = minggu + 1
        print(f"Minggu ke-{minggu}: tabungan Rp{tabungan}")
    print(f"Target Rp{target} tercapai dalam {minggu} minggu")


if __name__ == "__main__":
    main()
