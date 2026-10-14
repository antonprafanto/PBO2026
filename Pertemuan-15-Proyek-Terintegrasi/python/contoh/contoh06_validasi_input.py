"""
Contoh 06 - Validasi Input: Periksa, Tanya Ulang, Tangani Akhir Input
Pertemuan 15 - Proyek Terintegrasi

Program interaktif membaca input dengan input(). Di contoh ini input()
DIGANTIKAN oleh objek MasukanPalsu yang mengambil jawaban dari daftar yang
sudah disiapkan. Program bisa dijalankan tanpa mengetik apa pun, dan
output-nya selalu sama.

Tiga kebiasaan aman saat membaca input:
1. Validasi    : periksa jawaban (kosong? angka? dalam batas? pilihan dikenal?)
2. Tanya ulang : jika tidak valid, beri pesan yang jelas lalu tanya lagi
3. Akhir input : input() melempar EOFError jika input habis; tangani dengan rapi

Cara menjalankan:
    python contoh06_validasi_input.py
"""

HARGA_TIKET = {"U": 50000, "M": 25000}
NAMA_KATEGORI = {"U": "Umum", "M": "Mahasiswa"}


class MasukanPalsu:
    """Pengganti input(): jawaban diambil dari daftar yang sudah disiapkan."""

    def __init__(self, daftar_jawaban: list[str]):
        self._sisa = list(daftar_jawaban)

    def baca(self, pertanyaan: str) -> str:
        if not self._sisa:  # [1] jawaban habis = input berakhir
            print(f"{pertanyaan}(input habis)")
            raise EOFError("EOF when reading a line")  # sama seperti input() asli
        jawaban = self._sisa.pop(0)
        # Tampilkan pertanyaan + jawaban seolah-olah diketik pengguna.
        # Jawaban kosong ditampilkan sebagai <Enter> agar terlihat.
        print(f"{pertanyaan}{jawaban if jawaban else '<Enter>'}")
        return jawaban


def tanya_angka(masukan: MasukanPalsu, pertanyaan: str, minimum: int,
                maksimum: int) -> int:
    """Bertanya terus sampai jawabannya angka bulat dari minimum..maksimum."""
    while True:  # [2] ulangi sampai jawabannya valid
        teks = masukan.baca(pertanyaan).strip()
        if teks == "":
            print("  Jawaban tidak boleh kosong.")
            continue
        try:
            angka = int(teks)  # [3] melempar ValueError jika bukan angka
        except ValueError:
            print(f"  '{teks}' bukan angka bulat.")
            continue
        if angka < minimum or angka > maksimum:  # [4] periksa batas
            print(f"  Harus di antara {minimum} dan {maksimum}.")
            continue
        return angka


def tanya_pilihan(masukan: MasukanPalsu, pertanyaan: str,
                  pilihan: dict[str, str]) -> str:
    """Bertanya terus sampai jawabannya salah satu kunci di pilihan."""
    while True:
        teks = masukan.baca(pertanyaan).strip().upper()  # [5] "m" sama dengan "M"
        if teks in pilihan:
            return teks
        print(f"  Pilihan tersedia: {', '.join(pilihan)}.")


def daftar_seminar(masukan: MasukanPalsu):
    jumlah = tanya_angka(masukan, "Jumlah tiket (1-5): ", 1, 5)
    kategori = tanya_pilihan(masukan, "Kategori (U=Umum, M=Mahasiswa): ",
                             NAMA_KATEGORI)
    total = jumlah * HARGA_TIKET[kategori]
    print(f"Pendaftaran berhasil: {jumlah} tiket {NAMA_KATEGORI[kategori]}, "
          f"total Rp{total}")


def main():
    print("=== SKENARIO 1: PENGGUNA SALAH KETIK BEBERAPA KALI ===")
    daftar_seminar(MasukanPalsu(["", "dua", "9", "2", "x", "m"]))

    print()
    print("=== SKENARIO 2: INPUT BERAKHIR DI TENGAH JALAN ===")
    try:
        daftar_seminar(MasukanPalsu(["abc"]))
    except EOFError:  # [6] tangani dengan rapi, jangan biarkan program crash
        print("Input berakhir. Pendaftaran dibatalkan.")


if __name__ == "__main__":
    main()
