/** Bayar dengan uang tunai. Bisa menghasilkan kembalian. */
public class PembayaranTunai extends Pembayaran {
    private int uangDiterima;
    private int kembalian;

    public PembayaranTunai(int uangDiterima) {
        this.uangDiterima = uangDiterima;
        this.kembalian = 0;
    }

    public int getKembalian() {
        return kembalian;
    }

    @Override
    public String namaMetode() {
        return "Tunai";
    }

    @Override
    public boolean proses(int total) {
        if (uangDiterima < total) {
            int kurang = total - uangDiterima;
            System.out.println("  Uang kurang " + Rupiah.format(kurang));
            return false;
        }
        kembalian = uangDiterima - total;
        System.out.println("  Uang diterima " + Rupiah.format(uangDiterima)
                + ", kembalian " + Rupiah.format(kembalian));
        return true;
    }
}
