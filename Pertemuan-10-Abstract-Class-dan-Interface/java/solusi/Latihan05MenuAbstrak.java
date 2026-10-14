/*
 * Solusi Latihan 05 - KedaiKita: Menu Menjadi Kelas Abstrak
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * Ide penyelesaian:
 * - Versi ringkas Menu (kode, nama, harga) dijadikan kelas abstrak, karena
 *   di KedaiKita tidak ada "menu umum": setiap menu pasti Makanan atau Minuman.
 * - kategori() dan keterangan() menjadi method abstrak. Kategori tidak lagi
 *   dikirim lewat konstruktor, tetapi "dijawab" oleh setiap kelas anak.
 * - toString() ditulis SEKALI di kelas abstrak dan memanggil kedua method
 *   abstrak itu (template method). Kelas anak tidak perlu meng-override
 *   toString() lagi.
 *
 * Catatan nama kelas: di solusi ini kelasnya bernama MenuAbstrak, MenuMakanan,
 * dan MenuMinuman, BUKAN Menu, Makanan, dan Minuman. Alasannya, folder java/
 * pertemuan ini sudah punya kelas Menu, Makanan, dan Minuman (di studi-kasus).
 * Editor seperti VS Code menganggap satu folder sebagai satu proyek dan akan
 * protes "The type Menu is already defined" jika ada dua kelas bernama sama.
 * Di proyekmu sendiri, cukup ubah kelas Menu secara langsung.
 * Dengan alasan yang sama, formatRupiah() ditulis di sini (kelas Rupiah sudah
 * ada di studi-kasus).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05MenuAbstrak.java
 */
import java.util.List;
import java.util.Locale;

public class Latihan05MenuAbstrak {

    public static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    public static void main(String[] args) {
        List<MenuAbstrak> daftarMenu = List.of(
                new MenuMinuman("M01", "Kopi Susu Gula Aren", 18000, true),
                new MenuMinuman("M02", "Es Teh Manis", 8000, true),
                new MenuMakanan("M03", "Nasi Goreng Kampung", 25000, 2),
                new MenuMakanan("M04", "Mie Goreng Jawa", 23000, 1),
                new MenuMakanan("M05", "Pisang Goreng Keju", 15000, 0),
                new MenuMinuman("M06", "Teh Tarik Hangat", 12000, false));
        System.out.println("=== MENU KEDAIKITA (Menu kini abstrak) ===");
        for (MenuAbstrak menu : daftarMenu) {
            System.out.println(menu);
        }

        System.out.println();
        System.out.println("=== JUMLAH PER KATEGORI ===");
        int jumlahMakanan = 0;
        int jumlahMinuman = 0;
        for (MenuAbstrak menu : daftarMenu) {
            if (menu.kategori().equals("Makanan")) {
                jumlahMakanan++;
            } else {
                jumlahMinuman++;
            }
        }
        System.out.println("Makanan: " + jumlahMakanan);
        System.out.println("Minuman: " + jumlahMinuman);
    }
}

/** Kelas abstrak: data bersama semua menu KedaiKita. */
abstract class MenuAbstrak {
    private String kode;
    private String nama;
    private int harga;

    protected MenuAbstrak(String kode, String nama, int harga) {
        this.kode = kode;
        this.nama = nama;
        this.harga = harga;
    }

    /** "Makanan" atau "Minuman". */
    public abstract String kategori();

    /** Informasi khusus setiap jenis menu. */
    public abstract String keterangan();

    @Override
    public String toString() {
        return "[" + kode + "] " + nama + " (" + kategori() + ") - "
                + Latihan05MenuAbstrak.formatRupiah(harga) + " | " + keterangan();
    }
}

/** Makanan dengan level pedas 0 sampai 5. */
class MenuMakanan extends MenuAbstrak {
    private int levelPedas;

    public MenuMakanan(String kode, String nama, int harga, int levelPedas) {
        super(kode, nama, harga);
        this.levelPedas = levelPedas;
    }

    @Override
    public String kategori() {
        return "Makanan";
    }

    @Override
    public String keterangan() {
        return "pedas level " + levelPedas;
    }
}

/** Minuman yang disajikan dingin atau panas. */
class MenuMinuman extends MenuAbstrak {
    private boolean dingin;

    public MenuMinuman(String kode, String nama, int harga, boolean dingin) {
        super(kode, nama, harga);
        this.dingin = dingin;
    }

    @Override
    public String kategori() {
        return "Minuman";
    }

    @Override
    public String keterangan() {
        return dingin ? "dingin" : "panas";
    }
}
