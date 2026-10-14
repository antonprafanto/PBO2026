/*
 * KedaiKita - Pertemuan 09: Polimorfisme
 *
 * Yang baru dibanding Pertemuan 07:
 * - Pembayaran.java: kelas induk Pembayaran + PembayaranTunai, PembayaranQRIS,
 *   PembayaranKartu. Ketiganya punya method yang sama dengan perilaku berbeda.
 * - Pesanan.bayar(pembayaran) bekerja untuk SEMUA jenis pembayaran.
 * - Pesanan.tambahItem(menu) boleh tanpa jumlah (overloading, berarti 1 porsi).
 * - instanceof untuk memeriksa jenis objek sebelum memakai fitur khususnya.
 *
 * Cara menjalankan (dari dalam folder studi-kasus):
 *     javac *.java
 *     java Main
 */

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

    public static void main(String[] args) {
        Kedai kedai = siapkanKedai();
        kedai.tampilkanMenu();
        System.out.println();

        System.out.println("=== SATU PANGGILAN, BANYAK BENTUK ===");
        List<Pembayaran> daftarMetode = List.of(new PembayaranTunai(100000),
                new PembayaranQRIS(50000), new PembayaranKartu("BNI"));
        for (Pembayaran metode : daftarMetode) {
            int biaya = metode.hitungBiayaLayanan(100000);
            System.out.println(String.format("%-20s biaya layanan untuk Rp100.000: %s",
                    metode.namaMetode(), Rupiah.format(biaya)));
        }
        System.out.println();

        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        Pelanggan siti = new Pelanggan("Siti Aminah", "082198765432");

        Pesanan pesananBudi = kedai.buatPesanan(budi);
        pesananBudi.tambahItem(kedai.cariMenu("M01"), 2);
        pesananBudi.tambahItem(kedai.cariMenu("M03")); // jumlah bawaan: 1 (versi overload)
        pesananBudi.cetakStruk();
        PembayaranTunai pembayaranBudi = new PembayaranTunai(100000);
        pesananBudi.bayar(pembayaranBudi);
        System.out.println();

        Pesanan pesananSiti = kedai.buatPesanan(siti);
        pesananSiti.tambahItem(kedai.cariMenu("M02"), 2);
        pesananSiti.tambahItem(kedai.cariMenu("M05"));
        pesananSiti.cetakStruk();
        boolean berhasil = pesananSiti.bayar(new PembayaranQRIS(20000));
        if (!berhasil) {
            System.out.println();
            pesananSiti.bayar(new PembayaranKartu("BNI"));
        }
        System.out.println();

        System.out.println("=== MEMERIKSA JENIS PEMBAYARAN ===");
        List<Pembayaran> daftarPembayaran = List.of(pembayaranBudi,
                new PembayaranKartu("Mandiri"));
        for (Pembayaran pembayaran : daftarPembayaran) {
            if (pembayaran instanceof PembayaranTunai) {
                // Casting: pembayaran "dipandang" sebagai PembayaranTunai
                // agar getKembalian() (yang hanya ada di kelas itu) bisa dipanggil.
                PembayaranTunai tunai = (PembayaranTunai) pembayaran;
                String kembalian = Rupiah.format(tunai.getKembalian());
                System.out.println(pembayaran.namaMetode() + ": kembalian " + kembalian);
            } else {
                System.out.println(pembayaran.namaMetode() + ": tidak ada kembalian");
            }
        }
        System.out.println();

        System.out.println("=== STATUS AKHIR ===");
        System.out.println(pesananBudi.getNomor() + ": " + pesananBudi.getStatus());
        System.out.println(pesananSiti.getNomor() + ": " + pesananSiti.getStatus());
        System.out.println(budi);
        System.out.println(siti);
    }
}
