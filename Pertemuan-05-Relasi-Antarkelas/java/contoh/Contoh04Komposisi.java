/*
 * Contoh 04 - Komposisi: Bagian yang Dibuat dan Dimiliki Penuh
 * Pertemuan 05 - Relasi Antarkelas
 *
 * Rumah MEMBUAT sendiri objek-objek Ruangan miliknya. Kode di luar kelas
 * hanya mengirim DATA (nama, panjang, lebar), tidak pernah membuat Ruangan.
 * Karena hanya rumah yang memegang ruangannya, ruangan ikut hilang bersama
 * rumahnya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04Komposisi.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh04Komposisi {

    public static void main(String[] args) {
        System.out.println("=== MEMBANGUN RUMAH ===");
        Rumah rumah = new Rumah("Pak Hasan");
        rumah.bangunRuangan("Ruang tamu", 4, 3); // [4] hanya mengirim data
        rumah.bangunRuangan("Kamar tidur", 3, 3);
        rumah.bangunRuangan("Dapur", 3, 2);
        rumah.tampilkan();

        System.out.println();
        System.out.println("=== RUMAH DIROBOHKAN ===");
        rumah = null; // [5] satu-satunya pemegang ruangan dilepas
        System.out.println("Rumah dirobohkan. Tidak ada variabel lain yang memegang ruangannya,");
        System.out.println("jadi ruangan-ruangan itu ikut hilang bersama rumahnya.");
    }
}

/** Satu ruangan di dalam rumah. Ukuran dalam meter. */
class Ruangan {
    private String nama;
    private int panjang;
    private int lebar;

    public Ruangan(String nama, int panjang, int lebar) {
        this.nama = nama;
        this.panjang = panjang;
        this.lebar = lebar;
    }

    public int luas() {
        return panjang * lebar;
    }

    @Override
    public String toString() {
        return nama + " " + panjang + "x" + lebar + " m = " + luas() + " m2";
    }
}

/** Rumah yang membuat dan memiliki ruangan-ruangannya sendiri. */
class Rumah {
    private String pemilik;
    private List<Ruangan> daftarRuangan;

    public Rumah(String pemilik) {
        this.pemilik = pemilik;
        this.daftarRuangan = new ArrayList<>();
    }

    public void bangunRuangan(String nama, int panjang, int lebar) { // [1]
        Ruangan ruangan = new Ruangan(nama, panjang, lebar); // [2] dibuat DI DALAM rumah
        daftarRuangan.add(ruangan);
    }

    public int luasTotal() {
        int total = 0;
        for (Ruangan ruangan : daftarRuangan) {
            total += ruangan.luas(); // [3] rumah bertanya ke setiap ruangan
        }
        return total;
    }

    public void tampilkan() {
        System.out.println("Rumah " + pemilik + ":");
        for (Ruangan ruangan : daftarRuangan) {
            System.out.println("- " + ruangan);
        }
        System.out.println("Luas total: " + luasTotal() + " m2");
    }
}
