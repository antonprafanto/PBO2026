/*
 * Contoh 05 - Factory Method (versi GoF): Subclass yang Memilih Produknya
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Bedanya dengan Simple Factory (contoh 04):
 * - Simple Factory : SATU method (biasanya static) berisi if/else yang memilih
 *                    kelas mana yang dibuat.
 * - Factory Method : kelas induk punya method abstrak buatAngkutan(). Setiap
 *                    SUBCLASS meng-override-nya untuk membuat produk yang
 *                    berbeda. Kelas induk memakai produk itu tanpa tahu kelas
 *                    konkretnya. Tidak ada if/else sama sekali.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05FactoryMethod.java
 */
public class Contoh05FactoryMethod {

    public static void main(String[] args) {
        System.out.println("=== FACTORY METHOD: SUBCLASS MEMILIH ANGKUTANNYA ===");
        Ekspedisi darat = new EkspedisiDarat();
        Ekspedisi sungai = new EkspedisiSungai();
        darat.kirimPaket("Balikpapan"); // [4] method sama, angkutan berbeda
        sungai.kirimPaket("Tenggarong");
    }
}

/** Produk: sesuatu yang bisa mengantar paket. */
interface Angkutan {
    String antar(String tujuan);
}

class Truk implements Angkutan {
    @Override
    public String antar(String tujuan) {
        return "Truk melaju lewat jalan darat menuju " + tujuan;
    }
}

class KapalSungai implements Angkutan {
    @Override
    public String antar(String tujuan) {
        return "Kapal menyusuri Sungai Mahakam menuju " + tujuan;
    }
}

/** Langkah kerja tetap, tetapi produk angkutannya diserahkan ke subclass. */
abstract class Ekspedisi {
    public abstract String nama();

    public abstract Angkutan buatAngkutan(); // [1] inilah FACTORY METHOD

    public void kirimPaket(String tujuan) { // [2] memakai produk tanpa tahu kelasnya
        System.out.println("[" + nama() + "] Paket ke " + tujuan + " dikemas");
        Angkutan angkutan = buatAngkutan();
        System.out.println("  " + angkutan.antar(tujuan));
        System.out.println("  Paket tiba di " + tujuan);
    }
}

class EkspedisiDarat extends Ekspedisi {
    @Override
    public String nama() {
        return "Ekspedisi Darat";
    }

    @Override
    public Angkutan buatAngkutan() { // [3] subclass memilih produknya
        return new Truk();
    }
}

class EkspedisiSungai extends Ekspedisi {
    @Override
    public String nama() {
        return "Ekspedisi Sungai";
    }

    @Override
    public Angkutan buatAngkutan() {
        return new KapalSungai();
    }
}
