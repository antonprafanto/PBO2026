/*
 * Contoh 02 - Kelas Abstrak Pertamamu
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * - Bentuk diberi kata kunci abstract: kelas abstrak.
 * - luas() dan keliling() adalah method abstrak: hanya "janji" tanpa isi,
 *   diakhiri titik koma. Setiap kelas anak WAJIB mengisinya.
 * - Objek Bentuk tidak bisa dibuat langsung. Objek kelas anaknya bisa.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02KelasAbstrak.java
 */
import java.util.List;

public class Contoh02KelasAbstrak {

    public static String yaTidak(boolean nilai) {
        return nilai ? "ya" : "tidak";
    }

    public static void main(String[] args) {
        // Bentuk bentukUmum = new Bentuk(); // [4] hapus // di awal baris ini -> error kompilasi

        PersegiPanjang kartu = new PersegiPanjang(8, 5);
        SegitigaSiku penggaris = new SegitigaSiku(6, 8, 10);
        List<Bentuk> daftar = List.of(kartu, penggaris); // [5] list bertipe kelas abstrak

        System.out.println("=== DAFTAR BENTUK ===");
        for (Bentuk bentuk : daftar) {
            String nama = bentuk.getClass().getSimpleName();
            System.out.println(nama + ": luas " + bentuk.luas() + " cm2, keliling "
                    + bentuk.keliling() + " cm");
        }

        System.out.println();
        System.out.println("=== CEK JENIS ===");
        System.out.println("kartu dibuat dari kelas: " + kartu.getClass().getSimpleName());
        boolean termasukBentuk = kartu instanceof Bentuk; // [6]
        System.out.println("Apakah kartu termasuk Bentuk? " + yaTidak(termasukBentuk));
    }
}

/** Kelas abstrak: konsep umum semua bangun datar. */
abstract class Bentuk { // [1] kata kunci abstract -> kelas abstrak

    /** Menghitung luas (cm2). */
    public abstract int luas(); // [2] method abstrak: tanpa isi, diakhiri titik koma

    /** Menghitung keliling (cm). */
    public abstract int keliling();
}

/** Persegi panjang dengan panjang dan lebar. */
class PersegiPanjang extends Bentuk {
    private int panjang;
    private int lebar;

    public PersegiPanjang(int panjang, int lebar) {
        this.panjang = panjang;
        this.lebar = lebar;
    }

    @Override
    public int luas() { // [3] mengisi (meng-override) method abstrak
        return panjang * lebar;
    }

    @Override
    public int keliling() {
        return 2 * (panjang + lebar);
    }
}

/** Segitiga siku-siku dengan alas, tinggi, dan sisi miring. */
class SegitigaSiku extends Bentuk {
    private int alas;
    private int tinggi;
    private int miring;

    public SegitigaSiku(int alas, int tinggi, int miring) {
        this.alas = alas;
        this.tinggi = tinggi;
        this.miring = miring;
    }

    @Override
    public int luas() {
        return alas * tinggi / 2;
    }

    @Override
    public int keliling() {
        return alas + tinggi + miring;
    }
}
