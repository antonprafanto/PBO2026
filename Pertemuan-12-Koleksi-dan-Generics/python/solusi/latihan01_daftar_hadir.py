"""
Solusi Latihan 01 - Daftar Hadir Unik
Pertemuan 12 - Koleksi dan Generics

Ide penyelesaian:
- Hasil scan QR disimpan di list. Isinya bisa kembar, karena ada mahasiswa
  yang memindai dua kali.
- Ubah ke set agar setiap mahasiswa hanya dihitung sekali.
- Operasi himpunan:
    hadir di keduanya  = p1 & p2          (irisan)
    hadir sekali saja  = p1 ^ p2          (selisih simetris: hanya di salah satu)
    belum pernah hadir = kelas - (p1 | p2)
- Isi set selalu diurutkan dulu (sorted) sebelum dicetak.

Cara menjalankan:
    python latihan01_daftar_hadir.py
"""


def gabung(isi: set[str]) -> str:
    """Isi set -> teks berurutan abjad, dipisah koma."""
    return ", ".join(sorted(isi))


def main():
    kelas = ["Ayu", "Bima", "Citra", "Dimas", "Eka", "Fajar", "Gita", "Hadi"]
    scan_p1 = ["Ayu", "Bima", "Citra", "Ayu", "Eka", "Gita", "Bima"]
    scan_p2 = ["Bima", "Citra", "Dimas", "Gita", "Citra"]

    hadir_p1 = set(scan_p1)
    hadir_p2 = set(scan_p2)

    print("=== REKAP DAFTAR HADIR KELAS PBO ===")
    print(f"Pertemuan 1: {len(scan_p1)} kali scan, {len(hadir_p1)} mahasiswa")
    print(f"Pertemuan 2: {len(scan_p2)} kali scan, {len(hadir_p2)} mahasiswa")
    print(f"Hadir di kedua pertemuan: {gabung(hadir_p1 & hadir_p2)}")
    print(f"Hadir sekali saja       : {gabung(hadir_p1 ^ hadir_p2)}")
    belum = set(kelas) - (hadir_p1 | hadir_p2)
    print(f"Belum pernah hadir      : {gabung(belum)}")


if __name__ == "__main__":
    main()
