"""
Solusi Latihan 02 - Playlist dan Lagu (Agregasi)
Pertemuan 05 - Relasi Antar Kelas

Ide penyelesaian:
- Lagu dibuat di LUAR playlist, lalu dimasukkan dengan tambah(lagu).
  Karena itu, satu lagu yang sama boleh masuk ke dua playlist (agregasi).
- Property daftar_lagu mengembalikan SALINAN list, sehingga list asli di
  dalam playlist tidak bisa dikosongkan dari luar.
- Durasi disimpan dalam detik (integer), lalu diubah menjadi teks m:ss.

Cara menjalankan:
    python latihan02_playlist.py
"""


def format_durasi(detik: int) -> str:
    """Mengubah 215 menjadi '3:35'."""
    return f"{detik // 60}:{detik % 60:02d}"


class Lagu:
    """Sebuah lagu. Lagu bisa ada tanpa playlist mana pun."""

    def __init__(self, judul: str, penyanyi: str, durasi_detik: int):
        self._judul = judul
        self._penyanyi = penyanyi
        self._durasi_detik = durasi_detik

    @property
    def durasi_detik(self) -> int:
        return self._durasi_detik

    def __str__(self) -> str:
        durasi = format_durasi(self._durasi_detik)
        return f"{self._judul} - {self._penyanyi} ({durasi})"


class Playlist:
    """Playlist yang mengumpulkan lagu-lagu yang sudah ada."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_lagu: list[Lagu] = []

    def tambah(self, lagu: Lagu):
        self._daftar_lagu.append(lagu)

    @property
    def daftar_lagu(self) -> list[Lagu]:
        return list(self._daftar_lagu)  # salinan, bukan list asli

    def total_durasi(self) -> int:
        total = 0
        for lagu in self._daftar_lagu:
            total += lagu.durasi_detik
        return total

    def tampilkan(self):
        jumlah = len(self._daftar_lagu)
        total = format_durasi(self.total_durasi())
        print(f"{self._nama} ({jumlah} lagu, total {total}):")
        for nomor, lagu in enumerate(self._daftar_lagu, start=1):
            print(f"  {nomor}. {lagu}")


def main():
    pusaka = Lagu("Indonesia Pusaka", "Ismail Marzuki", 215)
    ampar = Lagu("Ampar-Ampar Pisang", "Lagu Daerah Kalimantan Selatan", 132)
    bengawan = Lagu("Bengawan Solo", "Gesang", 187)

    belajar = Playlist("Teman Belajar")
    mudik = Playlist("Perjalanan Mudik")
    belajar.tambah(pusaka)
    belajar.tambah(bengawan)
    mudik.tambah(ampar)
    mudik.tambah(bengawan)  # lagu yang sama ada di dua playlist

    print("=== DAFTAR PLAYLIST ===")
    belajar.tampilkan()
    mudik.tampilkan()

    print()
    print("=== MENGOSONGKAN SALINAN DARI LUAR ===")
    salinan = belajar.daftar_lagu
    salinan.clear()
    print(f"Salinan di luar kini berisi {len(salinan)} lagu")
    belajar.tampilkan()


if __name__ == "__main__":
    main()
