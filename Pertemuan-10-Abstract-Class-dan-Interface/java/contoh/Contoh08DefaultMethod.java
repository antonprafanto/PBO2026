/*
 * Contoh 08 - Default Method dan Konstanta di Interface (khusus Java)
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * - Sejak Java 8, interface boleh punya method BERISI yang diberi kata kunci
 *   default. Kelas yang mengimplementasikan interface itu otomatis
 *   mendapatkannya, tetapi tetap boleh meng-override-nya.
 * - Field di dalam interface otomatis public static final: sebuah konstanta.
 *
 * Contoh ini khusus Java. Padanannya di Python adalah method biasa (konkret)
 * di dalam kelas ABC (lihat Jembatan Python <-> Java).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh08DefaultMethod.java
 */
import java.util.List;

public class Contoh08DefaultMethod {

    public static void main(String[] args) {
        List<BisaDinilai> daftar = List.of(
                new WarungMakan("Warung Nasi Kuning Bu Ani", 46, 10),
                new DriverOjek("Pak Rahman", 95, 20),
                new WarungMakan("Warung Pecel Baru", 0, 0));

        System.out.println("=== RINGKASAN PENILAIAN ===");
        for (BisaDinilai yangDinilai : daftar) {
            System.out.println(yangDinilai.ringkasan()); // [5] versi default atau versi override
        }

        System.out.println();
        System.out.println("=== KONSTANTA INTERFACE ===");
        System.out.println("Bintang maksimal: " + BisaDinilai.BINTANG_MAKS); // [6]
    }
}

/** Kontrak: sesuatu yang bisa diberi bintang oleh pengguna aplikasi. */
interface BisaDinilai {
    int BINTANG_MAKS = 5; // [1] konstanta: otomatis public static final

    String nama(); // [2] method abstrak: otomatis public abstract

    int totalBintang();

    int jumlahUlasan();

    default int rataRata() { // [3] default method: punya isi
        if (jumlahUlasan() == 0) {
            return 0;
        }
        return totalBintang() / jumlahUlasan();
    }

    default String ringkasan() { // [3]
        return nama() + ": " + rataRata() + "/" + BINTANG_MAKS + " bintang dari "
                + jumlahUlasan() + " ulasan";
    }
}

/** Warung makan: memakai ringkasan() versi default apa adanya. */
class WarungMakan implements BisaDinilai {
    private String nama;
    private int totalBintang;
    private int jumlahUlasan;

    public WarungMakan(String nama, int totalBintang, int jumlahUlasan) {
        this.nama = nama;
        this.totalBintang = totalBintang;
        this.jumlahUlasan = jumlahUlasan;
    }

    @Override
    public String nama() {
        return nama;
    }

    @Override
    public int totalBintang() {
        return totalBintang;
    }

    @Override
    public int jumlahUlasan() {
        return jumlahUlasan;
    }
    // [4] tidak menulis rataRata() dan ringkasan(): keduanya didapat dari interface
}

/** Driver ojek: meng-override ringkasan() dengan versinya sendiri. */
class DriverOjek implements BisaDinilai {
    private String nama;
    private int totalBintang;
    private int jumlahUlasan;

    public DriverOjek(String nama, int totalBintang, int jumlahUlasan) {
        this.nama = nama;
        this.totalBintang = totalBintang;
        this.jumlahUlasan = jumlahUlasan;
    }

    @Override
    public String nama() {
        return nama;
    }

    @Override
    public int totalBintang() {
        return totalBintang;
    }

    @Override
    public int jumlahUlasan() {
        return jumlahUlasan;
    }

    @Override
    public String ringkasan() { // [4] default method boleh di-override
        String predikat = "perlu pembinaan";
        if (rataRata() >= 4) {
            predikat = "driver teladan";
        }
        return "Driver " + nama + ": " + rataRata() + "/" + BINTANG_MAKS + " (" + predikat + ")";
    }
}
