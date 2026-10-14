/*
 * Solusi Latihan 03 - Tarif Ojek Online
 * Pertemuan 09 - Polimorfisme
 *
 * Ide penyelesaian:
 * - OVERLOADING konstruktor: Ojek(namaDriver) memanggil
 *   Ojek(namaDriver, 2500) lewat this(...).
 * - OVERLOADING method: tiga versi hitungTarif() dengan jumlah parameter
 *   berbeda. Dua versi yang pendek cukup memanggil versi terlengkap dengan
 *   nilai bawaan, jadi rumus tarif hanya ditulis SEKALI.
 * - Semua perhitungan memakai bilangan bulat (persen: nilai * persen / 100).
 * - Teks dibandingkan dengan equals(), bukan ==.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03TarifOjek.java
 */
public class Latihan03TarifOjek {

    static void cetak(String keterangan, int tarif) {
        System.out.println(String.format("%-36s", keterangan) + ": Rp" + tarif);
    }

    public static void main(String[] args) {
        Ojek darto = new Ojek("Pak Darto"); // tarif per km memakai nilai bawaan
        Ojek yuni = new Ojek("Mbak Yuni", 3000);

        System.out.println("=== DRIVER ===");
        System.out.println(darto.info());
        System.out.println(yuni.info());

        System.out.println();
        System.out.println("=== HITUNG TARIF ===");
        cetak("Pak Darto, 3 km", darto.hitungTarif(3));
        cetak("Pak Darto, 8 km", darto.hitungTarif(8));
        cetak("Pak Darto, 8 km, jam sibuk", darto.hitungTarif(8, true));
        cetak("Pak Darto, 8 km, jam sibuk, HEMAT10", darto.hitungTarif(8, true, "HEMAT10"));
        cetak("Mbak Yuni, 5 km, HEMAT10", yuni.hitungTarif(5, false, "HEMAT10"));
        cetak("Mbak Yuni, 5 km, kode SALAH", yuni.hitungTarif(5, false, "SALAH"));
    }
}

/** Driver ojek online beserta tarifnya. */
class Ojek {
    private static final int TARIF_MINIMUM = 10000;
    private static final int PERSEN_JAM_SIBUK = 20;
    private static final int PERSEN_PROMO = 10;
    private static final String KODE_PROMO_BERLAKU = "HEMAT10";

    private String namaDriver;
    private int tarifPerKm;

    public Ojek(String namaDriver) {
        this(namaDriver, 2500); // overload konstruktor: isi tarif bawaan
    }

    public Ojek(String namaDriver, int tarifPerKm) {
        this.namaDriver = namaDriver;
        this.tarifPerKm = tarifPerKm;
    }

    public String getNamaDriver() {
        return namaDriver;
    }

    public String info() {
        return namaDriver + " (Rp" + tarifPerKm + "/km)";
    }

    public int hitungTarif(int jarakKm) { // versi 1: hanya jarak
        return hitungTarif(jarakKm, false, "");
    }

    public int hitungTarif(int jarakKm, boolean jamSibuk) { // versi 2: + jam sibuk
        return hitungTarif(jarakKm, jamSibuk, "");
    }

    public int hitungTarif(int jarakKm, boolean jamSibuk, String kodePromo) { // versi 3: lengkap
        int tarif = jarakKm * tarifPerKm;
        if (tarif < TARIF_MINIMUM) {
            tarif = TARIF_MINIMUM;
        }
        if (jamSibuk) {
            tarif += tarif * PERSEN_JAM_SIBUK / 100;
        }
        if (kodePromo.equals(KODE_PROMO_BERLAKU)) {
            tarif -= tarif * PERSEN_PROMO / 100;
        }
        return tarif;
    }
}
