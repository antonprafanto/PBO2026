/** Factory: membuat objek Pembayaran berdasarkan pilihan (teks). */
public class PembayaranFactory {

    /** nominal = uang diterima (tunai) atau saldo e-wallet (qris). */
    public static Pembayaran buat(String jenis, int nominal, String bank) {
        // equalsIgnoreCase: huruf besar/kecil dianggap sama ("QRIS" = "qris").
        if (jenis.equalsIgnoreCase("tunai")) {
            return new PembayaranTunai(nominal);
        }
        if (jenis.equalsIgnoreCase("qris")) {
            return new PembayaranQRIS(nominal);
        }
        if (jenis.equalsIgnoreCase("kartu")) {
            return new PembayaranKartu(bank);
        }
        throw new IllegalArgumentException("Metode pembayaran tidak dikenal: " + jenis);
    }
}
