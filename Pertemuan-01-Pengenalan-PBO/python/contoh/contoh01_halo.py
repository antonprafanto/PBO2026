"""
Contoh 01 - Program Pertamaku
Pertemuan 01 - Pengenalan PBO

- print() menampilkan teks ke layar, lalu pindah ke baris baru.
- Semua perintah utama kita taruh di dalam fungsi main().
- Bagian if __name__ == "__main__": adalah "pintu masuk" program.

Cara menjalankan:
    python contoh01_halo.py
"""


def main():  # [1] fungsi utama: tempat perintah-perintah kita
    print("=== PROGRAM PERTAMAKU ===")  # [2] print menampilkan teks ke layar
    print("Halo, Samarinda!")
    print("Selamat datang di mata kuliah PBO 2026.")
    print()  # [3] print tanpa isi = baris kosong
    # [4] baris yang diawali tanda pagar adalah komentar, tidak dijalankan
    print("Perintah dijalankan berurutan dari atas ke bawah:")
    print("Langkah 1: siapkan alat")
    print("Langkah 2: tulis kode")
    print("Langkah 3: jalankan program")


if __name__ == "__main__":  # [5] pintu masuk: benar jika file ini dijalankan langsung
    main()  # [6] memanggil fungsi main
