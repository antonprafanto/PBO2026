/** Simulasi QRIS: saldo e-wallet pelanggan disimpan di objek ini. */
public class PembayaranQRIS extends Pembayaran {
    private int saldo;

    public PembayaranQRIS(int saldoEwallet) {
        this.saldo = saldoEwallet;
    }

    public int getSaldo() {
        return saldo;
    }

    @Override
    public String namaMetode() {
        return "QRIS";
    }

    @Override
    public void proses(int total) throws PembayaranGagalException {
        if (saldo < total) {
            String alasan = "saldo e-wallet tidak cukup "
                    + "(saldo " + Rupiah.format(saldo) + ")";
            throw new PembayaranGagalException(namaMetode(), alasan);
        }
        saldo -= total;
        System.out.println("  Saldo e-wallet terpotong " + Rupiah.format(total)
                + ", sisa " + Rupiah.format(saldo));
    }
}
