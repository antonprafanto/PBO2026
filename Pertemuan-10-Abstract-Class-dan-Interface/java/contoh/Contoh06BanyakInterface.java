/*
 * Contoh 06 - Satu Kelas, Banyak Interface
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * - Hewan adalah kelas abstrak (punya field nama + method abstrak bersuara).
 * - BisaTerbang dan BisaBerenang adalah interface.
 * - Bebek meng-extends SATU kelas (Hewan) dan meng-implements DUA interface.
 * - Pesawat bukan Hewan, tetapi tetap BisaTerbang.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06BanyakInterface.java
 */
import java.util.List;

public class Contoh06BanyakInterface {

    public static String yaTidak(boolean nilai) {
        return nilai ? "ya" : "tidak";
    }

    public static void main(String[] args) {
        Bebek bebek = new Bebek("Bebek Kuning");
        Ikan ikan = new Ikan("Ikan Patin");
        Pesawat pesawat = new Pesawat("Rajawali 01");

        System.out.println("=== SEMUA HEWAN BERSUARA ===");
        List<Hewan> semuaHewan = List.of(bebek, ikan);
        for (Hewan hewan : semuaHewan) {
            System.out.println(hewan.getNama() + ": " + hewan.bersuara());
        }

        System.out.println();
        System.out.println("=== YANG BISA TERBANG ===");
        List<BisaTerbang> penerbang = List.of(bebek, pesawat); // [3] dikelompokkan per kontrak
        for (BisaTerbang benda : penerbang) {
            System.out.println(benda.terbang());
        }

        System.out.println();
        System.out.println("=== YANG BISA BERENANG ===");
        List<BisaBerenang> perenang = List.of(bebek, ikan);
        for (BisaBerenang benda : perenang) {
            System.out.println(benda.berenang());
        }

        System.out.println();
        System.out.println("=== CEK KEMAMPUAN ===");
        System.out.println(String.format("%-8s | %-5s | %-7s | %s",
                "Kelas", "Hewan", "Terbang", "Berenang"));
        List<Object> semuaBenda = List.of(bebek, ikan, pesawat);
        for (Object benda : semuaBenda) {
            String nama = benda.getClass().getSimpleName();
            String hewan = yaTidak(benda instanceof Hewan); // [4]
            String terbang = yaTidak(benda instanceof BisaTerbang);
            String berenang = yaTidak(benda instanceof BisaBerenang);
            System.out.println(String.format("%-8s | %-5s | %-7s | %s",
                    nama, hewan, terbang, berenang));
        }
    }
}

/** Kelas abstrak: semua hewan punya nama dan suara. */
abstract class Hewan {
    private String nama;

    protected Hewan(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    /** Bunyi khas hewan. */
    public abstract String bersuara();
}

/** Kontrak kemampuan terbang. */
interface BisaTerbang {
    String terbang();
}

/** Kontrak kemampuan berenang. */
interface BisaBerenang {
    String berenang();
}

/** Bebek: hewan yang bisa terbang dan berenang. */
class Bebek extends Hewan implements BisaTerbang, BisaBerenang { // [1] satu induk + dua interface

    public Bebek(String nama) {
        super(nama);
    }

    @Override
    public String bersuara() {
        return "Kwek kwek!";
    }

    @Override
    public String terbang() {
        return getNama() + " terbang rendah di atas sawah";
    }

    @Override
    public String berenang() {
        return getNama() + " mengapung sambil mengayuh kaki";
    }
}

/** Ikan: hewan yang bisa berenang, tetapi tidak bisa terbang. */
class Ikan extends Hewan implements BisaBerenang {

    public Ikan(String nama) {
        super(nama);
    }

    @Override
    public String bersuara() {
        return "(diam saja)";
    }

    @Override
    public String berenang() {
        return getNama() + " berenang di Sungai Mahakam";
    }
}

/** Pesawat: benda mati yang bisa terbang. */
class Pesawat implements BisaTerbang { // [2] bukan Hewan, tetapi BisaTerbang
    private String nama;

    public Pesawat(String nama) {
        this.nama = nama;
    }

    @Override
    public String terbang() {
        return "Pesawat " + nama + " terbang di atas awan";
    }
}
