/*
 * Solusi Latihan 01 - Pengatur Suhu AC
 * Pertemuan 04 - Enkapsulasi
 *
 * Ide penyelesaian:
 * - Semua field private: ruangan dan suhu.
 * - ruangan cukup punya getter (tanpa setter), jadi read-only dari luar.
 * - suhu punya getter dan setter. Setter menolak suhu di luar batas dengan
 *   throw new IllegalArgumentException.
 * - Konstruktor mengisi suhu LEWAT setter (setSuhu(suhu)), sehingga AC
 *   dengan suhu awal yang salah juga ditolak.
 * - Batas suhu disimpan sebagai konstanta (static final). Konstanta boleh
 *   public karena nilainya memang tidak bisa diubah oleh siapa pun.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan01AC.java
 */
public class Latihan01AC {

    public static void main(String[] args) {
        AC ac = new AC("Ruang Dosen", 24);
        System.out.println("=== AC RUANG DOSEN ===");
        System.out.println("Suhu awal: " + ac.getSuhu() + " derajat");
        ac.setSuhu(20);
        System.out.println("Suhu diatur ke " + ac.getSuhu() + " derajat");
        try {
            ac.setSuhu(10);
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        try {
            ac.setSuhu(35);
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        System.out.println("Suhu sekarang: " + ac.getSuhu() + " derajat");

        System.out.println();
        System.out.println("=== MEMASANG AC BARU ===");
        try {
            AC lab = new AC("Lab Komputer", 40);
            System.out.println("AC " + lab.getRuangan() + " terpasang");
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal memasang AC: " + e.getMessage());
        }
    }
}

/** Pendingin ruangan yang suhunya hanya bisa diatur 16-30 derajat. */
class AC {
    public static final int SUHU_MIN = 16; // konstanta: static final, tidak bisa diubah
    public static final int SUHU_MAKS = 30;

    private String ruangan;
    private int suhu;

    public AC(String ruangan, int suhu) {
        this.ruangan = ruangan;
        setSuhu(suhu); // lewat setter, jadi ikut diperiksa
    }

    public String getRuangan() {
        return ruangan;
    }

    public int getSuhu() {
        return suhu;
    }

    public void setSuhu(int suhu) {
        if (suhu < SUHU_MIN || suhu > SUHU_MAKS) {
            throw new IllegalArgumentException("Suhu harus " + SUHU_MIN + "-" + SUHU_MAKS
                    + " derajat, bukan " + suhu);
        }
        this.suhu = suhu;
    }
}
