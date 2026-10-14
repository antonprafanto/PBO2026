/*
 * Contoh 01 - Masalah: Kelas Induk yang Terlalu Umum
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * BangunDatar di sini masih kelas induk BIASA (belum abstrak). Akibatnya:
 * 1. Objek "bangun datar umum" bisa dibuat, padahal tidak ada artinya.
 * 2. Kelas anak yang LUPA menulis luas() tidak diprotes sama sekali.
 *    Ia diam-diam memakai luas() milik induk yang selalu 0.
 *
 * Contoh 02 memperbaiki kedua masalah ini dengan kelas abstrak.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01MasalahIndukUmum.java
 */
import java.util.List;

public class Contoh01MasalahIndukUmum {

    public static void main(String[] args) {
        System.out.println("=== MASALAH 1: OBJEK 'UMUM' BISA DIBUAT ===");
        BangunDatar misterius = new BangunDatar("Bangun datar misterius"); // [3] tidak dilarang
        System.out.println(misterius.info());

        System.out.println();
        System.out.println("=== MASALAH 2: LUPA OVERRIDE, TIDAK ADA YANG PROTES ===");
        List<BangunDatar> daftar = List.of(new Persegi(5), new Segitiga(6, 4));
        for (BangunDatar bangun : daftar) {
            System.out.println(bangun.info()); // [4] Segitiga memakai luas() milik induk
        }
        System.out.println("Padahal luas segitiga seharusnya 6 x 4 / 2 = 12 cm2!");
    }
}

/** Kelas induk biasa (BELUM abstrak) untuk semua bangun datar. */
class BangunDatar {
    private String nama;

    public BangunDatar(String nama) {
        this.nama = nama;
    }

    public int luas() {
        return 0; // [1] luas "bangun datar umum"? Tidak ada jawaban yang masuk akal
    }

    public String info() {
        return nama + ": luas " + luas() + " cm2";
    }
}

/** Persegi dengan panjang sisi tertentu. */
class Persegi extends BangunDatar {
    private int sisi;

    public Persegi(int sisi) {
        super("Persegi");
        this.sisi = sisi;
    }

    @Override
    public int luas() { // override dengan benar
        return sisi * sisi;
    }
}

/** Segitiga dengan alas dan tinggi. */
class Segitiga extends BangunDatar {
    private int alas;
    private int tinggi;

    public Segitiga(int alas, int tinggi) {
        super("Segitiga");
        this.alas = alas;
        this.tinggi = tinggi;
    }

    // [2] Programmer LUPA menulis method luas() di sini!
}
