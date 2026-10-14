/*
 * Contoh 03 - Try-with-resources: Membuka dan Menutup Sumber Daya dengan Aman
 * Pertemuan 15 - Proyek Terintegrasi
 *
 * File, koneksi printer, atau koneksi database adalah SUMBER DAYA: setelah
 * dibuka, ia wajib ditutup lagi. Try-with-resources menjamin penutupan itu,
 * bahkan ketika terjadi exception di tengah blok:
 *
 *     try (Tipe nama = new Tipe(...)) {
 *         ... memakai nama ...
 *     }   <- di sini nama.close() dipanggil OTOMATIS
 *
 * Syaratnya: kelas Tipe mengimplementasikan interface AutoCloseable.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03TryWithResources.java
 */
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Contoh03TryWithResources {

    public static void main(String[] args) throws IOException {
        System.out.println("=== 1. BLOK SELESAI TANPA ERROR ===");
        try (SambunganPrinter printer = new SambunganPrinter("Printer Lab")) { // [1]
            printer.cetak("Laporan Praktikum");
        } // [2] printer.close() dipanggil otomatis di sini
        System.out.println("Setelah blok selesai");

        System.out.println();
        System.out.println("=== 2. ERROR DI TENGAH BLOK ===");
        try (SambunganPrinter printer = new SambunganPrinter("Printer Lab")) {
            printer.cetak("Halaman 1");
            printer.cetak(""); // [3] melempar IllegalArgumentException
            printer.cetak("Halaman 3"); // tidak pernah dijalankan
        } catch (IllegalArgumentException e) {
            System.out.println("Error ditangkap: " + e.getMessage()); // [4] sudah ditutup
        }

        System.out.println();
        System.out.println("=== 3. DUA SUMBER DAYA SEKALIGUS ===");
        try (SambunganPrinter a = new SambunganPrinter("Printer A");
                SambunganPrinter b = new SambunganPrinter("Printer B")) {
            a.cetak("Sampul");
            b.cetak("Isi");
        }
        System.out.println("Ditutup dengan urutan terbalik: yang terakhir dibuka, pertama ditutup");

        System.out.println();
        System.out.println("=== 4. MENULIS DAN MEMBACA FILE ===");
        Path folder = Files.createTempDirectory("contoh03");
        Path path = folder.resolve("daftar-hadir.txt");
        try {
            try (BufferedWriter penulis = Files.newBufferedWriter(path, StandardCharsets.UTF_8)) { // [5]
                for (String nama : List.of("Ayu", "Bima", "Citra")) {
                    penulis.write(nama + "\n");
                }
            }
            try (BufferedReader pembaca = Files.newBufferedReader(path, StandardCharsets.UTF_8)) {
                String baris = pembaca.readLine();
                while (baris != null) { // [6] readLine() mengembalikan null di akhir file
                    System.out.println("Hadir: " + baris);
                    baris = pembaca.readLine();
                }
            }
        } finally {
            Files.deleteIfExists(path);
            Files.deleteIfExists(folder);
        }
    }
}

/** Sumber daya pura-pura: setelah dibuka, wajib ditutup lagi. */
class SambunganPrinter implements AutoCloseable { // [7]
    private String nama;

    SambunganPrinter(String nama) {
        this.nama = nama;
        System.out.println("  [" + nama + "] sambungan dibuka");
    }

    void cetak(String halaman) {
        if (halaman.isEmpty()) {
            throw new IllegalArgumentException("Halaman kosong tidak bisa dicetak");
        }
        System.out.println("  [" + nama + "] mencetak " + halaman);
    }

    @Override
    public void close() { // [8] SELALU dipanggil saat keluar dari blok try
        System.out.println("  [" + nama + "] sambungan ditutup");
    }
}
