/*
 * KedaiKita - Pertemuan 13: Prinsip SOLID
 * Bagian SEBELUM refactor: satu kelas yang "serba bisa".
 *
 * KasirSerbaBisa mengerjakan SEMUANYA sendirian:
 *   1. menyimpan data menu,
 *   2. menghitung subtotal dan diskon (dengan rantai if/else if),
 *   3. menyusun dan mencetak struk,
 *   4. menyimpan riwayat pesanan.
 *
 * Program ini BERJALAN dengan benar. Masalahnya bukan pada hasil, tetapi pada
 * desain: setiap perubahan kecil (promo baru, format struk baru, tempat
 * penyimpanan baru) memaksa kita membongkar kelas yang sama.
 * Bandingkan dengan folder ../sesudah yang hasil outputnya SAMA PERSIS.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java KasirSerbaBisa.java
 */

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

/** Kelas "dewa" (god class): terlalu banyak tanggung jawab. */
public class KasirSerbaBisa {
    private Map<String, DataMenu> menu;
    private List<CatatanRiwayat> riwayat;
    private int nomorTerakhir;

    public KasirSerbaBisa() {
        // Tugas 1: menyimpan data menu (kode -> nama dan harga)
        menu = new LinkedHashMap<>();
        menu.put("M01", new DataMenu("Kopi Susu Gula Aren", 18000));
        menu.put("M02", new DataMenu("Es Teh Manis", 8000));
        menu.put("M03", new DataMenu("Nasi Goreng Kampung", 25000));
        menu.put("M04", new DataMenu("Mie Goreng Jawa", 23000));
        menu.put("M05", new DataMenu("Pisang Goreng Keju", 15000));
        // Tugas 4: menyimpan riwayat pesanan
        riwayat = new ArrayList<>();
        nomorTerakhir = 0;
    }

    public void prosesPesanan(String namaPelanggan, int poinPelanggan,
            List<ItemBeli> daftarBeli, String jenisDiskon) {
        nomorTerakhir++;
        String nomor = String.format("P%03d", nomorTerakhir);

        // Tugas 2: menghitung subtotal
        int subtotal = 0;
        for (ItemBeli beli : daftarBeli) {
            DataMenu data = menu.get(beli.kode);
            subtotal += data.harga * beli.jumlah;
        }

        // Tugas 2 (lanjutan): diskon memakai rantai if/else if.
        // Setiap ada jenis promo baru, method ini HARUS dibongkar (melanggar OCP).
        int potongan;
        String keterangan;
        if (jenisDiskon.equals("member")) {
            if (poinPelanggan >= 10) {
                potongan = subtotal * 10 / 100;
                keterangan = "Member 10%";
            } else {
                potongan = 0;
                keterangan = "Member (poin belum cukup)";
            }
        } else if (jenisDiskon.equals("promo")) {
            potongan = subtotal * 15 / 100;
            keterangan = "Promo 15%";
        } else {
            potongan = 0;
            keterangan = "Tanpa diskon";
        }
        int total = subtotal - potongan;

        // Tugas 3: menyusun dan mencetak struk
        System.out.println("=".repeat(40));
        System.out.println("KEDAIKITA - STRUK PESANAN");
        System.out.println("=".repeat(40));
        System.out.println("No. Pesanan : " + nomor);
        System.out.println("Pelanggan   : " + namaPelanggan);
        System.out.println("Status      : BARU");
        System.out.println("-".repeat(40));
        for (ItemBeli beli : daftarBeli) {
            DataMenu data = menu.get(beli.kode);
            String kiri = beli.jumlah + " x " + data.nama;
            System.out.println(String.format("%-30s%10s", kiri,
                    formatRupiah(data.harga * beli.jumlah)));
        }
        System.out.println("-".repeat(40));
        System.out.println(String.format("%-30s%10s", "Subtotal", formatRupiah(subtotal)));
        if (potongan > 0) {
            String kiri = "Diskon " + keterangan;
            String kanan = "-" + formatRupiah(potongan);
            System.out.println(String.format("%-30s%10s", kiri, kanan));
        }
        System.out.println(String.format("%-30s%10s", "TOTAL", formatRupiah(total)));
        System.out.println("=".repeat(40));

        // Tugas 4: menyimpan riwayat (hanya bisa ke list di memori)
        riwayat.add(new CatatanRiwayat(nomor, namaPelanggan, total));
    }

    public static void main(String[] args) {
        KasirSerbaBisa kasir = new KasirSerbaBisa();
        kasir.prosesPesanan("Budi Santoso", 0,
                List.of(new ItemBeli("M01", 2), new ItemBeli("M03", 1)), "tanpa");
        System.out.println();
        kasir.prosesPesanan("Siti Aminah", 12,
                List.of(new ItemBeli("M02", 2), new ItemBeli("M05", 1)), "member");
        System.out.println();
        kasir.prosesPesanan("Rina Marlina", 0,
                List.of(new ItemBeli("M01", 1), new ItemBeli("M04", 1)), "promo");
        System.out.println();

        System.out.println("=== RIWAYAT PESANAN ===");
        int totalSemua = 0;
        for (CatatanRiwayat catatan : kasir.riwayat) {
            System.out.println(String.format("%s  %-20s%12s", catatan.nomor,
                    catatan.namaPelanggan, formatRupiah(catatan.total)));
            totalSemua += catatan.total;
        }
        System.out.println("Total pendapatan: " + formatRupiah(totalSemua));
    }

    private static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    // ----- kelas-kelas kecil pembawa data (dipakai hanya di dalam file ini) -----

    /** Data satu menu: nama dan harga. */
    private static class DataMenu {
        private String nama;
        private int harga;

        DataMenu(String nama, int harga) {
            this.nama = nama;
            this.harga = harga;
        }
    }

    /** Satu baris pembelian: kode menu dan jumlah porsinya. */
    private static class ItemBeli {
        private String kode;
        private int jumlah;

        ItemBeli(String kode, int jumlah) {
            this.kode = kode;
            this.jumlah = jumlah;
        }
    }

    /** Satu catatan riwayat: nomor pesanan, nama pelanggan, dan total bayar. */
    private static class CatatanRiwayat {
        private String nomor;
        private String namaPelanggan;
        private int total;

        CatatanRiwayat(String nomor, String namaPelanggan, int total) {
            this.nomor = nomor;
            this.namaPelanggan = namaPelanggan;
            this.total = total;
        }
    }
}
