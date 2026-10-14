"""
Solusi Latihan 02 - Struk Belanja Koperasi Mahasiswa
Pertemuan 01 - Pengenalan PBO

Ide penyelesaian:
1. Simpan data belanja di tiga list paralel: nama barang, harga satuan, jumlah.
2. Ulangi untuk setiap indeks: hitung subtotal = harga x jumlah, cetak barisnya,
   lalu tambahkan subtotal ke total dan jumlah ke total barang.
3. Jika total >= 50000, beri diskon 10%. Hitung dengan bilangan bulat:
   total * 10 // 100 (uang tidak pernah memakai float).

Cara menjalankan:
    python latihan02_struk_belanja.py
"""


def main():
    nama_barang = ["Buku Tulis", "Pulpen", "Map Plastik", "Kertas HVS"]
    harga_satuan = [5000, 3000, 2000, 45000]
    jumlah_beli = [4, 3, 5, 1]

    print("=== STRUK KOPERASI MAHASISWA ===")
    total = 0
    total_barang = 0
    for i in range(len(nama_barang)):
        subtotal = harga_satuan[i] * jumlah_beli[i]
        print(f"{nama_barang[i]} x {jumlah_beli[i]} = Rp{subtotal}")
        total = total + subtotal
        total_barang = total_barang + jumlah_beli[i]
    print("-" * 30)

    if total >= 50000:
        diskon = total * 10 // 100
    else:
        diskon = 0

    print(f"Jumlah barang : {total_barang} buah")
    print(f"Total belanja : Rp{total}")
    print(f"Diskon        : Rp{diskon}")
    print(f"Total bayar   : Rp{total - diskon}")


if __name__ == "__main__":
    main()
