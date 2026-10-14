"""
Solusi Latihan 02 - Akun dan Akun Premium
Pertemuan 07 - Pewarisan (Inheritance)

Ide penyelesaian:
- AkunPremium(Akun) menambah atribut masa aktif (bulan).
- info() di-override: ambil teks versi induk dengan super().info(), lalu
  tambahkan keterangan premium.
- batas_unggah_mb() di-override: hasil versi induk dikali 10, sehingga jika
  batas akun biasa berubah, batas akun premium otomatis ikut menyesuaikan.

Cara menjalankan:
    python latihan02_akun_premium.py
"""


class Akun:
    """Akun biasa di sebuah aplikasi penyimpanan berkas."""

    def __init__(self, username: str, email: str):
        self._username = username
        self._email = email

    @property
    def username(self) -> str:
        return self._username

    def info(self) -> str:
        return f"{self._username} <{self._email}>"

    def batas_unggah_mb(self) -> int:
        return 100


class AkunPremium(Akun):
    """Akun berbayar dengan batas unggah 10 kali lipat."""

    def __init__(self, username: str, email: str, masa_aktif_bulan: int):
        super().__init__(username, email)
        self._masa_aktif_bulan = masa_aktif_bulan

    def info(self) -> str:  # override: versi induk + keterangan premium
        return f"{super().info()} [PREMIUM {self._masa_aktif_bulan} bulan]"

    def batas_unggah_mb(self) -> int:  # override: memakai hasil versi induk
        return super().batas_unggah_mb() * 10


def main():
    budi = Akun("budi_s", "budi@contoh.id")
    siti = AkunPremium("siti_a", "siti@contoh.id", 6)

    print("=== DAFTAR AKUN ===")
    print(budi.info())
    print(siti.info())

    print()
    print("=== BATAS UNGGAH ===")
    print(f"{budi.username}: {budi.batas_unggah_mb()} MB")
    print(f"{siti.username}: {siti.batas_unggah_mb()} MB")


if __name__ == "__main__":
    main()
