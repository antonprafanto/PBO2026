/** Menu kategori minuman. Tambahan: disajikan dingin atau panas. */
public class Minuman extends Menu {
    private boolean dingin;

    public Minuman(String kode, String nama, int harga, int stok, boolean dingin) {
        super(kode, nama, harga, "Minuman", stok);
        this.dingin = dingin;
    }

    /** Versi overload: tanpa parameter dingin, minuman dianggap disajikan dingin. */
    public Minuman(String kode, String nama, int harga, int stok) {
        this(kode, nama, harga, stok, true);
    }

    public boolean isDingin() {
        return dingin;
    }

    @Override
    public String toString() {
        String suhu = dingin ? "dingin" : "panas";
        return super.toString() + " | " + suhu;
    }
}
