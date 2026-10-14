"""
Solusi Latihan 03 - Paket Kiriman
Pertemuan 03 - Atribut dan Method Lebih Dalam

Ide penyelesaian:
- Parameter layanan diberi nilai bawaan "REG", jadi paket bisa dibuat
  dengan 3 atau 4 argumen.
- berat_kg() membulatkan berat ke ATAS dengan rumus bilangan bulat
  (berat_gram + 999) // 1000. Contoh: 1200 gram -> 2 kg, 500 gram -> 1 kg.
- ongkir() memakai berat_kg() (method memanggil method lain lewat self).
- __str__ menyusun teks satu baris berisi semua data paket dan ongkirnya.

Cara menjalankan:
    python latihan03_paket_kiriman.py
"""


class Paket:
    """Paket kiriman dengan ongkos kirim berdasarkan berat dan layanan."""

    def __init__(self, resi, tujuan, berat_gram, layanan="REG"):
        self.resi = resi
        self.tujuan = tujuan
        self.berat_gram = berat_gram
        self.layanan = layanan

    def berat_kg(self):
        """Berat dibulatkan ke atas ke kilogram terdekat."""
        return (self.berat_gram + 999) // 1000

    def ongkir(self):
        if self.layanan == "KILAT":
            tarif = 15000
        else:
            tarif = 9000
        return self.berat_kg() * tarif

    def __str__(self):
        return (f"[{self.resi}] {self.tujuan}, {self.berat_gram} gram, "
                f"{self.layanan} - ongkir Rp{self.ongkir()}")


def main():
    paket1 = Paket("PKT001", "Balikpapan", 1200)  # layanan bawaan: REG
    paket2 = Paket("PKT002", "Bontang", 500, "KILAT")
    paket3 = Paket("PKT003", "Tenggarong", 2100)

    print("=== DAFTAR PAKET ===")
    print(paket1)
    print(paket2)
    print(paket3)
    total = paket1.ongkir() + paket2.ongkir() + paket3.ongkir()
    print(f"Total ongkir: Rp{total}")


if __name__ == "__main__":
    main()
