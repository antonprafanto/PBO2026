/*
 * KedaiKita - Pertemuan 10: Abstract Class dan Interface
 *
 * Yang baru dibanding Pertemuan 09:
 * - Pembayaran menjadi kelas abstrak: objeknya tidak bisa dibuat langsung.
 * - DapatDicetak.java: interface DapatDicetak dengan satu method, cetak().
 * - Kedai dan Pesanan sama-sama DapatDicetak, walaupun keduanya tidak
 *   punya hubungan pewarisan lain. Method cetakSemua() bisa mencetak
 *   keduanya tanpa peduli jenis aslinya.
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

    /** Mencetak objek apa pun, asalkan ia memenuhi kontrak DapatDicetak. */
    public static void cetakSemua(List<DapatDicetak> daftarDokumen) {
        int jumlah = daftarDokumen.size();
        for (int nomor = 1; nomor <= jumlah; nomor++) {
            DapatDicetak dokumen = daftarDokumen.get(nomor - 1);
            System.out.println("--- Dokumen " + nomor + " dari " + jumlah + " ---");
            dokumen.cetak();
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Kedai kedai = siapkanKedai();

        System.out.println("=== MENGENAL METODE PEMBAYARAN ===");
        List<Pembayaran> daftarMetode = List.of(new PembayaranTunai(100000),
                new PembayaranQRIS(50000), new PembayaranKartu("BNI"));
        for (Pembayaran metode : daftarMetode) {
            System.out.println(metode.deskripsi(100000));
        }
        System.out.println();

        System.out.println("=== TRANSAKSI ===");
        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        Pelanggan siti = new Pelanggan("Siti Aminah", "082198765432");

        Pesanan pesananBudi = kedai.buatPesanan(budi);
        pesananBudi.tambahItem(kedai.cariMenu("M01"), 2);
        pesananBudi.tambahItem(kedai.cariMenu("M03"));
        pesananBudi.bayar(new PembayaranTunai(100000));
        System.out.println();

        Pesanan pesananSiti = kedai.buatPesanan(siti);
        pesananSiti.tambahItem(kedai.cariMenu("M02"), 2);
        pesananSiti.tambahItem(kedai.cariMenu("M05"));
        if (!pesananSiti.bayar(new PembayaranQRIS(20000))) {
            System.out.println();
            pesananSiti.bayar(new PembayaranKartu("BNI"));
        }
        System.out.println();

        System.out.println("=== CETAK SEMUA DOKUMEN ===");
        cetakSemua(List.of(kedai, pesananBudi, pesananSiti));

        System.out.println("=== POIN PELANGGAN ===");
        System.out.println(budi);
        System.out.println(siti);
    }
}
