/*
 * Solusi Latihan 05 - Validasi Nama Menu KedaiKita
 * Pertemuan 04 - Enkapsulasi
 *
 * Ide penyelesaian:
 * - Salin kelas Menu dari studi kasus pertemuan ini. Bagian yang berubah
 *   ditandai dengan komentar "BARU".
 * - nama kini punya setter. Setter merapikan spasi di awal/akhir dengan
 *   strip(), lalu menolak nama yang kosong.
 * - Konstruktor mengisi nama LEWAT setter (setNama(nama)), sehingga menu
 *   tanpa nama ditolak sejak dibuat dan tidak ikut dihitung di jumlahMenu.
 *
 * Catatan nama kelas: di solusi ini kelasnya diberi nama MenuKedai, BUKAN Menu.
 * Alasannya, folder java/ pertemuan ini sudah punya kelas Menu dan Rupiah
 * (di studi-kasus). Editor seperti VS Code menganggap satu folder sebagai satu
 * proyek dan akan protes "The type Menu is already defined" jika ada dua kelas
 * bernama sama. Karena itu format Rupiah juga ditulis sebagai method private
 * static di dalam MenuKedai. Di proyekmu sendiri, cukup ubah kelas Menu secara
 * langsung.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05NamaMenu.java
 */
import java.util.Locale;

public class Latihan05NamaMenu {

    public static void main(String[] args) {
        MenuKedai kopi = new MenuKedai("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20);
        MenuKedai esTeh = new MenuKedai("M02", "Es Teh Manis", 8000, "Minuman", 30);
        System.out.println("=== MENU AWAL ===");
        System.out.println(kopi);
        System.out.println(esTeh);

        System.out.println();
        System.out.println("=== GANTI NAMA MENU ===");
        esTeh.setNama("Es Teh Manis Jumbo");
        System.out.println("Nama baru: " + esTeh.getNama());
        try {
            esTeh.setNama("   ");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        System.out.println(esTeh);

        System.out.println();
        System.out.println("=== NAMA DIRAPIKAN OTOMATIS ===");
        MenuKedai nasiGoreng = new MenuKedai("M03", "  Nasi Goreng Kampung  ", 25000,
                "Makanan", 15);
        System.out.println("Nama tersimpan: '" + nasiGoreng.getNama() + "'");
        System.out.println(nasiGoreng);

        System.out.println();
        System.out.println("=== MENU BARU TANPA NAMA ===");
        try {
            new MenuKedai("M04", "", 23000, "Makanan");
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat menu: " + e.getMessage());
        }
        System.out.println("Jumlah menu terdaftar: " + MenuKedai.getJumlahMenu());
    }
}

/** Satu menu KedaiKita. Datanya dilindungi dan hanya diubah lewat method. */
class MenuKedai {
    private static int jumlahMenu = 0; // atribut kelas, dibaca lewat getJumlahMenu()

    private String kode;
    private String nama;
    private int harga;
    private String kategori;
    private int stok;

    public MenuKedai(String kode, String nama, int harga, String kategori, int stok) {
        if (stok < 0) {
            throw new IllegalArgumentException("Stok tidak boleh negatif");
        }
        this.kode = kode;
        setNama(nama); // BARU: lewat setter, jadi ikut divalidasi
        this.kategori = kategori;
        this.stok = stok;
        setHarga(harga); // lewat setter, jadi ikut divalidasi
        MenuKedai.jumlahMenu += 1; // dihitung hanya jika objek berhasil dibuat
    }

    /** Konstruktor tanpa stok: stok awal 0. */
    public MenuKedai(String kode, String nama, int harga, String kategori) {
        this(kode, nama, harga, kategori, 0);
    }

    /** Banyaknya objek MenuKedai yang berhasil dibuat. */
    public static int getJumlahMenu() {
        return jumlahMenu;
    }

    /** Mengubah 18000 menjadi "Rp18.000" (private: hanya dipakai kelas ini). */
    private static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    // ----- getter (read-only) -----
    public String getKode() {
        return kode;
    }

    public String getKategori() {
        return kategori;
    }

    public int getStok() {
        return stok;
    }

    // ----- getter + setter dengan validasi -----
    public String getNama() {
        return nama;
    }

    public void setNama(String nama) { // BARU: setter nama
        String namaRapi = nama.strip(); // buang spasi di awal dan akhir
        if (namaRapi.isEmpty()) {
            throw new IllegalArgumentException("Nama menu tidak boleh kosong");
        }
        this.nama = namaRapi;
    }

    public int getHarga() {
        return harga;
    }

    public void setHarga(int harga) {
        if (harga <= 0) {
            throw new IllegalArgumentException("Harga harus lebih dari 0");
        }
        this.harga = harga;
    }

    // ----- method pengubah stok -----
    public void tambahStok(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        stok += jumlah;
    }

    public void kurangiStok(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        if (jumlah > stok) {
            throw new IllegalArgumentException("Stok " + nama + " tidak cukup (sisa " + stok + ")");
        }
        stok -= jumlah;
    }

    // ----- method lain -----
    public int hitungTotal(int jumlah) {
        return harga * jumlah;
    }

    public int hargaSetelahDiskon(int persen) {
        int potongan = harga * persen / 100;
        return harga - potongan;
    }

    public boolean stokCukup(int jumlah) {
        return stok >= jumlah;
    }

    @Override
    public String toString() {
        return "[" + kode + "] " + nama + " (" + kategori + ") - "
                + formatRupiah(harga) + " | stok " + stok;
    }
}
