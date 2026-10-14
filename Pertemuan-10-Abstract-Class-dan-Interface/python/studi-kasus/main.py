"""
KedaiKita - Pertemuan 10: Abstract Class dan Interface

Yang baru dibanding Pertemuan 09:
- Pembayaran menjadi kelas abstrak: objeknya tidak bisa dibuat langsung.
- dapat_dicetak.py: "interface" DapatDicetak dengan satu method, cetak().
- Kedai dan Pesanan sama-sama DapatDicetak walaupun keduanya tidak
  punya hubungan pewarisan lain. Fungsi cetak_semua() bisa mencetak
  keduanya tanpa peduli jenis aslinya.

Cara menjalankan (dari dalam folder studi-kasus):
    python main.py
"""

from dapat_dicetak import DapatDicetak
from kedai import Kedai
from menu import Makanan, Minuman
from pelanggan import Pelanggan
from pembayaran import PembayaranKartu, PembayaranQRIS, PembayaranTunai


def siapkan_kedai() -> Kedai:
    """Membuat kedai beserta lima menu awalnya."""
    kedai = Kedai("KedaiKita")
    kedai.tambah_menu(Minuman("M01", "Kopi Susu Gula Aren", 18000, 20, True))
    kedai.tambah_menu(Minuman("M02", "Es Teh Manis", 8000, 30, True))
    kedai.tambah_menu(Makanan("M03", "Nasi Goreng Kampung", 25000, 15, 2))
    kedai.tambah_menu(Makanan("M04", "Mie Goreng Jawa", 23000, 10, 1))
    kedai.tambah_menu(Makanan("M05", "Pisang Goreng Keju", 15000, 12, 0))
    return kedai


def cetak_semua(daftar_dokumen: list[DapatDicetak]):
    """Mencetak objek apa pun, asalkan ia memenuhi kontrak DapatDicetak."""
    jumlah = len(daftar_dokumen)
    for nomor, dokumen in enumerate(daftar_dokumen, start=1):
        print(f"--- Dokumen {nomor} dari {jumlah} ---")
        dokumen.cetak()
        print()


def main():
    kedai = siapkan_kedai()

    print("=== MENGENAL METODE PEMBAYARAN ===")
    daftar_metode = [PembayaranTunai(100000), PembayaranQRIS(50000),
                     PembayaranKartu("BNI")]
    for metode in daftar_metode:
        print(metode.deskripsi(100000))
    print()

    print("=== TRANSAKSI ===")
    budi = Pelanggan("Budi Santoso", "081234567890")
    siti = Pelanggan("Siti Aminah", "082198765432")

    pesanan_budi = kedai.buat_pesanan(budi)
    pesanan_budi.tambah_item(kedai.cari_menu("M01"), 2)
    pesanan_budi.tambah_item(kedai.cari_menu("M03"))
    pesanan_budi.bayar(PembayaranTunai(100000))
    print()

    pesanan_siti = kedai.buat_pesanan(siti)
    pesanan_siti.tambah_item(kedai.cari_menu("M02"), 2)
    pesanan_siti.tambah_item(kedai.cari_menu("M05"))
    if not pesanan_siti.bayar(PembayaranQRIS(20000)):
        print()
        pesanan_siti.bayar(PembayaranKartu("BNI"))
    print()

    print("=== CETAK SEMUA DOKUMEN ===")
    cetak_semua([kedai, pesanan_budi, pesanan_siti])

    print("=== POIN PELANGGAN ===")
    print(budi)
    print(siti)


if __name__ == "__main__":
    main()
