/*
 * Solusi Latihan 04 - Teko dan Gelas
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Ide penyelesaian:
 * - tuangKe(tujuan, jumlah) menerima OBJEK Wadah lain sebagai parameter dan
 *   mengubah isi KEDUA objek. Banyaknya yang benar-benar dituang adalah nilai
 *   terkecil dari: yang diminta, isi sumber, dan sisa ruang di tujuan.
 *   Math.min dan Math.max adalah method static bawaan Java.
 * - kosong() dan penuh() adalah method boolean (jawabannya ya/tidak).
 * - Konstruktor tanpa isi meneruskan ke konstruktor lengkap dengan this(..., 0).
 * - gelasTamu = gelasBima TIDAK membuat gelas baru. Keduanya menunjuk objek
 *   yang sama, jadi minum lewat gelasTamu ikut mengurangi isi gelasBima.
 * - Nilai boolean tidak dicetak mentah; method yaTidak() mengubahnya menjadi
 *   teks "ya" atau "tidak".
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04TekoDanGelas.java
 */
public class Latihan04TekoDanGelas {

    static String yaTidak(boolean nilai) {
        if (nilai) {
            return "ya";
        }
        return "tidak";
    }

    static void tuang(Wadah sumber, Wadah tujuan, int jumlah) {
        int dituang = sumber.tuangKe(tujuan, jumlah);
        System.out.println(sumber.nama + " -> " + tujuan.nama + ": diminta " + jumlah
                + " ml, dituang " + dituang + " ml");
    }

    public static void main(String[] args) {
        Wadah teko = new Wadah("Teko", 1000, 900);
        Wadah gelasAyu = new Wadah("Gelas Ayu", 250); // isi bawaan 0
        Wadah gelasBima = new Wadah("Gelas Bima", 250);

        System.out.println("=== KONDISI AWAL ===");
        System.out.println(teko);
        System.out.println(gelasAyu);
        System.out.println(gelasBima);

        System.out.println();
        System.out.println("=== MENUANG DARI TEKO ===");
        tuang(teko, gelasAyu, 300);
        tuang(teko, gelasBima, 200);
        tuang(teko, gelasBima, 100);
        System.out.println(teko);
        System.out.println("Gelas Ayu penuh? " + yaTidak(gelasAyu.penuh()));
        System.out.println("Teko kosong? " + yaTidak(teko.kosong()));

        System.out.println();
        System.out.println("=== GELAS BIMA DIPAKAI TAMU ===");
        Wadah gelasTamu = gelasBima; // bukan gelas baru, hanya nama lain
        gelasTamu.minum(150);
        System.out.println("Tamu minum 150 ml");
        System.out.println(gelasBima);
        System.out.println("Gelas Bima penuh? " + yaTidak(gelasBima.penuh()));
    }
}

/** Wadah minuman (teko, gelas, botol) dengan kapasitas dalam ml. */
class Wadah {
    String nama;
    int kapasitas;
    int isi;

    Wadah(String nama, int kapasitas, int isi) {
        this.nama = nama;
        this.kapasitas = kapasitas;
        this.isi = isi;
    }

    Wadah(String nama, int kapasitas) {
        this(nama, kapasitas, 0);
    }

    boolean kosong() {
        return isi == 0;
    }

    boolean penuh() {
        return isi == kapasitas;
    }

    int sisaRuang() {
        return kapasitas - isi;
    }

    /** Menuang ke wadah lain. Mengembalikan banyaknya ml yang dituang. */
    int tuangKe(Wadah tujuan, int jumlah) {
        int dituang = Math.min(jumlah, Math.min(isi, tujuan.sisaRuang()));
        isi = isi - dituang;
        tujuan.isi = tujuan.isi + dituang; // mengubah objek yang dikirim
        return dituang;
    }

    void minum(int jumlah) {
        isi = Math.max(0, isi - jumlah);
    }

    @Override
    public String toString() {
        return nama + ": " + isi + "/" + kapasitas + " ml";
    }
}
