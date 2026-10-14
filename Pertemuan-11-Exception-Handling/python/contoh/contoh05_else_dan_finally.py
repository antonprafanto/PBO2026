"""
Contoh 05 - else dan finally
Pertemuan 11 - Exception Handling

Bentuk lengkap try di Python:
    try:      kode yang mungkin gagal
    except:   dijalankan jika GAGAL (dan jenis error-nya cocok)
    else:     dijalankan jika TIDAK ADA error sama sekali
    finally:  SELALU dijalankan, berhasil maupun gagal

finally cocok untuk "bersih-bersih": mematikan alat, menutup file, dan
sejenisnya. Di contoh ini, proyektor harus SELALU dimatikan setelah
presentasi, apa pun yang terjadi.

Cara menjalankan:
    python contoh05_else_dan_finally.py
"""


class Proyektor:
    """Proyektor ruang kelas yang hanya bisa menampilkan file PDF."""

    def __init__(self, ruang: str):
        self._ruang = ruang
        self._lampu_putus = False

    def rusakkan_lampu(self):
        """Simulasi kerusakan: lampu proyektor putus."""
        self._lampu_putus = True

    def nyalakan(self):
        print(f"  Proyektor {self._ruang} menyala")

    def matikan(self):
        print(f"  Proyektor {self._ruang} dimatikan")

    def tampilkan(self, nama_file: str):
        if self._lampu_putus:
            raise RuntimeError("lampu proyektor putus")
        if not nama_file.endswith(".pdf"):
            raise ValueError(f"file {nama_file} bukan PDF")
        print(f"  Menampilkan {nama_file}")


def presentasi(proyektor: Proyektor, nama_file: str):
    proyektor.nyalakan()
    try:
        proyektor.tampilkan(nama_file)  # [1] bisa gagal
    except ValueError as e:  # [2] hanya menangani ValueError
        print(f"  Gagal presentasi: {e}")
    else:  # [3] hanya jika blok try berhasil tanpa error
        print("  Presentasi lancar, terima kasih!")
    finally:  # [4] SELALU dijalankan
        proyektor.matikan()


def main():
    proyektor = Proyektor("R301")

    print("=== PRESENTASI 1: LANCAR ===")
    presentasi(proyektor, "laporan-akhir.pdf")

    print()
    print("=== PRESENTASI 2: FILE SALAH ===")
    presentasi(proyektor, "laporan-akhir.docx")

    print()
    print("=== PRESENTASI 3: LAMPU PUTUS ===")
    proyektor.rusakkan_lampu()
    try:
        presentasi(proyektor, "laporan-akhir.pdf")  # [5]
    except RuntimeError as e:  # [6] ditangkap oleh pemanggil
        print(f"Ditangani di main: {e}")


if __name__ == "__main__":
    main()
