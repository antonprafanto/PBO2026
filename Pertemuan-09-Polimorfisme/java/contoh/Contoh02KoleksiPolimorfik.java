/*
 * Contoh 02 - Koleksi Polimorfik: Menambah Jenis Baru Tanpa Mengubah Pemanggil
 * Pertemuan 09 - Polimorfisme
 *
 * Satu List berisi bermacam bangun datar. Method cetakLaporan() memanggil
 * nama() dan luas() pada setiap objek TANPA menyebut satu pun kelas anak.
 * Akibatnya, jenis baru (Trapesium) bisa ditambahkan belakangan tanpa
 * mengubah method itu sedikit pun.
 *
 * Semua ukuran dalam cm dan berupa bilangan bulat.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02KoleksiPolimorfik.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh02KoleksiPolimorfik {

    static void cetakLaporan(List<BangunDatar> daftar) { // [3] tidak kenal kelas anak mana pun
        int total = 0;
        for (BangunDatar bangun : daftar) {
            int luas = bangun.luas(); // [4] versi luas() milik objek yang sebenarnya
            System.out.println(String.format("%-30s luas %4d cm2", bangun.nama(), luas));
            total += luas;
        }
        System.out.println("Total luas: " + total + " cm2");
    }

    public static void main(String[] args) {
        System.out.println("=== LAPORAN AWAL: TIGA JENIS ===");
        List<BangunDatar> daftar = new ArrayList<>(); // [5] satu List untuk semua jenis
        daftar.add(new Persegi(10));
        daftar.add(new PersegiPanjang(12, 5));
        daftar.add(new Segitiga(8, 6));
        cetakLaporan(daftar);

        System.out.println();
        System.out.println("=== SETELAH ADA JENIS BARU ===");
        daftar.add(new Trapesium(6, 10, 4)); // [6] cetakLaporan() tidak diubah
        daftar.add(new BangunDatar());
        cetakLaporan(daftar);
    }
}

/** Kelas induk semua bangun datar. */
class BangunDatar {

    public String nama() {
        return "Bangun datar";
    }

    public int luas() {
        return 0; // [1] bangun datar "umum" tidak punya rumus luas
    }
}

class Persegi extends BangunDatar {
    private int sisi;

    public Persegi(int sisi) {
        this.sisi = sisi;
    }

    @Override
    public String nama() {
        return "Persegi " + sisi + "x" + sisi;
    }

    @Override
    public int luas() {
        return sisi * sisi;
    }
}

class PersegiPanjang extends BangunDatar {
    private int panjang;
    private int lebar;

    public PersegiPanjang(int panjang, int lebar) {
        this.panjang = panjang;
        this.lebar = lebar;
    }

    @Override
    public String nama() {
        return "Persegi panjang " + panjang + "x" + lebar;
    }

    @Override
    public int luas() {
        return panjang * lebar;
    }
}

class Segitiga extends BangunDatar {
    private int alas;
    private int tinggi;

    public Segitiga(int alas, int tinggi) {
        this.alas = alas;
        this.tinggi = tinggi;
    }

    @Override
    public String nama() {
        return "Segitiga alas " + alas + " tinggi " + tinggi;
    }

    @Override
    public int luas() {
        return alas * tinggi / 2;
    }
}

// ----- Jenis BARU yang ditambahkan belakangan -----
class Trapesium extends BangunDatar { // [2] cukup menulis kelas baru
    private int sisiAtas;
    private int sisiBawah;
    private int tinggi;

    public Trapesium(int sisiAtas, int sisiBawah, int tinggi) {
        this.sisiAtas = sisiAtas;
        this.sisiBawah = sisiBawah;
        this.tinggi = tinggi;
    }

    @Override
    public String nama() {
        return "Trapesium " + sisiAtas + "/" + sisiBawah + " tinggi " + tinggi;
    }

    @Override
    public int luas() {
        return (sisiAtas + sisiBawah) * tinggi / 2;
    }
}
