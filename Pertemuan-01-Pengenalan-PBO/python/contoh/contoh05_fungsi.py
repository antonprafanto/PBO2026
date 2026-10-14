"""
Contoh 05 - Fungsi dengan Parameter dan Nilai Kembalian
Pertemuan 01 - Pengenalan PBO

- Fungsi dibuat dengan def, lalu dipanggil dengan menuliskan namanya.
- Parameter adalah "pintu masuk" data ke dalam fungsi.
- return mengirim hasil kembali ke pemanggil (nilai kembalian).
- Fungsi tanpa return juga boleh, misalnya fungsi yang tugasnya hanya mencetak.

Cara menjalankan:
    python contoh05_fungsi.py
"""

TARIF_DASAR = 10000  # [1] konstanta: nama HURUF BESAR, nilainya tidak pernah diubah
TARIF_PER_KM = 2500


def hitung_ongkos(jarak_km):  # [2] jarak_km adalah parameter
    """Tarif dasar untuk 4 km pertama, ditambah tarif per km berikutnya."""
    if jarak_km <= 4:
        return TARIF_DASAR  # [3] return langsung mengakhiri fungsi
    return TARIF_DASAR + (jarak_km - 4) * TARIF_PER_KM


def label_jarak(jarak_km):  # fungsi juga boleh mengembalikan teks
    if jarak_km <= 4:
        return "dekat"
    elif jarak_km <= 10:
        return "sedang"
    else:
        return "jauh"


def hitung_potongan(total, persen):  # boleh punya lebih dari satu parameter
    return total * persen // 100  # persen dihitung dengan bilangan bulat


def cetak_garis(panjang):  # [4] fungsi tanpa return: tugasnya hanya mencetak
    print("-" * panjang)


def main():
    print("=== TARIF OJEK ONLINE ===")
    cetak_garis(32)
    jarak_budi = 3
    jarak_siti = 7
    jarak_rina = 12
    ongkos_budi = hitung_ongkos(jarak_budi)  # [5] nilai kembalian disimpan ke variabel
    ongkos_siti = hitung_ongkos(jarak_siti)
    ongkos_rina = hitung_ongkos(jarak_rina)
    # [6] nilai kembalian juga bisa langsung dipakai di dalam f-string
    print(f"Budi : {jarak_budi} km ({label_jarak(jarak_budi)}) -> Rp{ongkos_budi}")
    print(f"Siti : {jarak_siti} km ({label_jarak(jarak_siti)}) -> Rp{ongkos_siti}")
    print(f"Rina : {jarak_rina} km ({label_jarak(jarak_rina)}) -> Rp{ongkos_rina}")
    cetak_garis(32)

    total = ongkos_budi + ongkos_siti + ongkos_rina
    potongan = hitung_potongan(total, 20)
    print(f"Total ongkos        : Rp{total}")
    print(f"Promo 20%           : -Rp{potongan}")
    print(f"Total setelah promo : Rp{total - potongan}")


if __name__ == "__main__":
    main()
