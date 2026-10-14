"""
Solusi Soal C1 - Sistem Pemesanan Tiket Bioskop
Pertemuan 16 - UAS (latihan persiapan, BUKAN soal ujian asli)

Konsep yang dipakai:
- Kelas abstrak Tiket (ABC + @abstractmethod) dengan tiga kelas anak:
  TiketReguler, TiketVIP, dan TiketPelajar.
- Polimorfisme: Jadwal dan Bioskop cukup memanggil tiket.hitung_harga()
  dan tiket.jenis() tanpa memeriksa jenis tiketnya.
- Exception buatan sendiri: BioskopError dan tiga turunannya.
  KursiSudahTerjualError membawa data tambahan (sisa_kursi).
- Koleksi: dict (kode jadwal -> Jadwal, kode kursi -> Tiket), list,
  dan sorted() dengan key untuk laporan yang terurut.
- Bonus: TiketFactory (pola Factory sederhana dari Pertemuan 14).

Cara menjalankan:
    python soal_c1_tiket_bioskop.py
"""

from abc import ABC, abstractmethod


def format_rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


# ------------------------------------------------------------ exception
class BioskopError(Exception):
    """Induk semua error BioskopKita."""


class JadwalTidakDitemukanError(BioskopError):
    """Dilempar saat kode jadwal tidak terdaftar."""

    def __init__(self, kode_jadwal: str):
        super().__init__(f"Jadwal {kode_jadwal} tidak ditemukan")
        self.kode_jadwal = kode_jadwal


class KursiTidakAdaError(BioskopError):
    """Dilempar saat kode kursi tidak ada di studio."""

    def __init__(self, kode_kursi: str, studio: int):
        super().__init__(f"Kursi {kode_kursi} tidak ada di Studio {studio}")
        self.kode_kursi = kode_kursi
        self.studio = studio


class KursiSudahTerjualError(BioskopError):
    """Dilempar saat kursi sudah dipesan orang lain."""

    def __init__(self, kode_kursi: str, judul: str, sisa_kursi: int):
        super().__init__(f"Kursi {kode_kursi} untuk {judul} sudah terjual")  # [1]
        self.kode_kursi = kode_kursi
        self.judul = judul
        self.sisa_kursi = sisa_kursi  # [2] data tambahan untuk penangkap error


# ---------------------------------------------------------------- tiket
class Tiket(ABC):
    """Kelas abstrak: kerangka untuk semua jenis tiket."""

    def __init__(self, kode_kursi: str, pemesan: str, harga_dasar: int):
        self._kode_kursi = kode_kursi
        self._pemesan = pemesan
        self._harga_dasar = harga_dasar

    @property
    def kode_kursi(self) -> str:
        return self._kode_kursi

    @property
    def pemesan(self) -> str:
        return self._pemesan

    @property
    def harga_dasar(self) -> int:
        return self._harga_dasar

    @abstractmethod
    def jenis(self) -> str:  # [3] method abstrak: WAJIB diisi kelas anak
        """Nama jenis tiket, misalnya 'Reguler'."""

    @abstractmethod
    def hitung_harga(self) -> int:
        """Harga akhir tiket dalam rupiah (bilangan bulat)."""

    def __str__(self) -> str:  # [4] method konkret yang memanggil method abstrak
        harga = format_rupiah(self.hitung_harga())
        return f"{self._kode_kursi:<4}{self.jenis():<9}{self._pemesan:<16}{harga:>10}"


class TiketReguler(Tiket):
    """Tiket reguler: harganya sama dengan harga dasar jadwal."""

    def jenis(self) -> str:
        return "Reguler"

    def hitung_harga(self) -> int:
        return self.harga_dasar


class TiketVIP(Tiket):
    """Kursi sofa + popcorn: harga dasar ditambah biaya tetap."""

    TAMBAHAN = 25000

    def jenis(self) -> str:
        return "VIP"

    def hitung_harga(self) -> int:
        return self.harga_dasar + TiketVIP.TAMBAHAN


class TiketPelajar(Tiket):
    """Tiket pelajar/mahasiswa: diskon 20% dari harga dasar."""

    DISKON_PERSEN = 20

    def jenis(self) -> str:
        return "Pelajar"

    def hitung_harga(self) -> int:
        potongan = self.harga_dasar * TiketPelajar.DISKON_PERSEN // 100
        return self.harga_dasar - potongan


class TiketFactory:
    """Factory sederhana: membuat objek Tiket dari pilihan berupa teks."""

    @staticmethod
    def buat(jenis: str, kode_kursi: str, pemesan: str,
             harga_dasar: int) -> Tiket:
        pilihan = jenis.lower()  # "VIP", "vip", dan "Vip" dianggap sama
        if pilihan == "reguler":
            return TiketReguler(kode_kursi, pemesan, harga_dasar)
        if pilihan == "vip":
            return TiketVIP(kode_kursi, pemesan, harga_dasar)
        if pilihan == "pelajar":
            return TiketPelajar(kode_kursi, pemesan, harga_dasar)
        raise ValueError(f"Jenis tiket '{jenis}' tidak dikenal")


