/*
 * Solusi Latihan 01 - Kelas Buku
 * Pertemuan 02 - Kelas dan Objek
 *
 * Ide penyelesaian:
 * 1. Buat kelas Buku dengan field judul, penulis, tahun dan konstruktornya.
 * 2. Method tampilkanInfo() mencetak data; method umur(tahunSekarang)
 *    MENGEMBALIKAN selisih tahun (tipe kembalian int).
 *
 * Cara menjalankan dari folder java/solusi (Java 11 ke atas):
 *     java Latihan01Buku.java
 */
public class Latihan01Buku {

    public static void main(String[] args) {
        Buku buku1 = new Buku("Laskar Pelangi", "Andrea Hirata", 2005);
        Buku buku2 = new Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980);
        Buku buku3 = new Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009);

        System.out.println("=== RAK BUKU ===");
        buku1.tampilkanInfo();
        buku2.tampilkanInfo();
        buku3.tampilkanInfo();

        System.out.println();
        System.out.println("=== UMUR BUKU DI TAHUN 2026 ===");
        System.out.println(buku1.judul + ": " + buku1.umur(2026) + " tahun");
        System.out.println(buku2.judul + ": " + buku2.umur(2026) + " tahun");
        System.out.println(buku3.judul + ": " + buku3.umur(2026) + " tahun");
    }
}

/** Data sebuah buku. */
class Buku {
    String judul;
    String penulis;
    int tahun;

    Buku(String judul, String penulis, int tahun) {
        this.judul = judul;
        this.penulis = penulis;
        this.tahun = tahun;
    }

    void tampilkanInfo() {
        System.out.println(judul + " - " + penulis + " (" + tahun + ")");
    }

    int umur(int tahunSekarang) {
        return tahunSekarang - tahun;
    }
}
