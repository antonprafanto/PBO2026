/*
 * KedaiKita - Pertemuan 07: Pewarisan (Inheritance)
 *
 * Yang baru dibanding Pertemuan 05/06:
 * - Kelas induk Menu kini punya dua kelas anak: Makanan (Makanan.java)
 *   dan Minuman (Minuman.java).
 * - Semua menu dibuat sebagai Makanan atau Minuman.
 * - Kelas Pesanan, ItemPesanan, Kedai, dan Pelanggan TIDAK diubah sama sekali,
 *   tetapi tetap bisa bekerja dengan Makanan dan Minuman. Itulah kekuatan pewarisan.
 *
 * Cara menjalankan (dari dalam folder studi-kasus):
 *     javac *.java
 *     java Main
 */
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

    public static void main(String[] args) {
        Kedai kedai = siapkanKedai();
        kedai.tampilkanMenu();
        System.out.println();

        System.out.println("=== CEK PEWARISAN ===");
        Menu kopi = kedai.cariMenu("M01");
        Menu nasi = kedai.cariMenu("M03");
        System.out.println(kopi.getNama() + " termasuk Minuman? "
                + yaTidak(kopi instanceof Minuman));
        System.out.println(kopi.getNama() + " termasuk Menu? "
                + yaTidak(kopi instanceof Menu));
        System.out.println(nasi.getNama() + " termasuk Minuman? "
                + yaTidak(nasi instanceof Minuman));
        System.out.println("Kategori " + nasi.getNama() + ": " + nasi.getKategori());
        String hargaPromo = Rupiah.format(kopi.hargaSetelahDiskon(10));
        System.out.println("Diskon 10% untuk " + kopi.getNama() + " (method warisan Menu): "
                + hargaPromo);
        System.out.println();

        System.out.println("=== MENAMBAH MENU BARU ===");
        Minuman kopiTubruk = new Minuman("M06", "Kopi Tubruk", 12000, 25, false);
        kedai.tambahMenu(kopiTubruk);
        System.out.println("Ditambahkan: " + kopiTubruk);
        try {
            new Makanan("M07", "Seblak Super Pedas", 20000, 10, 9);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal menambah menu: " + e.getMessage());
        }
        System.out.println();

        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        Pelanggan siti = new Pelanggan("Siti Aminah", "082198765432");

        Pesanan pesananBudi = kedai.buatPesanan(budi);
        pesananBudi.tambahItem(kedai.cariMenu("M01"), 2);
        pesananBudi.tambahItem(kedai.cariMenu("M03"), 1);
        pesananBudi.cetakStruk();
        System.out.println();

        Pesanan pesananSiti = kedai.buatPesanan(siti);
        pesananSiti.tambahItem(kedai.cariMenu("M06"), 1);
        pesananSiti.tambahItem(kedai.cariMenu("M05"), 2);
        pesananSiti.cetakStruk();
        System.out.println();

        System.out.println("=== SETELAH TRANSAKSI ===");
        kedai.tampilkanMenu();
        System.out.println("Jumlah pesanan tercatat: " + kedai.jumlahPesanan());
    }
}
