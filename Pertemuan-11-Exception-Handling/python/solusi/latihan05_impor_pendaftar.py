"""
Solusi Latihan 05 - Impor Data Pendaftar Lomba
Pertemuan 11 - Exception Handling

Ide penyelesaian:
- BarisDataError membawa nomor_baris dan alasan. Pesannya sudah memuat
  nomor baris sehingga penangkap cukup mencetak str(e).
- baca_pendaftar() memeriksa satu baris dari yang paling mendasar:
  jumlah kolom -> nama -> umur angka -> rentang umur. Kesalahan apa pun
  diubah menjadi BarisDataError, jadi pemanggil cukup menangkap SATU jenis.
- ValueError dari int() dibungkus dengan "raise ... from e" (exception
  chaining) sehingga penyebab aslinya tetap tersimpan di e.__cause__.
- main() memakai try/except/else: baris yang lolos masuk daftar peserta,
  baris yang gagal dihitung dan dilaporkan, lalu impor lanjut.

Cara menjalankan:
    python latihan05_impor_pendaftar.py
"""

UMUR_MIN = 17
UMUR_MAKS = 25


class BarisDataError(Exception):
    """Kesalahan pada satu baris data. Menyimpan nomor barisnya."""

    def __init__(self, nomor_baris: int, alasan: str):
        super().__init__(f"Baris {nomor_baris}: {alasan}")
        self.nomor_baris = nomor_baris
        self.alasan = alasan


class Pendaftar:
    """Pendaftar lomba yang datanya sudah lolos pemeriksaan."""

    def __init__(self, nama: str, umur: int):
        self._nama = nama
        self._umur = umur

    def __str__(self) -> str:
        return f"{self._nama} ({self._umur} tahun)"


def baca_pendaftar(nomor_baris: int, teks: str) -> Pendaftar:
    """Mengubah satu baris 'nama;umur' menjadi Pendaftar."""
    bagian = teks.split(";")
    if len(bagian) != 2:
        raise BarisDataError(nomor_baris, "format harus nama;umur")
    nama = bagian[0].strip()
    teks_umur = bagian[1].strip()
    if nama == "":
        raise BarisDataError(nomor_baris, "nama tidak boleh kosong")
    try:
        umur = int(teks_umur)
    except ValueError as e:
        raise BarisDataError(nomor_baris,
                             f"umur '{teks_umur}' bukan angka") from e
    if umur < UMUR_MIN or umur > UMUR_MAKS:
        raise BarisDataError(nomor_baris, f"umur {umur} di luar syarat "
                                          f"{UMUR_MIN}-{UMUR_MAKS} tahun")
    return Pendaftar(nama, umur)


def main():
    data = [
        "Ayu Lestari;20",
        "Bima Saputra",
        "Citra Dewi;dua puluh",
        ";19",
        "Dimas Pratama;30",
        "Eka Putri;18",
        "Fajar Nugraha;21;Samarinda",
    ]
    peserta: list[Pendaftar] = []
    jumlah_ditolak = 0

    print("=== IMPOR DATA PENDAFTAR LOMBA DEBAT ===")
    for nomor, teks in enumerate(data, start=1):
        try:
            pendaftar = baca_pendaftar(nomor, teks)
        except BarisDataError as e:
            jumlah_ditolak += 1
            print(f"[DITOLAK] {e}")
            if e.__cause__ is not None:
                print("          (penyebab asli: kesalahan konversi angka)")
        else:
            peserta.append(pendaftar)
            print(f"[OK] Baris {nomor}: {pendaftar}")

    print()
    print(f"Diterima: {len(peserta)}, ditolak: {jumlah_ditolak}")
    print("Daftar peserta:")
    for pendaftar in peserta:
        print(f"- {pendaftar}")


if __name__ == "__main__":
    main()
