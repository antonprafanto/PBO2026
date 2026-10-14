/** Dilempar saat jumlah yang dipesan melebihi stok. */
public class StokTidakCukupException extends KedaiException {
    private static final long serialVersionUID = 1L; // lihat KedaiException.java

    private String namaMenu;
    private int diminta;
    private int tersedia;

    public StokTidakCukupException(String namaMenu, int diminta, int tersedia) {
        super("Stok " + namaMenu + " tidak cukup: "
                + "diminta " + diminta + ", tersedia " + tersedia);
        this.namaMenu = namaMenu;
        this.diminta = diminta;
        this.tersedia = tersedia;
    }

    public String getNamaMenu() {
        return namaMenu;
    }

    public int getDiminta() {
        return diminta;
    }

    public int getTersedia() {
        return tersedia;
    }
}
