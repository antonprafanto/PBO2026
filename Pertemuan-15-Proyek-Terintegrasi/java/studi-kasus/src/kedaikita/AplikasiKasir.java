package kedaikita;

/*
 * File AplikasiKasir.java: kelas AplikasiKasir, antarmuka teks (CLI) kasir KedaiKita.
 *
 * Ada dua cara menjalankan:
 * - jalankan()     : mode interaktif, kasir mengetik pilihan lewat keyboard.
 *                    Stok disimpan ke data/menu.csv, transaksi ke data/transaksi.csv.
 * - jalankanDemo() : mode demo tanpa input, selalu menghasilkan output yang sama.
 *                    Memakai file data/demo-menu.csv dan data/demo-transaksi.csv.
 */

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.NoSuchElementException;
import java.util.Scanner;
import java.util.function.Supplier;

/** Menghubungkan pengguna (keyboard & layar) dengan LayananKasir. */
public class AplikasiKasir {
    // Pilihan diskon -> "resep" pembuat objek Diskon. TanpaDiskon::new artinya
    // "panggil konstruktor TanpaDiskon", dijalankan setiap kali get() dipanggil.
    private static final Map<String, Supplier<Diskon>> PILIHAN_DISKON = Map.of(
            "1", TanpaDiskon::new,
            "2", DiskonMember::new,
            "3", DiskonHappyHour::new);

    private Path folderData;
    private Scanner masukan; // satu Scanner untuk semua input dari keyboard

    public AplikasiKasir(Path folderData) {
        this.folderData = folderData;
        this.masukan = new Scanner(System.in);
    }

    // ------------------------------------------------------------ persiapan
    private LayananKasir siapkan(Path fileMenu, PencatatTransaksiCSV pencatat)
            throws IOException, FormatDataException {
        Kedai kedai = new Kedai("KedaiKita", new PenyimpananMemori());
        for (Menu menu : new RepositoriMenuCSV(fileMenu).muat()) {
            kedai.tambahMenu(menu);
        }
        System.out.println("Memuat menu dari data/" + fileMenu.getFileName() + ": "
                + kedai.jumlahMenu() + " menu");
        return new LayananKasir(kedai, List.of(pencatat));
    }

