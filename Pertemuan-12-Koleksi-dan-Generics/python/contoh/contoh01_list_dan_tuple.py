"""
Contoh 01 - List dan Tuple
Pertemuan 12 - Koleksi dan Generics

- list  : berurutan, boleh berisi data kembar, dan isinya BISA diubah (mutable).
- tuple : berurutan, boleh berisi data kembar, tetapi isinya TETAP (immutable).
- list comprehension: membuat list baru dari list lama dalam satu baris.

Cara menjalankan:
    python contoh01_list_dan_tuple.py
"""


def main():
    belanja: list[str] = ["beras", "telur", "minyak"]  # [1] list berisi teks
    print("=== LIST: DAFTAR BELANJA ANAK KOS ===")
    print(f"Isi awal      : {', '.join(belanja)}")

    belanja.append("gula")  # [2] tambah di akhir
    belanja.insert(0, "kopi")  # sisipkan di indeks 0 (paling depan)
    belanja.remove("minyak")  # [3] hapus berdasarkan ISI, bukan indeks
    belanja.append("telur")  # data kembar boleh
    print(f"Setelah diubah: {', '.join(belanja)}")
    print(f"Jumlah item   : {len(belanja)}")
    print(f"Item pertama  : {belanja[0]}")  # [4] akses lewat indeks
    print(f"Item terakhir : {belanja[-1]}")
    if "gula" in belanja:  # [5] cek keanggotaan
        print(f"Posisi gula   : indeks {belanja.index('gula')}")
    print(f"Telur dicatat : {belanja.count('telur')} kali")

    print()
    print("=== DATA TETAP: HARI KULIAH PBO ===")
    hari_kuliah: tuple[str, ...] = ("Senin", "Rabu")  # [6] tuple memakai ( )
    print(f"Hari kuliah   : {', '.join(hari_kuliah)}")
    try:
        hari_kuliah[0] = "Selasa"  # [7] mencoba mengubah isi tuple
    except TypeError:
        print("Gagal mengubah: isinya tetap (immutable)")

    print()
    print("=== MEMBUAT LIST BARU DARI LIST LAMA ===")
    huruf_besar = [barang.upper() for barang in belanja]  # [8] list comprehension
    pendek = [barang for barang in belanja if len(barang) <= 4]  # [9] dengan syarat
    print(f"Huruf besar   : {', '.join(huruf_besar)}")
    print(f"Nama pendek   : {', '.join(pendek)}")
    print(f"List asli     : {', '.join(belanja)}")


if __name__ == "__main__":
    main()
