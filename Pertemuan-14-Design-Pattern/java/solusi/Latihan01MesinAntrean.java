/*
 * Solusi Latihan 01 - Mesin Antrean (Singleton)
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Ide penyelesaian:
 * - MesinAntrean adalah Singleton: hanya ada SATU mesin pembagi nomor, sehingga
 *   nomor dari pintu mana pun tidak pernah kembar.
 * - Konstruktornya private, jadi satu-satunya cara mendapatkan mesin adalah
 *   MesinAntrean.getInstance().
 * - TombolAntrean di setiap pintu TIDAK menyimpan mesin sendiri. Setiap kali
 *   ditekan, ia meminta mesin lewat getInstance().
 * - Nomor dibuat dengan format A001, A002, ... memakai String.format("A%03d", n).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan01MesinAntrean.java
 */
public class Latihan01MesinAntrean {

    public static void main(String[] args) {
        TombolAntrean utara = new TombolAntrean("Pintu Utara");
        TombolAntrean selatan = new TombolAntrean("Pintu Selatan");

        System.out.println("=== PENGUNJUNG MENGAMBIL NOMOR ===");
        utara.tekan();
        utara.tekan();
        selatan.tekan();
        utara.tekan();
        selatan.tekan();

        System.out.println();
        System.out.println("=== RINGKASAN ===");
        MesinAntrean mesin1 = MesinAntrean.getInstance();
        MesinAntrean mesin2 = MesinAntrean.getInstance();
        System.out.println("Mesin yang sama? " + (mesin1 == mesin2 ? "ya" : "tidak"));
        System.out.println("Total nomor dibagikan: " + mesin1.jumlahDibagikan());
    }
}

/** Singleton: satu-satunya mesin pembagi nomor antrean. */
class MesinAntrean {
    private static MesinAntrean instance = null;

    private int nomorTerakhir = 0;

    private MesinAntrean() {
    }

    public static MesinAntrean getInstance() {
        if (instance == null) {
            instance = new MesinAntrean();
        }
        return instance;
    }

    public String ambilNomor() {
        nomorTerakhir++;
        return String.format("A%03d", nomorTerakhir);
    }

    public int jumlahDibagikan() {
        return nomorTerakhir;
    }
}

/** Tombol pengambil nomor yang dipasang di sebuah pintu masuk. */
class TombolAntrean {
    private String lokasi;

    TombolAntrean(String lokasi) {
        this.lokasi = lokasi;
    }

    public void tekan() {
        String nomor = MesinAntrean.getInstance().ambilNomor(); // selalu mesin yang sama
        System.out.println(String.format("%-14s: nomor %s", lokasi, nomor));
    }
}
