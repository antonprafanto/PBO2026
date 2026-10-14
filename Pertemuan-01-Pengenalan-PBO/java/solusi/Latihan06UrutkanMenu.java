/*
 * Solusi Latihan 06 - KedaiKita: Mengurutkan Tanpa Tertukar (cara prosedural)
 * Pertemuan 01 - Pengenalan PBO
 *
 * Ide penyelesaian:
 * - Pakai bubble sort seperti contoh 06: bandingkan dua menu yang bertetangga,
 *   lalu tukar jika nama di kiri lebih belakang abjadnya daripada nama di kanan.
 *   Teks di Java dibandingkan dengan compareTo(): hasilnya lebih dari 0 jika
 *   teks pertama lebih belakang abjadnya.
 * - KUNCINYA: setiap kali menukar nama, tukar juga harga dan stok di posisi
 *   yang sama. Ketiga array harus selalu bergerak bersama.
 * - Bandingkan dengan versi OOP (studi-kasus/KedaiKitaOop.java): di sana cukup
 *   satu baris sort, karena data satu menu sudah terbungkus dalam satu objek.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan06UrutkanMenu.java
 */
public class Latihan06UrutkanMenu {

    // Data menu sama dengan studi kasus: tiga array paralel.
    static String[] namaMenu = {"Kopi Susu Gula Aren", "Nasi Goreng Kampung", "Es Teh Manis"};
    static int[] hargaMenu = {18000, 25000, 8000};
    static int[] stokMenu = {20, 15, 30};

    static void tampilkanMenu() {
        System.out.println("=== DAFTAR MENU KEDAIKITA ===");
        for (int i = 0; i < namaMenu.length; i++) {
            System.out.println((i + 1) + ". " + namaMenu[i] + " - Rp" + hargaMenu[i]
                    + " (stok " + stokMenu[i] + ")");
        }
    }

    /** Sama dengan studi kasus: daftarPesanan berisi pasangan {indeks, jumlah}. */
    static int hitungTotal(int[][] daftarPesanan) {
        int total = 0;
        for (int[] pesanan : daftarPesanan) {
            int indeks = pesanan[0];
            int jumlah = pesanan[1];
            total = total + hargaMenu[indeks] * jumlah;
            stokMenu[indeks] = stokMenu[indeks] - jumlah;
        }
        return total;
    }

    static void urutkanMenuBerdasarkanNama() {
        int n = namaMenu.length;
        for (int putaran = 0; putaran < n - 1; putaran++) {
            for (int i = 0; i < n - 1 - putaran; i++) {
                if (namaMenu[i].compareTo(namaMenu[i + 1]) > 0) { // dibandingkan sesuai abjad
                    // tukar SEMUA data milik dua menu ini, bukan hanya namanya
                    String sementaraNama = namaMenu[i];
                    namaMenu[i] = namaMenu[i + 1];
                    namaMenu[i + 1] = sementaraNama;

                    int sementaraHarga = hargaMenu[i];
                    hargaMenu[i] = hargaMenu[i + 1];
                    hargaMenu[i + 1] = sementaraHarga;

                    int sementaraStok = stokMenu[i];
                    stokMenu[i] = stokMenu[i + 1];
                    stokMenu[i + 1] = sementaraStok;
                }
            }
        }
    }

    public static void main(String[] args) {
        tampilkanMenu();
        System.out.println();

        int[][] pesananBudi = {{0, 2}, {2, 1}};
        int total = hitungTotal(pesananBudi);
        System.out.println("Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis");
        System.out.println("Total bayar : Rp" + total);
        System.out.println();

        System.out.println("Mengurutkan menu sesuai abjad (harga dan stok ikut ditukar)...");
        urutkanMenuBerdasarkanNama();
        tampilkanMenu();
        System.out.println();
        System.out.println("Berhasil! Harga dan stok ikut pindah bersama namanya.");
        System.out.println("Namun, jika nanti ada data baru (misalnya kategori),");
        System.out.println("kode pengurut ini harus diubah lagi agar data baru itu ikut ditukar.");
    }
}
