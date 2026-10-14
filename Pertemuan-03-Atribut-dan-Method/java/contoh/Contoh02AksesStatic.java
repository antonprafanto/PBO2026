/*
 * Contoh 02 - Atribut static Selalu Diakses Lewat Nama Kelas
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Di Java, atribut static hanya ada SATU, milik kelas. Java memang MENGIZINKAN
 * kita menulisnya lewat objek (this.total atau ayu.total), tetapi tulisan itu
 * menyesatkan: kelihatannya milik objek, padahal yang diubah tetap nilai
 * BERSAMA. Karena itu, biasakan menulis NamaKelas.atribut.
 *
 * Program ini sengaja memakai skenario yang sama dengan
 * contoh02_jebakan_atribut_kelas.py. Hasilnya BERBEDA dengan versi Python,
 * dan perbedaan itulah pelajarannya (lihat Jembatan Python - Java).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02AksesStatic.java
 */
public class Contoh02AksesStatic {

    public static void main(String[] args) {
        Pengunjung ayu = new Pengunjung("Ayu");
        Pengunjung bima = new Pengunjung("Bima");

        System.out.println("=== LEWAT OBJEK: this.total += 1 ===");
        ayu.masukLewatObjek();
        bima.masukLewatObjek();
        System.out.println("Total menurut kelas : " + Pengunjung.total);
        System.out.println("Total menurut ayu   : " + ayu.total);  // [3] boleh, tapi menyesatkan
        System.out.println("Total menurut bima  : " + bima.total);

        System.out.println();
        System.out.println("=== LEWAT NAMA KELAS: Pengunjung.total += 1 ===");
        Pengunjung citra = new Pengunjung("Citra");
        Pengunjung dimas = new Pengunjung("Dimas");
        citra.masukLewatKelas();
        dimas.masukLewatKelas();
        System.out.println("Total menurut kelas : " + Pengunjung.total);
        System.out.println("Total menurut citra : " + citra.total);
        System.out.println("Total menurut dimas : " + dimas.total);
        System.out.println("Total menurut ayu   : " + ayu.total); // [4] tetap total bersama
    }
}

/** Pengunjung perpustakaan kampus. */
class Pengunjung {
    static int total = 0; // atribut kelas: jumlah seluruh pengunjung hari ini

    String nama;

    Pengunjung(String nama) {
        this.nama = nama;
    }

    void masukLewatObjek() {
        this.total += 1; // [1] boleh, tetapi menyesatkan: yang berubah tetap total BERSAMA
    }

    void masukLewatKelas() {
        Pengunjung.total += 1; // [2] cara yang jelas: lewat nama kelas
    }
}
