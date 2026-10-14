/*
 * KedaiKita - Pertemuan 04: Enkapsulasi
 *
 * Yang baru dibanding Pertemuan 03:
 * - Semua field diberi access modifier private, sehingga tidak bisa diakses
 *   langsung dari luar kelasnya. Konstruktor dan method diberi public.
 * - Akses dari luar lewat getter (getHarga(), getStok(), ...) dan setter
 *   setHarga() yang MEMVALIDASI data.
 * - kode, nama, kategori, dan stok bersifat read-only dari luar (hanya ada getter).
 * - Stok hanya bisa berubah lewat method tambahStok() dan kurangiStok().
 * - Poin pelanggan hanya bisa berubah lewat tambahPoin() dan tukarPoin().
 * - Penghitung jumlahMenu kini private static, dibaca lewat Menu.getJumlahMenu().
 * - Data yang tidak valid ditolak dengan throw new IllegalArgumentException(...).
 *   Cara menangkapnya (try/catch) baru kita intip sekilas; bahasan lengkapnya
 *   ada di Pertemuan 11.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java KedaiKita.java
 *
 * Catatan: kelas yang memiliki main (KedaiKita) sengaja ditulis PALING ATAS,
 * karena itu syarat menjalankan file dengan perintah "java NamaFile.java".
 */
import java.util.Locale;

public class KedaiKita {

    public static void main(String[] args) {
        Menu kopi = new Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20);
        Menu esTeh = new Menu("M02", "Es Teh Manis", 8000, "Minuman", 30);
        Menu nasiGoreng = new Menu("M03", "Nasi Goreng Kampung", 25000, "Makanan", 15);

        System.out.println("=== MENU KEDAIKITA ===");
        System.out.println(kopi);
        System.out.println(esTeh);
        System.out.println(nasiGoreng);
        System.out.println("Jumlah menu terdaftar: " + Menu.getJumlahMenu());

        System.out.println();
        System.out.println("=== DATA TIDAK VALID DITOLAK ===");
        try {
            new Menu("M09", "Menu Gratis", 0, "Minuman");
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat menu: " + e.getMessage());
        }
        System.out.println("Jumlah menu terdaftar tetap: " + Menu.getJumlahMenu());

        System.out.println();
        System.out.println("=== MENGUBAH HARGA LEWAT SETTER ===");
        esTeh.setHarga(10000);
        System.out.println("Harga " + esTeh.getNama() + " naik menjadi "
                + Rupiah.format(esTeh.getHarga()));
        try {
            esTeh.setHarga(-5000);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal mengubah harga: " + e.getMessage());
        }
        System.out.println("Harga " + esTeh.getNama() + " tetap "
                + Rupiah.format(esTeh.getHarga()));

        System.out.println();
        System.out.println("=== MENGELOLA STOK ===");
        System.out.println("Stok awal " + kopi.getNama() + ": " + kopi.getStok());
        kopi.kurangiStok(5);
        System.out.println("Terjual 5, stok sekarang " + kopi.getStok());
        kopi.tambahStok(10);
        System.out.println("Restok 10, stok sekarang " + kopi.getStok());
        try {
            kopi.kurangiStok(30);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal menjual: " + e.getMessage());
        }

        System.out.println();
        System.out.println("=== POIN PELANGGAN ===");
        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        System.out.println(budi);
        budi.tambahPoin(12);
        System.out.println(budi);
        int potongan = budi.tukarPoin(10);
        System.out.println("Tukar 10 poin -> potongan " + Rupiah.format(potongan));
        System.out.println(budi);
        try {
            budi.tukarPoin(5);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal menukar poin: " + e.getMessage());
        }
    }
}

/** Kelas utilitas untuk menampilkan uang dalam format Rupiah. */
class Rupiah {

    /** Mengubah 18000 menjadi "Rp18.000". */
    public static String format(int angka) {
        // Locale.US menjamin pemisah ribuan selalu koma (lalu diganti titik),
        // apa pun pengaturan bahasa di komputer yang menjalankan program.
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

/** Satu menu KedaiKita. Datanya dilindungi dan hanya diubah lewat method. */
class Menu {
    private static int jumlahMenu = 0; // atribut kelas, dibaca lewat Menu.getJumlahMenu()

    private String kode;
    private String nama;
    private int harga;
    private String kategori;
    private int stok;

    public Menu(String kode, String nama, int harga, String kategori, int stok) {
        if (stok < 0) {
            throw new IllegalArgumentException("Stok tidak boleh negatif");
        }
        this.kode = kode;
        this.nama = nama;
        this.kategori = kategori;
        this.stok = stok;
        setHarga(harga); // lewat setter, jadi ikut divalidasi
        Menu.jumlahMenu += 1; // dihitung hanya jika objek berhasil dibuat
    }

    /** Konstruktor tanpa stok: stok awal 0 (padanan stok=0 di versi Python). */
    public Menu(String kode, String nama, int harga, String kategori) {
        this(kode, nama, harga, kategori, 0);
    }

    /** Banyaknya objek Menu yang berhasil dibuat. */
    public static int getJumlahMenu() {
        return jumlahMenu;
    }

    // ----- getter (read-only) -----
    public String getKode() {
        return kode;
    }

    public String getNama() {
        return nama;
    }

    public String getKategori() {
        return kategori;
    }

    public int getStok() {
        return stok;
    }

    // ----- getter + setter dengan validasi -----
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

    // ----- method lain (sama seperti Pertemuan 03) -----
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
                + Rupiah.format(harga) + " | stok " + stok;
    }
}

/** Pelanggan KedaiKita. Poin hanya berubah lewat method resmi. */
class Pelanggan {
    private String nama;
    private String noHp;
    private int poin;

    public Pelanggan(String nama, String noHp) {
        this.nama = nama;
        this.noHp = noHp;
        this.poin = 0;
    }

    public String getNama() {
        return nama;
    }

    public String getNoHp() {
        return noHp;
    }

    public int getPoin() {
        return poin;
    }

    public void tambahPoin(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Poin yang ditambahkan harus lebih dari 0");
        }
        poin += jumlah;
    }

    /** Menukar poin menjadi potongan harga. 1 poin = Rp1.000. */
    public int tukarPoin(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Poin yang ditukar harus lebih dari 0");
        }
        if (jumlah > poin) {
            throw new IllegalArgumentException("Poin tidak cukup (sisa " + poin + ")");
        }
        poin -= jumlah;
        return jumlah * 1000;
    }

    @Override
    public String toString() {
        return nama + " (" + noHp + ") - " + poin + " poin";
    }
}
