/*
 * Contoh 05 - Interface: Kontrak Kemampuan
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * Java punya kata kunci khusus interface. Method di dalam interface yang
 * ditulis tanpa isi otomatis public dan abstract. Kelas yang menulis
 * "implements BisaDinyalakan" WAJIB mengisi semua method tersebut.
 *
 * Lampu, KomporGas, dan Televisi tidak bersaudara: ketiganya tidak punya
 * kelas induk bersama selain kontrak BisaDinyalakan. Method matikanSemua()
 * cukup mengenal kontraknya, tidak perlu tahu jenis asli objeknya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05Interface.java
 */
import java.util.List;

public class Contoh05Interface {

    /** Mematikan semua benda yang masih menyala, apa pun jenisnya. */
    public static void matikanSemua(List<BisaDinyalakan> daftar) { // [3] tipe: interface
        System.out.println("Memeriksa " + daftar.size() + " benda...");
        for (BisaDinyalakan benda : daftar) {
            if (benda.sedangMenyala()) { // [4] yang dipakai hanya method dari kontrak
                benda.matikan();
            }
        }
        System.out.println("Semua sudah padam. Aman!");
    }

    public static void main(String[] args) {
        Lampu lampu = new Lampu("teras");
        KomporGas kompor = new KomporGas();
        Televisi tv = new Televisi(5);

        System.out.println("=== PAGI HARI ===");
        lampu.nyalakan();
        kompor.nyalakan();
        tv.nyalakan();
        tv.matikan();

        System.out.println();
        System.out.println("=== SEBELUM BERANGKAT KULIAH ===");
        matikanSemua(List.of(lampu, kompor, tv));
    }
}

/** Kontrak: benda ini bisa dinyalakan dan dimatikan. */
interface BisaDinyalakan { // [1] interface: daftar kemampuan tanpa isi
    void nyalakan();

    void matikan();

    boolean sedangMenyala();
}

/** Lampu di sebuah ruangan. */
class Lampu implements BisaDinyalakan { // [2] memenuhi kontrak dengan implements
    private String ruangan;
    private boolean menyala;

    public Lampu(String ruangan) {
        this.ruangan = ruangan;
        this.menyala = false;
    }

    @Override
    public void nyalakan() {
        menyala = true;
        System.out.println("Lampu " + ruangan + " menyala");
    }

    @Override
    public void matikan() {
        menyala = false;
        System.out.println("Lampu " + ruangan + " padam");
    }

    @Override
    public boolean sedangMenyala() {
        return menyala;
    }
}

/** Kompor gas: bukan alat listrik, tetapi juga bisa dinyalakan. */
class KomporGas implements BisaDinyalakan {
    private boolean apiMenyala;

    public KomporGas() {
        this.apiMenyala = false;
    }

    @Override
    public void nyalakan() {
        apiMenyala = true;
        System.out.println("Kompor gas: klik... api biru menyala");
    }

    @Override
    public void matikan() {
        apiMenyala = false;
        System.out.println("Kompor gas: api dimatikan, katup gas ditutup");
    }

    @Override
    public boolean sedangMenyala() {
        return apiMenyala;
    }
}

/** Televisi dengan nomor saluran. */
class Televisi implements BisaDinyalakan {
    private int saluran;
    private boolean menyala;

    public Televisi(int saluran) {
        this.saluran = saluran;
        this.menyala = false;
    }

    @Override
    public void nyalakan() {
        menyala = true;
        System.out.println("TV menyala di saluran " + saluran);
    }

    @Override
    public void matikan() {
        menyala = false;
        System.out.println("TV dimatikan");
    }

    @Override
    public boolean sedangMenyala() {
        return menyala;
    }
}
