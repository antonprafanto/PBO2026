/*
 * File Pembayaran.java: kelas induk Pembayaran. Tiga kelas anaknya ada di
 * PembayaranTunai.java, PembayaranQRIS.java, dan PembayaranKartu.java.
 *
 * Ketiga kelas anak meng-override method yang SAMA (namaMetode,
 * hitungBiayaLayanan, proses) dengan perilaku yang BERBEDA.
 * Pesanan cukup memanggil pembayaran.proses(...) tanpa perlu tahu
 * jenis pembayarannya. Itulah polimorfisme.
 */

/** Kelas induk semua metode pembayaran. */
public class Pembayaran {

    public String namaMetode() {
        return "Pembayaran umum";
    }

    /** Biaya tambahan yang dibebankan ke pelanggan. Bawaannya 0. */
    public int hitungBiayaLayanan(int total) {
        return 0;
    }

    /** Memproses pembayaran. Mengembalikan true jika berhasil. */
    public boolean proses(int total) {
        System.out.println("  Memproses pembayaran " + Rupiah.format(total));
        return true;
    }
}
