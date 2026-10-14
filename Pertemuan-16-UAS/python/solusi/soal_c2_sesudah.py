"""
Solusi Soal C2 (kode SESUDAH refactor) - Kasir Laundry
Pertemuan 16 - UAS (latihan persiapan, BUKAN soal ujian asli)

Refactor = mengubah STRUKTUR kode tanpa mengubah PERILAKU-nya.
Output program ini SAMA PERSIS dengan soal_c2_sebelum.py.

Pembagian tugas setelah refactor:
    KatalogLayanan + Layanan -> menyimpan tarif (dict), menolak layanan asing
    PesananLaundry           -> data satu order + hitungan subtotal/potongan/total
    Promo + 3 kelas anak     -> aturan promo yang bisa ditukar (pola STRATEGY)
    NotaLaundry              -> menyusun teks nota (SRP)
    Pengirim + PengirimWhatsApp -> mengirim pesan (ISP: kontrak kecil)
    LaporanHarian            -> menyusun laporan harian (SRP)
    KasirLaundry             -> mengatur alur kerja; menerima Pengirim lewat
                                konstruktor (DIP, dependency injection)

Catatan: di proyek sungguhan, kelas-kelas ini sebaiknya dipisah ke beberapa
modul (seperti KedaiKita Pertemuan 13). Di sini sengaja dibuat satu file
agar mudah dijalankan dan dibandingkan dengan kode sebelum refactor.

Cara menjalankan:
    python soal_c2_sesudah.py
"""

from abc import ABC, abstractmethod

LEBAR_NOTA = 36


def format_rupiah(angka: int) -> str:
    """Satu-satunya tempat aturan format uang (DRY)."""
    return f"Rp{angka:,}".replace(",", ".")


class LayananTidakTersediaError(Exception):
    """Dilempar saat layanan yang diminta tidak ada di katalog."""

    def __init__(self, nama_layanan: str):
        super().__init__(f"Layanan '{nama_layanan}' tidak tersedia")
        self.nama_layanan = nama_layanan


# ------------------------------------------------------------- data dasar
class Layanan:
    """Satu jenis layanan beserta tarifnya per kg."""

    def __init__(self, nama: str, tarif_per_kg: int):
        if tarif_per_kg <= 0:
            raise ValueError("Tarif harus lebih dari 0")
        self._nama = nama
        self._tarif_per_kg = tarif_per_kg

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def tarif_per_kg(self) -> int:
        return self._tarif_per_kg


class KatalogLayanan:
    """Daftar layanan. Layanan baru cukup DIDAFTARKAN, tanpa mengubah kode (OCP)."""

    def __init__(self):
        # [1] nama layanan -> Layanan. Katalog hanya dipakai untuk MENCARI.
        self._daftar: dict[str, Layanan] = {}

    def tambah(self, layanan: Layanan):
        self._daftar[layanan.nama] = layanan

    def cari(self, nama: str) -> Layanan:
        if nama not in self._daftar:
            raise LayananTidakTersediaError(nama)  # [2] bukan lagi print + return
        return self._daftar[nama]


class Pelanggan:
    """Data pelanggan: nama dan nomor HP."""

    def __init__(self, nama: str, no_hp: str):
        self._nama = nama
        self._no_hp = no_hp

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def no_hp(self) -> str:
        return self._no_hp


# ---------------------------------------------------- promo (STRATEGY)
class Promo(ABC):
    """Strategi promo. Promo baru = kelas baru; kelas lain tidak diubah (OCP)."""

    @abstractmethod
    def hitung_potongan(self, pesanan: "PesananLaundry") -> int:  # [3]
        """Besar potongan dalam rupiah. Tidak pernah negatif (LSP)."""

    @abstractmethod
    def keterangan(self) -> str:
        """Nama promo untuk dicetak di nota."""


