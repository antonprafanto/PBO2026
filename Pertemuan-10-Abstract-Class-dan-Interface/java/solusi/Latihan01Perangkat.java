/*
 * Solusi Latihan 01 - Kelas Abstrak Perangkat
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * Ide penyelesaian:
 * - Perangkat adalah kelas abstrak. Konstruktor (merek, dayaWatt) dan
 *   method konkret info() cukup ditulis SEKALI di sini.
 * - jenis() dan fungsiUtama() dibuat abstrak, karena jawabannya berbeda untuk
 *   setiap perangkat. info() memanggil keduanya (template method kecil).
 * - totalDaya() menerima list Perangkat jenis apa pun.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan01Perangkat.java
 */
import java.util.List;

public class Latihan01Perangkat {

    public static int totalDaya(List<Perangkat> daftar) {
        int total = 0;
        for (Perangkat perangkat : daftar) {
            total += perangkat.getDayaWatt();
        }
        return total;
    }

    public static void main(String[] args) {
        List<Perangkat> daftar = List.of(
                new Laptop("Lenovo", 65),
                new Ponsel("Samsung", 18),
                new Printer("Epson", 30));
        System.out.println("=== DAFTAR PERANGKAT ===");
        for (Perangkat perangkat : daftar) {
            System.out.println(perangkat.info());
        }
        System.out.println("Total daya jika menyala bersamaan: " + totalDaya(daftar) + " watt");
    }
}

/** Kelas abstrak untuk semua perangkat elektronik. */
abstract class Perangkat {
    private String merek;
    private int dayaWatt;

    protected Perangkat(String merek, int dayaWatt) {
        this.merek = merek;
        this.dayaWatt = dayaWatt;
    }

    public int getDayaWatt() {
        return dayaWatt;
    }

    /** Jenis perangkat, misalnya "Laptop". */
    public abstract String jenis();

    /** Kegunaan utama perangkat. */
    public abstract String fungsiUtama();

    public String info() {
        return jenis() + " " + merek + " (" + dayaWatt + " watt): " + fungsiUtama();
    }
}

/** Laptop untuk kuliah. */
class Laptop extends Perangkat {

    public Laptop(String merek, int dayaWatt) {
        super(merek, dayaWatt);
    }

    @Override
    public String jenis() {
        return "Laptop";
    }

    @Override
    public String fungsiUtama() {
        return "mengetik laporan dan menulis kode";
    }
}

/** Ponsel pintar. */
class Ponsel extends Perangkat {

    public Ponsel(String merek, int dayaWatt) {
        super(merek, dayaWatt);
    }

    @Override
    public String jenis() {
        return "Ponsel";
    }

    @Override
    public String fungsiUtama() {
        return "menelepon dan mengirim pesan";
    }
}

/** Printer di kamar kos. */
class Printer extends Perangkat {

    public Printer(String merek, int dayaWatt) {
        super(merek, dayaWatt);
    }

    @Override
    public String jenis() {
        return "Printer";
    }

    @Override
    public String fungsiUtama() {
        return "mencetak tugas kuliah";
    }
}
