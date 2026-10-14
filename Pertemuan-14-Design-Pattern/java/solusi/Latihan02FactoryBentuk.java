/*
 * Solusi Latihan 02 - Factory Bangun Datar
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Ide penyelesaian:
 * - Kelas abstrak Bentuk punya dua method abstrak: nama() dan luas().
 * - Tiga kelas konkret: Persegi, PersegiPanjang, Segitiga.
 * - BentukFactory.buat(jenis, a, b) adalah SATU-SATUNYA tempat yang memilih
 *   kelas mana yang dibuat. Jenis yang tidak dikenal -> IllegalArgumentException.
 * - Program utama hanya mengenal Bentuk dan BentukFactory.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02FactoryBentuk.java
 */
public class Latihan02FactoryBentuk {

    public static void main(String[] args) {
        String[] daftarJenis = {"persegi", "Persegi Panjang", "SEGITIGA", "lingkaran"};
        int[][] daftarUkuran = {{5, 0}, {8, 3}, {6, 4}, {7, 0}};
        int totalLuas = 0;

        System.out.println("=== MEMBUAT BENTUK DARI PILIHAN TEKS ===");
        for (int i = 0; i < daftarJenis.length; i++) {
            Bentuk bentuk;
            try {
                bentuk = BentukFactory.buat(daftarJenis[i], daftarUkuran[i][0],
                        daftarUkuran[i][1]);
            } catch (IllegalArgumentException e) {
                System.out.println("Ditolak: " + e.getMessage());
                continue;
            }
            System.out.println(String.format("%-30s luas ", bentuk.nama()) + bentuk.luas());
            totalLuas += bentuk.luas();
        }

        System.out.println();
        System.out.println("Total luas bentuk yang berhasil dibuat: " + totalLuas);
    }
}

/** Produk abstrak: bangun datar. */
abstract class Bentuk {
    public abstract String nama();

    public abstract int luas();
}

class Persegi extends Bentuk {
    private int sisi;

    Persegi(int sisi) {
        this.sisi = sisi;
    }

    @Override
    public String nama() {
        return "Persegi sisi " + sisi;
    }

    @Override
    public int luas() {
        return sisi * sisi;
    }
}

class PersegiPanjang extends Bentuk {
    private int panjang;
    private int lebar;

    PersegiPanjang(int panjang, int lebar) {
        this.panjang = panjang;
        this.lebar = lebar;
    }

    @Override
    public String nama() {
        return "Persegi panjang " + panjang + " x " + lebar;
    }

    @Override
    public int luas() {
        return panjang * lebar;
    }
}

class Segitiga extends Bentuk {
    private int alas;
    private int tinggi;

    Segitiga(int alas, int tinggi) {
        this.alas = alas;
        this.tinggi = tinggi;
    }

    @Override
    public String nama() {
        return "Segitiga alas " + alas + " tinggi " + tinggi;
    }

    @Override
    public int luas() {
        return alas * tinggi / 2;
    }
}

/** Simple Factory untuk bangun datar. */
class BentukFactory {

    /** a dan b adalah ukuran; b tidak dipakai oleh persegi. */
    public static Bentuk buat(String jenis, int a, int b) {
        if (jenis.equalsIgnoreCase("persegi")) {
            return new Persegi(a);
        }
        if (jenis.equalsIgnoreCase("persegi panjang")) {
            return new PersegiPanjang(a, b);
        }
        if (jenis.equalsIgnoreCase("segitiga")) {
            return new Segitiga(a, b);
        }
        throw new IllegalArgumentException("Bentuk tidak dikenal: " + jenis);
    }
}
