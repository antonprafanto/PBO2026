/*
 * Solusi Latihan 01 - Buku Tamu Pameran
 * Pertemuan 15 - Proyek Terintegrasi
 *
 * Ide penyelesaian:
 * 1. Tulis 3 tamu pertama ke file baru, satu tamu per baris dengan format
 *    "Nama - Asal" (Files.writeString tanpa opsi = menimpa/membuat baru).
 * 2. Tambahkan tamu susulan dengan StandardOpenOption.APPEND, isi lama tetap.
 * 3. Baca semua baris, pecah dengan split(" - "), lalu tampilkan bernomor
 *    sambil menghitung jumlah tamu dan tamu dari Samarinda.
 * File dibuat di folder sementara dan dihapus lagi di blok finally.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan01BukuTamu.java
 */
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.List;

public class Latihan01BukuTamu {

    public static void main(String[] args) throws IOException {
        Path folder = Files.createTempDirectory("latihan01");
        Path path = folder.resolve("buku-tamu.txt");
        int jumlah = 0;
        int dariSamarinda = 0;
        try {
            System.out.println("=== BUKU TAMU PAMERAN PROYEK PBO ===");
            tulisTamu(path, new String[][] {
                {"Ayu Lestari", "Samarinda"},
                {"Bima Saputra", "Balikpapan"},
                {"Citra Dewi", "Samarinda"}}, false);
            System.out.println("3 tamu pertama ditulis ke " + path.getFileName());
            tulisTamu(path, new String[][] {{"Dimas Pratama", "Bontang"}}, true);
            System.out.println("1 tamu susulan ditambahkan");

            System.out.println();
            System.out.println("Isi buku tamu:");
            List<String> semuaBaris = Files.readAllLines(path, StandardCharsets.UTF_8);
            for (String baris : semuaBaris) {
                String[] bagian = baris.split(" - ");
                String nama = bagian[0];
                String asal = bagian[1];
                jumlah++;
                if (asal.equals("Samarinda")) { // bandingkan String dengan equals()
                    dariSamarinda++;
                }
                System.out.println(jumlah + ". " + nama + " (" + asal + ")");
            }
        } finally {
            Files.deleteIfExists(path);
            Files.deleteIfExists(folder);
        }

        System.out.println();
        System.out.println("Jumlah tamu         : " + jumlah);
        System.out.println("Tamu dari Samarinda : " + dariSamarinda);
    }

    /** Menulis tamu ke file. tambahDiAkhir false = file baru, true = append. */
    static void tulisTamu(Path path, String[][] daftar, boolean tambahDiAkhir)
            throws IOException {
        String teks = "";
        for (String[] tamu : daftar) {
            teks += tamu[0] + " - " + tamu[1] + "\n";
        }
        if (tambahDiAkhir) {
            Files.writeString(path, teks, StandardCharsets.UTF_8, StandardOpenOption.APPEND);
        } else {
            Files.writeString(path, teks, StandardCharsets.UTF_8);
        }
    }
}
