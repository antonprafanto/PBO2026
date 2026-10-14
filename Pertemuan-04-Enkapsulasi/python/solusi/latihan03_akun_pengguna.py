"""
Solusi Latihan 03 - Akun Pengguna dengan Password
Pertemuan 04 - Enkapsulasi

Ide penyelesaian:
- username: read-only (property tanpa setter).
- password disimpan di _password dan SENGAJA tidak diberi property sama
  sekali. Dari luar, password hanya bisa DICOCOKKAN lewat cek_password(),
  tidak pernah bisa dibaca.
- Password hanya bisa diganti lewat ganti_password(lama, baru), dan hanya
  jika password lama benar.
- Aturan "minimal 8 karakter" dipakai di dua tempat (konstruktor dan
  ganti_password), jadi ditulis sekali di method internal _periksa_password().
  Garis bawah di depan nama method = method itu urusan internal kelas.

Catatan: di aplikasi sungguhan, password TIDAK PERNAH disimpan sebagai teks
asli, melainkan diubah dulu dengan fungsi hash. Di latihan ini kita
sederhanakan agar fokus pada enkapsulasi.

Cara menjalankan:
    python latihan03_akun_pengguna.py
"""


class AkunPengguna:
    """Akun aplikasi. Password tersimpan tersembunyi dan tidak punya getter."""

    PANJANG_MINIMAL = 8

    def __init__(self, username, password):
        self._periksa_password(password)  # ditolak di sini jika terlalu pendek
        self._username = username
        self._password = password  # tidak ada property untuk atribut ini

    @property
    def username(self):
        return self._username

    def _periksa_password(self, password):
        """Method internal: menolak password yang terlalu pendek."""
        if len(password) < AkunPengguna.PANJANG_MINIMAL:
            raise ValueError(
                f"Password minimal {AkunPengguna.PANJANG_MINIMAL} karakter")

    def cek_password(self, password):
        """True jika password cocok. Password asli tidak pernah dikeluarkan."""
        return password == self._password

    def ganti_password(self, password_lama, password_baru):
        if not self.cek_password(password_lama):
            raise ValueError("Password lama salah")
        self._periksa_password(password_baru)
        self._password = password_baru


def coba_login(akun, password):
    if akun.cek_password(password):
        hasil = "berhasil"
    else:
        hasil = "gagal"
    print(f"Login {akun.username} dengan '{password}': {hasil}")


def main():
    print("=== MEMBUAT AKUN ===")
    akun = AkunPengguna("ayu_unmul", "rahasia123")
    print(f"Akun {akun.username} berhasil dibuat")
    try:
        AkunPengguna("bima_unmul", "12345")
    except ValueError as e:
        print(f"Gagal membuat akun: {e}")

    print()
    print("=== LOGIN ===")
    coba_login(akun, "salah123")
    coba_login(akun, "rahasia123")

    print()
    print("=== GANTI PASSWORD ===")
    try:
        akun.ganti_password("tebak-tebak", "kopiSusu2026")
    except ValueError as e:
        print(f"Ditolak: {e}")
    try:
        akun.ganti_password("rahasia123", "kopi")
    except ValueError as e:
        print(f"Ditolak: {e}")
    akun.ganti_password("rahasia123", "kopiSusu2026")
    print("Password berhasil diganti")
    coba_login(akun, "rahasia123")
    coba_login(akun, "kopiSusu2026")


if __name__ == "__main__":
    main()
