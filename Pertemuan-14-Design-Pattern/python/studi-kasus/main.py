"""
KedaiKita - Pertemuan 14: Design Pattern Dasar

Empat pola desain dalam satu program:
1. SINGLETON - PengaturanKedai (pengaturan.py): hanya ada satu objek.
2. FACTORY   - PembayaranFactory (pembayaran.py): membuat objek dari pilihan.
3. STRATEGY  - kelas-kelas Diskon (diskon.py): aturan yang bisa ditukar.
4. OBSERVER  - PengamatPesanan (pengamat.py, notifikasi.py): pemberitahuan
               otomatis setiap kali status pesanan berubah.

Cara menjalankan (dari dalam folder studi-kasus):
    python main.py
"""

from diskon import DiskonHappyHour, DiskonPersen, TanpaDiskon
from kedai import Kedai
from menu import Makanan, Minuman
from notifikasi import LayarDapur, NotifikasiPelanggan
from pelanggan import Pelanggan
from pembayaran import PembayaranFactory
from pengaturan import PengaturanKedai
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


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    print("=== 1. SINGLETON: PENGATURAN KEDAI ===")
    pengaturan_a = PengaturanKedai.get_instance()
    pengaturan_b = PengaturanKedai.get_instance()
    print(f"Objek yang sama? {ya_tidak(pengaturan_a is pengaturan_b)}")
    print(f"Nama   : {pengaturan_a.nama_kedai}")
    print(f"Alamat : {pengaturan_a.alamat}")
    print(f"Pajak  : {pengaturan_b.pajak_persen}%")
    print()

    print("=== 2. FACTORY: MEMBUAT PEMBAYARAN DARI PILIHAN ===")
    for pilihan in ["tunai", "QRIS", "kartu"]:
        pembayaran = PembayaranFactory.buat(pilihan, 100000, "BNI")
        print(f"Pilihan '{pilihan}' -> {pembayaran.deskripsi(100000)}")
    try:
        PembayaranFactory.buat("bitcoin", 0, "")
    except ValueError as e:
        print(f"Ditolak: {e}")
    print()

    print("=== 3. STRATEGY: MENUKAR ATURAN DISKON ===")
    kedai = siapkan_kedai(PenyimpananMemori())
    rina = Pelanggan("Rina Marlina", "085312345678")
    pesanan_rina = kedai.buat_pesanan(rina)
    pesanan_rina.tambah_item(kedai.cari_menu("M01"), 2)
    pesanan_rina.tambah_item(kedai.cari_menu("M04"), 1)
    print(f"Subtotal pesanan Rina: {format_rupiah(pesanan_rina.hitung_subtotal())}")
    for strategi in [TanpaDiskon(), DiskonPersen(15), DiskonHappyHour()]:
        pesanan_rina.atur_diskon(strategi)
        potongan = format_rupiah(pesanan_rina.hitung_potongan())
        total = format_rupiah(pesanan_rina.hitung_total())
        print(f"{strategi.keterangan():<22} potongan {potongan:>8}, "
              f"total {total:>8}")
    print()

    print("=== 4. OBSERVER: NOTIFIKASI STATUS PESANAN ===")
    budi = Pelanggan("Budi Santoso", "081234567890")
    pesanan_budi = kedai.buat_pesanan(budi)
    pesanan_budi.tambah_item(kedai.cari_menu("M01"), 2)
    pesanan_budi.tambah_item(kedai.cari_menu("M03"), 1)
    pesanan_budi.tambah_pengamat(LayarDapur())
    pesanan_budi.tambah_pengamat(NotifikasiPelanggan())
    pesanan_budi.bayar(PembayaranFactory.buat("tunai", 100000, ""))
    for status in ["DIPROSES", "SIAP", "SELESAI"]:
        print(f"Status diubah menjadi {status}:")
        pesanan_budi.ubah_status(status)
    print()
    StrukPesanan(pesanan_budi).cetak()


if __name__ == "__main__":
    main()
