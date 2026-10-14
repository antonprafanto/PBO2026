"""
Solusi Latihan 01 - Rata-rata Nilai dari Teks
Pertemuan 11 - Exception Handling

Ide penyelesaian:
- Setiap teks diubah dengan int() di dalam try. Jika gagal (ValueError),
  cetak pesan, lalu perulangan lanjut ke teks berikutnya.
- Blok else hanya berjalan jika int() berhasil: di sanalah nilai dijumlahkan.
- Rata-rata = total // jumlah_valid. Jika TIDAK ADA nilai yang valid,
  jumlah_valid = 0 sehingga pembagian melempar ZeroDivisionError.
  Exception itu sengaja tidak ditangkap di rata_rata_nilai(), tetapi
  merambat ke proses_kelas(), yang tahu harus menampilkan pesan apa.

Cara menjalankan:
    python latihan01_rata_rata_nilai.py
"""


def rata_rata_nilai(daftar_teks: list[str]) -> int:
    """Rata-rata (dibulatkan ke bawah) dari teks yang berisi bilangan bulat."""
    total = 0
    jumlah_valid = 0
    for teks in daftar_teks:
        try:
            nilai = int(teks)
        except ValueError:
            print(f"  '{teks}' bukan angka, dilewati")
        else:
            total += nilai
            jumlah_valid += 1
    return total // jumlah_valid  # ZeroDivisionError jika jumlah_valid = 0


def proses_kelas(nama_kelas: str, daftar_teks: list[str]):
    print(f"=== {nama_kelas} ===")
    try:
        rata = rata_rata_nilai(daftar_teks)
        print(f"Rata-rata: {rata}")
    except ZeroDivisionError:
        print("Tidak ada nilai yang valid, rata-rata tidak bisa dihitung")


def main():
    proses_kelas("KELAS A", ["80", "75", "sembilan puluh", "92", ""])
    print()
    proses_kelas("KELAS B", ["-", "tidak hadir"])


if __name__ == "__main__":
    main()
