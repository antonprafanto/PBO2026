/*
 * Solusi Latihan 03 - Melanjutkan Nomor Pesanan dari File
 * Pertemuan 15 - Proyek Terintegrasi
 *
 * Ide penyelesaian:
 * - Jika file transaksi belum ada, nomor berikutnya adalah P001.
 * - Baca semua baris (lewati judul kolom dan baris kosong). Kolom pertama
 *   berisi nomor seperti "P012". Buang huruf P, ubah sisanya menjadi int.
 * - Cari angka TERBESAR (bukan baris terakhir: urutan baris bisa saja acak),
 *   lalu tambah 1 dan format lagi menjadi P + 3 digit.
 * - Jangan membandingkan nomor sebagai TEKS: "P999" > "P1000" menurut abjad!
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03NomorPesanan.java
 */
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Collections;
import java.util.List;

public class Latihan03NomorPesanan {
    private static final String JUDUL = "nomor;pelanggan;no_hp;jumlah_porsi;total\n";

    public static void main(String[] args) throws IOException {
        Path folder = Files.createTempDirectory("latihan03");
        Path path = folder.resolve("transaksi.csv");
        try {
            System.out.println("=== NOMOR PESANAN BERIKUTNYA ===");
            cetak("File belum ada", nomorBerikutnya(path));
            uji(path, "Hanya baris judul", List.of());
            uji(path, "P001, P002, P003", List.of("P001", "P002", "P003"));
            uji(path, "P001, P002, P001 (ganda)", List.of("P001", "P002", "P001"));
            uji(path, "P998, P999, P1000", List.of("P998", "P999", "P1000"));
        } finally {
            Files.deleteIfExists(path);
            Files.deleteIfExists(folder);
        }

        System.out.println();
        System.out.println("=== JEBAKAN: MEMBANDINGKAN SEBAGAI TEKS ===");
        String terbesar = Collections.max(List.of("P998", "P999", "P1000"));
        System.out.println("Nomor terbesar menurut abjad: " + terbesar + " (SALAH)");
    }

    static String nomorBerikutnya(Path path) throws IOException {
        if (!Files.exists(path)) {
            return "P001";
        }
        int terbesar = 0;
        List<String> semuaBaris = Files.readAllLines(path, StandardCharsets.UTF_8);
        for (int i = 1; i < semuaBaris.size(); i++) { // mulai dari 1: lewati judul kolom
            String baris = semuaBaris.get(i);
            if (baris.isEmpty()) {
                continue;
            }
            String nomor = baris.split(";", -1)[0];
            int angka = Integer.parseInt(nomor.substring(1)); // "P012" -> "012" -> 12
            if (angka > terbesar) {
                terbesar = angka;
            }
        }
        return String.format("P%03d", terbesar + 1);
    }

    /** Menulis file transaksi palsu berisi nomor-nomor tertentu, lalu mencetak hasilnya. */
    static void uji(Path path, String keterangan, List<String> daftarNomor) throws IOException {
        String teks = JUDUL;
        for (String nomor : daftarNomor) {
            teks += nomor + ";Pelanggan Uji;080000000000;1;10000\n";
        }
        Files.writeString(path, teks, StandardCharsets.UTF_8);
        cetak(keterangan, nomorBerikutnya(path));
    }

    static void cetak(String keterangan, String nomor) {
        System.out.println(String.format("%-28s-> %s", keterangan, nomor));
    }
}
