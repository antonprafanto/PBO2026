/*
 * Contoh 03 - Sisi Gelap Singleton: State Global yang Diam-Diam Berubah
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Singleton praktis, tetapi isinya adalah STATE GLOBAL: siapa pun bisa
 * mengubahnya dari mana pun. Akibatnya:
 * - method yang memakainya punya "ketergantungan tersembunyi" (tidak terlihat
 *   dari parameternya),
 * - hasil pengujian bisa bergantung pada URUTAN uji dijalankan.
 *
 * Solusinya (ingat dependency injection di Pertemuan 13): kirim kebutuhan lewat
 * parameter atau konstruktor sehingga setiap pengujian bisa memakai nilainya sendiri.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03BahayaStateGlobal.java
 */
public class Contoh03BahayaStateGlobal {

    static int hargaAkhir(int harga) {
        // [1] ketergantungan tersembunyi: tidak terlihat dari parameternya
        int persen = PengaturanPajak.getInstance().getPersen();
        return harga + harga * persen / 100;
    }

    /** Rp10000 ditambah pajak 10% harus menjadi Rp11000. */
    static String ujiHargaNormal() {
        int hasil = hargaAkhir(10000);
        return hasil == 11000 ? "LULUS" : "GAGAL (dapat Rp" + hasil + ")";
    }

    /** Saat acara bebas pajak, Rp10000 harus tetap Rp10000. */
    static String ujiAcaraBebasPajak() {
        PengaturanPajak.getInstance().setPersen(0); // [2] mengubah state global...
        int hasil = hargaAkhir(10000);              // ...dan lupa mengembalikannya
        return hasil == 10000 ? "LULUS" : "GAGAL (dapat Rp" + hasil + ")";
    }

    public static void main(String[] args) {
        System.out.println("=== PUTARAN 1: DUA UJI DIJALANKAN ===");
        System.out.println("Uji harga normal      : " + ujiHargaNormal());
        System.out.println("Uji acara bebas pajak : " + ujiAcaraBebasPajak());

        System.out.println();
        System.out.println("=== PUTARAN 2: UJI YANG SAMA DIULANG ===");
        System.out.println("Uji harga normal      : " + ujiHargaNormal()); // [4] kini gagal!
        System.out.println("Pajak sekarang " + PengaturanPajak.getInstance().getPersen()
                + "%, sisa perubahan uji sebelumnya");

        System.out.println();
        System.out.println("=== SOLUSI: KIRIM NILAINYA LEWAT KONSTRUKTOR ===");
        KalkulatorHarga normal = new KalkulatorHarga(10); // [5] setiap uji punya objeknya sendiri
        KalkulatorHarga bebasPajak = new KalkulatorHarga(0);
        System.out.println("Pajak 10%: Rp10000 -> Rp" + normal.hargaAkhir(10000));
        System.out.println("Pajak 0% : Rp10000 -> Rp" + bebasPajak.hargaAkhir(10000));
        System.out.println("Diulang  : Rp10000 -> Rp" + normal.hargaAkhir(10000)
                + " (tetap benar)");
    }
}

/** Singleton: persentase pajak untuk seluruh program. */
class PengaturanPajak {
    private static PengaturanPajak instance = null;

    private int persen = 10;

    private PengaturanPajak() {
    }

    public static PengaturanPajak getInstance() {
        if (instance == null) {
            instance = new PengaturanPajak();
        }
        return instance;
    }

    public int getPersen() {
        return persen;
    }

    public void setPersen(int persen) {
        this.persen = persen;
    }
}

/** [3] Solusi: persen pajak DIKIRIM lewat konstruktor (dependency injection). */
class KalkulatorHarga {
    private int persenPajak;

    KalkulatorHarga(int persenPajak) {
        this.persenPajak = persenPajak;
    }

    public int hargaAkhir(int harga) {
        return harga + harga * persenPajak / 100;
    }
}
