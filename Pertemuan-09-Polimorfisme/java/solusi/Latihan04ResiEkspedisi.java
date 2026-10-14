/*
 * Solusi Latihan 04 - Resi Ekspedisi
 * Pertemuan 09 - Polimorfisme
 *
 * Ide penyelesaian:
 * - ongkir() dan cetakResi() ditulis SEKALI di kelas induk Pengiriman.
 *   Di dalamnya, keduanya memanggil namaLayanan(), tarifPerKg(), dan
 *   beratDitagih(). Kelas anak cukup meng-override method kecil itu
 *   (polimorfisme dari dalam kelas).
 * - Kargo meng-override beratDitagih(): minimal 10 kg.
 * - SameDay (jenis baru) meng-override ongkir() dengan gaya "memperluas":
 *   ongkir versi induk + biaya kurir.
 * - cetakManifest() tidak menyebut kelas anak mana pun, jadi tidak perlu
 *   diubah saat SameDay ditambahkan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04ResiEkspedisi.java
 */
import java.util.List;

public class Latihan04ResiEkspedisi {

    static void cetakManifest(List<Pengiriman> daftar) {
        int total = 0;
        for (Pengiriman kiriman : daftar) {
            kiriman.cetakResi();
            total += kiriman.ongkir();
        }
        System.out.println("Total ongkir: Rp" + total);
    }

    public static void main(String[] args) {
        System.out.println("=== MANIFEST PAGI ===");
        List<Pengiriman> pagi = List.of(
                new Reguler("KK001", "Balikpapan", 2),
                new Kilat("KK002", "Bontang", 3),
                new Kargo("KK003", "Tenggarong", 4),
                new Kargo("KK004", "Sangatta", 25));
        cetakManifest(pagi);

        System.out.println();
        System.out.println("=== MANIFEST SORE (ADA LAYANAN BARU) ===");
        List<Pengiriman> sore = List.of(
                new SameDay("KK005", "Samarinda", 1),
                new Reguler("KK006", "Balikpapan", 5),
                new SameDay("KK007", "Samarinda", 3));
        cetakManifest(sore);
    }
}

/** Kelas induk semua layanan pengiriman. Berat dalam kg (bilangan bulat). */
class Pengiriman {
    private String kode;
    private String kotaTujuan;
    private int beratKg;

    public Pengiriman(String kode, String kotaTujuan, int beratKg) {
        this.kode = kode;
        this.kotaTujuan = kotaTujuan;
        this.beratKg = beratKg;
    }

    public int getBeratKg() {
        return beratKg;
    }

    public String namaLayanan() {
        return "Umum";
    }

    public int tarifPerKg() {
        return 10000;
    }

    public int beratDitagih() {
        return beratKg;
    }

    public int ongkir() {
        return beratDitagih() * tarifPerKg(); // memanggil versi anak
    }

    public void cetakResi() {
        System.out.println(String.format("[%s] %-8s %-11s%3d kg  Rp%d",
                kode, namaLayanan(), kotaTujuan, beratKg, ongkir()));
    }
}

class Reguler extends Pengiriman {
    public Reguler(String kode, String kotaTujuan, int beratKg) {
        super(kode, kotaTujuan, beratKg);
    }

    @Override
    public String namaLayanan() {
        return "Reguler";
    }

    @Override
    public int tarifPerKg() {
        return 9000;
    }
}

class Kilat extends Pengiriman {
    public Kilat(String kode, String kotaTujuan, int beratKg) {
        super(kode, kotaTujuan, beratKg);
    }

    @Override
    public String namaLayanan() {
        return "Kilat";
    }

    @Override
    public int tarifPerKg() {
        return 15000;
    }
}

class Kargo extends Pengiriman {
    private static final int BERAT_MINIMUM = 10;

    public Kargo(String kode, String kotaTujuan, int beratKg) {
        super(kode, kotaTujuan, beratKg);
    }

    @Override
    public String namaLayanan() {
        return "Kargo";
    }

    @Override
    public int tarifPerKg() {
        return 6000;
    }

    @Override
    public int beratDitagih() {
        return Math.max(getBeratKg(), BERAT_MINIMUM);
    }
}

// ----- Jenis BARU (bagian 2 soal) -----
class SameDay extends Pengiriman {
    private static final int BIAYA_KURIR = 10000;

    public SameDay(String kode, String kotaTujuan, int beratKg) {
        super(kode, kotaTujuan, beratKg);
    }

    @Override
    public String namaLayanan() {
        return "SameDay";
    }

    @Override
    public int tarifPerKg() {
        return 20000;
    }

    @Override
    public int ongkir() {
        return super.ongkir() + BIAYA_KURIR; // memperluas versi induk
    }
}
