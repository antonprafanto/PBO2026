/*
 * Contoh 03 - LSP: Kelas Anak Harus Bisa Menggantikan Induknya
 * Pertemuan 13 - Prinsip SOLID
 *
 * Versi MELANGGAR: kelas Burung berjanji "semua burung bisa terbang".
 * Penguin mewarisi Burung, lalu mengingkari janji itu dengan melempar
 * exception. Pemanggil yang percaya pada janji induk pun terkejut.
 *
 * Versi SESUAI LSP: janji dipecah sesuai kenyataan.
 * - BurungDasar   -> janji yang ditepati SEMUA burung: bisa bertelur
 * - BurungTerbang -> janji tambahan khusus burung penerbang: bisa terbang
 * PenguinKutub cukup mewarisi BurungDasar sehingga tidak ada janji yang diingkari.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03Lsp.java
 */
import java.util.List;

public class Contoh03Lsp {

    /** Pemanggil yang percaya pada janji kelas Burung. */
    static void lepasKeUdara(List<Burung> daftar) {
        for (Burung burung : daftar) {
            try {
                System.out.println("  " + burung.terbang());
            } catch (UnsupportedOperationException e) { // [2] pemanggil terpaksa berjaga-jaga
                System.out.println("  [KEJUTAN] " + e.getMessage());
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("=== VERSI MELANGGAR LSP ===");
        System.out.println("Melepas semua Burung ke udara:");
        lepasKeUdara(List.of(new Burung("Merpati"), new Burung("Elang"), new Penguin("Penguin")));

        System.out.println();
        System.out.println("=== VERSI SESUAI LSP ===");
        BurungTerbang merpati = new BurungTerbang("Merpati");
        BurungTerbang elang = new BurungTerbang("Elang");
        PenguinKutub penguin = new PenguinKutub("Penguin");

        System.out.println("Janji BurungDasar: bisa bertelur");
        List<BurungDasar> semuaBurung = List.of(merpati, elang, penguin); // [4]
        for (BurungDasar burung : semuaBurung) {
            System.out.println("  " + burung.bertelur());
        }

        System.out.println("Janji BurungTerbang: bisa terbang");
        List<BurungTerbang> penerbang = List.of(merpati, elang); // [5]
        for (BurungTerbang burung : penerbang) {
            System.out.println("  " + burung.terbang());
        }

        System.out.println("Kemampuan khusus penguin:");
        System.out.println("  " + penguin.berenang());
        System.out.println("Tidak ada kejutan: setiap kelas anak menepati janji induknya.");
    }
}

// ------------------------------------------------------------ MELANGGAR LSP
/** Janji kelas induk: setiap burung bisa terbang. */
class Burung {
    private String nama;

    public Burung(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public String terbang() {
        return nama + " terbang tinggi";
    }
}

class Penguin extends Burung {
    public Penguin(String nama) {
        super(nama);
    }

    @Override
    public String terbang() { // [1] meng-override hanya untuk menolak
        throw new UnsupportedOperationException(getNama() + " tidak bisa terbang");
    }
}

// -------------------------------------------------------------- SESUAI LSP
/** Hanya berisi janji yang ditepati SEMUA burung. */
class BurungDasar {
    private String nama;

    public BurungDasar(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public String bertelur() {
        return nama + " bertelur";
    }
}

/** Janji tambahan: burung jenis ini benar-benar bisa terbang. */
class BurungTerbang extends BurungDasar {
    public BurungTerbang(String nama) {
        super(nama);
    }

    public String terbang() {
        return getNama() + " terbang tinggi";
    }
}

class PenguinKutub extends BurungDasar { // [3] tidak mewarisi janji terbang
    public PenguinKutub(String nama) {
        super(nama);
    }

    public String berenang() {
        return getNama() + " berenang di air dingin";
    }
}
