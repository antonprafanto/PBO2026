/*
 * KedaiKita - Pertemuan 13: Prinsip SOLID
 * Bagian SESUDAH refactor.
 *
 * Skenario di file ini SAMA dengan ../sebelum/KasirSerbaBisa.java, dan
 * outputnya pun SAMA PERSIS. Refactor = mengubah STRUKTUR kode tanpa
 * mengubah PERILAKU-nya.
 *
 * Pembagian tugas setelah refactor:
 *     Kedai               -> menyimpan menu (dan menerima penyimpanan pesanan)
 *     Pesanan + Diskon    -> menghitung subtotal, potongan, dan total
 *     StrukPesanan        -> menyusun dan mencetak struk
 *     PenyimpananPesanan  -> menyimpan riwayat (saat ini: PenyimpananMemori)
 *
 * Cara menjalankan (dari dalam folder sesudah):
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

    // Meneruskan KedaiException (throws) ke pemanggil: di skenario ini semua
    // kode menu terdaftar dan stoknya cukup, jadi tidak ada yang perlu ditangani.
    public static void prosesPesanan(Kedai kedai, Pelanggan pelanggan,
            List<Pasangan<String, Integer>> daftarBeli, Diskon diskon) throws KedaiException {
        Pesanan pesanan = kedai.buatPesanan(pelanggan);
        for (Pasangan<String, Integer> beli : daftarBeli) {
            pesanan.tambahItem(kedai.cariMenu(beli.getPertama()), beli.getKedua());
        }
        pesanan.aturDiskon(diskon);
        new StrukPesanan(pesanan).cetak();
    }

    // main ikut meneruskan KedaiException dari prosesPesanan() (alasannya sama).
    public static void main(String[] args) throws KedaiException {
        // DIP: jenis penyimpanan ditentukan DI SINI, bukan di dalam Kedai.
        PenyimpananPesanan penyimpanan = new PenyimpananMemori();
        Kedai kedai = siapkanKedai(penyimpanan);

        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        Pelanggan siti = new Pelanggan("Siti Aminah", "082198765432");
        siti.tambahPoin(12); // pelanggan lama, sudah mengumpulkan 12 poin
        Pelanggan rina = new Pelanggan("Rina Marlina", "085312345678");

        prosesPesanan(kedai, budi, List.of(new Pasangan<>("M01", 2), new Pasangan<>("M03", 1)),
                new TanpaDiskon());
        System.out.println();
        prosesPesanan(kedai, siti, List.of(new Pasangan<>("M02", 2), new Pasangan<>("M05", 1)),
                new DiskonMember());
        System.out.println();
        prosesPesanan(kedai, rina, List.of(new Pasangan<>("M01", 1), new Pasangan<>("M04", 1)),
                new DiskonPersen(15));
        System.out.println();

        System.out.println("=== RIWAYAT PESANAN ===");
        int totalSemua = 0;
        for (Pesanan pesanan : kedai.riwayatPesanan()) {
            int total = pesanan.hitungTotal();
            System.out.println(String.format("%s  %-20s%12s", pesanan.getNomor(),
                    pesanan.getPelanggan().getNama(), Rupiah.format(total)));
            totalSemua += total;
        }
        System.out.println("Total pendapatan: " + Rupiah.format(totalSemua));
    }
}
