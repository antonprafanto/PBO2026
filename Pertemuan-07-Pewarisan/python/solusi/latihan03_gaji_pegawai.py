"""
Solusi Latihan 03 - Gaji Pegawai Tetap dan Pegawai Kontrak
Pertemuan 07 - Pewarisan (Inheritance)

Ide penyelesaian:
- Pegawai (induk) menyimpan NIP, nama, dan gaji pokok. hitung_gaji() versi
  induk mengembalikan gaji pokok saja.
- PegawaiTetap dan PegawaiKontrak meng-override hitung_gaji(): keduanya
  memakai super().hitung_gaji() lalu menambahkan komponen milik masing-masing.
- __str__ juga di-override agar jenis pegawai ikut tampil.
- Saat perulangan memanggil p.hitung_gaji(), setiap objek otomatis memakai
  versi miliknya sendiri (bahasan lengkapnya di Pertemuan 09: Polimorfisme).

Cara menjalankan:
    python latihan03_gaji_pegawai.py
"""

UPAH_LEMBUR_PER_JAM = 40000  # Rupiah
LEBAR_SLIP = 44


def format_rupiah(angka: int) -> str:
    """Mengubah 7500000 menjadi 'Rp7.500.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class Pegawai:
    """Kelas induk semua pegawai."""

    def __init__(self, nip: str, nama: str, gaji_pokok: int):
        if gaji_pokok <= 0:
            raise ValueError("Gaji pokok harus lebih dari 0")
        self._nip = nip
        self._nama = nama
        self._gaji_pokok = gaji_pokok

    def hitung_gaji(self) -> int:
        return self._gaji_pokok

    def __str__(self) -> str:
        return f"{self._nip} {self._nama}"


class PegawaiTetap(Pegawai):
    """Pegawai tetap: gaji pokok ditambah tunjangan bulanan."""

    def __init__(self, nip: str, nama: str, gaji_pokok: int, tunjangan: int):
        super().__init__(nip, nama, gaji_pokok)
        self._tunjangan = tunjangan

    def hitung_gaji(self) -> int:
        return super().hitung_gaji() + self._tunjangan

    def __str__(self) -> str:
        return f"{super().__str__()} (tetap)"


class PegawaiKontrak(Pegawai):
    """Pegawai kontrak: gaji pokok ditambah upah lembur per jam."""

    def __init__(self, nip: str, nama: str, gaji_pokok: int, jam_lembur: int):
        super().__init__(nip, nama, gaji_pokok)
        if jam_lembur < 0:
            raise ValueError("Jam lembur tidak boleh negatif")
        self._jam_lembur = jam_lembur

    def hitung_gaji(self) -> int:
        return super().hitung_gaji() + self._jam_lembur * UPAH_LEMBUR_PER_JAM

    def __str__(self) -> str:
        return f"{super().__str__()} (kontrak)"


def main():
    daftar_pegawai = [
        PegawaiTetap("198703", "Andi Wijaya", 6000000, 1500000),
        PegawaiKontrak("200105", "Rina Marlina", 4400000, 20),
        PegawaiKontrak("199912", "Dodi Pratama", 4500000, 0),
    ]

    print("=== SLIP GAJI OKTOBER 2026 ===")
    total = 0
    for pegawai in daftar_pegawai:
        gaji = pegawai.hitung_gaji()
        total += gaji
        print(f"{str(pegawai):<30}{format_rupiah(gaji):>14}")
    print("-" * LEBAR_SLIP)
    print(f"{'Total gaji':<30}{format_rupiah(total):>14}")


if __name__ == "__main__":
    main()
