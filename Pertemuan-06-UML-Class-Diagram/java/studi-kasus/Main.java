/*
 * KedaiKita - Pertemuan 06: UML Class Diagram
 *
 * Kode di pertemuan ini SAMA PERSIS dengan Pertemuan 05. Tugas kita kali ini
 * adalah membaca kode ini lalu menggambarkannya sebagai class diagram UML,
 * dan sebaliknya: memastikan setiap kotak & garis di diagram ada wujudnya di kode.
 *
 * Daftar file:
 *     Rupiah.java      -> Rupiah.format()
 *     Menu.java        -> Menu
 *     Pelanggan.java   -> Pelanggan
 *     ItemPesanan.java -> ItemPesanan
 *     Pesanan.java     -> Pesanan
 *     Kedai.java       -> Kedai
 *     Main.java        -> program utama (file ini)
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
        kedai.tambahMenu(new Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20));
        kedai.tambahMenu(new Menu("M02", "Es Teh Manis", 8000, "Minuman", 30));
        kedai.tambahMenu(new Menu("M03", "Nasi Goreng Kampung", 25000, "Makanan", 15));
        kedai.tambahMenu(new Menu("M04", "Mie Goreng Jawa", 23000, "Makanan", 10));
        kedai.tambahMenu(new Menu("M05", "Pisang Goreng Keju", 15000, "Makanan", 12));
        return kedai;
    }

    public static void main(String[] args) {
        Kedai kedai = siapkanKedai();
        kedai.tampilkanMenu();
        System.out.println("Jumlah menu: " + kedai.jumlahMenu());
        System.out.println();

        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        Pelanggan siti = new Pelanggan("Siti Aminah", "082198765432");

        // Pesanan pertama: Budi
        Pesanan pesananBudi = kedai.buatPesanan(budi);
        pesananBudi.tambahItem(kedai.cariMenu("M01"), 2);
        pesananBudi.tambahItem(kedai.cariMenu("M03"), 1);
        pesananBudi.cetakStruk();
        System.out.println();

        // Pesanan kedua: Siti (salah satu item gagal karena stok kurang)
        Pesanan pesananSiti = kedai.buatPesanan(siti);
        pesananSiti.tambahItem(kedai.cariMenu("M02"), 2);
        pesananSiti.tambahItem(kedai.cariMenu("M05"), 1);
        try {
            pesananSiti.tambahItem(kedai.cariMenu("M04"), 20);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal menambah item: " + e.getMessage());
        }
        pesananSiti.cetakStruk();
        System.out.println();

        System.out.println("=== MENCARI MENU ===");
        for (String kode : List.of("M02", "M99")) { // List.of: daftar berisi data tetap
            Menu menu = kedai.cariMenu(kode);
            if (menu == null) {
                System.out.println("Cari " + kode + ": tidak ditemukan");
            } else {
                System.out.println("Cari " + kode + ": " + menu);
            }
        }
        System.out.println();

        System.out.println("=== SETELAH TRANSAKSI ===");
        kedai.tampilkanMenu();
        System.out.println("Jumlah pesanan tercatat: " + kedai.jumlahPesanan());
    }
}
