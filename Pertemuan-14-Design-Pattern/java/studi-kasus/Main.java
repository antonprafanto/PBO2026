/*
 * KedaiKita - Pertemuan 14: Design Pattern Dasar
 *
 * Empat pola desain dalam satu program:
 * 1. SINGLETON - PengaturanKedai (PengaturanKedai.java): hanya ada satu objek.
 * 2. FACTORY   - PembayaranFactory (PembayaranFactory.java): membuat objek dari pilihan.
 * 3. STRATEGY  - kelas-kelas Diskon (Diskon.java dan kelas pemakainya): aturan
 *                yang bisa ditukar.
 * 4. OBSERVER  - PengamatPesanan (PengamatPesanan.java, LayarDapur.java,
 *                NotifikasiPelanggan.java): pemberitahuan otomatis setiap kali
 *                status pesanan berubah.
 *
 * Cara menjalankan (dari dalam folder studi-kasus):
 *     javac *.java
 *     java Main
 */

import java.util.List;

public class Main {

    /** Membuat kedai beserta lima menu awalnya. */
    public static Kedai siapkanKedai(PenyimpananPesanan penyimpanan) {
        Kedai kedai = new Kedai("KedaiKita", penyimpanan);
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

    // main meneruskan KedaiException (throws): di skenario demo ini kita yakin
    // datanya valid (kode menu terdaftar, stok cukup, uang tunai Budi cukup).
    public static void main(String[] args) throws KedaiException {
        System.out.println("=== 1. SINGLETON: PENGATURAN KEDAI ===");
        PengaturanKedai pengaturanA = PengaturanKedai.getInstance();
        PengaturanKedai pengaturanB = PengaturanKedai.getInstance();
        System.out.println("Objek yang sama? " + yaTidak(pengaturanA == pengaturanB));
        System.out.println("Nama   : " + pengaturanA.getNamaKedai());
        System.out.println("Alamat : " + pengaturanA.getAlamat());
        System.out.println("Pajak  : " + pengaturanB.getPajakPersen() + "%");
        System.out.println();

        System.out.println("=== 2. FACTORY: MEMBUAT PEMBAYARAN DARI PILIHAN ===");
        for (String pilihan : List.of("tunai", "QRIS", "kartu")) {
            Pembayaran pembayaran = PembayaranFactory.buat(pilihan, 100000, "BNI");
            System.out.println("Pilihan '" + pilihan + "' -> " + pembayaran.deskripsi(100000));
        }
        try {
            PembayaranFactory.buat("bitcoin", 0, "");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        System.out.println();

        System.out.println("=== 3. STRATEGY: MENUKAR ATURAN DISKON ===");
        Kedai kedai = siapkanKedai(new PenyimpananMemori());
        Pelanggan rina = new Pelanggan("Rina Marlina", "085312345678");
        Pesanan pesananRina = kedai.buatPesanan(rina);
        pesananRina.tambahItem(kedai.cariMenu("M01"), 2);
        pesananRina.tambahItem(kedai.cariMenu("M04"), 1);
        System.out.println("Subtotal pesanan Rina: "
                + Rupiah.format(pesananRina.hitungSubtotal()));
        List<Diskon> daftarStrategi = List.of(new TanpaDiskon(), new DiskonPersen(15),
                new DiskonHappyHour());
        for (Diskon strategi : daftarStrategi) {
            pesananRina.aturDiskon(strategi);
            String potongan = Rupiah.format(pesananRina.hitungPotongan());
            String total = Rupiah.format(pesananRina.hitungTotal());
            System.out.println(String.format("%-22s potongan %8s, total %8s",
                    strategi.keterangan(), potongan, total));
        }
        System.out.println();

        System.out.println("=== 4. OBSERVER: NOTIFIKASI STATUS PESANAN ===");
        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        Pesanan pesananBudi = kedai.buatPesanan(budi);
        pesananBudi.tambahItem(kedai.cariMenu("M01"), 2);
        pesananBudi.tambahItem(kedai.cariMenu("M03"), 1);
        pesananBudi.tambahPengamat(new LayarDapur());
        pesananBudi.tambahPengamat(new NotifikasiPelanggan());
        pesananBudi.bayar(PembayaranFactory.buat("tunai", 100000, ""));
        for (String status : List.of("DIPROSES", "SIAP", "SELESAI")) {
            System.out.println("Status diubah menjadi " + status + ":");
            pesananBudi.ubahStatus(status);
        }
        System.out.println();
        new StrukPesanan(pesananBudi).cetak();
    }
}
