"""
KedaiKita - Pertemuan 13: Prinsip SOLID
Bagian SESUDAH refactor.

Skenario di file ini SAMA dengan ../sebelum/kasir_serba_bisa.py, dan
outputnya pun SAMA PERSIS. Refactor = mengubah STRUKTUR kode tanpa
mengubah PERILAKU-nya.

Pembagian tugas setelah refactor:
    Kedai               -> menyimpan menu (dan menerima penyimpanan pesanan)
    Pesanan + Diskon    -> menghitung subtotal, potongan, dan total
    StrukPesanan        -> menyusun dan mencetak struk
    PenyimpananPesanan  -> menyimpan riwayat (saat ini: PenyimpananMemori)

Cara menjalankan (dari dalam folder sesudah):
    python main.py
"""

from diskon import Diskon, DiskonMember, DiskonPersen, TanpaDiskon
from kedai import Kedai
from menu import Makanan, Minuman
from pasangan import Pasangan
from pelanggan import Pelanggan
from penyimpanan import PenyimpananMemori, PenyimpananPesanan
from struk import StrukPesanan
from utilitas import format_rupiah


def siapkan_kedai(penyimpanan: PenyimpananPesanan) -> Kedai:
    """Membuat kedai beserta lima menu awalnya."""
    kedai = Kedai("KedaiKita", penyimpanan)
    kedai.tambah_menu(Minuman("M01", "Kopi Susu Gula Aren", 18000, 20, True))
    kedai.tambah_menu(Minuman("M02", "Es Teh Manis", 8000, 30, True))
    kedai.tambah_menu(Makanan("M03", "Nasi Goreng Kampung", 25000, 15, 2))
    kedai.tambah_menu(Makanan("M04", "Mie Goreng Jawa", 23000, 10, 1))
    kedai.tambah_menu(Makanan("M05", "Pisang Goreng Keju", 15000, 12, 0))
    return kedai


def proses_pesanan(kedai: Kedai, pelanggan: Pelanggan,
                   daftar_beli: list[Pasangan[str, int]], diskon: Diskon):
    pesanan = kedai.buat_pesanan(pelanggan)
    for beli in daftar_beli:
        pesanan.tambah_item(kedai.cari_menu(beli.pertama), beli.kedua)
    pesanan.atur_diskon(diskon)
    StrukPesanan(pesanan).cetak()


def main():
    # DIP: jenis penyimpanan ditentukan DI SINI, bukan di dalam Kedai.
    penyimpanan = PenyimpananMemori()
    kedai = siapkan_kedai(penyimpanan)

    budi = Pelanggan("Budi Santoso", "081234567890")
    siti = Pelanggan("Siti Aminah", "082198765432")
    siti.tambah_poin(12)  # pelanggan lama, sudah mengumpulkan 12 poin
    rina = Pelanggan("Rina Marlina", "085312345678")

    proses_pesanan(kedai, budi, [Pasangan("M01", 2), Pasangan("M03", 1)],
                   TanpaDiskon())
    print()
    proses_pesanan(kedai, siti, [Pasangan("M02", 2), Pasangan("M05", 1)],
                   DiskonMember())
    print()
    proses_pesanan(kedai, rina, [Pasangan("M01", 1), Pasangan("M04", 1)],
                   DiskonPersen(15))
    print()

    print("=== RIWAYAT PESANAN ===")
    total_semua = 0
    for pesanan in kedai.riwayat_pesanan():
        total = pesanan.hitung_total()
        print(f"{pesanan.nomor}  {pesanan.pelanggan.nama:<20}"
              f"{format_rupiah(total):>12}")
        total_semua += total
    print(f"Total pendapatan: {format_rupiah(total_semua)}")


if __name__ == "__main__":
    main()
