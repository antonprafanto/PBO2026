/*
 * Contoh 01 - Singleton: Satu Objek Konfigurasi untuk Seluruh Program
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Pola SINGLETON menjamin sebuah kelas hanya punya SATU objek, dan objek itu
 * diambil lewat satu pintu yang sama: Konfigurasi.getInstance().
 *
 * - Field static instance menyimpan satu-satunya objek.
 * - Konstruktor PRIVATE: kode di luar kelas tidak bisa menulis new Konfigurasi().
 * - getInstance() membuat objek saat PERTAMA kali diminta (lazy), lalu
 *   selalu mengembalikan objek yang sama.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01SingletonKonfigurasi.java
 */
import java.util.LinkedHashMap;
import java.util.Map;

public class Contoh01SingletonKonfigurasi {

    static void halamanBeranda() {
        Konfigurasi konfigurasi = Konfigurasi.getInstance(); // [5] tanpa parameter tambahan
        System.out.println("Beranda: bahasa " + konfigurasi.ambil("bahasa")
                + ", tema " + konfigurasi.ambil("tema"));
    }

    static void halamanProfil() {
        Konfigurasi konfigurasi = Konfigurasi.getInstance();
        System.out.println("Profil : bahasa " + konfigurasi.ambil("bahasa")
                + ", tema " + konfigurasi.ambil("tema"));
    }

    static void halamanPengaturan() {
        System.out.println("Pengguna memilih tema gelap di halaman Pengaturan");
        Konfigurasi.getInstance().ubah("tema", "gelap"); // [6]
    }

    public static void main(String[] args) {
        System.out.println("=== MEMINTA KONFIGURASI DUA KALI ===");
        System.out.println("Permintaan pertama:");
        Konfigurasi a = Konfigurasi.getInstance();
        System.out.println("Permintaan kedua:");
        Konfigurasi b = Konfigurasi.getInstance();
        String sama = (a == b) ? "ya" : "tidak"; // [7] ==: objek yang sama?
        System.out.println("a dan b objek yang sama? " + sama);

        System.out.println();
        System.out.println("=== SEMUA HALAMAN MEMBACA PENGATURAN YANG SAMA ===");
        halamanBeranda();
        halamanProfil();

        System.out.println();
        System.out.println("=== DIUBAH DI SATU TEMPAT, TERLIHAT DI SEMUA TEMPAT ===");
        halamanPengaturan();
        halamanBeranda();
        halamanProfil();
    }
}

/** Pengaturan aplikasi yang harus SAMA di semua bagian program. */
class Konfigurasi {
    private static Konfigurasi instance = null; // [1] field static: satu-satunya objek

    private Map<String, String> data = new LinkedHashMap<>();

    private Konfigurasi() { // [2] private: new Konfigurasi() ditolak di luar kelas ini
        System.out.println("  (objek Konfigurasi dibuat)");
        data.put("bahasa", "Indonesia");
        data.put("tema", "terang");
    }

    public static Konfigurasi getInstance() { // [3] satu-satunya pintu masuk
        if (instance == null) { // [4] dibuat hanya saat pertama diminta
            instance = new Konfigurasi();
        }
        return instance;
    }

    public String ambil(String kunci) {
        return data.get(kunci);
    }

    public void ubah(String kunci, String nilai) {
        data.put(kunci, nilai);
    }
}
