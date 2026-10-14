/*
 * Soal C2 (kode SEBELUM refactor) - Kasir Laundry "Serba Bisa"
 * Pertemuan 16 - UAS (latihan persiapan, BUKAN soal ujian asli)
 *
 * Program ini BERJALAN dengan benar, tetapi desainnya berantakan: hampir
 * semua pekerjaan ditumpuk di satu kelas. Inilah kode awal Soal C2.
 * Tugasmu: refactor dengan prinsip SOLID + minimal satu design pattern,
 * dan output-nya TIDAK BOLEH berubah sedikit pun.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java SoalC2Sebelum.java
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class SoalC2Sebelum {

    public static void main(String[] args) {
        LaundrySerbaBisa laundry = new LaundrySerbaBisa();
        laundry.terimaCucian("Budi Santoso", "081234567890", "cuci setrika", 4, "member");
        System.out.println();
        laundry.terimaCucian("Siti Aminah", "082198765432", "cuci kering", 6, "gratis1kg");
        System.out.println();
        laundry.terimaCucian("Rina Marlina", "085312345678", "setrika saja", 3, "gratis1kg");
        System.out.println();
        laundry.terimaCucian("Andi Wijaya", "087711223344", "dry clean", 2, "");
        System.out.println();
        laundry.terimaCucian("Dimas Pratama", "081355577799", "cuci setrika", 5, "");
        System.out.println();
        laundry.cetakLaporan();
    }
}

class LaundrySerbaBisa {
    List<String[]> riwayat = new ArrayList<>(); // isi: {kode, nama, berat, total}
    int nomor = 0;

    void terimaCucian(String nama, String noHp, String layanan, int berat, String promo) {
        // cari tarif per kg
        int tarif;
        if (layanan.equals("cuci kering")) {
            tarif = 6000;
        } else if (layanan.equals("cuci setrika")) {
            tarif = 8000;
        } else if (layanan.equals("setrika saja")) {
            tarif = 5000;
        } else {
            System.out.println("[DITOLAK] Layanan '" + layanan + "' tidak tersedia");
            return;
        }
        nomor++;
        String kode = String.format("L%03d", nomor);
        int subtotal = tarif * berat;

        // hitung promo
        int potongan = 0;
        String namaPromo = "";
        if (promo.equals("member")) {
            potongan = subtotal * 10 / 100;
            namaPromo = "Member 10%";
        } else if (promo.equals("gratis1kg")) {
            if (berat >= 5) {
                potongan = tarif;
                namaPromo = "Gratis 1 kg";
            }
        }
        int total = subtotal - potongan;

        // cetak nota
        System.out.println("=".repeat(36));
        System.out.println("LAUNDRY BERSIH KILAT");
        System.out.println("=".repeat(36));
        System.out.println("No. Order : " + kode);
        System.out.println("Pelanggan : " + nama);
        System.out.println("Layanan   : " + layanan);
        String teksTarif = "Rp" + String.format(Locale.US, "%,d", tarif).replace(',', '.');
        System.out.println("Berat     : " + berat + " kg x " + teksTarif);
        System.out.println("-".repeat(36));
        String teksSubtotal = "Rp" + String.format(Locale.US, "%,d", subtotal).replace(',', '.');
        System.out.println(String.format("%-24s%12s", "Subtotal", teksSubtotal));
        if (potongan > 0) {
            String teksPotongan = "-Rp"
                    + String.format(Locale.US, "%,d", potongan).replace(',', '.');
            System.out.println(String.format("%-24s%12s", "Promo " + namaPromo, teksPotongan));
        }
        String teksTotal = "Rp" + String.format(Locale.US, "%,d", total).replace(',', '.');
        System.out.println(String.format("%-24s%12s", "TOTAL", teksTotal));
        System.out.println("=".repeat(36));

        // kirim WhatsApp
        System.out.println("[WA ke " + noHp + "] Halo " + nama + ", cucian " + kode
                + " sudah kami terima. Total " + teksTotal + ".");

        // simpan riwayat
        riwayat.add(new String[] {kode, nama, String.valueOf(berat), String.valueOf(total)});
    }

    void cetakLaporan() {
        System.out.println("=== LAPORAN HARIAN ===");
        int totalBerat = 0;
        int pendapatan = 0;
        for (String[] data : riwayat) {
            int berat = Integer.parseInt(data[2]);
            int total = Integer.parseInt(data[3]);
            String teks = "Rp" + String.format(Locale.US, "%,d", total).replace(',', '.');
            System.out.println(String.format("%s  %-16s%3d kg%12s", data[0], data[1], berat,
                    teks));
            totalBerat += berat;
            pendapatan += total;
        }
        System.out.println("Jumlah order : " + riwayat.size());
        System.out.println("Total berat  : " + totalBerat + " kg");
        System.out.println("Pendapatan   : Rp"
                + String.format(Locale.US, "%,d", pendapatan).replace(',', '.'));
    }
}
