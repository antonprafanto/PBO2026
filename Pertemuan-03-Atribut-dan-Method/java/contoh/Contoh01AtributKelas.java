/*
 * Contoh 01 - Atribut Objek dan Atribut Kelas (static)
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * - Atribut OBJEK (nim, nama) dimiliki oleh setiap objek. Nilainya bisa
 *   berbeda-beda dan diisi di konstruktor.
 * - Atribut KELAS ditandai kata kunci static (kampus, jumlah). Hanya ada SATU
 *   nilai yang dipakai bersama oleh semua objek. Atribut static sudah ada
 *   sebelum objek mana pun dibuat.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01AtributKelas.java
 */
public class Contoh01AtributKelas {

    public static void main(String[] args) {
        System.out.println("=== SEBELUM ADA OBJEK ===");
        System.out.println("Kampus          : " + Mahasiswa.kampus); // [6] dibaca tanpa objek
        System.out.println("Jumlah mahasiswa: " + Mahasiswa.jumlah);

        Mahasiswa ayu = new Mahasiswa("2409106001", "Ayu Lestari");
        Mahasiswa bima = new Mahasiswa("2409106002", "Bima Saputra");
        Mahasiswa citra = new Mahasiswa("2409106003", "Citra Dewi");

        System.out.println();
        System.out.println("=== SETELAH TIGA OBJEK DIBUAT ===");
        ayu.perkenalan();
        bima.perkenalan();
        citra.perkenalan();
        System.out.println("Jumlah mahasiswa: " + Mahasiswa.jumlah);

        System.out.println();
        System.out.println("=== NAMA KAMPUS DITULIS LENGKAP ===");
        Mahasiswa.kampus = "Universitas Mulawarman"; // [7] berlaku untuk SEMUA objek
        ayu.perkenalan();
        bima.perkenalan();
        citra.perkenalan();
    }
}

/** Mahasiswa Informatika di Samarinda. */
class Mahasiswa {
    static String kampus = "Unmul"; // [1] atribut kelas: sama untuk semua mahasiswa
    static int jumlah = 0;          // [2] atribut kelas: penghitung objek yang sudah dibuat

    String nim;  // [3] atribut objek: milik masing-masing mahasiswa
    String nama;

    Mahasiswa(String nim, String nama) {
        this.nim = nim;
        this.nama = nama;
        Mahasiswa.jumlah += 1; // [4] mengubah atribut kelas lewat NAMA KELAS
    }

    void perkenalan() {
        System.out.println("Saya " + nama + " (" + nim + ") dari " + Mahasiswa.kampus); // [5]
    }
}
