"""
KedaiKita - Pertemuan 11: Exception Handling

Yang baru dibanding Pertemuan 10:
- pengecualian.py: KedaiError dan turunannya (StokTidakCukupError,
  MenuTidakDitemukanError, PembayaranGagalError).
- Kesalahan tidak lagi ditandai dengan None/False, tetapi dengan
  exception yang dilempar (raise) lalu ditangkap (try/except).
- Contoh lengkap try / except / else / finally.

Cara menjalankan (dari dalam folder studi-kasus):
    python main.py
"""

from kedai import Kedai
from menu import Makanan, Minuman
from pelanggan import Pelanggan
from pembayaran import PembayaranKartu, PembayaranQRIS, PembayaranTunai
from pengecualian import (KedaiError, MenuTidakDitemukanError,
                          PembayaranGagalError, StokTidakCukupError)


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
    budi = Pelanggan("Budi Santoso", "081234567890")
    siti = Pelanggan("Siti Aminah", "082198765432")
    rina = Pelanggan("Rina Marlina", "085312345678")

    print("=== PESANAN BUDI: MENAMBAH ITEM ===")
    pesanan_budi = kedai.buat_pesanan(budi)
    permintaan = [("M01", 2), ("M03", 1), ("M99", 1), ("M04", 50), ("M02", 0)]
    for kode, jumlah in permintaan:
        try:
            menu = kedai.cari_menu(kode)
            pesanan_budi.tambah_item(menu, jumlah)
        except MenuTidakDitemukanError as e:
            print(f"  [GAGAL] {e}")
        except StokTidakCukupError as e:
            print(f"  [GAGAL] {e}")
            print(f"          Saran: pesan paling banyak {e.tersedia} porsi")
        except KedaiError as e:  # error kedai lain (misalnya pesanan sudah lunas)
            print(f"  [GAGAL] {e}")
        except ValueError as e:
            print(f"  [GAGAL] {kode}: {e}")
        else:
            print(f"  [OK] {jumlah} x {menu.nama}")
    print()

    try:
        pesanan_budi.bayar(PembayaranTunai(100000))
    except KedaiError as e:
        print(f"  [GAGAL] {e}")
    print()

    print("=== PESANAN SITI: BAYAR GAGAL, LALU COBA LAGI ===")
    pesanan_siti = kedai.buat_pesanan(siti)
    try:
        pesanan_siti.tambah_item(kedai.cari_menu("M02"), 2)
        pesanan_siti.tambah_item(kedai.cari_menu("M05"))
        pesanan_siti.bayar(PembayaranQRIS(20000))
    except PembayaranGagalError as e:
        print(f"  [GAGAL] {e}")
        print("  Mencoba kartu kredit...")
        try:
            pesanan_siti.bayar(PembayaranKartu("BNI"))
        except KedaiError as e2:
            print(f"  [GAGAL LAGI] {e2}")
    except KedaiError as e:
        print(f"  [GAGAL] {e}")
    finally:
        print("  [log] proses pesanan Siti selesai")
    print()

    print("=== SATU PENANGKAP UNTUK SEMUA ERROR KEDAI ===")
    pesanan_rina = kedai.buat_pesanan(rina)
    for kode, jumlah in [("M77", 1), ("M04", 99)]:
        try:
            pesanan_rina.tambah_item(kedai.cari_menu(kode), jumlah)
        except KedaiError as e:  # menangkap SEMUA turunan KedaiError
            print(f"  Ditolak: {e}")
    try:
        pesanan_budi.bayar(PembayaranTunai(100000))
    except KedaiError as e:
        print(f"  Ditolak: {e}")
    try:
        pesanan_budi.tambah_item(kedai.cari_menu("M02"), 1)
    except KedaiError as e:
        print(f"  Ditolak: {e}")
    print()

    print("=== RINGKASAN ===")
    print(f"{pesanan_budi.nomor} ({budi.nama}): {pesanan_budi.status}")
    print(f"{pesanan_siti.nomor} ({siti.nama}): {pesanan_siti.status}")
    print(f"{pesanan_rina.nomor} ({rina.nama}): {pesanan_rina.status}, "
          f"{len(pesanan_rina.daftar_item)} item")
    kedai.cetak()


if __name__ == "__main__":
    main()
