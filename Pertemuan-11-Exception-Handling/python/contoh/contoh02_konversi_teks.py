"""
Contoh 02 - Mengubah Teks Menjadi Angka
Pertemuan 11 - Exception Handling

Data dari formulir, file, atau jaringan selalu datang sebagai TEKS. Saat
teks diubah menjadi angka dengan int(), teks yang bukan bilangan bulat
membuat Python melempar ValueError. Di contoh ini, isian yang salah
dilewati dengan pesan yang ramah, dan isian yang benar tetap dijumlahkan.

Data sengaja ditulis langsung di program (bukan dari input keyboard),
supaya hasilnya selalu sama setiap kali dijalankan.

Cara menjalankan:
    python contoh02_konversi_teks.py
"""


def main():
    # [1] isian jumlah porsi dari formulir pesanan online (semuanya teks)
    isian_formulir = ["3", "dua", "5", "2.5", "", "4"]
    total = 0
    jumlah_salah = 0

    print("=== REKAP JUMLAH PORSI ===")
    for teks in isian_formulir:
        try:
            porsi = int(teks)  # [2] bisa melempar ValueError
            total += porsi  # [3] hanya dijalankan jika int() berhasil
            print(f"'{teks}' -> {porsi} porsi")
        except ValueError:  # [4] isian ini dilewati, perulangan lanjut
            jumlah_salah += 1
            print(f"'{teks}' -> bukan bilangan bulat, dilewati")

    print()
    print(f"Total porsi     : {total}")
    print(f"Isian yang salah: {jumlah_salah}")


if __name__ == "__main__":
    main()
