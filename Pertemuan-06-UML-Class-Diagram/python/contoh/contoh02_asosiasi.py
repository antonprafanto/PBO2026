"""
Contoh 02 - Asosiasi Berarah dan Multiplisitas
Pertemuan 06 - UML Class Diagram

Diagram (versi Python, sintaks Mermaid):

    PesananOjek "*" --> "1" Penumpang : _penumpang
    PesananOjek "*" --> "0..1" Pengemudi : _pengemudi

- Panah --> berarti PesananOjek MENGENAL Penumpang dan Pengemudi.
  Navigasinya satu arah: Penumpang tidak menyimpan daftar pesanannya.
- "1"    : setiap pesanan WAJIB punya tepat satu penumpang (diisi di konstruktor).
- "0..1" : pengemudi boleh belum ada (None) saat pesanan baru dibuat.
- "*"    : satu penumpang boleh punya banyak pesanan.

Cara menjalankan:
    python contoh02_asosiasi.py
"""


class Penumpang:
    """Pengguna aplikasi yang memesan ojek."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama


class Pengemudi:
    """Pengemudi ojek beserta pelat nomor motornya."""

    def __init__(self, nama: str, plat: str):
        self._nama = nama
        self._plat = plat

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def plat(self) -> str:
        return self._plat


class PesananOjek:
    """Satu pesanan ojek: penumpang wajib ada, pengemudi menyusul."""

    def __init__(self, penumpang: Penumpang, tujuan: str):
        self._penumpang = penumpang  # [1] multiplisitas 1: diisi saat objek lahir
        self._tujuan = tujuan
        self._pengemudi: Pengemudi | None = None  # [2] multiplisitas 0..1

    def tetapkan_pengemudi(self, pengemudi: Pengemudi):
        self._pengemudi = pengemudi  # [3] tautan ke pengemudi dibuat belakangan

    def info(self) -> str:
        if self._pengemudi is None:  # [4] 0..1 berarti harus siap menghadapi None
            teks_pengemudi = "belum ada"
        else:
            teks_pengemudi = f"{self._pengemudi.nama} ({self._pengemudi.plat})"
        return f"{self._penumpang.nama} -> {self._tujuan} | pengemudi: {teks_pengemudi}"


def main():
    rina = Penumpang("Rina")
    joko = Pengemudi("Pak Joko", "KT 4521 AB")

    pesanan1 = PesananOjek(rina, "Kampus Unmul Gunung Kelua")
    pesanan2 = PesananOjek(rina, "Pasar Segiri")  # [5] satu penumpang, dua pesanan

    print("=== PESANAN BARU ===")
    print(pesanan1.info())
    print(pesanan2.info())

    print()
    print("=== SETELAH PENGEMUDI DITEMUKAN ===")
    pesanan1.tetapkan_pengemudi(joko)
    print(pesanan1.info())
    print(pesanan2.info())


if __name__ == "__main__":
    main()