class TanpaPromo(Promo):
    def hitung_potongan(self, pesanan: "PesananLaundry") -> int:
        return 0

    def keterangan(self) -> str:
        return "Tanpa promo"


class PromoMember(Promo):
    """Member mendapat potongan 10% dari subtotal."""

    PERSEN = 10

    def hitung_potongan(self, pesanan: "PesananLaundry") -> int:
        return pesanan.subtotal() * PromoMember.PERSEN // 100

    def keterangan(self) -> str:
        return f"Member {PromoMember.PERSEN}%"


class PromoGratisSatuKg(Promo):
    """Cucian minimal 5 kg: gratis 1 kg (potongan = tarif 1 kg)."""

    MINIMAL_BERAT = 5

    def hitung_potongan(self, pesanan: "PesananLaundry") -> int:
        if pesanan.berat < PromoGratisSatuKg.MINIMAL_BERAT:
            return 0
        return pesanan.layanan.tarif_per_kg

    def keterangan(self) -> str:
        return "Gratis 1 kg"


# ---------------------------------------------------------------- pesanan
class PesananLaundry:
    """Satu order cucian: hanya data dan perhitungan harga (SRP)."""

    def __init__(self, kode: str, pelanggan: Pelanggan, layanan: Layanan,
                 berat: int, promo: Promo):
        if berat <= 0:
            raise ValueError("Berat harus lebih dari 0")
        self._kode = kode
        self._pelanggan = pelanggan
        self._layanan = layanan
        self._berat = berat
        self._promo = promo

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def pelanggan(self) -> Pelanggan:
        return self._pelanggan

    @property
    def layanan(self) -> Layanan:
        return self._layanan

    @property
    def berat(self) -> int:
        return self._berat

    @property
    def promo(self) -> Promo:
        return self._promo

    def subtotal(self) -> int:
        return self._layanan.tarif_per_kg * self._berat

    def potongan(self) -> int:
        return self._promo.hitung_potongan(self)  # [4] diserahkan ke strategi

    def total(self) -> int:
        return self.subtotal() - self.potongan()


# ------------------------------------------------------- tampilan (SRP)
class NotaLaundry:
    """Menyusun teks nota untuk satu pesanan. Hanya berubah jika format nota berubah."""

    def __init__(self, pesanan: PesananLaundry):
        self._pesanan = pesanan

    @staticmethod
    def _baris(kiri: str, kanan: str) -> str:
        return f"{kiri:<24}{kanan:>12}"

    def buat_teks(self) -> str:
        p = self._pesanan
        garis = "=" * LEBAR_NOTA
        tarif = format_rupiah(p.layanan.tarif_per_kg)
        baris = [
            garis,
            "LAUNDRY BERSIH KILAT",
            garis,
            f"No. Order : {p.kode}",
            f"Pelanggan : {p.pelanggan.nama}",
            f"Layanan   : {p.layanan.nama}",
            f"Berat     : {p.berat} kg x {tarif}",
            "-" * LEBAR_NOTA,
            self._baris("Subtotal", format_rupiah(p.subtotal())),
        ]
        if p.potongan() > 0:
            baris.append(self._baris(f"Promo {p.promo.keterangan()}",
                                     "-" + format_rupiah(p.potongan())))
        baris.append(self._baris("TOTAL", format_rupiah(p.total())))
        baris.append(garis)
        return "\n".join(baris)


class LaporanHarian:
    """Menyusun laporan harian dari daftar pesanan (SRP)."""

    def __init__(self, daftar_pesanan: list[PesananLaundry]):
        self._daftar_pesanan = daftar_pesanan

    def buat_teks(self) -> str:
        baris = ["=== LAPORAN HARIAN ==="]
        total_berat = 0
        pendapatan = 0
        for p in self._daftar_pesanan:
            baris.append(f"{p.kode}  {p.pelanggan.nama:<16}{p.berat:>3} kg"
                         f"{format_rupiah(p.total()):>12}")
            total_berat += p.berat
            pendapatan += p.total()
        baris.append(f"Jumlah order : {len(self._daftar_pesanan)}")
        baris.append(f"Total berat  : {total_berat} kg")
        baris.append(f"Pendapatan   : {format_rupiah(pendapatan)}")
        return "\n".join(baris)


