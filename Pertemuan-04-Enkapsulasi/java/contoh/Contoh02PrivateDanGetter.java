/*
 * Contoh 02 - private dan Getter
 * Pertemuan 04 - Enkapsulasi
 *
 * - Field private hanya bisa disentuh oleh kode di DALAM kelasnya sendiri.
 *   Membacanya dari kelas lain ditolak saat kompilasi.
 * - Untuk membaca data dari luar, kelas menyediakan method public yang
 *   disebut getter, misalnya getPemilik().
 * - Data yang terlalu rahasia (PIN) sengaja TIDAK diberi getter.
 *
 * Contoh 02 di jalur Python membahas name mangling (fitur khusus Python).
 * Padanannya di Java adalah contoh ini. Perbandingannya ada di Jembatan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02PrivateDanGetter.java
 */
public class Contoh02PrivateDanGetter {

    public static void main(String[] args) {
        Brankas brankas = new Brankas("Budi", "246810");

        System.out.println("=== MEMAKAI BRANKAS LEWAT METHOD ===");
        brankas.buka("123456");
        brankas.buka("246810");

        System.out.println();
        System.out.println("=== MEMBACA DATA LEWAT GETTER ===");
        System.out.println("Pemilik brankas: " + brankas.getPemilik()); // [5]
        // System.out.println(brankas.pin); // [6] jika tanda // dihapus: error kompilasi
        System.out.println("PIN tidak punya getter, jadi tidak bisa dibaca dari luar kelas");
    }
}

/** Brankas sederhana: punya pemilik dan PIN. */
class Brankas {
    private String pemilik; // [1] private: hanya kode di dalam kelas Brankas yang boleh menyentuh
    private String pin;

    public Brankas(String pemilik, String pin) { // [2] public: boleh dipanggil dari mana saja
        this.pemilik = pemilik;
        this.pin = pin;
    }

    public String getPemilik() { // [3] getter: "pintu baca" untuk field pemilik
        return pemilik;
    }

    public void buka(String pin) {
        if (pin.equals(this.pin)) { // [4] di DALAM kelas, field private bebas dipakai
            System.out.println("PIN benar. Brankas milik " + pemilik + " terbuka.");
        } else {
            System.out.println("PIN salah. Brankas tetap terkunci.");
        }
    }
}
