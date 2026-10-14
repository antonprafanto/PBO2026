/*
 * Contoh 01 - Dari Diagram ke Kode: Kotak Kelas Lengkap
 * Pertemuan 06 - UML Class Diagram
 *
 * Kelas Paket di bawah ini adalah wujud kode dari kotak kelas berikut
 * (versi Java, ditulis dengan sintaks Mermaid):
 *
 *     class Paket {
 *         +TARIF_PER_KG : int = 8000$
 *         -penghitung : int = 0$
 *         -resi : String
 *         -tujuan : String
 *         -beratGram : int
 *         +Paket(tujuan: String, beratGram: int)
 *         +getResi() String
 *         +getTujuan() String
 *         -beratKg() int
 *         +hitungOngkir() int
 *         +jumlahPaket() int$
 *     }
 *
 * Tanda $ berarti static (milik kelas). Di diagram UML, anggota static
 * digambar dengan garis bawah.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01KotakKelas.java
 */
public class Contoh01KotakKelas {

    public static void main(String[] args) {
        System.out.println("=== PAKET MASUK ===");
        Paket[] daftarPaket = {
            new Paket("Samarinda", 1200),
            new Paket("Balikpapan", 500),
            new Paket("Bontang", 3000)
        };
        for (Paket paket : daftarPaket) {
            System.out.println(paket.getResi() + " ke " + paket.getTujuan()
                    + ": ongkir Rp" + paket.hitungOngkir());
        }

        System.out.println();
        System.out.println("=== DATA MILIK KELAS ===");
        System.out.println("Tarif per kg : Rp" + Paket.TARIF_PER_KG); // [9] static dibaca lewat kelas
        System.out.println("Jumlah paket : " + Paket.jumlahPaket());
    }
}

/** Paket kiriman di sebuah jasa ekspedisi. */
class Paket {
    public static final int TARIF_PER_KG = 8000; // [1] +TARIF_PER_KG : int = 8000$
    private static int penghitung = 0;           // [2] -penghitung : int = 0$

    private String resi;                         // [4] -resi : String
    private String tujuan;
    private int beratGram;

    public Paket(String tujuan, int beratGram) { // [3] +Paket(...)
        penghitung++;
        this.resi = String.format("KRM%03d", penghitung);
        this.tujuan = tujuan;
        this.beratGram = beratGram;
    }

    public String getResi() { // [5] +getResi() String
        return resi;
    }

    public String getTujuan() {
        return tujuan;
    }

    /** Berat dibulatkan ke atas per kilogram: 1200 gram dihitung 2 kg. */
    private int beratKg() { // [6] -beratKg() int (method privat)
        return (beratGram + 999) / 1000;
    }

    public int hitungOngkir() { // [7] +hitungOngkir() int
        return beratKg() * TARIF_PER_KG;
    }

    public static int jumlahPaket() { // [8] +jumlahPaket() int$ (method static)
        return penghitung;
    }
}
