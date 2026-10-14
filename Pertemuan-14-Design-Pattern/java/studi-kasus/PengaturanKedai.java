/*
 * File PengaturanKedai.java: kelas PengaturanKedai dengan pola SINGLETON.
 *
 * Singleton menjamin hanya ada SATU objek pengaturan di seluruh program.
 * Bagian program yang membutuhkannya (pesanan dan struk) membaca nama kedai,
 * alamat, dan persentase pajak dari objek yang sama sehingga tidak mungkin berbeda.
 *
 * Cara memakainya:
 *     PengaturanKedai pengaturan = PengaturanKedai.getInstance();
 */

/** Pengaturan global KedaiKita (Singleton). */
public class PengaturanKedai {
    private static PengaturanKedai instance = null; // tempat menyimpan satu-satunya objek

    private String namaKedai;
    private String alamat;
    private int pajakPersen;

    // Konstruktor PRIVATE: kode di luar kelas ini tidak bisa menulis
    // new PengaturanKedai(). Satu-satunya jalan adalah getInstance().
    private PengaturanKedai() {
        this.namaKedai = "KedaiKita";
        this.alamat = "Jl. Pramuka No. 10, Samarinda";
        this.pajakPersen = 10; // Pajak Barang dan Jasa Tertentu (PBJT) 10%
    }

    /** Mengembalikan satu-satunya objek; dibuat saat pertama kali diminta. */
    public static PengaturanKedai getInstance() {
        if (instance == null) {
            instance = new PengaturanKedai();
        }
        return instance;
    }

    public String getNamaKedai() {
        return namaKedai;
    }

    public String getAlamat() {
        return alamat;
    }

    public int getPajakPersen() {
        return pajakPersen;
    }

    public void setPajakPersen(int pajakPersen) {
        if (pajakPersen < 0 || pajakPersen > 100) {
            throw new IllegalArgumentException("Pajak harus 0 sampai 100 persen");
        }
        this.pajakPersen = pajakPersen;
    }
}
