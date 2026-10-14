/*
 * Solusi Latihan 05 - Menambah Stok pada Menu KedaiKita
 * Pertemuan 02 - Kelas dan Objek
 *
 * Ide penyelesaian:
 * - Salin kelas Menu dari studi kasus, lalu tambahkan field stok.
 * - jual(jumlah): jika stok cukup, kurangi stok dan KEMBALIKAN total harga;
 *   jika tidak cukup, cetak pesan dan kembalikan 0.
 *
 * Catatan nama kelas: di solusi ini kelasnya diberi nama MenuKedai, BUKAN Menu.
 * Alasannya, folder java/ pertemuan ini sudah punya kelas Menu (di studi-kasus).
 * Editor seperti VS Code menganggap satu folder sebagai satu proyek dan akan
 * protes "The type Menu is already defined" jika ada dua kelas bernama sama.
 * Di proyekmu sendiri, cukup ubah kelas Menu secara langsung.
 *
 * Cara menjalankan dari folder java/solusi (Java 11 ke atas):
 *     java Latihan05StokMenu.java
 */
public class Latihan05StokMenu {

    public static void main(String[] args) {
        MenuKedai kopi = new MenuKedai("Kopi Susu Gula Aren", 18000, 20);
        MenuKedai nasiGoreng = new MenuKedai("Nasi Goreng Kampung", 25000, 2);

        System.out.println("=== STOK AWAL ===");
        kopi.tampilkanInfo();
        nasiGoreng.tampilkanInfo();

        System.out.println();
        System.out.println("=== PENJUALAN ===");
        int pendapatan = 0;
        pendapatan = pendapatan + kopi.jual(2);
        pendapatan = pendapatan + nasiGoreng.jual(3);
        pendapatan = pendapatan + nasiGoreng.jual(2);
        System.out.println("Pendapatan: Rp" + pendapatan);

        System.out.println();
        System.out.println("=== STOK AKHIR ===");
        kopi.tampilkanInfo();
        nasiGoreng.tampilkanInfo();
    }
}

/** Menu KedaiKita yang kini punya stok. */
class MenuKedai {
    String nama;
    int harga;
    int stok;

    MenuKedai(String nama, int harga, int stok) {
        this.nama = nama;
        this.harga = harga;
        this.stok = stok;
    }

    void tampilkanInfo() {
        System.out.println(nama + " - Rp" + harga + " (stok " + stok + ")");
    }

    int jual(int jumlah) {
        if (jumlah > stok) {
            System.out.println("Gagal: stok " + nama + " tidak cukup (sisa " + stok + ")");
            return 0;
        }
        stok = stok - jumlah;
        int total = harga * jumlah;
        System.out.println("Terjual " + jumlah + " " + nama + ", total Rp" + total);
        return total;
    }
}
