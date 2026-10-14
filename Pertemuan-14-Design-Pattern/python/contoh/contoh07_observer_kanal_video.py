"""
Contoh 07 - Observer: Berlangganan Kanal Video
Pertemuan 14 - Design Pattern Dasar

Pola OBSERVER punya dua peran:
- SUBJECT (KanalVideo): menyimpan daftar pengamat, lalu memberi kabar ke
  SEMUA pengamat setiap kali ada kejadian (video baru diunggah).
- OBSERVER (PengamatKanal): siapa pun yang ingin diberi kabar. Bisa penonton,
  bisa pencatat statistik, bisa apa saja yang ditambahkan kelak.

Kanal tidak perlu tahu jenis pengamatnya. Ia cukup memanggil perbarui().
Di contoh ini, data kejadian (nama kanal dan judul) DIKIRIM langsung ke
pengamat. Gaya ini disebut PUSH.

Cara menjalankan:
    python contoh07_observer_kanal_video.py
"""

from abc import ABC, abstractmethod


class PengamatKanal(ABC):
    """Observer: kontrak untuk siapa pun yang ingin diberi kabar video baru."""

    @abstractmethod
    def perbarui(self, nama_kanal: str, judul: str):
        """Dipanggil kanal setiap kali ada video baru."""


class Penonton(PengamatKanal):
    def __init__(self, nama: str):
        self._nama = nama

    def perbarui(self, nama_kanal: str, judul: str):
        print(f"  [HP {self._nama}] Video baru dari {nama_kanal}: {judul}")


class PencatatStatistik(PengamatKanal):
    """Pengamat jenis lain: bukan penonton, tetapi boleh ikut berlangganan."""

    def __init__(self):
        self._jumlah_video = 0

    def perbarui(self, nama_kanal: str, judul: str):
        self._jumlah_video += 1
        print(f"  [STATISTIK] {nama_kanal} sudah mengunggah "
              f"{self._jumlah_video} video")


class KanalVideo:
    """Subject: menyimpan daftar pengamat dan memberi kabar ke semuanya."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_pengamat: list[PengamatKanal] = []  # [1]

    def langganan(self, pengamat: PengamatKanal):  # [2]
        self._daftar_pengamat.append(pengamat)

    def berhenti_langganan(self, pengamat: PengamatKanal):
        self._daftar_pengamat.remove(pengamat)

    def unggah_video(self, judul: str):
        print(f"{self._nama} mengunggah: {judul}")
        self._beri_kabar(judul)  # [3] kejadian -> semua pengamat diberi tahu

    def _beri_kabar(self, judul: str):
        for pengamat in self._daftar_pengamat:  # [4] tidak peduli jenisnya
            pengamat.perbarui(self._nama, judul)


def main():
    kanal = KanalVideo("Belajar PBO")
    ayu = Penonton("Ayu")
    bima = Penonton("Bima")
    kanal.langganan(ayu)
    kanal.langganan(bima)
    kanal.langganan(PencatatStatistik())

    print("=== VIDEO PERTAMA (3 PENGAMAT) ===")
    kanal.unggah_video("Kelas dan Objek")

    print()
    print("=== BIMA BERHENTI BERLANGGANAN ===")
    kanal.berhenti_langganan(bima)  # [5]
    kanal.unggah_video("Design Pattern Dasar")


if __name__ == "__main__":
    main()
