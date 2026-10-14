/*
 * Solusi Latihan 06 - Kamar Penginapan Wisma Tepian (Pewarisan Bertingkat)
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * Ide penyelesaian:
 * - Tiga tingkat: Kamar -> KamarDeluxe -> KamarSuite.
 * - Setiap tingkat meng-override hitungBiaya(malam) dan toString(), dan SELALU
 *   memulai dari hasil versi induknya (super). Jadi aturan tingkat bawah
 *   (validasi malam, tarif x malam) otomatis ikut berlaku di tingkat atas.
 * - KamarSuite tidak menambah field, tetapi tetap WAJIB menulis konstruktor
 *   yang meneruskan data ke super(...), karena konstruktor tidak diwariskan.
 * - Semua uang berupa int; diskon dihitung dengan / 100.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan06WismaTepian.java
 */
import java.util.Locale;

public class Latihan06WismaTepian {

    public static void main(String[] args) {
        Kamar standar = new Kamar("101", 300000);
        KamarDeluxe deluxe = new KamarDeluxe("205", 450000, 2);
        KamarSuite suite = new KamarSuite("301", 800000, 2);

        System.out.println("=== DAFTAR KAMAR WISMA TEPIAN ===");
        System.out.println(standar);
        System.out.println(deluxe);
        System.out.println(suite);

        System.out.println();
        System.out.println("=== RINCIAN BIAYA ===");
        System.out.println("Kamar " + standar.getNomor() + ", 2 malam: "
                + Kamar.formatRupiah(standar.hitungBiaya(2)));
        System.out.println("Kamar " + deluxe.getNomor() + ", 2 malam: "
                + Kamar.formatRupiah(deluxe.hitungBiaya(2)));
        System.out.println("Kamar " + suite.getNomor() + ", 2 malam: "
                + Kamar.formatRupiah(suite.hitungBiaya(2)));
        System.out.println("Kamar " + suite.getNomor() + ", 3 malam: "
                + Kamar.formatRupiah(suite.hitungBiaya(3)));

        System.out.println();
        System.out.println("=== CEK PEWARISAN ===");
        System.out.println("Kamar 301 adalah KamarDeluxe? " + yaTidak(suite instanceof KamarDeluxe));
        System.out.println("Kamar 301 adalah Kamar?       " + yaTidak(suite instanceof Kamar));
        System.out.println("Kamar 205 adalah KamarSuite?  " + yaTidak(deluxe instanceof KamarSuite));

        System.out.println();
        System.out.println("=== VALIDASI ===");
        try {
            suite.hitungBiaya(0);
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        try {
            new KamarDeluxe("206", 450000, 6);
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
    }

    static String yaTidak(boolean nilai) {
        return nilai ? "ya" : "tidak";
    }
}

/** Tingkat 1: kamar standar. */
class Kamar {
    private String nomor;
    private int tarif;

    public Kamar(String nomor, int tarif) {
        if (tarif <= 0) {
            throw new IllegalArgumentException("Tarif harus lebih dari 0");
        }
        this.nomor = nomor;
        this.tarif = tarif;
    }

    /** Mengubah 300000 menjadi "Rp300.000". Bisa dipakai semua kelas turunan. */
    public static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    public String getNomor() {
        return nomor;
    }

    public int hitungBiaya(int malam) {
        if (malam < 1) {
            throw new IllegalArgumentException("Lama menginap minimal 1 malam");
        }
        return tarif * malam;
    }

    @Override
    public String toString() {
        return "Kamar " + nomor + " - " + formatRupiah(tarif) + "/malam";
    }
}

/** Tingkat 2: kamar dengan sarapan untuk setiap tamu. */
class KamarDeluxe extends Kamar {
    private static final int SARAPAN_PER_TAMU = 50000; // per tamu per malam

    private int jumlahTamu;

    public KamarDeluxe(String nomor, int tarif, int jumlahTamu) {
        super(nomor, tarif);
        if (jumlahTamu < 1 || jumlahTamu > 4) {
            throw new IllegalArgumentException("Jumlah tamu harus 1 sampai 4");
        }
        this.jumlahTamu = jumlahTamu;
    }

    @Override
    public int hitungBiaya(int malam) {
        int biayaKamar = super.hitungBiaya(malam); // validasi malam ikut berjalan
        return biayaKamar + SARAPAN_PER_TAMU * jumlahTamu * malam;
    }

    @Override
    public String toString() {
        return super.toString() + " | sarapan " + jumlahTamu + " tamu";
    }
}

/** Tingkat 3: deluxe + antar-jemput bandara + diskon menginap lama. */
class KamarSuite extends KamarDeluxe {
    private static final int ANTAR_JEMPUT = 150000; // dibayar sekali, bukan per malam
    private static final int DISKON_PERSEN = 10;
    private static final int MALAM_MINIMAL_DISKON = 3;

    public KamarSuite(String nomor, int tarif, int jumlahTamu) {
        super(nomor, tarif, jumlahTamu); // konstruktor tidak diwariskan: tetap ditulis
    }

    @Override
    public int hitungBiaya(int malam) {
        int biaya = super.hitungBiaya(malam) + ANTAR_JEMPUT;
        if (malam >= MALAM_MINIMAL_DISKON) {
            biaya -= biaya * DISKON_PERSEN / 100;
        }
        return biaya;
    }

    @Override
    public String toString() {
        return super.toString() + " | antar-jemput bandara";
    }
}
