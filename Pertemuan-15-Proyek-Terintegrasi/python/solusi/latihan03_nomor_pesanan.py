"""
Solusi Latihan 03 - Melanjutkan Nomor Pesanan dari File
Pertemuan 15 - Proyek Terintegrasi

Ide penyelesaian:
- Jika file transaksi belum ada, nomor berikutnya adalah P001.
- Baca semua baris (lewati judul kolom dan baris kosong). Kolom pertama
  berisi nomor seperti "P012". Buang huruf P, ubah sisanya menjadi int.
- Cari angka TERBESAR (bukan baris terakhir: urutan baris bisa saja acak),
  lalu tambah 1 dan format lagi menjadi P + 3 digit.
- Jangan membandingkan nomor sebagai TEKS: "P999" > "P1000" menurut abjad!

Cara menjalankan:
    python latihan03_nomor_pesanan.py
"""

import csv
import tempfile
from pathlib import Path

JUDUL = "nomor;pelanggan;no_hp;jumlah_porsi;total\n"


def nomor_berikutnya(path: Path) -> str:
    if not path.exists():
        return "P001"
    terbesar = 0
    with open(path, encoding="utf-8", newline="") as berkas:
        pembaca = csv.reader(berkas, delimiter=";")
        next(pembaca, None)  # lewati judul kolom (None: aman jika file kosong)
        for kolom in pembaca:
            if not kolom:
                continue
            angka = int(kolom[0][1:])  # "P012" -> "012" -> 12
            if angka > terbesar:
                terbesar = angka
    return f"P{terbesar + 1:03d}"


def buat_baris(daftar_nomor: list[str]) -> str:
    """Membuat isi file transaksi palsu dengan nomor-nomor tertentu."""
    teks = JUDUL
    for nomor in daftar_nomor:
        teks += f"{nomor};Pelanggan Uji;080000000000;1;10000\n"
    return teks


def main():
    skenario = [
        ("Hanya baris judul", []),
        ("P001, P002, P003", ["P001", "P002", "P003"]),
        ("P001, P002, P001 (ganda)", ["P001", "P002", "P001"]),
        ("P998, P999, P1000", ["P998", "P999", "P1000"]),
    ]
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "transaksi.csv"
        print("=== NOMOR PESANAN BERIKUTNYA ===")
        print(f"{'File belum ada':<28}-> {nomor_berikutnya(path)}")
        for keterangan, daftar_nomor in skenario:
            path.write_text(buat_baris(daftar_nomor), encoding="utf-8")
            print(f"{keterangan:<28}-> {nomor_berikutnya(path)}")

    print()
    print("=== JEBAKAN: MEMBANDINGKAN SEBAGAI TEKS ===")
    print(f"Nomor terbesar menurut abjad: {max(['P998', 'P999', 'P1000'])} (SALAH)")


if __name__ == "__main__":
    main()
