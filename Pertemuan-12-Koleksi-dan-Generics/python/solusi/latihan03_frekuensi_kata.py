"""
Solusi Latihan 03 - Frekuensi Kata
Pertemuan 12 - Koleksi dan Generics

Ide penyelesaian:
- Bersihkan teks: jadikan huruf kecil, buang titik dan koma, pecah per spasi.
- Hitung dengan dict: frekuensi[kata] = frekuensi.get(kata, 0) + 1
- Urutkan pasangan (kata, jumlah) dengan key=lambda p: (-p[1], p[0])
  -> jumlah terbanyak dulu; jika seri, kata diurutkan A-Z.
- Kata yang muncul sekali: list comprehension, lalu diurutkan.

Cara menjalankan:
    python latihan03_frekuensi_kata.py
"""

TEKS = ("Kopi susu gula aren enak. Kopi hitam juga enak, "
        "tapi kopi susu paling laris di kedai.")


def hitung_frekuensi(teks: str) -> dict[str, int]:
    bersih = teks.lower().replace(".", "").replace(",", "")
    frekuensi: dict[str, int] = {}
    for kata in bersih.split():
        frekuensi[kata] = frekuensi.get(kata, 0) + 1
    return frekuensi


def main():
    frekuensi = hitung_frekuensi(TEKS)
    urut = sorted(frekuensi.items(), key=lambda p: (-p[1], p[0]))

    print("=== FREKUENSI KATA ===")
    print(f"Jumlah kata     : {sum(frekuensi.values())}")
    print(f"Jumlah kata unik: {len(frekuensi)}")
    print("3 kata terbanyak:")
    for nomor, (kata, jumlah) in enumerate(urut[:3], start=1):
        print(f"  {nomor}. {kata} ({jumlah} kali)")
    sekali = sorted([kata for kata, jumlah in frekuensi.items() if jumlah == 1])
    print(f"Muncul sekali   : {', '.join(sekali)}")


if __name__ == "__main__":
    main()
