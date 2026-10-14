/*
 * Solusi Latihan 04 - Ojek Online: Satu Kelas, Banyak Interface
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * Ide penyelesaian:
 * - Armada adalah kelas abstrak: semua armada punya pengemudi dan jenis.
 *   Ini hubungan "adalah" (is-a), jadi cocok memakai kelas abstrak.
 * - BisaAntarPenumpang dan BisaAntarMakanan adalah interface (kemampuan,
 *   hubungan "bisa"). Satu kelas boleh mengimplementasikan lebih dari satu
 *   interface.
 * - instanceof dipakai untuk memeriksa KEMAMPUAN, lalu objeknya di-cast ke
 *   tipe interface itu agar method-nya bisa dipanggil (downcasting, P09).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04OjekOnline.java
 */
import java.util.List;

public class Latihan04OjekOnline {

    public static String yaTidak(boolean nilai) {
        return nilai ? "ya" : "tidak";
    }

    public static void main(String[] args) {
        List<Armada> armada = List.of(
                new OjekMotor("Pak Rudi"),
                new TaksiMobil("Pak Joko"),
                new KurirSepeda("Mas Dimas"));

        System.out.println("=== KEMAMPUAN ARMADA ===");
        for (Armada kendaraan : armada) {
            String penumpang = yaTidak(kendaraan instanceof BisaAntarPenumpang);
            String makanan = yaTidak(kendaraan instanceof BisaAntarMakanan);
            System.out.println(kendaraan + ": penumpang " + penumpang + ", makanan " + makanan);
        }

        System.out.println();
        System.out.println("=== PESANAN MAKANAN DARI WARUNG SOTO BANJAR ===");
        for (Armada kendaraan : armada) {
            if (kendaraan instanceof BisaAntarMakanan) {
                BisaAntarMakanan pengantar = (BisaAntarMakanan) kendaraan;
                System.out.println(pengantar.antarMakanan("Warung Soto Banjar"));
            }
        }

        System.out.println();
        System.out.println("=== PENUMPANG KE KAMPUS UNMUL ===");
        for (Armada kendaraan : armada) {
            if (kendaraan instanceof BisaAntarPenumpang) {
                BisaAntarPenumpang pengantar = (BisaAntarPenumpang) kendaraan;
                System.out.println(pengantar.antarPenumpang("Kampus Unmul"));
            }
        }
    }
}

/** Kelas abstrak: semua armada punya pengemudi. */
abstract class Armada {
    private String pengemudi;

    protected Armada(String pengemudi) {
        this.pengemudi = pengemudi;
    }

    /** Jenis armada, misalnya "Ojek motor". */
    public abstract String jenis();

    @Override
    public String toString() {
        return jenis() + " " + pengemudi;
    }
}

/** Kontrak: bisa mengantar penumpang. */
interface BisaAntarPenumpang {
    String antarPenumpang(String tujuan);
}

/** Kontrak: bisa mengantar pesanan makanan. */
interface BisaAntarMakanan {
    String antarMakanan(String warung);
}

/** Ojek motor: bisa mengantar penumpang DAN makanan. */
class OjekMotor extends Armada implements BisaAntarPenumpang, BisaAntarMakanan {

    public OjekMotor(String pengemudi) {
        super(pengemudi);
    }

    @Override
    public String jenis() {
        return "Ojek motor";
    }

    @Override
    public String antarPenumpang(String tujuan) {
        return this + " membonceng penumpang ke " + tujuan;
    }

    @Override
    public String antarMakanan(String warung) {
        return this + " mengambil pesanan di " + warung;
    }
}

/** Taksi mobil: hanya mengantar penumpang. */
class TaksiMobil extends Armada implements BisaAntarPenumpang {

    public TaksiMobil(String pengemudi) {
        super(pengemudi);
    }

    @Override
    public String jenis() {
        return "Taksi mobil";
    }

    @Override
    public String antarPenumpang(String tujuan) {
        return this + " mengantar penumpang ke " + tujuan;
    }
}

/** Kurir sepeda: hanya mengantar makanan. */
class KurirSepeda extends Armada implements BisaAntarMakanan {

    public KurirSepeda(String pengemudi) {
        super(pengemudi);
    }

    @Override
    public String jenis() {
        return "Kurir sepeda";
    }

    @Override
    public String antarMakanan(String warung) {
        return this + " mengayuh sepeda ke " + warung;
    }
}
