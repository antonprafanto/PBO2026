/*
 * KedaiKita - Pertemuan 12: Koleksi dan Generics
 *
 * Yang baru dibanding Pertemuan 11:
 * - Kedai menyimpan menu di Map (kode -> Menu) dan bisa memfilter,
 *   mengurutkan, serta mengambil kategori unik (Set).
 * - Menu punya equals(), hashCode(), dan compareTo() (kesamaan dan urutan alami).
 * - Pasangan.java: kelas generik Pasangan<A, B>.
 * - LaporanPenjualan.java: LaporanPenjualan yang merangkum penjualan hari ini.
 *
 * Cara menjalankan (dari dalam folder studi-kasus):
 *     javac *.java
 *     java Main
 */

import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Main {

    /** Membuat kedai beserta lima menu awalnya. */
    public static Kedai siapkanKedai() {
        Kedai kedai = new Kedai("KedaiKita");
        kedai.tambahMenu(new Minuman("M01", "Kopi Susu Gula Aren", 18000, 20, true));
        kedai.tambahMenu(new Minuman("M02", "Es Teh Manis", 8000, 30, true));
        kedai.tambahMenu(new Makanan("M03", "Nasi Goreng Kampung", 25000, 15, 2));
        kedai.tambahMenu(new Makanan("M04", "Mie Goreng Jawa", 23000, 10, 1));
        kedai.tambahMenu(new Makanan("M05", "Pisang Goreng Keju", 15000, 12, 0));
        return kedai;
    }

    public static String yaTidak(boolean nilai) {
        return nilai ? "ya" : "tidak";
    }

    /** Membuat pesanan, mengisi item (kode, jumlah), lalu membayarnya. */
    public static Pesanan transaksi(Kedai kedai, Pelanggan pelanggan,
            List<Pasangan<String, Integer>> daftarBeli, Pembayaran pembayaran) {
        Pesanan pesanan = kedai.buatPesanan(pelanggan);
        try {
            for (Pasangan<String, Integer> beli : daftarBeli) {
                pesanan.tambahItem(kedai.cariMenu(beli.getPertama()), beli.getKedua());
            }
            pesanan.bayar(pembayaran);
        } catch (KedaiException e) {
            System.out.println("  [GAGAL] " + e.getMessage());
        }
        return pesanan;
    }

    // main meneruskan KedaiException (throws): di bagian KESAMAAN OBJEK,
    // cariMenu("M01") sengaja dipanggil di luar try karena kita yakin M01 terdaftar.
    public static void main(String[] args) throws KedaiException {
        Kedai kedai = siapkanKedai();
        kedai.cetak();
        System.out.println();

        System.out.println("=== KATEGORI UNIK ===");
        System.out.println(String.join(", ", kedai.daftarKategori()));
        System.out.println();

        System.out.println("=== FILTER: MINUMAN SAJA ===");
        for (Menu menu : kedai.menuBerdasarkanKategori("Minuman")) {
            System.out.println(menu);
        }
        System.out.println();

        System.out.println("=== URUT HARGA TERMURAH (urutan alami) ===");
        List<Menu> urutHarga = kedai.semuaMenu();
        Collections.sort(urutHarga); // memakai compareTo() milik Menu
        for (Menu menu : urutHarga) {
            System.out.println(String.format("%10s  %s", Rupiah.format(menu.getHarga()),
                    menu.getNama()));
        }
        System.out.println();

        System.out.println("=== URUT NAMA A-Z (kunci pengurutan) ===");
        List<Menu> urutNama = kedai.semuaMenu();
        urutNama.sort(Comparator.comparing(m -> m.getNama())); // lambda: kunci pengurutan
        for (Menu menu : urutNama) {
            System.out.println(menu.getKode() + "  " + menu.getNama());
        }
        System.out.println();

        System.out.println("=== KODE GANDA DITOLAK ===");
        try {
            kedai.tambahMenu(new Minuman("M01", "Kopi Hitam", 10000, 5));
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        System.out.println("Jumlah menu tetap " + kedai.jumlahMenu());
        System.out.println();

        System.out.println("=== KESAMAAN OBJEK ===");
        Menu kopiA = kedai.cariMenu("M01");
        Menu kopiB = new Minuman("M01", "Kopi Susu Gula Aren", 18000, 20);
        System.out.println("Sama isinya (kode sama)? " + yaTidak(kopiA.equals(kopiB)));
        System.out.println("Objek yang sama persis? " + yaTidak(kopiA == kopiB));
        System.out.println();

        System.out.println("=== TRANSAKSI HARI INI ===");
        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        Pelanggan siti = new Pelanggan("Siti Aminah", "082198765432");
        Pelanggan rina = new Pelanggan("Rina Marlina", "085312345678");
        Pelanggan andi = new Pelanggan("Andi Wijaya", "087711223344");
        transaksi(kedai, budi, List.of(new Pasangan<>("M01", 2), new Pasangan<>("M03", 1)),
                new PembayaranTunai(100000));
        transaksi(kedai, siti, List.of(new Pasangan<>("M02", 2), new Pasangan<>("M05", 1)),
                new PembayaranKartu("BNI"));
        transaksi(kedai, rina, List.of(new Pasangan<>("M01", 1), new Pasangan<>("M04", 1)),
                new PembayaranQRIS(100000));
        transaksi(kedai, budi, List.of(new Pasangan<>("M01", 1), new Pasangan<>("M02", 2)),
                new PembayaranTunai(50000));
        transaksi(kedai, andi, List.of(new Pasangan<>("M03", 1)), new PembayaranQRIS(10000));
        System.out.println();

        System.out.println("Pesanan tercatat: " + kedai.jumlahPesanan());
        LaporanPenjualan laporan = new LaporanPenjualan(kedai.riwayatPesanan());
        laporan.cetak();
    }
}
