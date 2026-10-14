/*
 * Solusi Latihan 05 - Kelas Snack untuk KedaiKita
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * Ide penyelesaian:
 * - Snack adalah menu (is-a), sama seperti Makanan dan Minuman.
 * - Konstruktor Snack memanggil super(...) dengan kategori "Snack" di baris
 *   PERTAMA, lalu memeriksa dan menyimpan beratGram (harus lebih dari 0).
 * - toString() di-override: teks versi induk + " | <berat> gram".
 * - hargaSetelahDiskon() tidak ditulis ulang: cukup diwarisi dari induk.
 *
 * Catatan nama kelas: kelas induk di solusi ini bernama MenuKedai, BUKAN Menu.
 * Alasannya, folder java/ pertemuan ini sudah punya kelas Menu dan Rupiah
 * (di studi-kasus), dan editor seperti VS Code akan protes "The type Menu is
 * already defined". MenuKedai adalah SALINAN RINGKAS kelas Menu (hanya bagian
 * yang dibutuhkan), dan format Rupiah ditulis sebagai method static di
 * dalamnya. Di proyek KedaiKita-mu, cukup buat file Snack.java berisi
 * "public class Snack extends Menu".
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05SnackKedaiKita.java
 */
import java.util.Locale;

public class Latihan05SnackKedaiKita {

    public static void main(String[] args) {
        Snack keripik = new Snack("M07", "Keripik Singkong Balado", 10000, 20, 150);
        Snack amplang = new Snack("M08", "Amplang Ikan Pipih", 15000, 15, 100);

        System.out.println("=== MENU BARU: SNACK ===");
        System.out.println(keripik);
        System.out.println(amplang);

        System.out.println();
        System.out.println("=== CEK PEWARISAN ===");
        String jawaban = (amplang instanceof MenuKedai) ? "ya" : "tidak";
        System.out.println(amplang.getNama() + " termasuk Menu? " + jawaban);
        String hargaPromo = MenuKedai.formatRupiah(amplang.hargaSetelahDiskon(10));
        System.out.println("Diskon 10% untuk " + amplang.getNama() + ": " + hargaPromo);

        System.out.println();
        System.out.println("=== VALIDASI ===");
        try {
            new Snack("M09", "Kacang Sangrai", 8000, 10, 0);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal menambah menu: " + e.getMessage());
        }
    }
}

/** Salinan ringkas kelas induk Menu dari studi kasus. */
class MenuKedai {
    private String kode;
    private String nama;
    private int harga;
    private String kategori;
    private int stok;

    public MenuKedai(String kode, String nama, int harga, String kategori, int stok) {
        if (harga <= 0) {
            throw new IllegalArgumentException("Harga harus lebih dari 0");
        }
        this.kode = kode;
        this.nama = nama;
        this.harga = harga;
        this.kategori = kategori;
        this.stok = stok;
    }

    /** Mengubah 18000 menjadi "Rp18.000". */
    public static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    public String getNama() {
        return nama;
    }

    public int hargaSetelahDiskon(int persen) {
        int potongan = harga * persen / 100;
        return harga - potongan;
    }

    @Override
    public String toString() {
        return "[" + kode + "] " + nama + " (" + kategori + ") - "
                + formatRupiah(harga) + " | stok " + stok;
    }
}

/** Menu kategori snack. Tambahan: berat per porsi dalam gram. */
class Snack extends MenuKedai {
    private int beratGram;

    public Snack(String kode, String nama, int harga, int stok, int beratGram) {
        super(kode, nama, harga, "Snack", stok); // kategori diisi otomatis
        if (beratGram <= 0) {
            throw new IllegalArgumentException("Berat harus lebih dari 0 gram");
        }
        this.beratGram = beratGram;
    }

    public int getBeratGram() {
        return beratGram;
    }

    @Override
    public String toString() {
        return super.toString() + " | " + beratGram + " gram";
    }
}
