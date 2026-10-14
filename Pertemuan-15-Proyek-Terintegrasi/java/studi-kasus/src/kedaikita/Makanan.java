package kedaikita;

/** Menu kategori makanan. Tambahan: level pedas 0 sampai 5. */
public class Makanan extends Menu {
    private int levelPedas;

    public Makanan(String kode, String nama, int harga, int stok, int levelPedas) {
        // Panggil konstruktor induk. Kategori diisi otomatis "Makanan".
        super(kode, nama, harga, "Makanan", stok);
        setLevelPedas(levelPedas); // lewat setter, jadi ikut divalidasi
    }

    /** Versi overload: tanpa parameter levelPedas, makanan dianggap tidak pedas (level 0). */
    public Makanan(String kode, String nama, int harga, int stok) {
        this(kode, nama, harga, stok, 0);
    }

    public int getLevelPedas() {
        return levelPedas;
    }

    // final: setter ini tidak bisa di-override oleh kelas anak,
    // sehingga aman dipanggil dari konstruktor.
    public final void setLevelPedas(int levelPedas) {
        if (levelPedas < 0 || levelPedas > 5) {
            throw new IllegalArgumentException("Level pedas harus 0 sampai 5");
        }
        this.levelPedas = levelPedas;
    }

    @Override
    public String toString() {
        // Override: pakai teks dari induk, lalu tambahkan info pedas
        return super.toString() + " | pedas level " + levelPedas;
    }
}
