/*
 * Contoh 06 - throw: Melempar dan Melempar Ulang
 * Pertemuan 11 - Exception Handling
 *
 * - throw new IllegalArgumentException("pesan") MELEMPAR exception buatan
 *   kita sendiri. Kita memakainya untuk menolak data yang tidak masuk akal
 *   (validasi), seperti di Pertemuan 04.
 * - throw e; di dalam blok catch MELEMPAR ULANG exception yang sedang
 *   ditangani. Polanya: "catat dulu, lalu teruskan ke pemanggil".
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06ThrowDanLemparUlang.java
 */
public class Contoh06ThrowDanLemparUlang {

    /** Meneruskan perintah ke AC. Penolakan dicatat, lalu dilempar ulang. */
    static void tekanRemote(AC ac, int suhu) {
        try {
            ac.aturSuhu(suhu);
        } catch (IllegalArgumentException e) {
            System.out.println("  [log] perintah " + suhu + " derajat ditolak"); // [4] catat...
            throw e; // [5] ...lalu lempar ulang exception yang SAMA ke pemanggil
        }
    }

    public static void main(String[] args) {
        AC ac = new AC("Lab Komputer 2");
        System.out.println("=== REMOTE AC (suhu awal " + ac.getSuhu() + " derajat) ===");
        int[] daftarSuhu = {22, 10, 35, 18};
        for (int suhu : daftarSuhu) {
            try {
                tekanRemote(ac, suhu);
                System.out.println("Suhu diatur ke " + suhu + " derajat");
            } catch (IllegalArgumentException e) { // [6] pesan dari throw ikut terbawa
                System.out.println("Layar remote: " + e.getMessage());
            }
        }
        System.out.println("Suhu akhir: " + ac.getSuhu() + " derajat");
    }
}

/** AC ruangan dengan batas suhu 16 sampai 30 derajat. */
class AC {
    public static final int SUHU_MIN = 16;
    public static final int SUHU_MAKS = 30;

    private String ruangan;
    private int suhu;

    public AC(String ruangan) {
        this.ruangan = ruangan;
        this.suhu = 25;
    }

    public int getSuhu() {
        return suhu;
    }

    public void aturSuhu(int suhu) {
        if (suhu < SUHU_MIN || suhu > SUHU_MAKS) { // [1] periksa lebih dulu
            throw new IllegalArgumentException("Suhu " + suhu + " di luar batas "
                    + SUHU_MIN + "-" + SUHU_MAKS + " derajat"); // [2]
        }
        this.suhu = suhu; // [3] hanya dijalankan jika lolos pemeriksaan
    }
}
