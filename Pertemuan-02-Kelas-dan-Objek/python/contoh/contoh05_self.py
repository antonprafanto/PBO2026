"""
Contoh 05 - Memahami self
Pertemuan 02 - Kelas dan Objek

self adalah "objek yang sedang menjalankan method ini".
- self.email    -> atribut milik objek
- email         -> parameter (variabel lokal method)
- self.method() -> memanggil method lain milik objek yang sama

Cara menjalankan (dari folder python/contoh; macOS/Linux: python3):
    python contoh05_self.py
"""


class Akun:
    """Akun aplikasi dengan username dan email."""

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def ganti_email(self, email):
        # [1] kiri: atribut milik objek, kanan: parameter yang baru diterima
        print(f"{self.username}: email {self.email} diganti ke {email}")
        self.email = email

    def sapa(self):
        return f"Halo, {self.username}!"

    def tampilkan_profil(self):
        print(self.sapa())  # [2] memanggil method lain lewat self
        print(f"  Email terdaftar: {self.email}")


def main():
    akun_budi = Akun("budi_s", "budi@contoh.id")
    akun_siti = Akun("siti_a", "siti@contoh.id")

    print("=== PROFIL AWAL ===")
    akun_budi.tampilkan_profil()  # [3] di dalam method, self = akun_budi
    akun_siti.tampilkan_profil()  #     di dalam method, self = akun_siti

    print()
    print("=== BUDI MENGGANTI EMAIL ===")
    akun_budi.ganti_email("budi.santoso@contoh.id")
    akun_budi.tampilkan_profil()
    akun_siti.tampilkan_profil()  # email Siti tidak ikut berubah


if __name__ == "__main__":
    main()
