/** Dilempar saat kode menu tidak terdaftar. */
public class MenuTidakDitemukanException extends KedaiException {
    private static final long serialVersionUID = 1L; // lihat KedaiException.java

    private String kode;

    public MenuTidakDitemukanException(String kode) {
        super("Menu dengan kode " + kode + " tidak ditemukan");
        this.kode = kode;
    }

    public String getKode() {
        return kode;
    }
}
