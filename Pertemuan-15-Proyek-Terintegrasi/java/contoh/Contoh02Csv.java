/*
 * Contoh 02 - Menyimpan dan Memuat Objek dengan File CSV
 * Pertemuan 15 - Proyek Terintegrasi
 *
 * CSV (Comma-Separated Values) adalah file teks berbentuk tabel: satu baris =
 * satu data, kolom dipisahkan tanda tertentu. Di sini pemisahnya TITIK KOMA,
 * karena isi kolom (misalnya asal "Samarinda, Kaltim") boleh mengandung koma.
 *
 * Java tidak punya modul CSV bawaan. Untuk CSV sederhana cukup:
 * - menulis : String.join(";", kolom)
 * - membaca : baris.split(";", -1)   (-1 agar kolom kosong di akhir tidak hilang)
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02Csv.java
 */
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;

public class Contoh02Csv {
    private static final String PEMISAH = ";";
    private static final List<String> JUDUL_KOLOM = List.of("nim", "nama", "asal", "sks", "catatan");

    public static void main(String[] args) throws IOException {
        List<Mahasiswa> dataAwal = List.of(
                new Mahasiswa("2409106001", "Ayu Lestari", "Samarinda, Kaltim", 20, "ketua kelas"),
                new Mahasiswa("2409106002", "Bima Saputra", "Balikpapan, Kaltim", 18, ""),
                new Mahasiswa("2409106003", "Citra Dewi", "Tenggarong, Kukar", 22, "asisten lab"));
        Path folder = Files.createTempDirectory("contoh02");
        Path path = folder.resolve("mahasiswa.csv");
        try {
            System.out.println("=== 1. MENYIMPAN 3 OBJEK KE CSV ===");
            simpan(path, dataAwal);
            System.out.println("Tersimpan di " + path.getFileName());

            System.out.println();
            System.out.println("=== 2. ISI FILE APA ADANYA ===");
            System.out.print(Files.readString(path, StandardCharsets.UTF_8));

            System.out.println();
            System.out.println("=== 3. MEMUAT KEMBALI MENJADI OBJEK ===");
            List<Mahasiswa> daftar = muat(path);
            int totalSks = 0;
            for (Mahasiswa mhs : daftar) {
                String catatan = mhs.catatan.isEmpty() ? "-" : mhs.catatan; // kolom kosong
                // %3s (bukan %3d) agar angka tidak terpengaruh pengaturan bahasa komputer
                System.out.println(String.format("%-14s%-20s%3s sks  (%s)",
                        mhs.nama, mhs.asal, mhs.sks, catatan));
                totalSks += mhs.sks;
            }
            System.out.println("Total " + daftar.size() + " mahasiswa, " + totalSks + " sks");

            System.out.println();
            System.out.println("=== 4. FILE DENGAN BARIS RUSAK ===");
            Files.writeString(path, "2409106004;Dimas Pratama;Bontang;dua puluh;\n"
                    + "2409106005;Eka Putri\n", StandardCharsets.UTF_8, StandardOpenOption.APPEND);
            daftar = muat(path);
            System.out.println("Berhasil dimuat: " + daftar.size() + " mahasiswa");
        } finally {
            Files.deleteIfExists(path);
            Files.deleteIfExists(folder);
        }
    }

    static void simpan(Path path, List<Mahasiswa> daftar) throws IOException {
        List<String> semuaBaris = new ArrayList<>();
        semuaBaris.add(String.join(PEMISAH, JUDUL_KOLOM)); // baris pertama: judul kolom
        for (Mahasiswa mhs : daftar) {
            semuaBaris.add(String.join(PEMISAH, mhs.keKolom())); // [1]
        }
        // [2] Setiap baris diakhiri "\n" agar isi file sama di Windows, macOS, dan Linux.
        Files.writeString(path, String.join("\n", semuaBaris) + "\n", StandardCharsets.UTF_8);
    }

    static List<Mahasiswa> muat(Path path) throws IOException {
        List<Mahasiswa> hasil = new ArrayList<>();
        List<String> semuaBaris = Files.readAllLines(path, StandardCharsets.UTF_8);
        for (int i = 1; i < semuaBaris.size(); i++) { // [3] mulai dari 1: lewati judul kolom
            int nomorBaris = i + 1;
            String[] kolom = semuaBaris.get(i).split(PEMISAH, -1); // [4]
            try {
                hasil.add(Mahasiswa.dariKolom(kolom));
            } catch (IllegalArgumentException e) { // [5] termasuk NumberFormatException
                System.out.println("  Baris " + nomorBaris + " dilewati: data tidak valid");
            }
        }
        return hasil;
    }
}

/** Data mahasiswa yang akan disimpan ke file CSV (field sengaja dibuat sederhana). */
class Mahasiswa {
    String nim;
    String nama;
    String asal;
    int sks;
    String catatan;

    Mahasiswa(String nim, String nama, String asal, int sks, String catatan) {
        this.nim = nim;
        this.nama = nama;
        this.asal = asal;
        this.sks = sks;
        this.catatan = catatan;
    }

    /** Objek -> isi kolom-kolom satu baris CSV. */
    List<String> keKolom() {
        return List.of(nim, nama, asal, String.valueOf(sks), catatan);
    }

    /** Isi kolom satu baris CSV -> objek. Melempar IllegalArgumentException jika rusak. */
    static Mahasiswa dariKolom(String[] kolom) {
        if (kolom.length != 5) {
            throw new IllegalArgumentException("Harus ada 5 kolom");
        }
        return new Mahasiswa(kolom[0], kolom[1], kolom[2], Integer.parseInt(kolom[3]), kolom[4]);
    }
}
