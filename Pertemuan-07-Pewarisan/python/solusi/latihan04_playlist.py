"""
Solusi Latihan 04 - Playlist Bukan Lagu (is-a vs has-a)
Pertemuan 07 - Pewarisan (Inheritance)

Ide penyelesaian:
- Rancangan lama "class Playlist(Lagu)" keliru: playlist BUKAN sebuah lagu.
  Uji kalimatnya: "Playlist adalah Lagu" terdengar janggal, sedangkan
  "Playlist punya banyak Lagu" terdengar wajar -> hubungannya has-a.
- Karena itu Playlist TIDAK mewarisi Lagu. Playlist menyimpan list berisi
  objek Lagu sebagai atribut (agregasi, seperti di Pertemuan 05).
- Method tambah() memasukkan lagu, total_durasi() menjumlahkan durasi
  semua lagu, tampilkan() mencetak isinya.

Cara menjalankan:
    python latihan04_playlist.py
"""


class Lagu:
    """Satu lagu dengan durasi dalam detik."""

    def __init__(self, judul: str, durasi_detik: int):
        self._judul = judul
        self._durasi_detik = durasi_detik

    @property
    def durasi_detik(self) -> int:
        return self._durasi_detik

    def __str__(self) -> str:
        menit = self._durasi_detik // 60
        detik = self._durasi_detik % 60
        return f"{self._judul} ({menit}:{detik:02d})"


class Playlist:  # TIDAK mewarisi Lagu
    """Playlist PUNYA banyak lagu (has-a), bukan sebuah lagu (is-a)."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_lagu: list[Lagu] = []  # has-a: list berisi objek Lagu

    def tambah(self, lagu: Lagu):
        self._daftar_lagu.append(lagu)

    def total_durasi(self) -> int:
        total = 0
        for lagu in self._daftar_lagu:
            total += lagu.durasi_detik
        return total

    def tampilkan(self):
        print(f"=== PLAYLIST: {self._nama} ===")
        for nomor, lagu in enumerate(self._daftar_lagu, start=1):
            print(f"{nomor}. {lagu}")
        total = self.total_durasi()
        print(f"Jumlah lagu : {len(self._daftar_lagu)}")
        print(f"Total durasi: {total // 60} menit {total % 60} detik")


def main():
    playlist = Playlist("Lagu Daerah Kalimantan")
    playlist.tambah(Lagu("Ampar-Ampar Pisang", 132))
    playlist.tambah(Lagu("Paris Barantai", 185))
    playlist.tambah(Lagu("Indung-Indung", 170))
    playlist.tampilkan()


if __name__ == "__main__":
    main()
