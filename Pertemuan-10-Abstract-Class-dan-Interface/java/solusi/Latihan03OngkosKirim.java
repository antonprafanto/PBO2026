/*
 * Solusi Latihan 03 - Ongkos Kirim dengan Template Method
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * Ide penyelesaian:
 * - Pengiriman adalah kelas abstrak. Rumus ongkir ditulis SEKALI di
 *   hitungOngkir() (template method):
 *       ongkir = berat x tarifPerKg() + biayaTambahan(berat)
 * - tarifPerKg() dan namaLayanan() abstrak: wajib diisi kelas anak.
 * - biayaTambahan() adalah hook: bawaannya 0, di-override oleh layanan
 *   yang punya aturan khusus (Kilat dan Kargo).
 *
 * Catatan: formatRupiah() ditulis di kelas ini karena nama kelas Rupiah sudah
 * dipakai di folder studi-kasus (nama kelas Java di satu folder harus unik).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03OngkosKirim.java
 */
import java.util.List;
import java.util.Locale;

public class Latihan03OngkosKirim {

    public static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    public static Pengiriman termurah(List<Pengiriman> daftar, int beratKg) {
        Pengiriman pilihan = daftar.get(0);
        for (Pengiriman layanan : daftar) {
            if (layanan.hitungOngkir(beratKg) < pilihan.hitungOngkir(beratKg)) {
                pilihan = layanan;
            }
        }
        return pilihan;
    }

    public static void bandingkan(List<Pengiriman> daftar, int beratKg) {
        System.out.println("=== ONGKOS KIRIM PAKET " + beratKg + " KG ===");
        for (Pengiriman layanan : daftar) {
            System.out.println(layanan.rincian(beratKg));
        }
        Pengiriman pilihan = termurah(daftar, beratKg);
        String ongkir = formatRupiah(pilihan.hitungOngkir(beratKg));
        System.out.println("Termurah: " + pilihan.namaLayanan() + " (" + ongkir + ")");
    }

    public static void main(String[] args) {
        List<Pengiriman> daftar = List.of(new KirimReguler(), new KirimKilat(), new KirimKargo());
        bandingkan(daftar, 3);
        System.out.println();
        bandingkan(daftar, 12);
    }
}

/** Kelas abstrak: kerangka perhitungan ongkos kirim. */
abstract class Pengiriman {

    /** Nama layanan pengiriman. */
    public abstract String namaLayanan();

    /** Tarif dasar per kilogram. */
    public abstract int tarifPerKg();

    /** Hook: biaya tambahan. Bawaannya 0. */
    public int biayaTambahan(int beratKg) {
        return 0;
    }

    /** Template method: rumusnya sama untuk semua layanan. */
    public int hitungOngkir(int beratKg) {
        return beratKg * tarifPerKg() + biayaTambahan(beratKg);
    }

    public String rincian(int beratKg) {
        String tarif = Latihan03OngkosKirim.formatRupiah(tarifPerKg());
        String tambahan = Latihan03OngkosKirim.formatRupiah(biayaTambahan(beratKg));
        String total = Latihan03OngkosKirim.formatRupiah(hitungOngkir(beratKg));
        return String.format(Locale.US, "%-8s: %d kg x %s + tambahan %s = %s",
                namaLayanan(), beratKg, tarif, tambahan, total);
    }
}

/** Layanan biasa tanpa biaya tambahan. */
class KirimReguler extends Pengiriman {

    @Override
    public String namaLayanan() {
        return "Reguler";
    }

    @Override
    public int tarifPerKg() {
        return 8000;
    }
}

/** Layanan cepat: ada biaya prioritas tetap Rp5.000. */
class KirimKilat extends Pengiriman {

    @Override
    public String namaLayanan() {
        return "Kilat";
    }

    @Override
    public int tarifPerKg() {
        return 15000;
    }

    @Override
    public int biayaTambahan(int beratKg) {
        return 5000;
    }
}

/** Murah untuk barang berat, tetapi dihitung minimal 10 kg. */
class KirimKargo extends Pengiriman {
    private static final int BERAT_MINIMUM = 10;

    @Override
    public String namaLayanan() {
        return "Kargo";
    }

    @Override
    public int tarifPerKg() {
        return 5000;
    }

    @Override
    public int biayaTambahan(int beratKg) {
        if (beratKg < BERAT_MINIMUM) {
            return (BERAT_MINIMUM - beratKg) * tarifPerKg();
        }
        return 0;
    }
}
