"""
Solusi Latihan 06 - Robot Penjelajah
Pertemuan 02 - Kelas dan Objek

Ide penyelesaian:
- Simpan arah sebagai indeks ke daftar ARAH ["Utara", "Timur", "Selatan", "Barat"].
  Belok kanan: (indeks + 1) % 4. Belok kiri: (indeks + 3) % 4, sama dengan
  mundur 1. Operator % 4 membuat indeks berputar kembali ke 0 sampai 3.
- maju() mengubah x atau y sesuai arah saat ini.
- jalankan(perintah) membaca huruf satu per satu lalu memanggil method lain
  milik objek yang sama (self.maju(), self.belok_kanan(), ...).

Cara menjalankan (dari folder python/solusi; macOS/Linux: python3):
    python latihan06_robot.py
"""

# Konstanta: nama berhuruf kapital semua menandakan nilainya tidak diubah.
ARAH = ["Utara", "Timur", "Selatan", "Barat"]


class Robot:
    """Robot di bidang koordinat. Mulai di (0, 0) menghadap Utara."""

    def __init__(self, nama):
        self.nama = nama
        self.x = 0
        self.y = 0
        self.indeks_arah = 0  # 0 = Utara

    def belok_kanan(self):
        self.indeks_arah = (self.indeks_arah + 1) % 4

    def belok_kiri(self):
        self.indeks_arah = (self.indeks_arah + 3) % 4  # sama dengan mundur 1

    def maju(self):
        arah = ARAH[self.indeks_arah]
        if arah == "Utara":
            self.y = self.y + 1
        elif arah == "Timur":
            self.x = self.x + 1
        elif arah == "Selatan":
            self.y = self.y - 1
        else:
            self.x = self.x - 1

    def posisi(self):
        return f"({self.x}, {self.y}) menghadap {ARAH[self.indeks_arah]}"

    def jalankan(self, perintah):
        print(f"{self.nama} menjalankan perintah '{perintah}'")
        for huruf in perintah:
            if huruf == "M":
                self.maju()
            elif huruf == "R":
                self.belok_kanan()
            elif huruf == "L":
                self.belok_kiri()
            else:
                print(f"  Perintah '{huruf}' tidak dikenal, dilewati")
        print(f"  Posisi sekarang: {self.posisi()}")


def main():
    robi = Robot("Robi")
    print(f"Posisi awal: {robi.posisi()}")
    robi.jalankan("MMRMM")
    robi.jalankan("LLMX")


if __name__ == "__main__":
    main()
