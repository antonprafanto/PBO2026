package kedaikita;

/*
 * File RepositoriMenuCSV.java: membaca dan menulis data KedaiKita ke file CSV.
 * Pasangannya, PencatatTransaksiCSV, ada di file PencatatTransaksiCSV.java.
 *
 * - RepositoriMenuCSV    : memuat daftar menu dari file, dan menyimpan stok
 *                          terbaru kembali ke file.
 * - PencatatTransaksiCSV : sebuah PENGAMAT (Observer, Pertemuan 14) yang
 *                          menulis satu baris ke file setiap kali ada pesanan
 *                          berstatus LUNAS. Pesanan tidak perlu diubah sedikit pun.
 *
 * Format CSV yang dipakai memisahkan kolom dengan titik koma (;).
 * Contoh baris menu:  Minuman;M01;Kopi Susu Gula Aren;18000;20;dingin
 *
 * Catatan versi Java: file dibaca dan ditulis dengan kelas Files (UTF-8).
 * Setiap baris dipecah dengan split(";", -1); angka -1 menjaga kolom kosong
 * di akhir baris agar tidak hilang. Versi sederhana ini tidak mengenal tanda
 * kutip ala CSV, jadi isi kolom (misalnya nama) tidak boleh memuat titik koma.
 */

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/** Menghubungkan objek Menu dengan file CSV. */
public class RepositoriMenuCSV {
    public static final String PEMISAH = ";";
    private static final List<String> KOLOM_MENU =
            List.of("jenis", "kode", "nama", "harga", "stok", "ekstra");

    private Path path;

    public RepositoriMenuCSV(Path path) {
        this.path = path;
    }

    /**
     * Membaca file CSV menjadi daftar objek Menu.
     *
     * Isi file yang rusak SELALU dilaporkan sebagai FormatDataException lengkap
     * dengan nomor barisnya; NumberFormatException atau IllegalArgumentException
     * tidak lolos keluar.
     */
    public List<Menu> muat() throws IOException, FormatDataException {
        List<Menu> hasil = new ArrayList<>();
        Set<String> kodeTerpakai = new HashSet<>();
        List<String> semuaBaris = Files.readAllLines(path, StandardCharsets.UTF_8);
        if (semuaBaris.isEmpty()) {
            return hasil; // file kosong: belum ada menu
        }
        for (int i = 1; i < semuaBaris.size(); i++) { // mulai dari 1: lewati baris judul kolom
            int nomorBaris = i + 1; // nomor baris di file dihitung mulai dari 1
            String baris = semuaBaris.get(i);
            if (baris.isEmpty()) { // lewati baris kosong
                continue;
            }
            Menu menu = buatMenu(baris.split(PEMISAH, -1), nomorBaris);
            if (kodeTerpakai.contains(menu.getKode())) {
                throw new FormatDataException("Baris " + nomorBaris + ": kode "
                        + menu.getKode() + " sudah dipakai");
            }
            kodeTerpakai.add(menu.getKode());
            hasil.add(menu);
        }
        return hasil;
    }

    /** Factory kecil: mengubah satu baris CSV menjadi Makanan/Minuman. */
    private static Menu buatMenu(String[] kolom, int nomorBaris) throws FormatDataException {
        if (kolom.length != KOLOM_MENU.size()) {
            throw new FormatDataException("Baris " + nomorBaris + ": harus ada "
                    + KOLOM_MENU.size() + " kolom");
        }
        String jenis = kolom[0];
        String kode = kolom[1];
        String nama = kolom[2];
        String teksHarga = kolom[3];
        String teksStok = kolom[4];
        String ekstra = kolom[5];
        if (!jenis.equals("Makanan") && !jenis.equals("Minuman")) {
            throw new FormatDataException("Baris " + nomorBaris + ": jenis '" + jenis
                    + "' tidak dikenal");
        }
        int harga;
        int stok;
        int levelPedas = 0; // hanya dipakai oleh Makanan
        try {
            harga = Integer.parseInt(teksHarga);
            stok = Integer.parseInt(teksStok);
            if (jenis.equals("Makanan")) {
                levelPedas = Integer.parseInt(ekstra);
            }
        } catch (NumberFormatException e) {
            throw new FormatDataException("Baris " + nomorBaris + ": harga, stok, dan level "
                    + "pedas harus berupa angka");
        }
        try {
            if (jenis.equals("Makanan")) {
                return new Makanan(kode, nama, harga, stok, levelPedas);
            }
            return new Minuman(kode, nama, harga, stok, ekstra.equals("dingin"));
        } catch (IllegalArgumentException e) { // ditolak validasi Menu, misalnya harga 0
            throw new FormatDataException("Baris " + nomorBaris + ": " + e.getMessage());
        }
    }

    /** Kebalikan buatMenu: objek Menu menjadi isi kolom-kolom satu baris CSV. */
    private static List<String> keKolom(Menu menu) {
        String ekstra;
        if (menu instanceof Makanan) {
            ekstra = String.valueOf(((Makanan) menu).getLevelPedas());
        } else if (menu instanceof Minuman) {
            ekstra = ((Minuman) menu).isDingin() ? "dingin" : "panas";
        } else {
            ekstra = "";
        }
        return List.of(menu.getKategori(), menu.getKode(), menu.getNama(),
                String.valueOf(menu.getHarga()), String.valueOf(menu.getStok()), ekstra);
    }

    /** Menulis ulang file CSV dengan data menu terbaru. */
    public void simpan(List<Menu> daftarMenu) throws IOException {
        List<String> semuaBaris = new ArrayList<>();
        semuaBaris.add(String.join(PEMISAH, KOLOM_MENU));
        for (Menu menu : daftarMenu) {
            semuaBaris.add(String.join(PEMISAH, keKolom(menu)));
        }
        // Setiap baris diakhiri "\n" (bukan System.lineSeparator()), sehingga
        // isi file sama persis di Windows, macOS, maupun Linux.
        Files.writeString(path, String.join("\n", semuaBaris) + "\n", StandardCharsets.UTF_8);
    }
}
