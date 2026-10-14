/*
 * Contoh 05 - Mengurutkan dengan Comparator dan Lambda
 * Pertemuan 12 - Koleksi dan Generics
 *
 * Satu daftar produk bisa diurutkan dengan banyak cara, seperti tombol
 * "Termurah", "Terlaris", dan "Rating" di toko online.
 * - list.sort(pembanding)              -> mengurutkan list ITU SENDIRI
 * - (a, b) -> ...                      -> lambda = fungsi kecil tanpa nama
 * - Comparator.comparing(Produk::getHarga) -> pembanding dari "kunci"
 *   (Produk::getHarga adalah method reference, singkatan lambda p -> p.getHarga())
 * - .reversed() membalik urutan, .thenComparing(...) kriteria kedua jika seri
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05SortingComparator.java
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;

public class Contoh05SortingComparator {

    static void tampilkan(String judul, List<Produk> daftar) {
        System.out.println("=== " + judul + " ===");
        for (Produk produk : daftar) {
            System.out.println(produk);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        List<Produk> daftar = List.of(
                new Produk("Flashdisk 64GB", 85000, 5, 120),
                new Produk("Mouse Wireless", 75000, 4, 340),
                new Produk("Kabel Data USB-C", 25000, 4, 520),
                new Produk("Headset Gaming", 150000, 5, 95),
                new Produk("Powerbank 10000mAh", 125000, 4, 210));
        tampilkan("URUTAN ASLI", daftar);

        List<Produk> termurah = new ArrayList<>(daftar); // [1] salin dulu: sort mengubah list
        termurah.sort((a, b) -> Integer.compare(a.getHarga(), b.getHarga())); // [2] lambda
        tampilkan("TERMURAH", termurah);

        List<Produk> terlaris = new ArrayList<>(daftar);
        terlaris.sort(Comparator.comparing(Produk::getTerjual).reversed()); // [3]
        tampilkan("TERLARIS", terlaris);

        List<Produk> rating = new ArrayList<>(daftar);
        rating.sort(Comparator.comparing(Produk::getRating).reversed()
                .thenComparing(Produk::getHarga)); // [4] dua kriteria
        tampilkan("RATING TERTINGGI, LALU TERMURAH", rating);

        System.out.println("=== LAIN-LAIN ===");
        List<Produk> urutNama = new ArrayList<>(daftar);
        urutNama.sort(Comparator.comparing(p -> p.getNama())); // [5] lambda sebagai kunci
        List<String> nama = new ArrayList<>();
        for (Produk p : urutNama) {
            nama.add(p.getNama());
        }
        System.out.println("Nama A-Z      : " + String.join(", ", nama));
        Produk murah = Collections.min(daftar, Comparator.comparing(Produk::getHarga)); // [6]
        Produk mahal = Collections.max(daftar, Comparator.comparing(Produk::getHarga));
        System.out.println("Paling murah  : " + murah.getNama());
        System.out.println("Paling mahal  : " + mahal.getNama());
        System.out.println("Urutan asli tetap, pertama: " + daftar.get(0).getNama()); // [7]
        List<String> rating5 = daftar.stream() // [8] bonus: Stream (boleh dilewati)
                .filter(p -> p.getRating() == 5)
                .map(Produk::getNama)
                .toList();
        System.out.println("Rating 5      : " + String.join(", ", rating5));
    }
}

/** Produk di toko online kampus. */
class Produk {
    private String nama;
    private int harga;
    private int rating;
    private int terjual;

    public Produk(String nama, int harga, int rating, int terjual) {
        this.nama = nama;
        this.harga = harga;
        this.rating = rating;
        this.terjual = terjual;
    }

    public String getNama() {
        return nama;
    }

    public int getHarga() {
        return harga;
    }

    public int getRating() {
        return rating;
    }

    public int getTerjual() {
        return terjual;
    }

    private static String rupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    @Override
    public String toString() {
        return String.format("%-20s%11s  rating %d  terjual %d", nama, rupiah(harga), rating,
                terjual);
    }
}
