"""
Contoh 07 - Menyimpan Banyak Objek dalam List
Pertemuan 02 - Kelas dan Objek

Objek bisa disimpan di list seperti data biasa. Dengan perulangan for,
kita bisa memanggil method yang sama untuk setiap objek.

Cara menjalankan:
    python contoh07_daftar_objek.py
"""


class Lagu:
    """Satu lagu di playlist."""

    def __init__(self, judul, penyanyi, durasi_detik):
        self.judul = judul
        self.penyanyi = penyanyi
        self.durasi_detik = durasi_detik

    def durasi_teks(self):
        menit = self.durasi_detik // 60
        detik = self.durasi_detik % 60
        return f"{menit}:{detik:02d}"

    def tampilkan(self):
        print(f"- {self.judul} ({self.penyanyi}) {self.durasi_teks()}")


def main():
    playlist = [  # [1] list berisi tiga objek Lagu
        Lagu("Indonesia Pusaka", "Ismail Marzuki", 215),
        Lagu("Ampar-Ampar Pisang", "Lagu Daerah Kalimantan Selatan", 132),
        Lagu("Bengawan Solo", "Gesang", 187),
    ]

    print("=== PLAYLIST BELAJAR ===")
    total = 0
    for lagu in playlist:  # [2] variabel lagu bergantian menunjuk tiap objek
        lagu.tampilkan()
        total = total + lagu.durasi_detik
    print(f"Jumlah lagu : {len(playlist)}")
    print(f"Total durasi: {total // 60} menit {total % 60} detik")


if __name__ == "__main__":
    main()
