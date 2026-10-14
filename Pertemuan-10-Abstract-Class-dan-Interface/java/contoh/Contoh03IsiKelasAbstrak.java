/*
 * Contoh 03 - Kelas Abstrak Boleh Punya Konstruktor, Field, dan Method Biasa
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * Kelas abstrak bukan kelas "kosong". Kendaraan di bawah ini punya:
 * - konstruktor dan field (plat, bensin) yang dipakai bersama anak-anaknya,
 * - method biasa (konkret) isiBensin(), jarakTempuh(), dan info(),
 * - method abstrak kmPerLiter() yang WAJIB diisi setiap kelas anak.
 *
 * Konstruktor kelas abstrak tetap berjalan, yaitu saat objek kelas anak dibuat.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03IsiKelasAbstrak.java
 */
public class Contoh03IsiKelasAbstrak {

    public static void main(String[] args) {
        System.out.println("=== MEMBUAT KENDARAAN ===");
        Motor motor = new Motor("KT 1234 AB", 3);
        Mobil mobil = new Mobil("KT 5678 CD", 20, 7);

        System.out.println();
        System.out.println("=== INFO AWAL ===");
        System.out.println(motor.info());
        System.out.println(mobil.info());

        System.out.println();
        System.out.println("=== ISI BENSIN (method konkret milik Kendaraan) ===");
        motor.isiBensin(2);
        mobil.isiBensin(10);
        System.out.println(motor.info());
        System.out.println(mobil.info());
    }
}

/** Kelas abstrak: data dan perilaku bersama semua kendaraan. */
abstract class Kendaraan {
    private String plat; // [2] field bersama
    private int bensin;

    protected Kendaraan(String plat, int bensinLiter) { // [1] konstruktor
        System.out.println("  (konstruktor Kendaraan dijalankan untuk " + plat + ")");
        this.plat = plat;
        this.bensin = bensinLiter;
    }

    public String getPlat() {
        return plat;
    }

    public void isiBensin(int liter) { // [3] method konkret: langsung diwarisi
        bensin += liter;
        System.out.println(plat + " mengisi bensin " + liter + " liter");
    }

    public int jarakTempuh() { // [4] method konkret yang memakai method abstrak
        return bensin * kmPerLiter();
    }

    public String info() {
        return getClass().getSimpleName() + " " + plat + ": bensin " + bensin
                + " liter, bisa menempuh " + jarakTempuh() + " km";
    }

    /** Jarak (km) yang bisa ditempuh dengan 1 liter bensin. */
    public abstract int kmPerLiter(); // [5] berbeda untuk setiap jenis kendaraan
}

/** Motor: tetap wajib menulis konstruktor yang meneruskan data ke super(...). */
class Motor extends Kendaraan {

    public Motor(String plat, int bensinLiter) {
        super(plat, bensinLiter);
    }

    @Override
    public int kmPerLiter() {
        return 40;
    }
}

/** Mobil: punya field tambahan jumlah kursi. */
class Mobil extends Kendaraan {
    private int jumlahKursi;

    public Mobil(String plat, int bensinLiter, int jumlahKursi) {
        super(plat, bensinLiter); // [6] memanggil konstruktor kelas abstrak
        this.jumlahKursi = jumlahKursi;
    }

    @Override
    public int kmPerLiter() {
        return 12;
    }

    @Override
    public String info() { // method konkret milik induk juga boleh di-override
        return super.info() + ", " + jumlahKursi + " kursi";
    }
}
