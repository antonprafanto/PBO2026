/*
 * Solusi Latihan 05 - KedaiKita: Membuat Menu dari Teks
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Ide penyelesaian:
 * - Salin kelas Rupiah dan Menu dari studi kasus.
 * - Tambahkan method static dariTeks(teks) sebagai konstruktor alternatif.
 *   teks.split(";") memecah "M09;Teh Tarik;12000;Minuman;10" menjadi array
 *   berisi 5 bagian. Harga dan stok diubah ke int dengan Integer.parseInt().
 * - Jika teks hanya berisi 4 bagian (tanpa stok), panggil konstruktor 4
 *   parameter sehingga stok bawaan 0 yang dipakai.
 *
 * Catatan nama kelas: di solusi ini kelasnya diberi nama MenuKedai dan
 * RupiahKedai, BUKAN Menu dan Rupiah. Alasannya, folder java/ pertemuan ini
 * sudah punya kelas Menu dan Rupiah (di studi-kasus). Editor seperti VS Code
 * menganggap satu folder sebagai satu proyek dan akan protes
 * "The type Menu is already defined" jika ada dua kelas bernama sama.
 * Di proyekmu sendiri, cukup tambahkan method ini ke kelas Menu secara langsung.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05MenuDariTeks.java
 */
import java.util.Locale;

public class Latihan05MenuDariTeks {

    public static void main(String[] args) {
        String[] data = {
            "M09;Teh Tarik;12000;Minuman;10",
            "M10;Roti Bakar Cokelat;15000;Makanan",
            "M11;Es Jeruk;10000;Minuman;25"
        };
        System.out.println("=== MENU DARI TEKS ===");
        for (String baris : data) {
            MenuKedai menu = MenuKedai.dariTeks(baris);
            System.out.println(baris);
            System.out.println("  -> " + menu);
        }
        System.out.println("Jumlah menu terdaftar: " + MenuKedai.jumlahMenu);
    }
}

/** Kelas utilitas untuk menampilkan uang (salinan Rupiah dari studi kasus). */
class RupiahKedai {

    /** Mengubah 18000 menjadi "Rp18.000". */
    static String format(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

/** Menu KedaiKita yang kini bisa dibuat dari sebaris teks. */
class MenuKedai {
    static int jumlahMenu = 0;

    String kode;
    String nama;
    int harga;
    String kategori;
    int stok;

    MenuKedai(String kode, String nama, int harga, String kategori, int stok) {
        this.kode = kode;
        this.nama = nama;
        this.harga = harga;
        this.kategori = kategori;
        this.stok = stok;
        MenuKedai.jumlahMenu += 1;
    }

    MenuKedai(String kode, String nama, int harga, String kategori) {
        this(kode, nama, harga, kategori, 0);
    }

    /** Konstruktor alternatif dari teks "kode;nama;harga;kategori;stok". */
    static MenuKedai dariTeks(String teks) {
        String[] bagian = teks.split(";");
        String kode = bagian[0];
        String nama = bagian[1];
        int harga = Integer.parseInt(bagian[2]);
        String kategori = bagian[3];
        if (bagian.length == 5) {
            return new MenuKedai(kode, nama, harga, kategori, Integer.parseInt(bagian[4]));
        }
        return new MenuKedai(kode, nama, harga, kategori); // stok bawaan 0
    }

    @Override
    public String toString() {
        return "[" + kode + "] " + nama + " (" + kategori + ") - "
                + RupiahKedai.format(harga) + " | stok " + stok;
    }
}
