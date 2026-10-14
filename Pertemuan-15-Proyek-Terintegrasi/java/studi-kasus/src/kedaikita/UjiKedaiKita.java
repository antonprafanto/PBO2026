package kedaikita;

/*
 * File UjiKedaiKita.java: unit test untuk KedaiKita (Pertemuan 15).
 *
 * Unit test adalah kode kecil yang memeriksa kode kita secara otomatis.
 * Versi Python memakai modul unittest bawaan. JDK tidak membawa pustaka unit
 * test (JUnit harus diunduh terpisah), jadi di sini kita membuat "mini
 * framework" sendiri yang cukup untuk belajar:
 * - setiap pengujian adalah satu method uji...() yang mengembalikan true
 *   (lulus) atau false (gagal),
 * - periksa() mencetak [LULUS] atau [GAGAL] untuk setiap pengujian,
 * - harusMelempar() memeriksa bahwa sebuah kode MELEMPAR exception tertentu.
 * Jika ada pengujian yang gagal, program keluar dengan kode 1.
 *
 * Cara menjalankan (dari dalam folder studi-kasus):
 *     uji.bat (Windows)  atau  ./uji.sh (macOS/Linux)
 * Kedua skrip itu menjalankan dua perintah berikut:
 *     javac -d out src/kedaikita/*.java
 *     java -cp out kedaikita.UjiKedaiKita
 */

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class UjiKedaiKita {
    private static int jumlahLulus = 0;
    private static int jumlahGagal = 0;

    // Objek uji kelompok Pesanan, dibuat ulang oleh siapkanPesanan().
    private static Minuman kopi;
    private static Makanan nasi;
    private static Pelanggan pelanggan;
    private static Pesanan pesanan;

    public static void main(String[] args) {
        System.out.println("=== UNIT TEST KEDAIKITA ===");
        // Kelompok Menu
        uji("Menu: harga harus positif", UjiKedaiKita::ujiHargaHarusPositif);
        uji("Menu: level pedas maksimal lima", UjiKedaiKita::ujiLevelPedasMaksimalLima);
        uji("Menu: stok tidak berubah jika gagal",
                UjiKedaiKita::ujiStokTidakBerubahJikaGagal);
        // Kelompok Pesanan
        uji("Pesanan: subtotal", UjiKedaiKita::ujiSubtotal);
        uji("Pesanan: total sudah termasuk pajak 10 persen",
                UjiKedaiKita::ujiTotalSudahTermasukPajak10Persen);
        uji("Pesanan: stok berkurang setelah dipesan",
                UjiKedaiKita::ujiStokBerkurangSetelahDipesan);
        uji("Pesanan: diskon persen", UjiKedaiKita::ujiDiskonPersen);
        uji("Pesanan: happy hour hanya untuk minuman",
                UjiKedaiKita::ujiHappyHourHanyaUntukMinuman);
        uji("Pesanan: diskon member butuh 10 poin", UjiKedaiKita::ujiDiskonMemberButuh10Poin);
        uji("Pesanan: bayar gagal, status tetap BARU",
                UjiKedaiKita::ujiBayarGagalStatusTetapBaru);
        uji("Pesanan: struk memuat total", UjiKedaiKita::ujiStrukMemuatTotal);
        // Kelompok PembayaranFactory
        uji("PembayaranFactory: jenis tidak dikenal", UjiKedaiKita::ujiJenisTidakDikenal);
        uji("PembayaranFactory: huruf besar/kecil tidak masalah",
                UjiKedaiKita::ujiHurufBesarKecilTidakMasalah);
        // Kelompok RepositoriMenuCSV
        uji("RepositoriMenuCSV: simpan lalu muat kembali",
                UjiKedaiKita::ujiSimpanLaluMuatKembali);
        uji("RepositoriMenuCSV: file rusak ditolak", UjiKedaiKita::ujiFileRusakDitolak);
        uji("RepositoriMenuCSV: kode ganda ditolak", UjiKedaiKita::ujiKodeGandaDitolak);

        System.out.println();
        System.out.println("Hasil: " + jumlahLulus + " lulus, " + jumlahGagal + " gagal");
        if (jumlahGagal > 0) {
            System.exit(1); // kode keluar 1 menandakan ada pengujian yang gagal
        }
    }

    // ===================================================== kelompok: Menu

    private static boolean ujiHargaHarusPositif() {
        return harusMelempar(IllegalArgumentException.class,
                () -> new Minuman("X01", "Menu Uji", 0, 5));
    }

    private static boolean ujiLevelPedasMaksimalLima() {
        return harusMelempar(IllegalArgumentException.class,
                () -> new Makanan("X02", "Menu Uji", 10000, 5, 6));
    }

    private static boolean ujiStokTidakBerubahJikaGagal() {
        Makanan menu = new Makanan("X03", "Menu Uji", 10000, 3);
        boolean melempar = harusMelempar(StokTidakCukupException.class,
                () -> menu.kurangiStok(5));
        return melempar && menu.getStok() == 3;
    }

    // ================================================== kelompok: Pesanan

    /** Dijalankan ulang sebelum SETIAP uji Pesanan, agar tiap uji mulai dari nol. */
    private static void siapkanPesanan() throws KedaiException {
        kopi = new Minuman("M01", "Kopi Susu Gula Aren", 18000, 10);
        nasi = new Makanan("M03", "Nasi Goreng Kampung", 25000, 10, 2);
        pelanggan = new Pelanggan("Uji Coba", "080000000000");
        pesanan = new Pesanan(pelanggan);
        pesanan.tambahItem(kopi, 2);
        pesanan.tambahItem(nasi, 1);
    }

    private static boolean ujiSubtotal() throws KedaiException {
        siapkanPesanan();
        return pesanan.hitungSubtotal() == 61000;
    }

    private static boolean ujiTotalSudahTermasukPajak10Persen() throws KedaiException {
        siapkanPesanan();
        return pesanan.hitungTotal() == 67100;
    }

    private static boolean ujiStokBerkurangSetelahDipesan() throws KedaiException {
        siapkanPesanan();
        return kopi.getStok() == 8;
    }

    private static boolean ujiDiskonPersen() throws KedaiException {
        siapkanPesanan();
        pesanan.aturDiskon(new DiskonPersen(10));
        return pesanan.hitungPotongan() == 6100;
    }

    private static boolean ujiHappyHourHanyaUntukMinuman() throws KedaiException {
        siapkanPesanan();
        pesanan.aturDiskon(new DiskonHappyHour());
        return pesanan.hitungPotongan() == 7200;
    }

    private static boolean ujiDiskonMemberButuh10Poin() throws KedaiException {
        siapkanPesanan();
        pesanan.aturDiskon(new DiskonMember());
        boolean belumDapat = pesanan.hitungPotongan() == 0;
        pelanggan.tambahPoin(10);
        return belumDapat && pesanan.hitungPotongan() == 6100;
    }

    private static boolean ujiBayarGagalStatusTetapBaru() throws KedaiException {
        siapkanPesanan();
        PrintStream layarAsli = System.out;
        boolean melempar;
        // System.out dialihkan sementara ke "layar bisu" agar print dari bayar()
        // tidak mengotori hasil pengujian.
        try (PrintStream layarBisu = new PrintStream(new ByteArrayOutputStream())) {
            System.setOut(layarBisu);
            melempar = harusMelempar(PembayaranGagalException.class,
                    () -> pesanan.bayar(new PembayaranTunai(1000)));
        } finally {
            System.setOut(layarAsli); // kembalikan layar seperti semula
        }
        return melempar && pesanan.getStatus().equals("BARU");
    }

    private static boolean ujiStrukMemuatTotal() throws KedaiException {
        siapkanPesanan();
        String teks = new StrukPesanan(pesanan).buatTeks();
        return teks.contains("TOTAL") && teks.contains("Rp67.100");
    }

    // ======================================== kelompok: PembayaranFactory

    private static boolean ujiJenisTidakDikenal() {
        return harusMelempar(IllegalArgumentException.class,
                () -> PembayaranFactory.buat("bitcoin", 0, ""));
    }

    private static boolean ujiHurufBesarKecilTidakMasalah() {
        return PembayaranFactory.buat("QRIS", 0, "").namaMetode().equals("QRIS");
    }

    // ======================================== kelompok: RepositoriMenuCSV

    private static boolean ujiSimpanLaluMuatKembali() throws Exception {
        Path folder = Files.createTempDirectory("kedaikita-uji");
        Path path = folder.resolve("menu.csv");
        List<Menu> hasil;
        try {
            RepositoriMenuCSV repo = new RepositoriMenuCSV(path);
            repo.simpan(List.of(new Minuman("M01", "Kopi", 18000, 7, false),
                    new Makanan("M02", "Nasi", 25000, 3, 4)));
            hasil = repo.muat();
        } finally {
            hapusFolderUji(folder, path);
        }
        return hasil.size() == 2
                && hasil.get(0).getStok() == 7
                && !((Minuman) hasil.get(0)).isDingin()
                && ((Makanan) hasil.get(1)).getLevelPedas() == 4;
    }

    private static boolean ujiFileRusakDitolak() throws Exception {
        Path folder = Files.createTempDirectory("kedaikita-uji");
        Path path = folder.resolve("menu.csv");
        try {
            Files.writeString(path, "jenis;kode;nama;harga;stok;ekstra\n"
                    + "Makanan;M01;Nasi;mahal;3;0\n", StandardCharsets.UTF_8);
            return harusMelempar(FormatDataException.class,
                    () -> new RepositoriMenuCSV(path).muat());
        } finally {
            hapusFolderUji(folder, path);
        }
    }

    private static boolean ujiKodeGandaDitolak() throws Exception {
        Path folder = Files.createTempDirectory("kedaikita-uji");
        Path path = folder.resolve("menu.csv");
        try {
            Files.writeString(path, "jenis;kode;nama;harga;stok;ekstra\n"
                    + "Minuman;M01;Kopi;18000;5;dingin\n"
                    + "Makanan;M01;Nasi;25000;3;0\n", StandardCharsets.UTF_8);
            return harusMelempar(FormatDataException.class,
                    () -> new RepositoriMenuCSV(path).muat());
        } finally {
            hapusFolderUji(folder, path);
        }
    }

    /** Menghapus file dan folder sementara milik satu pengujian. */
    private static void hapusFolderUji(Path folder, Path file) throws IOException {
        Files.deleteIfExists(file);
        Files.deleteIfExists(folder);
    }

    // ================================================== alat bantu uji

    /** Isi satu pengujian: mengembalikan true jika semua pemeriksaannya benar. */
    @FunctionalInterface
    private interface KasusUji {
        boolean jalankan() throws Exception;
    }

    /** Potongan kode yang diharapkan MELEMPAR exception. */
    @FunctionalInterface
    private interface KodeUji {
        void jalankan() throws Exception;
    }

    /** Menjalankan satu pengujian. Exception yang tidak diduga dihitung GAGAL. */
    private static void uji(String nama, KasusUji kasus) {
        try {
            periksa(nama, kasus.jalankan());
        } catch (Exception e) {
            periksa(nama + " (exception tak terduga: " + e + ")", false);
        }
    }

    /** Mencetak hasil satu pengujian, lalu menghitung jumlah lulus dan gagal. */
    private static void periksa(String nama, boolean kondisi) {
        if (kondisi) {
            jumlahLulus++;
            System.out.println("[LULUS] " + nama);
        } else {
            jumlahGagal++;
            System.out.println("[GAGAL] " + nama);
        }
    }

    /**
     * true jika kode MELEMPAR exception bertipe jenis (atau turunannya),
     * seperti assertRaises di unittest Python.
     */
    private static boolean harusMelempar(Class<? extends Exception> jenis, KodeUji kode) {
        try {
            kode.jalankan();
        } catch (Exception e) {
            return jenis.isInstance(e); // isInstance = versi "instanceof" untuk objek Class
        }
        return false; // tidak ada exception sama sekali: pengujian gagal
    }
}
