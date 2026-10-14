package kedaikita;

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
    public void proses(int total) throws PembayaranGagalException {
        if (uangDiterima < total) {
            int kurang = total - uangDiterima;
            throw new PembayaranGagalException(namaMetode(),
                    "uang kurang " + Rupiah.format(kurang));
        }
        kembalian = uangDiterima - total;
        System.out.println("  Uang diterima " + Rupiah.format(uangDiterima)
                + ", kembalian " + Rupiah.format(kembalian));
    }
}
