/** Dilempar saat pembayaran tidak bisa diselesaikan. */
public class PembayaranGagalException extends KedaiException {
    private static final long serialVersionUID = 1L; // lihat KedaiException.java

    private String metode;
    private String alasan;

    public PembayaranGagalException(String metode, String alasan) {
        super("Pembayaran " + metode + " gagal: " + alasan);
        this.metode = metode;
        this.alasan = alasan;
    }

    public String getMetode() {
        return metode;
    }

    public String getAlasan() {
        return alasan;
    }
}