# --------------------------------------------------------------- jadwal
class Jadwal:
    """Satu jadwal tayang: film, jam, studio, harga dasar, dan kursi terjual."""

    BARIS = "ABC"
    KURSI_PER_BARIS = 5

    def __init__(self, kode: str, judul: str, jam: str, studio: int,
                 harga_dasar: int):
        if harga_dasar <= 0:
            raise ValueError("Harga dasar harus lebih dari 0")
        self._kode = kode
        self._judul = judul
        self._jam = jam
        self._studio = studio
        self._harga_dasar = harga_dasar
        self._semua_kursi: list[str] = []  # A1..A5, B1..B5, C1..C5
        for baris in Jadwal.BARIS:
            for nomor in range(1, Jadwal.KURSI_PER_BARIS + 1):
                self._semua_kursi.append(f"{baris}{nomor}")
        self._terjual: dict[str, Tiket] = {}  # [5] kode kursi -> Tiket

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def judul(self) -> str:
        return self._judul

    @property
    def harga_dasar(self) -> int:
        return self._harga_dasar

    def tambah_tiket(self, tiket: Tiket):
        """Menyimpan tiket. Melempar error jika kursi tidak ada/sudah terjual."""
        kursi = tiket.kode_kursi
        if kursi not in self._semua_kursi:
            raise KursiTidakAdaError(kursi, self._studio)
        if kursi in self._terjual:  # [6] cek kunci dict
            raise KursiSudahTerjualError(kursi, self._judul,
                                         len(self.kursi_kosong()))
        self._terjual[kursi] = tiket

    def kursi_kosong(self) -> list[str]:
        return [k for k in self._semua_kursi if k not in self._terjual]

    def daftar_tiket(self) -> list[Tiket]:
        """Tiket terjual, diurutkan berdasarkan kode kursi."""
        return [self._terjual[kursi] for kursi in sorted(self._terjual)]

    def jumlah_terjual(self) -> int:
        return len(self._terjual)

    def pendapatan(self) -> int:
        total = 0
        for tiket in self._terjual.values():
            total += tiket.hitung_harga()  # [7] polimorfisme
        return total

    def __str__(self) -> str:
        harga = format_rupiah(self._harga_dasar)
        return (f"{self._kode}  {self._jam}  Studio {self._studio}  "
                f"{self._judul:<18}{harga:>10}")


