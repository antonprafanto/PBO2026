/*
 * KedaiKita - versi PROSEDURAL (tanpa kelas buatan sendiri)
 * Pertemuan 01 - Pengenalan PBO
 *
 * Program ini menyimpan data menu dalam TIGA array terpisah.
 * Menu ke-0 ada di indeks 0 pada ketiga array, menu ke-1 di indeks 1, dan seterusnya.
 * Cara ini terlihat sederhana, tetapi mudah sekali rusak. Perhatikan bagian akhir output!
 *
 * Catatan: Java mewajibkan semua kode berada di dalam sebuah kelas, jadi kelas
 * KedaiKitaProsedural di bawah hanya dipakai sebagai "pembungkus". Isinya tetap
 * gaya prosedural: data (array static) terpisah dari method yang mengolahnya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java KedaiKitaProsedural.java
 */
import java.util.Arrays;

public class KedaiKitaProsedural {

    // Data menu dipisah ke tiga array. Indeks yang sama = menu yang sama.
    static String[] namaMenu = {"Kopi Susu Gula Aren", "Nasi Goreng Kampung", "Es Teh Manis"};
    static int[] hargaMenu = {18000, 25000, 8000};
    static int[] stokMenu = {20, 15, 30};

    /** Mencetak semua menu beserta harga dan stoknya. */
    static void tampilkanMenu() {
        System.out.println("=== DAFTAR MENU KEDAIKITA ===");
        for (int i = 0; i < namaMenu.length; i++) {
            System.out.println((i + 1) + ". " + namaMenu[i] + " - Rp" + hargaMenu[i]
                    + " (stok " + stokMenu[i] + ")");
        }
    }

    /**
     * Menghitung total harga sekaligus mengurangi stok.
     *
     * daftarPesanan berisi pasangan {indeksMenu, jumlah}.
     */
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

    public static void main(String[] args) {
        tampilkanMenu();
        System.out.println();

        // Budi memesan 2 Kopi Susu Gula Aren (indeks 0) dan 1 Es Teh Manis (indeks 2)
        int[][] pesananBudi = {{0, 2}, {2, 1}};
        int total = hitungTotal(pesananBudi);
        System.out.println("Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis");
        System.out.println("Total bayar : Rp" + total);
        System.out.println();

        // Pemilik kedai ingin daftar menu tampil urut abjad.
        // Ia hanya mengurutkan array nama... dan lupa bahwa harga & stok ada di array lain!
        System.out.println("Mengurutkan nama menu sesuai abjad...");
        Arrays.sort(namaMenu);
        tampilkanMenu();
        System.out.println();
        System.out.println("Lho? Es Teh Manis jadi Rp18000 dan Nasi Goreng Kampung jadi Rp8000!");
        // Kata "list" di bawah sengaja dipakai agar output SAMA PERSIS dengan versi Python.
        System.out.println("Data satu menu tercerai-berai di tiga list, jadi mudah tertukar.");
    }
}
