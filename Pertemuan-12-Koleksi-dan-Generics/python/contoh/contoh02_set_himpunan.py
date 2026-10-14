"""
Contoh 02 - Set: Kumpulan Tanpa Data Kembar
Pertemuan 12 - Koleksi dan Generics

- set otomatis membuang data kembar (duplikat).
- Operasi himpunan: irisan (&), gabungan (|), selisih (-).
- URUTAN isi set TIDAK dijamin. Karena itu, set selalu diurutkan dulu
  dengan sorted() sebelum dicetak.

Cara menjalankan:
    python contoh02_set_himpunan.py
"""


def cetak(judul: str, isi: set[str]):
    """Mencetak isi set dalam urutan abjad agar hasilnya selalu sama."""
    print(f"{judul:<14}: {', '.join(sorted(isi))}")  # [5] urutkan dulu!


def main():
    pendaftar = ["Ayu", "Bima", "Citra", "Ayu", "Dimas", "Bima"]  # [1] ada yang 2 kali
    peserta_python: set[str] = set(pendaftar)  # [2] list -> set: duplikat hilang
    peserta_java = {"Citra", "Eka", "Ayu", "Fajar"}  # [3] set ditulis dengan { }

    print("=== PENDAFTARAN WORKSHOP PYTHON ===")
    print(f"Formulir masuk: {len(pendaftar)}")
    print(f"Peserta unik  : {len(peserta_python)}")
    cetak("Peserta Python", peserta_python)
    peserta_python.add("Eka")  # [4] tambah anggota baru
    peserta_python.add("Ayu")  # sudah ada: diabaikan, tanpa error
    print(f"Setelah tambah Eka dan Ayu: {len(peserta_python)} peserta")

    print()
    print("=== OPERASI HIMPUNAN ===")
    cetak("Peserta Java", peserta_java)
    cetak("Ikut keduanya", peserta_python & peserta_java)  # [6] irisan
    cetak("Semua peserta", peserta_python | peserta_java)  # gabungan
    cetak("Hanya Python", peserta_python - peserta_java)  # selisih
    if "Fajar" not in peserta_python:  # [7] cek keanggotaan
        print("Fajar belum ikut workshop Python")


if __name__ == "__main__":
    main()