# -------------------------------------------------------------- bioskop
class Bioskop:
    """Bioskop yang menyimpan jadwal tayang dan melayani pemesanan."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_jadwal: dict[str, Jadwal] = {}  # kode jadwal -> Jadwal

    @property
    def nama(self) -> str:
        return self._nama

    def tambah_jadwal(self, jadwal: Jadwal):
        if jadwal.kode in self._daftar_jadwal:
            raise ValueError(f"Kode jadwal {jadwal.kode} sudah dipakai")
        self._daftar_jadwal[jadwal.kode] = jadwal

    def cari_jadwal(self, kode: str) -> Jadwal:
        if kode not in self._daftar_jadwal:
            raise JadwalTidakDitemukanError(kode)
        return self._daftar_jadwal[kode]

    def pesan(self, kode_jadwal: str, jenis: str, kode_kursi: str,
              pemesan: str) -> Tiket:
        """Memesan satu tiket. Urutan pemeriksaan: jadwal, jenis, kursi."""
        jadwal = self.cari_jadwal(kode_jadwal)  # bisa JadwalTidakDitemukanError
        tiket = TiketFactory.buat(jenis, kode_kursi, pemesan,
                                  jadwal.harga_dasar)  # bisa ValueError
        jadwal.tambah_tiket(tiket)  # bisa KursiTidakAdaError / KursiSudahTerjualError
        return tiket

    def semua_jadwal(self) -> list[Jadwal]:
        return list(self._daftar_jadwal.values())

    def semua_tiket(self) -> list[Tiket]:
        hasil: list[Tiket] = []
        for jadwal in self._daftar_jadwal.values():
            hasil.extend(jadwal.daftar_tiket())
        return hasil

    def total_pendapatan(self) -> int:
        total = 0
        for jadwal in self._daftar_jadwal.values():
            total += jadwal.pendapatan()
        return total

    def laporan_per_film(self) -> list[Jadwal]:
        """Pendapatan terbesar dulu; jika sama, judul A-Z."""
        return sorted(self._daftar_jadwal.values(),
                      key=lambda j: (-j.pendapatan(), j.judul))  # [8]

    def jumlah_per_jenis(self) -> dict[str, int]:
        """Jenis tiket -> banyak tiket terjual, urut nama jenis."""
        hasil: dict[str, int] = {}
        for tiket in self.semua_tiket():
            hasil[tiket.jenis()] = hasil.get(tiket.jenis(), 0) + 1
        return dict(sorted(hasil.items()))

    def pendapatan_per_jenis(self) -> dict[str, int]:
        """Jenis tiket -> total pendapatan, urut nama jenis."""
        hasil: dict[str, int] = {}
        for tiket in self.semua_tiket():
            hasil[tiket.jenis()] = (hasil.get(tiket.jenis(), 0)
                                    + tiket.hitung_harga())
        return dict(sorted(hasil.items()))


# ------------------------------------------------------- program utama
# Setiap permintaan: (kode jadwal, jenis tiket, kode kursi, nama pemesan)
DAFTAR_PERMINTAAN = [
    ("J02", "reguler", "A1", "Budi Santoso"),
    ("J02", "VIP", "A2", "Siti Aminah"),
    ("J02", "pelajar", "A1", "Rina Marlina"),
    ("J02", "pelajar", "A3", "Rina Marlina"),
    ("J03", "vip", "D1", "Andi Wijaya"),
    ("J03", "vip", "C5", "Andi Wijaya"),
    ("J05", "reguler", "A1", "Dimas Pratama"),
    ("J01", "premium", "B2", "Dimas Pratama"),
    ("J01", "vip", "B2", "Dimas Pratama"),
    ("J01", "reguler", "B3", "Ayu Lestari"),
    ("J01", "reguler", "B4", "Bima Saputra"),
    ("J03", "pelajar", "C4", "Citra Dewi"),
    ("J02", "reguler", "B1", "Eko Prasetyo"),
]


def siapkan_bioskop() -> Bioskop:
    """Membuat bioskop beserta tiga jadwal tayang hari ini."""
    bioskop = Bioskop("BioskopKita")
    bioskop.tambah_jadwal(Jadwal("J01", "Rindu di Tepian", "13:00", 1, 30000))
    bioskop.tambah_jadwal(Jadwal("J02", "Mahakam Biru", "16:00", 2, 40000))
    bioskop.tambah_jadwal(Jadwal("J03", "Detektif Kampus", "19:00", 1, 50000))
    return bioskop


def main():
    bioskop = siapkan_bioskop()
    print(f"=== JADWAL TAYANG {bioskop.nama} ===")
    for jadwal in bioskop.semua_jadwal():
        print(jadwal)
    print()

    print("=== PEMESANAN TIKET ===")
    for kode_jadwal, jenis, kursi, pemesan in DAFTAR_PERMINTAAN:
        try:
            tiket = bioskop.pesan(kode_jadwal, jenis, kursi, pemesan)
        except KursiSudahTerjualError as e:  # [9] yang spesifik ditulis dulu
            print(f"[GAGAL] {e}")
            print(f"        Saran: pilih kursi lain, masih ada "
                  f"{e.sisa_kursi} kursi kosong")
        except BioskopError as e:  # [10] semua error bioskop yang lain
            print(f"[GAGAL] {e}")
        except ValueError as e:  # jenis tiket tidak dikenal
            print(f"[GAGAL] {e}")
        else:  # [11] hanya dijalankan jika TIDAK ada exception
            harga = format_rupiah(tiket.hitung_harga())
            print(f"[OK]    {kode_jadwal}/{tiket.kode_kursi} {tiket.jenis()} "
                  f"untuk {tiket.pemesan}: {harga}")
    print()

    jadwal = bioskop.cari_jadwal("J02")
    print(f"=== TIKET TERJUAL {jadwal.kode}: {jadwal.judul} ===")
    for tiket in jadwal.daftar_tiket():
        print(tiket)  # __str__ milik Tiket memanggil jenis()/hitung_harga() anak
    kosong = jadwal.kursi_kosong()
    print(f"Kursi kosong ({len(kosong)}): {', '.join(kosong)}")
    print()

    print("=== LAPORAN PENDAPATAN PER FILM ===")
    for nomor, jadwal in enumerate(bioskop.laporan_per_film(), start=1):
        pendapatan = format_rupiah(jadwal.pendapatan())
        print(f"{nomor}. {jadwal.judul:<18}{jadwal.jumlah_terjual():>2} tiket"
              f"{pendapatan:>12}")
    print(f"Total pendapatan: {format_rupiah(bioskop.total_pendapatan())}")
    print()

    print("=== REKAP PER JENIS TIKET ===")
    pendapatan_jenis = bioskop.pendapatan_per_jenis()
    for jenis, banyak in bioskop.jumlah_per_jenis().items():
        pendapatan = format_rupiah(pendapatan_jenis[jenis])
        print(f"{jenis:<9}{banyak:>2} tiket{pendapatan:>12}")


if __name__ == "__main__":
    main()
