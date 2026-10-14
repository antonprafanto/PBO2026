/*
 * Solusi Latihan 02 - Simpan dan Muat Data Pelanggan
 * Pertemuan 15 - Proyek Terintegrasi
 *
 * Ide penyelesaian:
 * - Kelas pelanggan punya dua method "penerjemah":
 *     keKolom()          : objek -> isi kolom satu baris CSV
 *     dariKolom(kolom)   : isi kolom -> objek (static method)
 * - RepositoriPelangganCSV meniru RepositoriMenuCSV di studi kasus:
 *     simpan(daftar) menulis ulang file, muat() membaca kembali menjadi objek.
 * - Bukti data benar-benar tersimpan: ubah poin, simpan, lalu MUAT ULANG dari
 *   file (bukan memakai objek lama di memori).
 *
 * Catatan nama kelas: kelasnya diberi nama PelangganKedai, BUKAN Pelanggan,
 * karena folder java/ pertemuan ini sudah punya kelas Pelanggan (di
 * studi-kasus). VS Code akan protes jika ada dua kelas bernama sama dalam
 * satu folder proyek. Di proyekmu sendiri, nama Pelanggan boleh dipakai.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02SimpanPelanggan.java
 */
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Latihan02SimpanPelanggan {

    public static void main(String[] args) throws IOException {
        Path folder = Files.createTempDirectory("latihan02");
        Path path = folder.resolve("pelanggan.csv");
        try {
            RepositoriPelangganCSV repo = new RepositoriPelangganCSV(path);

            System.out.println("=== SIMPAN 3 PELANGGAN ===");
            repo.simpan(List.of(new PelangganKedai("Budi Santoso", "081234567890", 12),
                    new PelangganKedai("Siti Aminah", "082198765432", 3),
                    new PelangganKedai("Rina Marlina", "085312345678", 0)));
            System.out.println("Isi " + path.getFileName() + ":");
            System.out.print(Files.readString(path, StandardCharsets.UTF_8));

            System.out.println();
            System.out.println("=== MUAT KEMBALI ===");
            List<PelangganKedai> daftar = repo.muat();
            tampilkan(daftar);

            System.out.println();
            System.out.println("=== SITI BERTRANSAKSI (+5 POIN), LALU DISIMPAN ULANG ===");
            daftar.get(1).tambahPoin(5);
            repo.simpan(daftar);
            List<PelangganKedai> daftarBaru = repo.muat(); // objek-objek BARU hasil membaca file
            System.out.println("Setelah dimuat ulang dari file:");
            tampilkan(daftarBaru);
            int total = 0;
            for (PelangganKedai pelanggan : daftarBaru) {
                total += pelanggan.getPoin();
            }
            System.out.println("Total poin semua pelanggan: " + total);
        } finally {
            Files.deleteIfExists(path);
            Files.deleteIfExists(folder);
        }
    }

    static void tampilkan(List<PelangganKedai> daftar) {
        for (PelangganKedai pelanggan : daftar) {
            System.out.println(pelanggan);
        }
    }
}

/** Pelanggan dengan poin. Poin hanya bertambah lewat tambahPoin(). */
class PelangganKedai {
    private String nama;
    private String noHp;
    private int poin;

    PelangganKedai(String nama, String noHp, int poin) {
        this.nama = nama;
        this.noHp = noHp;
        this.poin = poin;
    }

    int getPoin() {
        return poin;
    }

    void tambahPoin(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Poin yang ditambahkan harus lebih dari 0");
        }
        poin += jumlah;
    }

    List<String> keKolom() {
        return List.of(nama, noHp, String.valueOf(poin));
    }

    static PelangganKedai dariKolom(String[] kolom) {
        if (kolom.length != 3) {
            throw new IllegalArgumentException("Harus ada 3 kolom");
        }
        return new PelangganKedai(kolom[0], kolom[1], Integer.parseInt(kolom[2]));
    }

    @Override
    public String toString() {
        return nama + " (" + noHp + ") - " + poin + " poin";
    }
}

/** Menghubungkan objek PelangganKedai dengan file CSV. */
class RepositoriPelangganCSV {
    private static final String PEMISAH = ";";
    private Path path;

    RepositoriPelangganCSV(Path path) {
        this.path = path;
    }

    void simpan(List<PelangganKedai> daftar) throws IOException {
        List<String> semuaBaris = new ArrayList<>();
        semuaBaris.add("nama;no_hp;poin");
        for (PelangganKedai pelanggan : daftar) {
            semuaBaris.add(String.join(PEMISAH, pelanggan.keKolom()));
        }
        Files.writeString(path, String.join("\n", semuaBaris) + "\n", StandardCharsets.UTF_8);
    }

    List<PelangganKedai> muat() throws IOException {
        List<PelangganKedai> hasil = new ArrayList<>();
        List<String> semuaBaris = Files.readAllLines(path, StandardCharsets.UTF_8);
        for (int i = 1; i < semuaBaris.size(); i++) { // mulai dari 1: lewati judul kolom
            String baris = semuaBaris.get(i);
            if (!baris.isEmpty()) {
                hasil.add(PelangganKedai.dariKolom(baris.split(PEMISAH, -1)));
            }
        }
        return hasil;
    }
}
