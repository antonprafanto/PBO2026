/*
 * Contoh 02 - Variasi Singleton: Eager dan Lazy yang Aman untuk Thread
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Variasi 1 (EAGER, disiapkan di awal): objek langsung dibuat di field
 *     static final. Java membuatnya sekali saja, ketika kelas PencatatLog
 *     mulai dipakai. Sederhana, dan otomatis aman untuk banyak thread.
 * Variasi 2 (LAZY, dibuat saat pertama diminta): seperti contoh 01, tetapi
 *     getInstance() diberi kata kunci synchronized. Jika dua thread memanggil
 *     getInstance() bersamaan, mereka masuk bergantian, sehingga tidak
 *     mungkin tercipta dua objek.
 *
 * Output contoh ini sengaja sama dengan versi Python-nya, walaupun cara
 * kerjanya berbeda (lihat Jembatan Python <-> Java).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02VariasiSingleton.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh02VariasiSingleton {

    static void modulKasir() {
        PencatatLog.getInstance().catat("kasir", "transaksi dibuka"); // [5]
    }

    static void modulLaporan() {
        PencatatLog.getInstance().catat("laporan", "laporan harian dibuat");
    }

    public static void main(String[] args) {
        System.out.println("=== VARIASI 1: OBJEK DISIAPKAN DI AWAL (EAGER) ===");
        modulKasir();
        modulLaporan();
        System.out.println("Jumlah catatan: " + PencatatLog.getInstance().jumlah());

        System.out.println();
        System.out.println("=== VARIASI 2: DIBUAT SAAT PERTAMA DIMINTA (LAZY) ===");
        System.out.println("Permintaan pertama:");
        Tema t1 = Tema.getInstance(); // [6]
        System.out.println("Permintaan kedua:");
        Tema t2 = Tema.getInstance();
        System.out.println("t1 dan t2 objek yang sama? " + (t1 == t2 ? "ya" : "tidak"));
        t1.setWarna("gelap");
        System.out.println("Warna diubah lewat t1 menjadi gelap");
        System.out.println("Warna dibaca lewat t2: " + t2.getWarna());
    }
}

/** Variasi 1: Singleton EAGER (objek disiapkan di awal). */
class PencatatLog {
    private static final PencatatLog INSTANCE = new PencatatLog(); // [1] dibuat sekali

    private List<String> catatan = new ArrayList<>();

    private PencatatLog() {
    }

    public static PencatatLog getInstance() {
        return INSTANCE; // [2] tidak perlu if: objeknya pasti sudah ada
    }

    public void catat(String sumber, String pesan) {
        catatan.add(sumber + ": " + pesan);
        System.out.println("[LOG " + catatan.size() + "] " + sumber + ": " + pesan);
    }

    public int jumlah() {
        return catatan.size();
    }
}

/** Variasi 2: Singleton LAZY yang aman untuk banyak thread. */
class Tema {
    private static Tema instance = null;

    private String warna = "terang";

    private Tema() {
        System.out.println("  (objek Tema dibuat)");
    }

    public static synchronized Tema getInstance() { // [3] thread masuk bergantian
        if (instance == null) { // [4] tetap lazy: dibuat saat pertama diminta
            instance = new Tema();
        }
        return instance;
    }

    public String getWarna() {
        return warna;
    }

    public void setWarna(String warna) {
        this.warna = warna;
    }
}
