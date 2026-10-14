"""
KedaiKita - Pertemuan 13: Prinsip SOLID
Bagian SEBELUM refactor: satu kelas yang "serba bisa".

KasirSerbaBisa mengerjakan SEMUANYA sendirian:
  1. menyimpan data menu,
  2. menghitung subtotal dan diskon (dengan rantai if/elif),
  3. menyusun dan mencetak struk,
  4. menyimpan riwayat pesanan.

Program ini BERJALAN dengan benar. Masalahnya bukan pada hasil, tetapi pada
desain: setiap perubahan kecil (promo baru, format struk baru, tempat
penyimpanan baru) memaksa kita membongkar kelas yang sama.
Bandingkan dengan folder ../sesudah yang hasil outputnya SAMA PERSIS.

Cara menjalankan:
    python kasir_serba_bisa.py
"""


def format_rupiah(angka):
    return f"Rp{angka:,}".replace(",", ".")


class KasirSerbaBisa:
    """Kelas 'dewa' (god class): terlalu banyak tanggung jawab."""

    def __init__(self):
        # Tugas 1: menyimpan data menu (kode -> (nama, harga))
        self.menu = {
            "M01": ("Kopi Susu Gula Aren", 18000),
            "M02": ("Es Teh Manis", 8000),
            "M03": ("Nasi Goreng Kampung", 25000),
            "M04": ("Mie Goreng Jawa", 23000),
            "M05": ("Pisang Goreng Keju", 15000),
        }
        # Tugas 4: menyimpan riwayat pesanan
        self.riwayat = []
        self.nomor_terakhir = 0

    def proses_pesanan(self, nama_pelanggan, poin_pelanggan, daftar_beli,
                       jenis_diskon):
        self.nomor_terakhir += 1
        nomor = f"P{self.nomor_terakhir:03d}"

        # Tugas 2: menghitung subtotal
        subtotal = 0
        for kode, jumlah in daftar_beli:
            nama, harga = self.menu[kode]
            subtotal += harga * jumlah

        # Tugas 2 (lanjutan): diskon memakai rantai if/elif.
        # Setiap ada jenis promo baru, method ini HARUS dibongkar (melanggar OCP).
        if jenis_diskon == "member":
            if poin_pelanggan >= 10:
                potongan = subtotal * 10 // 100
                keterangan = "Member 10%"
            else:
                potongan = 0
                keterangan = "Member (poin belum cukup)"
        elif jenis_diskon == "promo":
            potongan = subtotal * 15 // 100
            keterangan = "Promo 15%"
        else:
            potongan = 0
            keterangan = "Tanpa diskon"
        total = subtotal - potongan

        # Tugas 3: menyusun dan mencetak struk
        print("=" * 40)
        print("KEDAIKITA - STRUK PESANAN")
        print("=" * 40)
        print(f"No. Pesanan : {nomor}")
        print(f"Pelanggan   : {nama_pelanggan}")
        print("Status      : BARU")
        print("-" * 40)
        for kode, jumlah in daftar_beli:
            nama, harga = self.menu[kode]
            kiri = f"{jumlah} x {nama}"
            print(f"{kiri:<30}{format_rupiah(harga * jumlah):>10}")
        print("-" * 40)
        print(f"{'Subtotal':<30}{format_rupiah(subtotal):>10}")
        if potongan > 0:
            kiri = f"Diskon {keterangan}"
            kanan = "-" + format_rupiah(potongan)
            print(f"{kiri:<30}{kanan:>10}")
        print(f"{'TOTAL':<30}{format_rupiah(total):>10}")
        print("=" * 40)

        # Tugas 4: menyimpan riwayat (hanya bisa ke list di memori)
        self.riwayat.append((nomor, nama_pelanggan, total))


def main():
    kasir = KasirSerbaBisa()
    kasir.proses_pesanan("Budi Santoso", 0, [("M01", 2), ("M03", 1)], "tanpa")
    print()
    kasir.proses_pesanan("Siti Aminah", 12, [("M02", 2), ("M05", 1)], "member")
    print()
    kasir.proses_pesanan("Rina Marlina", 0, [("M01", 1), ("M04", 1)], "promo")
    print()

    print("=== RIWAYAT PESANAN ===")
    total_semua = 0
    for nomor, nama, total in kasir.riwayat:
        print(f"{nomor}  {nama:<20}{format_rupiah(total):>12}")
        total_semua += total
    print(f"Total pendapatan: {format_rupiah(total_semua)}")


if __name__ == "__main__":
    main()
