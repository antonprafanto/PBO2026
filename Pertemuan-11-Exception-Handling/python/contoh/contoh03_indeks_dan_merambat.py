"""
Contoh 03 - Indeks di Luar Batas dan Exception yang Merambat
Pertemuan 11 - Exception Handling

Meminta elemen list di posisi yang tidak ada membuat Python melempar
IndexError. Perhatikan juga PERJALANAN exception-nya:

    main() -> umumkan() -> ambil_kelompok()   <- exception lahir di sini

ambil_kelompok() dan umumkan() tidak punya try/except, jadi exception
"merambat" naik ke pemanggilnya, terus sampai ada yang menangkap (main).
Baris-baris yang tersisa di fungsi yang dilewati tidak dijalankan.

Cara menjalankan:
    python contoh03_indeks_dan_merambat.py
"""


def ambil_kelompok(jadwal: list[str], giliran: int) -> str:
    """Mengembalikan nama kelompok pada giliran tertentu (mulai dari 1)."""
    print(f"    [ambil kelompok] mencari giliran {giliran}")
    return jadwal[giliran - 1]  # [1] IndexError jika giliran terlalu besar


def umumkan(jadwal: list[str], giliran: int):
    print(f"  [umumkan] giliran {giliran}")
    kelompok = ambil_kelompok(jadwal, giliran)  # [2] tidak ada try di sini
    print(f"  Giliran {giliran}: {kelompok}")  # [3] dilewati jika ada error


def main():
    jadwal = ["Kelompok Pesut", "Kelompok Enggang", "Kelompok Bekantan"]
    print("=== JADWAL PRESENTASI ===")
    for giliran in [1, 3, 5]:
        try:
            umumkan(jadwal, giliran)  # [4]
        except IndexError:  # [5] exception merambat sampai ke sini
            print(f"  -> Giliran {giliran} tidak ada. "
                  f"Hanya ada {len(jadwal)} kelompok.")


if __name__ == "__main__":
    main()
