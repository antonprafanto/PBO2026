/*
 * Contoh 05 - protected: Field yang Boleh Dipakai Kelas Anak
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * - private   : hanya kelas itu sendiri. Kelas anak pun TIDAK boleh menyentuh.
 * - protected : kelas itu sendiri, kelas anak, DAN semua kelas di paket yang sama.
 *
 * Bagian terakhir program ini membaca field protected dari main. Itu diizinkan
 * karena main berada di paket yang sama (paket tanpa nama), bukan karena main
 * kelas anak. Inilah jebakan protected yang sering terlupa.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05AksesKelasAnak.java
 */
public class Contoh05AksesKelasAnak {

    public static void main(String[] args) {
        RekeningTabungan tabungan = new RekeningTabungan("Siti", 1000000, 2);

        System.out.println("=== TABUNGAN SITI ===");
        System.out.println(tabungan.info());
        System.out.println("Bunga bulan ini: Rp" + tabungan.tambahBunga());
        System.out.println(tabungan.info());

        System.out.println();
        System.out.println("=== DIBACA DARI LUAR KELAS ===");
        System.out.println("Lewat pintu resmi  : Rp" + tabungan.getSaldo());
        System.out.println("Langsung ke atribut: Rp" + tabungan.saldo // [4] satu paket
                + " (bisa, tetapi hindari)");
    }
}

/** Kelas induk rekening. */
class RekeningBank {
    private String pemilik; // [1] private: kelas anak pun tidak bisa menyentuhnya
    protected int saldo; // [2] protected: boleh dipakai kelas anak (dan satu paket)

    public RekeningBank(String pemilik, int saldoAwal) {
        this.pemilik = pemilik;
        this.saldo = saldoAwal;
    }

    public int getSaldo() { // pintu resmi untuk membaca saldo dari luar
        return saldo;
    }

    public String info() {
        return "Rekening " + pemilik + ": saldo Rp" + saldo;
    }
}

/** Tabungan yang mendapat bunga bulanan (persen, bilangan bulat). */
class RekeningTabungan extends RekeningBank {
    private int bungaPersen;

    public RekeningTabungan(String pemilik, int saldoAwal, int bungaPersen) {
        super(pemilik, saldoAwal);
        this.bungaPersen = bungaPersen;
    }

    public int tambahBunga() {
        int bunga = saldo * bungaPersen / 100; // [3] membaca field protected induk
        saldo += bunga; // [3] mengubah field protected induk secara langsung
        return bunga;
    }
}
