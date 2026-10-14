/*
 * KedaiKita - Pertemuan 03: Atribut dan Method Lebih Dalam
 *
 * Yang baru dibanding Pertemuan 02:
 * - Menu punya atribut lebih lengkap: kode, nama, harga, kategori, stok.
 * - Dua konstruktor Menu (overloading): dengan stok, atau tanpa stok.
 *   Konstruktor tanpa stok meneruskan ke konstruktor lengkap lewat
 *   this(..., 0), jadi stok bawaannya 0.
 * - Atribut KELAS (static) jumlahMenu: dimiliki bersama oleh semua objek Menu.
 * - Method toString() agar objek bisa langsung dicetak dengan println().
 * - Method yang mengembalikan nilai: hitungTotal, hargaSetelahDiskon, stokCukup.
 * - Kelas utilitas Rupiah dengan method static format() untuk menampilkan
 *   uang dengan titik ribuan.
 * - Kelas baru: Pelanggan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java KedaiKita.java
 *
 * Catatan:
 * - Kelas yang memiliki main (KedaiKita) sengaja ditulis PALING ATAS,
 *   karena itu syarat menjalankan file dengan perintah "java NamaFile.java".
 * - Field dan method di kelas Menu dan Pelanggan belum diberi access modifier
 *   (public/private dibahas di Pertemuan 04). Satu-satunya pengecualian adalah
 *   toString(), yang WAJIB public karena menimpa toString() bawaan.
 */
import java.util.Locale;

public class KedaiKita {

    public static void main(String[] args) {
        Menu kopi = new Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20);
        Menu esTeh = new Menu("M02", "Es Teh Manis", 8000, "Minuman", 30);
        Menu nasiGoreng = new Menu("M03", "Nasi Goreng Kampung", 25000, "Makanan", 15);
        Menu mieGoreng = new Menu("M04", "Mie Goreng Jawa", 23000, "Makanan"); // stok bawaan 0

        System.out.println("=== MENU KEDAIKITA ===");
        System.out.println(kopi);
        System.out.println(esTeh);
        System.out.println(nasiGoreng);
        System.out.println(mieGoreng);
        System.out.println("Jumlah menu terdaftar: " + Menu.jumlahMenu);

        System.out.println();
        System.out.println("=== CEK STOK ===");
        if (kopi.stokCukup(2)) {
            System.out.println("Pesan 2 " + kopi.nama + "? Bisa");
        } else {
            System.out.println("Pesan 2 " + kopi.nama + "? Stok tidak cukup");
        }
        if (mieGoreng.stokCukup(1)) {
            System.out.println("Pesan 1 " + mieGoreng.nama + "? Bisa");
        } else {
            System.out.println("Pesan 1 " + mieGoreng.nama + "? Stok tidak cukup");
        }

        System.out.println();
        System.out.println("=== PROMO HARI INI: DISKON 10% ===");
        Menu[] menuPromo = {kopi, nasiGoreng};
        for (Menu menu : menuPromo) {
            int hargaBaru = menu.hargaSetelahDiskon(10);
            System.out.println(menu.nama + ": " + Rupiah.format(menu.harga) + " -> "
                    + Rupiah.format(hargaBaru));
        }

        System.out.println();
        System.out.println("=== PELANGGAN ===");
        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        System.out.println(budi);
        int belanja = kopi.hitungTotal(2) + esTeh.hitungTotal(1);
        int poinBaru = belanja / 10000; // 1 poin untuk setiap Rp10.000
        budi.tambahPoin(poinBaru);
        System.out.println("Budi belanja " + Rupiah.format(belanja) + ", dapat " + poinBaru
                + " poin");
        System.out.println(budi);
    }
}

/** Kelas utilitas untuk menampilkan uang. Isinya hanya method static. */
class Rupiah {

    /** Mengubah 18000 menjadi "Rp18.000". */
    static String format(int angka) {
        // Locale.US membuat pemisah ribuan selalu koma (18,000) di komputer mana
        // pun, apa pun pengaturan bahasanya. Setelah itu koma diganti titik.
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

/** Cetak biru untuk setiap menu di KedaiKita. */
class Menu {
    static int jumlahMenu = 0; // atribut KELAS: satu nilai untuk semua objek Menu

    String kode; // atribut OBJEK: tiap objek punya nilainya sendiri
    String nama;
    int harga;
    String kategori;
    int stok;

    Menu(String kode, String nama, int harga, String kategori, int stok) {
        this.kode = kode;
        this.nama = nama;
        this.harga = harga;
        this.kategori = kategori;
        this.stok = stok;
        Menu.jumlahMenu += 1; // setiap ada objek baru, penghitung bertambah
    }

    /** Konstruktor tanpa stok: stok bawaan 0 (padanan stok=0 di Python). */
    Menu(String kode, String nama, int harga, String kategori) {
        this(kode, nama, harga, kategori, 0); // teruskan ke konstruktor lengkap
    }

    /** Teks yang muncul saat objek dicetak dengan System.out.println(). */
    @Override
    public String toString() {
        return "[" + kode + "] " + nama + " (" + kategori + ") - "
                + Rupiah.format(harga) + " | stok " + stok;
    }

    /** Total harga untuk sejumlah porsi. */
    int hitungTotal(int jumlah) {
        return harga * jumlah;
    }

    /** Harga setelah dipotong diskon sekian persen. */
    int hargaSetelahDiskon(int persen) {
        int potongan = harga * persen / 100;
        return harga - potongan;
    }

    /** true jika stok masih cukup untuk sejumlah porsi. */
    boolean stokCukup(int jumlah) {
        return stok >= jumlah;
    }
}

/** Data pelanggan KedaiKita beserta poin belanjanya. */
class Pelanggan {
    String nama;
    String noHp;
    int poin;

    Pelanggan(String nama, String noHp) {
        this.nama = nama;
        this.noHp = noHp;
        this.poin = 0; // setiap pelanggan baru mulai dari 0 poin
    }

    @Override
    public String toString() {
        return nama + " (" + noHp + ") - " + poin + " poin";
    }

    void tambahPoin(int jumlah) {
        poin += jumlah;
    }
}
