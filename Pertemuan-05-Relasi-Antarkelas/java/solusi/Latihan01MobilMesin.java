/*
 * Solusi Latihan 01 - Mobil dan Mesin (Komposisi)
 * Pertemuan 05 - Relasi Antarkelas
 *
 * Ide penyelesaian:
 * - Mesin dibuat DI DALAM konstruktor Mobil. Setiap mobil punya mesinnya
 *   sendiri, dan kode di luar kelas tidak pernah menulis new Mesin(...).
 * - Mobil meneruskan perintah nyalakan/matikan ke mesinnya (mengirim pesan).
 * - jalan(km) hanya berhasil jika mesin sedang menyala.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan01MobilMesin.java
 */
public class Latihan01MobilMesin {

    public static void main(String[] args) {
        Mobil mobil = new Mobil("Avanza", 1300); // tidak ada new Mesin(...) di sini
        System.out.println("=== MOBIL BARU ===");
        System.out.println(mobil);

        System.out.println();
        System.out.println("=== PERJALANAN ===");
        mobil.jalan(5);
        mobil.nyalakan();
        mobil.jalan(12);
        mobil.jalan(5);
        mobil.matikan();

        System.out.println();
        System.out.println("=== SETELAH PERJALANAN ===");
        System.out.println(mobil);
    }
}

/** Mesin mobil dengan kapasitas tertentu (cc). */
class Mesin {
    private int kapasitasCc;
    private boolean menyala;

    public Mesin(int kapasitasCc) {
        this.kapasitasCc = kapasitasCc;
        this.menyala = false;
    }

    public boolean isMenyala() {
        return menyala;
    }

    public void hidupkan() {
        menyala = true;
        System.out.println("Mesin " + kapasitasCc + " cc dihidupkan");
    }

    public void matikan() {
        menyala = false;
        System.out.println("Mesin " + kapasitasCc + " cc dimatikan");
    }

    @Override
    public String toString() {
        String status;
        if (menyala) {
            status = "menyala";
        } else {
            status = "mati";
        }
        return "mesin " + kapasitasCc + " cc (" + status + ")";
    }
}

/** Mobil yang membuat dan memiliki mesinnya sendiri (komposisi). */
class Mobil {
    private String merek;
    private Mesin mesin;
    private int odometer;

    public Mobil(String merek, int kapasitasCc) {
        this.merek = merek;
        this.mesin = new Mesin(kapasitasCc); // mesin lahir bersama mobilnya
        this.odometer = 0;
    }

    public void nyalakan() {
        mesin.hidupkan(); // perintah diteruskan ke mesin
    }

    public void matikan() {
        mesin.matikan();
    }

    public void jalan(int km) {
        if (!mesin.isMenyala()) { // mobil bertanya ke mesinnya
            System.out.println(merek + " belum bisa jalan: mesin masih mati");
            return;
        }
        odometer += km;
        System.out.println(merek + " melaju " + km + " km");
    }

    @Override
    public String toString() {
        return merek + ", " + mesin + ", odometer " + odometer + " km";
    }
}
