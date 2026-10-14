"""
KedaiKita - Pertemuan 09: Polimorfisme

Yang baru dibanding Pertemuan 07:
- pembayaran.py: kelas induk Pembayaran + PembayaranTunai, PembayaranQRIS,
  PembayaranKartu. Ketiganya punya method yang sama dengan perilaku berbeda.
- Pesanan.bayar(pembayaran) bekerja untuk SEMUA jenis pembayaran.
- Pesanan.tambah_item(menu) boleh tanpa jumlah (bawaan 1).
- isinstance() untuk memeriksa jenis objek sebelum memakai fitur khususnya.

Cara menjalankan (dari dalam folder studi-kasus):
    python main.py
"""

from kedai import Kedai
from menu import Makanan, Minuman
from pelanggan import Pelanggan
from pembayaran import PembayaranKartu, PembayaranQRIS, PembayaranTunai
from utilitas import format_rupiah


def siapkan_kedai() -> Kedai:
    """Membuat kedai beserta lima menu awalnya."""
    kedai = Kedai("KedaiKita")
    kedai.tambah_menu(Minuman("M01", "Kopi Susu Gula Aren", 18000, 20, True))
    kedai.tambah_menu(Minuman("M02", "Es Teh Manis", 8000, 30, True))
    kedai.tambah_menu(Makanan("M03", "Nasi Goreng Kampung", 25000, 15, 2))
    kedai.tambah_menu(Makanan("M04", "Mie Goreng Jawa", 23000, 10, 1))
    kedai.tambah_menu(Makanan("M05", "Pisang Goreng Keju", 15000, 12, 0))
    return kedai


def main():
    kedai = siapkan_kedai()
    kedai.tampilkan_menu()
    print()

    print("=== SATU PANGGILAN, BANYAK BENTUK ===")
    daftar_metode = [PembayaranTunai(100000), PembayaranQRIS(50000),
                     PembayaranKartu("BNI")]
    for metode in daftar_metode:
        biaya = metode.hitung_biaya_layanan(100000)
        print(f"{metode.nama_metode():<20} biaya layanan untuk Rp100.000: "
              f"{format_rupiah(biaya)}")
    print()

    budi = Pelanggan("Budi Santoso", "081234567890")
    siti = Pelanggan("Siti Aminah", "082198765432")

    pesanan_budi = kedai.buat_pesanan(budi)
    pesanan_budi.tambah_item(kedai.cari_menu("M01"), 2)
    pesanan_budi.tambah_item(kedai.cari_menu("M03"))  # jumlah bawaan: 1
    pesanan_budi.cetak_struk()
    pembayaran_budi = PembayaranTunai(100000)
    pesanan_budi.bayar(pembayaran_budi)
    print()

    pesanan_siti = kedai.buat_pesanan(siti)
    pesanan_siti.tambah_item(kedai.cari_menu("M02"), 2)
    pesanan_siti.tambah_item(kedai.cari_menu("M05"))
    pesanan_siti.cetak_struk()
    berhasil = pesanan_siti.bayar(PembayaranQRIS(20000))
    if not berhasil:
        print()
        pesanan_siti.bayar(PembayaranKartu("BNI"))
    print()

    print("=== MEMERIKSA JENIS PEMBAYARAN ===")
    for pembayaran in [pembayaran_budi, PembayaranKartu("Mandiri")]:
        if isinstance(pembayaran, PembayaranTunai):
            kembalian = format_rupiah(pembayaran.kembalian)
            print(f"{pembayaran.nama_metode()}: kembalian {kembalian}")
        else:
            print(f"{pembayaran.nama_metode()}: tidak ada kembalian")
    print()

    print("=== STATUS AKHIR ===")
    print(f"{pesanan_budi.nomor}: {pesanan_budi.status}")
    print(f"{pesanan_siti.nomor}: {pesanan_siti.status}")
    print(budi)
    print(siti)


if __name__ == "__main__":
    main()
