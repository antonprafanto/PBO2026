package kedaikita;

/** Dilempar saat isi file data tidak sesuai format yang diharapkan. */
public class FormatDataException extends KedaiException {
    private static final long serialVersionUID = 1L; // lihat KedaiException.java

    public FormatDataException(String pesan) {
        super(pesan);
    }
}
