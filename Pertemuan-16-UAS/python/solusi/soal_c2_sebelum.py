"""
Soal C2 (kode SEBELUM refactor) - Kasir Laundry "Serba Bisa"
Pertemuan 16 - UAS (latihan persiapan, BUKAN soal ujian asli)

Program ini BERJALAN dengan benar, tetapi desainnya berantakan: hampir
semua pekerjaan ditumpuk di satu kelas. Inilah kode awal Soal C2.
Tugasmu: refactor dengan prinsip SOLID + minimal satu design pattern,
dan output-nya TIDAK BOLEH berubah sedikit pun.

Cara menjalankan:
    python soal_c2_sebelum.py
"""


class LaundrySerbaBisa:
    def __init__(self):
        self.riwayat = []  # isi: (kode, nama, berat, total)
        self.nomor = 0

    def terima_cucian(self, nama, no_hp, layanan, berat, promo):
        # cari tarif per kg
        if layanan == "cuci kering":
            tarif = 6000
        elif layanan == "cuci setrika":
            tarif = 8000
        elif layanan == "setrika saja":
            tarif = 5000
        else:
            print(f"[DITOLAK] Layanan '{layanan}' tidak tersedia")
            return
        self.nomor += 1
        kode = f"L{self.nomor:03d}"
        subtotal = tarif * berat

        # hitung promo
        potongan = 0
        nama_promo = ""
        if promo == "member":
            potongan = subtotal * 10 // 100
            nama_promo = "Member 10%"
        elif promo == "gratis1kg":
            if berat >= 5:
                potongan = tarif
                nama_promo = "Gratis 1 kg"
        total = subtotal - potongan

        # cetak nota
        print("=" * 36)
        print("LAUNDRY BERSIH KILAT")
        print("=" * 36)
        print(f"No. Order : {kode}")
        print(f"Pelanggan : {nama}")
        print(f"Layanan   : {layanan}")
        teks_tarif = f"Rp{tarif:,}".replace(",", ".")
        print(f"Berat     : {berat} kg x {teks_tarif}")
        print("-" * 36)
        teks_subtotal = f"Rp{subtotal:,}".replace(",", ".")
        print(f"{'Subtotal':<24}{teks_subtotal:>12}")
        if potongan > 0:
            teks_potongan = "-" + f"Rp{potongan:,}".replace(",", ".")
            print(f"{'Promo ' + nama_promo:<24}{teks_potongan:>12}")
        teks_total = f"Rp{total:,}".replace(",", ".")
        print(f"{'TOTAL':<24}{teks_total:>12}")
        print("=" * 36)

        # kirim WhatsApp
        print(f"[WA ke {no_hp}] Halo {nama}, cucian {kode} sudah kami terima. "
              f"Total {teks_total}.")

        # simpan riwayat
        self.riwayat.append((kode, nama, berat, total))

    def cetak_laporan(self):
        print("=== LAPORAN HARIAN ===")
        total_berat = 0
        pendapatan = 0
        for kode, nama, berat, total in self.riwayat:
            teks = f"Rp{total:,}".replace(",", ".")
            print(f"{kode}  {nama:<16}{berat:>3} kg{teks:>12}")
            total_berat += berat
            pendapatan += total
        print(f"Jumlah order : {len(self.riwayat)}")
        print(f"Total berat  : {total_berat} kg")
        print("Pendapatan   : " + f"Rp{pendapatan:,}".replace(",", "."))


def main():
    laundry = LaundrySerbaBisa()
    laundry.terima_cucian("Budi Santoso", "081234567890", "cuci setrika", 4,
                          "member")
    print()
    laundry.terima_cucian("Siti Aminah", "082198765432", "cuci kering", 6,
                          "gratis1kg")
    print()
    laundry.terima_cucian("Rina Marlina", "085312345678", "setrika saja", 3,
                          "gratis1kg")
    print()
    laundry.terima_cucian("Andi Wijaya", "087711223344", "dry clean", 2, "")
    print()
    laundry.terima_cucian("Dimas Pratama", "081355577799", "cuci setrika", 5, "")
    print()
    laundry.cetak_laporan()


if __name__ == "__main__":
    main()
