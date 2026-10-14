"""
Contoh 05 - Multiplisitas dan Mencari Objek
Pertemuan 05 - Relasi Antar Kelas

Grup belajar punya TEPAT SATU ketua (multiplisitas 1) dan MINIMAL SATU
anggota (multiplisitas 1..*). Kelas GrupBelajar sendiri yang menjaga
aturan itu. Method cari_anggota() mengembalikan objek Peserta, atau None
jika tidak ditemukan.

Cara menjalankan:
    python contoh05_multiplisitas.py
"""


class Peserta:
    """Mahasiswa peserta grup belajar."""

    def __init__(self, nim: str, nama: str):
        self._nim = nim
        self._nama = nama

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def nama(self) -> str:
        return self._nama

    def __str__(self) -> str:
        return f"{self._nama} ({self._nim})"


class GrupBelajar:
    """Grup belajar: tepat 1 ketua dan minimal 1 anggota."""

    def __init__(self, nama: str, ketua: Peserta):
        if ketua is None:  # [1] multiplisitas 1: ketua wajib ada
            raise ValueError("Grup wajib punya ketua")
        self._nama = nama
        self._ketua = ketua
        self._daftar_anggota: list[Peserta] = [ketua]  # [2] 1..*: sudah 1 anggota

    def tambah_anggota(self, peserta: Peserta):
        self._daftar_anggota.append(peserta)

    def cari_anggota(self, nim: str) -> Peserta | None:  # [3]
        for peserta in self._daftar_anggota:
            if peserta.nim == nim:
                return peserta
        return None  # [4] sudah diperiksa semua, tidak ketemu

    def keluarkan(self, nim: str):
        peserta = self.cari_anggota(nim)
        if peserta is None:  # [5] periksa None sebelum memakai hasilnya
            print(f"Gagal: NIM {nim} bukan anggota {self._nama}")
        elif peserta is self._ketua:  # [6] ketua tidak boleh keluar
            print(f"Gagal: {peserta.nama} adalah ketua, tidak bisa dikeluarkan")
        else:
            self._daftar_anggota.remove(peserta)
            print(f"{peserta.nama} keluar dari {self._nama}")

    def tampilkan(self):
        print(f"{self._nama} - ketua: {self._ketua.nama}")
        print(f"Anggota ({len(self._daftar_anggota)} orang):")
        for peserta in self._daftar_anggota:
            print(f"- {peserta}")


def main():
    ayu = Peserta("2409106001", "Ayu")
    bima = Peserta("2409106002", "Bima")
    citra = Peserta("2409106003", "Citra")

    print("=== GRUP BARU ===")
    grup = GrupBelajar("Grup PBO", ayu)
    grup.tampilkan()

    print()
    print("=== GRUP TANPA KETUA ===")
    try:
        GrupBelajar("Grup Hantu", None)  # [7] sengaja melanggar aturan
    except ValueError as e:
        print(f"Gagal membuat grup: {e}")

    print()
    print("=== MENAMBAH ANGGOTA ===")
    grup.tambah_anggota(bima)
    grup.tambah_anggota(citra)
    grup.tampilkan()

    print()
    print("=== MENCARI ANGGOTA ===")
    for nim in ["2409106002", "2409106099"]:
        hasil = grup.cari_anggota(nim)
        if hasil is None:
            print(f"Cari {nim}: tidak ditemukan")
        else:
            print(f"Cari {nim}: {hasil}")

    print()
    print("=== MENGELUARKAN ANGGOTA ===")
    grup.keluarkan("2409106099")
    grup.keluarkan("2409106001")
    grup.keluarkan("2409106003")
    grup.tampilkan()


if __name__ == "__main__":
    main()
