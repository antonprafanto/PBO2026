/*
 * Solusi Latihan 02 - Struk Belanja Koperasi Mahasiswa
 * Pertemuan 01 - Pengenalan PBO
 *
 * Ide penyelesaian:
 * 1. Simpan data belanja di tiga array paralel: nama barang, harga satuan, jumlah.
 * 2. Ulangi untuk setiap indeks: hitung subtotal = harga x jumlah, cetak barisnya,
 *    lalu tambahkan subtotal ke total dan jumlah ke total barang.
 * 3. Jika total >= 50000, beri diskon 10%. Hitung dengan bilangan bulat:
 *    total * 10 / 100 (uang tidak pernah memakai double).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02StrukBelanja.java
 */
public class Latihan02StrukBelanja {

    public static void main(String[] args) {
        String[] namaBarang = {"Buku Tulis", "Pulpen", "Map Plastik", "Kertas HVS"};
        int[] hargaSatuan = {5000, 3000, 2000, 45000};
        int[] jumlahBeli = {4, 3, 5, 1};

        System.out.println("=== STRUK KOPERASI MAHASISWA ===");
        int total = 0;
        int totalBarang = 0;
        for (int i = 0; i < namaBarang.length; i++) {
            int subtotal = hargaSatuan[i] * jumlahBeli[i];
            System.out.println(namaBarang[i] + " x " + jumlahBeli[i] + " = Rp" + subtotal);
            total = total + subtotal;
            totalBarang = totalBarang + jumlahBeli[i];
        }
        System.out.println("-".repeat(30));

        int diskon;
        if (total >= 50000) {
            diskon = total * 10 / 100;
        } else {
            diskon = 0;
        }

        System.out.println("Jumlah barang : " + totalBarang + " buah");
        System.out.println("Total belanja : Rp" + total);
        System.out.println("Diskon        : Rp" + diskon);
        System.out.println("Total bayar   : Rp" + (total - diskon));
    }
}