# --------------------------------------------------- pengiriman (ISP, DIP)
class Pengirim(ABC):
    """Kontrak kecil: cukup satu method untuk mengirim pesan (ISP)."""

    @abstractmethod
    def kirim(self, no_hp: str, pesan: str):
        """Mengirim pesan teks ke nomor HP."""


class PengirimWhatsApp(Pengirim):
    """Simulasi WhatsApp: pesan dicetak ke layar."""

    def kirim(self, no_hp: str, pesan: str):
        print(f"[WA ke {no_hp}] {pesan}")


# ---------------------------------------------------- alur kerja kasir
class KasirLaundry:
    """Mengatur alur kerja kasir dengan memakai kelas-kelas di atas."""

    def __init__(self, katalog: KatalogLayanan, pengirim: Pengirim):  # [5]
        self._katalog = katalog
        self._pengirim = pengirim  # bergantung pada ABSTRAKSI (DIP)
        self._riwayat: list[PesananLaundry] = []
        self._nomor_terakhir = 0

    def terima_cucian(self, pelanggan: Pelanggan, nama_layanan: str,
                      berat: int, promo: Promo) -> PesananLaundry:
        """Melempar LayananTidakTersediaError jika layanan tidak dikenal."""
        layanan = self._katalog.cari(nama_layanan)  # dicek SEBELUM nomor dibuat
        self._nomor_terakhir += 1
        kode = f"L{self._nomor_terakhir:03d}"
        pesanan = PesananLaundry(kode, pelanggan, layanan, berat, promo)
        print(NotaLaundry(pesanan).buat_teks())
        self._pengirim.kirim(pelanggan.no_hp,
                             f"Halo {pelanggan.nama}, cucian {kode} sudah kami "
                             f"terima. Total {format_rupiah(pesanan.total())}.")
        self._riwayat.append(pesanan)
        return pesanan

    def riwayat(self) -> list[PesananLaundry]:
        return list(self._riwayat)


# ---------------------------------------------------------- program utama
def siapkan_katalog() -> KatalogLayanan:
    katalog = KatalogLayanan()
    katalog.tambah(Layanan("cuci kering", 6000))
    katalog.tambah(Layanan("cuci setrika", 8000))
    katalog.tambah(Layanan("setrika saja", 5000))
    return katalog


def terima(kasir: KasirLaundry, pelanggan: Pelanggan, nama_layanan: str,
           berat: int, promo: Promo):
    """Lapisan tampilan: memanggil kasir dan menampilkan pesan bila ditolak."""
    try:
        kasir.terima_cucian(pelanggan, nama_layanan, berat, promo)
    except LayananTidakTersediaError as e:
        print(f"[DITOLAK] {e}")
    print()


def main():
    kasir = KasirLaundry(siapkan_katalog(), PengirimWhatsApp())  # [6] injeksi
    terima(kasir, Pelanggan("Budi Santoso", "081234567890"), "cuci setrika", 4,
           PromoMember())
    terima(kasir, Pelanggan("Siti Aminah", "082198765432"), "cuci kering", 6,
           PromoGratisSatuKg())
    terima(kasir, Pelanggan("Rina Marlina", "085312345678"), "setrika saja", 3,
           PromoGratisSatuKg())
    terima(kasir, Pelanggan("Andi Wijaya", "087711223344"), "dry clean", 2,
           TanpaPromo())
    terima(kasir, Pelanggan("Dimas Pratama", "081355577799"), "cuci setrika", 5,
           TanpaPromo())
    print(LaporanHarian(kasir.riwayat()).buat_teks())


if __name__ == "__main__":
    main()
