"""
Contoh 01 - Menulis dan Membaca File Teks
Pertemuan 15 - Proyek Terintegrasi

- open(path, "w", encoding="utf-8") : menulis file (isi lama DITIMPA)
- open(path, "a", encoding="utf-8") : menambah di akhir file (append)
- open(path, encoding="utf-8")      : membaca file (mode "r" adalah bawaan)
- Blok with menutup file secara otomatis begitu blok selesai.

Semua file dibuat di folder sementara (modul tempfile). Folder itu dihapus
otomatis di akhir program, jadi tidak ada file yang tertinggal.

Cara menjalankan:
    python contoh01_baca_tulis_teks.py
"""

import tempfile
from pathlib import Path


def main():
    with tempfile.TemporaryDirectory() as folder:  # [1] folder sementara
        path = Path(folder) / "jadwal-piket.txt"  # [2] menyusun path dengan /

        print("=== 1. MENULIS FILE BARU ===")
        with open(path, "w", encoding="utf-8") as berkas:  # [3]
            berkas.write("Senin: Ayu\n")  # [4] write tidak menambah baris baru
            berkas.write("Selasa: Bima\n")
        print(f"File {path.name} sudah ada? {'ya' if path.exists() else 'tidak'}")

        print()
        print("=== 2. MENAMBAH DI AKHIR FILE ===")
        with open(path, "a", encoding="utf-8") as berkas:
            berkas.write("Rabu: Citra\n")
        print("Satu baris ditambahkan di akhir file")

        print()
        print("=== 3. MEMBACA SELURUH ISI ===")
        with open(path, encoding="utf-8") as berkas:
            isi = berkas.read()  # [5] seluruh isi file sebagai satu str
        print(isi, end="")  # isi sudah diakhiri "\n", jadi print tidak menambah lagi

        print()
        print("=== 4. MEMBACA BARIS DEMI BARIS ===")
        with open(path, encoding="utf-8") as berkas:
            for nomor, baris in enumerate(berkas, start=1):  # [6]
                hari, nama = baris.strip().split(": ")  # [7] buang "\n" dulu
                print(f"{nomor}. {nama} piket hari {hari}")

        print()
        print("=== 5. MENIMPA ISI FILE ===")
        with open(path, "w", encoding="utf-8") as berkas:
            berkas.write("Kamis: Dimas\n")
        print(path.read_text(encoding="utf-8"), end="")  # [8] cara singkat membaca

        print()
        print("=== 6. MEMBACA FILE YANG TIDAK ADA ===")
        try:
            with open(Path(folder) / "jadwal-lama.txt", encoding="utf-8") as berkas:
                print(berkas.read())
        except FileNotFoundError:  # [9]
            print("File jadwal-lama.txt tidak ditemukan, lanjut dengan data kosong")

    print()
    dihapus = "ya" if not Path(folder).exists() else "tidak"
    print(f"Folder sementara sudah dihapus? {dihapus}")  # [10]


if __name__ == "__main__":
    main()