    // ------------------------------------------------------------ mode demo
    // Meneruskan KedaiException (throws): di skenario demo ini kita yakin datanya
    // valid, jadi hanya kesalahan yang memang disengaja yang ditangkap di sini.
    public void jalankanDemo() throws KedaiException, IOException {
        System.out.println("=== MODE DEMO KASIR KEDAIKITA ===");
        Path fileTransaksi = folderData.resolve("demo-transaksi.csv");
        PencatatTransaksiCSV pencatat = new PencatatTransaksiCSV(fileTransaksi, true); // mulai baru
        LayananKasir layanan = siapkan(folderData.resolve("menu_awal.csv"), pencatat);
        layanan.getKedai().cetak();
        System.out.println();

        System.out.println("--- Transaksi 1: Budi, tanpa diskon, bayar tunai ---");
        Pelanggan budi = layanan.pelanggan("Budi Santoso", "081234567890");
        Pesanan pesanan1 = layanan.buatPesanan(budi);
        layanan.tambahItem(pesanan1, "M01", 2);
        layanan.tambahItem(pesanan1, "M03", 1);
        layanan.bayar(pesanan1, "tunai", 100000, "");
        new StrukPesanan(pesanan1).cetak();
        System.out.println();

        System.out.println("--- Transaksi 2: Siti, Happy Hour, QRIS gagal lalu kartu ---");
        Pelanggan siti = layanan.pelanggan("Siti Aminah", "082198765432");
        Pesanan pesanan2 = layanan.buatPesanan(siti);
        layanan.tambahItem(pesanan2, "M02", 2);
        layanan.tambahItem(pesanan2, "M05", 1);
        pesanan2.aturDiskon(new DiskonHappyHour());
        try {
            layanan.bayar(pesanan2, "qris", 20000, "");
        } catch (KedaiException e) {
            System.out.println("[GAGAL] " + e.getMessage());
        }
        layanan.bayar(pesanan2, "kartu", 0, "BNI");
        new StrukPesanan(pesanan2).cetak();
        System.out.println();

        System.out.println("--- Transaksi 3: input keliru ditangani dengan rapi ---");
        Pelanggan rina = layanan.pelanggan("Rina Marlina", "085312345678");
        Pesanan pesanan3 = layanan.buatPesanan(rina);
        List<Pasangan<String, Integer>> daftarBeli = List.of(new Pasangan<>("M99", 1),
                new Pasangan<>("M04", 100), new Pasangan<>("M06", 2));
        for (Pasangan<String, Integer> beli : daftarBeli) {
            String kode = beli.getPertama();
            int jumlah = beli.getKedua();
            try {
                Menu menu = layanan.tambahItem(pesanan3, kode, jumlah);
                System.out.println("  -> " + jumlah + " x " + menu.getNama() + " ditambahkan");
            } catch (KedaiException e) {
                System.out.println("  [GAGAL] " + e.getMessage());
            }
        }
        layanan.bayar(pesanan3, "qris", 100000, "");
        System.out.println();

        System.out.println("=== LAPORAN SESI INI ===");
        layanan.laporan().cetak();
        System.out.println();

        System.out.println("=== RIWAYAT DARI FILE data/demo-transaksi.csv ===");
        for (String[] kolom : pencatat.bacaSemua()) {
            System.out.println(String.join(" | ", kolom));
        }
        System.out.println();

        Path fileMenu = folderData.resolve("demo-menu.csv");
        new RepositoriMenuCSV(fileMenu).simpan(layanan.getKedai().semuaMenu());
        System.out.println("Stok terbaru disimpan ke data/" + fileMenu.getFileName()
                + ". Isinya:");
        System.out.print(Files.readString(fileMenu, StandardCharsets.UTF_8));
    }

    // ------------------------------------------------------ mode interaktif
    // Meneruskan KedaiException (misalnya FormatDataException karena file menu
    // rusak) dan IOException ke Main, yang menampilkannya dengan sopan.
    public void jalankan() throws KedaiException, IOException {
        Path fileMenu = folderData.resolve("menu.csv");
        Path sumber = Files.exists(fileMenu) ? fileMenu : folderData.resolve("menu_awal.csv");
        PencatatTransaksiCSV pencatat = new PencatatTransaksiCSV(
                folderData.resolve("transaksi.csv"));
        LayananKasir layanan = siapkan(sumber, pencatat);
        System.out.println("Selamat datang di Kasir KedaiKita!");
        try {
            while (true) {
                System.out.println();
                System.out.println("=========== MENU UTAMA ===========");
                System.out.println("1. Lihat daftar menu");
                System.out.println("2. Buat pesanan baru");
                System.out.println("3. Laporan penjualan sesi ini");
                System.out.println("4. Riwayat transaksi (dari file)");
                System.out.println("0. Simpan dan keluar");
                String pilihan = tanya("Pilihan: ");
                if (pilihan.equals("1")) {
                    layanan.getKedai().cetak();
                } else if (pilihan.equals("2")) {
                    alurPesanan(layanan);
                } else if (pilihan.equals("3")) {
                    layanan.laporan().cetak();
                } else if (pilihan.equals("4")) {
                    tampilkanRiwayat(pencatat);
                } else if (pilihan.equals("0")) {
                    break;
                } else {
                    System.out.println("Pilihan tidak dikenal, coba lagi.");
                }
            }
        } catch (NoSuchElementException e) { // input habis (misalnya saat input dari file)
            System.out.println();
            System.out.println("Input berakhir.");
        }
        new RepositoriMenuCSV(fileMenu).simpan(layanan.getKedai().semuaMenu());
        System.out.println("Stok terbaru disimpan ke data/" + fileMenu.getFileName()
                + ". Sampai jumpa!");
    }

