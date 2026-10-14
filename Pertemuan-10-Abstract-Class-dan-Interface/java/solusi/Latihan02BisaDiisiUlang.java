/*
 * Solusi Latihan 02 - Interface BisaDiisiUlang
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * Ide penyelesaian:
 * - BisaDiisiUlang adalah interface: daftar kemampuan tanpa isi.
 * - Tiga alat yang tidak bersaudara meng-implements kontrak itu dengan caranya
 *   sendiri (kecepatan isi daya berbeda), tetapi baterai tidak boleh > 100%.
 * - tampilkanStatus() dan isiSemua() hanya mengenal interface-nya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02BisaDiisiUlang.java
 */
import java.util.List;

public class Latihan02BisaDiisiUlang {

    public static void tampilkanStatus(List<BisaDiisiUlang> daftar) {
        for (BisaDiisiUlang alat : daftar) {
            System.out.println(alat.namaAlat() + ": " + alat.persenBaterai() + "%");
        }
    }

    public static void isiSemua(List<BisaDiisiUlang> daftar, int menit) {
        for (BisaDiisiUlang alat : daftar) {
            alat.isiDaya(menit);
        }
    }

    public static void main(String[] args) {
        List<BisaDiisiUlang> daftar = List.of(
                new SepedaListrik(20),
                new Powerbank(50),
                new SikatGigiElektrik(90));
        System.out.println("=== SEBELUM DIISI ===");
        tampilkanStatus(daftar);

        System.out.println();
        System.out.println("=== SETELAH DIISI 30 MENIT ===");
        isiSemua(daftar, 30);
        tampilkanStatus(daftar);

        int penuh = 0;
        for (BisaDiisiUlang alat : daftar) {
            if (alat.persenBaterai() == 100) {
                penuh++;
            }
        }
        System.out.println("Sudah penuh: " + penuh + " dari " + daftar.size() + " alat");
    }
}

/** Kontrak: alat yang baterainya bisa diisi ulang. */
interface BisaDiisiUlang {
    String namaAlat();

    int persenBaterai();

    void isiDaya(int menit);
}

/** Baterai besar: naik 1% per menit. */
class SepedaListrik implements BisaDiisiUlang {
    private int baterai;

    public SepedaListrik(int baterai) {
        this.baterai = baterai;
    }

    @Override
    public String namaAlat() {
        return "Sepeda listrik";
    }

    @Override
    public int persenBaterai() {
        return baterai;
    }

    @Override
    public void isiDaya(int menit) {
        baterai = Math.min(100, baterai + menit * 1);
    }
}

/** Naik 2% per menit. */
class Powerbank implements BisaDiisiUlang {
    private int baterai;

    public Powerbank(int baterai) {
        this.baterai = baterai;
    }

    @Override
    public String namaAlat() {
        return "Powerbank";
    }

    @Override
    public int persenBaterai() {
        return baterai;
    }

    @Override
    public void isiDaya(int menit) {
        baterai = Math.min(100, baterai + menit * 2);
    }
}

/** Baterai kecil: naik 5% per menit. */
class SikatGigiElektrik implements BisaDiisiUlang {
    private int baterai;

    public SikatGigiElektrik(int baterai) {
        this.baterai = baterai;
    }

    @Override
    public String namaAlat() {
        return "Sikat gigi elektrik";
    }

    @Override
    public int persenBaterai() {
        return baterai;
    }

    @Override
    public void isiDaya(int menit) {
        baterai = Math.min(100, baterai + menit * 5);
    }
}
