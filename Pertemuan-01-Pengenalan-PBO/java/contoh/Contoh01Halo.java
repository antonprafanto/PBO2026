/*
 * Contoh 01 - Program Pertamaku
 * Pertemuan 01 - Pengenalan PBO
 *
 * - Setiap program Java berada di dalam sebuah kelas (class).
 * - Method main adalah "pintu masuk": Java mulai menjalankan program dari sini.
 * - System.out.println() menampilkan teks ke layar, lalu pindah ke baris baru.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01Halo.java
 * Atau cara klasik dua langkah (kompilasi dulu, lalu jalankan):
 *     javac Contoh01Halo.java
 *     java Contoh01Halo
 */
public class Contoh01Halo { // [1] kelas pembungkus; namanya sama dengan nama file

    public static void main(String[] args) { // [2] method main: pintu masuk program
        System.out.println("=== PROGRAM PERTAMAKU ==="); // [3] cetak teks, lalu pindah baris
        System.out.println("Halo, Samarinda!");
        System.out.println("Selamat datang di mata kuliah PBO 2026.");
        System.out.println(); // [4] println tanpa isi = baris kosong
        // [5] baris yang diawali dua garis miring adalah komentar, tidak dijalankan
        System.out.println("Perintah dijalankan berurutan dari atas ke bawah:");
        System.out.println("Langkah 1: siapkan alat");
        System.out.println("Langkah 2: tulis kode");
        System.out.println("Langkah 3: jalankan program"); // [6] setiap perintah diakhiri ;
    } // [7] kurung kurawal tutup: akhir method main
} // akhir kelas Contoh01Halo
