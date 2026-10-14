"""
Contoh 06 - Urutan Alami dengan __lt__
Pertemuan 12 - Koleksi dan Generics

Jika sebuah kelas punya method __lt__ ("less than", kurang dari), objeknya
punya URUTAN ALAMI. sorted(), min(), dan operator < langsung bisa dipakai
tanpa key. Di sini pelari "lebih kecil" artinya "lebih cepat".

Cara menjalankan:
    python contoh06_urutan_alami.py
"""


class Pelari:
    """Peserta lomba lari 5K. Urutan alaminya: waktu tercepat dulu."""

    def __init__(self, nomor: int, nama: str, waktu_detik: int):
        self._nomor = nomor
        self._nama = nama
        self._waktu_detik = waktu_detik

    @property
    def nama(self) -> str:
        return self._nama

    def waktu_teks(self) -> str:
        return f"{self._waktu_detik // 60}:{self._waktu_detik % 60:02d}"

    def __str__(self) -> str:
        return f"#{self._nomor} {self._nama:<6}{self.waktu_teks()}"

    def __lt__(self, lain: "Pelari") -> bool:  # [1] dipakai untuk a < b
        if self._waktu_detik != lain._waktu_detik:
            return self._waktu_detik < lain._waktu_detik
        return self._nomor < lain._nomor  # [2] waktu sama: nomor dada kecil dulu


def main():
    hasil = [
        Pelari(105, "Rudi", 1290),
        Pelari(112, "Maya", 1125),
        Pelari(101, "Joko", 1198),
        Pelari(108, "Lina", 1510),
        Pelari(103, "Fikri", 1198),
    ]
    print("=== CATATAN PANITIA (urutan tiba di meja) ===")
    for pelari in hasil:
        print(pelari)

    print()
    print("=== PERINGKAT (urutan alami: tercepat dulu) ===")
    for nomor, pelari in enumerate(sorted(hasil), start=1):  # [3] tanpa key
        print(f"{nomor}. {pelari}")
    print(f"Juara 1: {min(hasil).nama}")  # [4] min() juga memakai __lt__
    rudi = hasil[0]
    joko = hasil[2]
    print(f"Joko lebih cepat dari Rudi? {'ya' if joko < rudi else 'tidak'}")  # [5]

    print()
    print("=== DARI YANG TERLAMBAT ===")
    for pelari in sorted(hasil, reverse=True):  # [6] urutan alami dibalik
        print(pelari)

    print()
    print("=== ABSENSI (urutan khusus: nama A-Z) ===")
    absensi = sorted(hasil, key=lambda p: p.nama)  # [7] key mengalahkan urutan alami
    print(", ".join([p.nama for p in absensi]))


if __name__ == "__main__":
    main()
