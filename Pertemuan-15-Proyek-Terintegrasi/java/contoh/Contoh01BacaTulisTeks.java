/*
 * Contoh 01 - Menulis dan Membaca File Teks
 * Pertemuan 15 - Proyek Terintegrasi
 *
 * Kelas Files (paket java.nio.file) menyediakan method siap pakai:
 * - Files.writeString(path, teks, charset)          : menulis (isi lama DITIMPA)
 * - Files.writeString(..., StandardOpenOption.APPEND): menambah di akhir file
 * - Files.readString(path, charset)                 : membaca seluruh isi
 * - Files.readAllLines(path, charset)               : membaca per baris (List)
 * Setiap method di atas membuka DAN menutup file sendiri.
 *
 * Semua file dibuat di folder sementara (Files.createTempDirectory) lalu
 * dihapus di blok finally, jadi tidak ada file yang tertinggal.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01BacaTulisTeks.java
 */
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.List;

public class Contoh01BacaTulisTeks {

    public static void main(String[] args) throws IOException { // [1]
        Path folder = Files.createTempDirectory("contoh01"); // [2] folder sementara
        Path path = folder.resolve("jadwal-piket.txt"); // [3] folder + nama file
        try {
            System.out.println("=== 1. MENULIS FILE BARU ===");
            Files.writeString(path, "Senin: Ayu\nSelasa: Bima\n", StandardCharsets.UTF_8); // [4]
            System.out.println("File " + path.getFileName() + " sudah ada? "
                    + (Files.exists(path) ? "ya" : "tidak"));

            System.out.println();
            System.out.println("=== 2. MENAMBAH DI AKHIR FILE ===");
            Files.writeString(path, "Rabu: Citra\n", StandardCharsets.UTF_8,
                    StandardOpenOption.APPEND); // [5]
            System.out.println("Satu baris ditambahkan di akhir file");

            System.out.println();
            System.out.println("=== 3. MEMBACA SELURUH ISI ===");
            String isi = Files.readString(path, StandardCharsets.UTF_8); // [6]
            System.out.print(isi); // isi sudah diakhiri "\n", jadi pakai print

            System.out.println();
            System.out.println("=== 4. MEMBACA BARIS DEMI BARIS ===");
            List<String> semuaBaris = Files.readAllLines(path, StandardCharsets.UTF_8); // [7]
            for (int i = 0; i < semuaBaris.size(); i++) {
                String[] bagian = semuaBaris.get(i).split(": "); // "\n" sudah dibuang
                System.out.println((i + 1) + ". " + bagian[1] + " piket hari " + bagian[0]);
            }

            System.out.println();
            System.out.println("=== 5. MENIMPA ISI FILE ===");
            Files.writeString(path, "Kamis: Dimas\n", StandardCharsets.UTF_8);
            System.out.print(Files.readString(path, StandardCharsets.UTF_8));

            System.out.println();
            System.out.println("=== 6. MEMBACA FILE YANG TIDAK ADA ===");
            try {
                System.out.print(Files.readString(folder.resolve("jadwal-lama.txt"),
                        StandardCharsets.UTF_8));
            } catch (NoSuchFileException e) { // [8]
                System.out.println("File jadwal-lama.txt tidak ditemukan, lanjut dengan data kosong");
            }
        } finally { // [9] bersih-bersih, apa pun yang terjadi
            Files.deleteIfExists(path);
            Files.deleteIfExists(folder);
        }

        System.out.println();
        String dihapus = Files.exists(folder) ? "tidak" : "ya";
        System.out.println("Folder sementara sudah dihapus? " + dihapus);
    }
}