    // Meneruskan KedaiException (throws): aturDiskon() hanya gagal untuk pesanan
    // yang sudah LUNAS, padahal pesanan di sini pasti masih BARU.
    private void alurPesanan(LayananKasir layanan) throws KedaiException {
        String nama = tanya("Nama pelanggan: ");
        String noHp = tanya("No. HP: ");
        Pesanan pesanan = layanan.buatPesanan(layanan.pelanggan(nama, noHp));
        System.out.println("Masukkan kode menu satu per satu (kosongkan untuk selesai).");
        while (true) {
            String kode = tanya("  Kode menu: ").toUpperCase(Locale.ROOT);
            if (kode.isEmpty()) {
                break;
            }
            int jumlah = tanyaAngka("  Jumlah: ");
            try {
                Menu menu = layanan.tambahItem(pesanan, kode, jumlah);
                System.out.println("  -> " + jumlah + " x " + menu.getNama() + " ditambahkan");
            } catch (KedaiException | IllegalArgumentException e) {
                System.out.println("  [GAGAL] " + e.getMessage());
            }
        }
        if (pesanan.getDaftarItem().isEmpty()) {
            System.out.println("Pesanan kosong, tidak diproses.");
            return;
        }
        pesanan.aturDiskon(pilihDiskon());
        new StrukPesanan(pesanan).cetak();
        alurBayar(layanan, pesanan);
        new StrukPesanan(pesanan).cetak();
    }

    private Diskon pilihDiskon() {
        System.out.println("Diskon: 1. Tanpa diskon  2. Member  3. Happy Hour");
        while (true) {
            String pilihan = tanya("Pilihan diskon: ");
            if (PILIHAN_DISKON.containsKey(pilihan)) {
                return PILIHAN_DISKON.get(pilihan).get();
            }
            System.out.println("Pilihan tidak dikenal, coba lagi.");
        }
    }

    private void alurBayar(LayananKasir layanan, Pesanan pesanan) {
        while (!pesanan.getStatus().equals("LUNAS")) {
            System.out.println("Pembayaran: 1. Tunai  2. QRIS  3. Kartu kredit");
            String pilihan = tanya("Pilihan pembayaran: ");
            try {
                if (pilihan.equals("1")) {
                    int uang = tanyaAngka("Uang diterima: ");
                    layanan.bayar(pesanan, "tunai", uang, "");
                } else if (pilihan.equals("2")) {
                    int saldo = tanyaAngka("Saldo e-wallet: ");
                    layanan.bayar(pesanan, "qris", saldo, "");
                } else if (pilihan.equals("3")) {
                    String bank = tanya("Nama bank: ");
                    layanan.bayar(pesanan, "kartu", 0, bank);
                } else {
                    System.out.println("Pilihan tidak dikenal, coba lagi.");
                }
            } catch (KedaiException e) {
                System.out.println("[GAGAL] " + e.getMessage());
            }
        }
    }

    private void tampilkanRiwayat(PencatatTransaksiCSV pencatat) throws IOException {
        List<String[]> daftar = pencatat.bacaSemua();
        if (daftar.isEmpty()) {
            System.out.println("Belum ada transaksi tercatat.");
        }
        for (String[] kolom : daftar) {
            System.out.println(String.join(" | ", kolom));
        }
    }

    // ------------------------------------------------------ bantuan input
    // nextLine() melempar NoSuchElementException jika input sudah habis;
    // exception itu ditangkap di jalankan().
    private String tanya(String pertanyaan) {
        System.out.print(pertanyaan);
        return masukan.nextLine().trim();
    }

    private int tanyaAngka(String pertanyaan) {
        while (true) {
            String teks = tanya(pertanyaan);
            try {
                return Integer.parseInt(teks);
            } catch (NumberFormatException e) {
                System.out.println("  Harap isi dengan angka bulat, misalnya 2 atau 50000.");
            }
        }
    }
}
