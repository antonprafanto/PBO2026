/*
 * Contoh 02 - OCP: Terbuka untuk Ditambah, Tertutup untuk Diubah
 * Pertemuan 13 - Prinsip SOLID
 *
 * Versi MELANGGAR: KalkulatorOngkirKaku memilih rumus dengan rantai if/else if.
 * Layanan baru (Same Day) belum dikenal, dan satu-satunya cara menambahkannya
 * adalah MEMBONGKAR method hitung() yang sudah berjalan.
 *
 * Versi SESUAI OCP: setiap layanan adalah kelas yang mengimplementasikan
 * LayananKirim. Layanan Same Day ditambahkan sebagai kelas BARU;
 * KalkulatorOngkir dan layanan lama tidak disentuh sama sekali.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02Ocp.java
 */
import java.util.List;
import java.util.Locale;

public class Contoh02Ocp {

    static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    public static void main(String[] args) {
        int berat = 3;

        System.out.println("=== VERSI MELANGGAR OCP (rantai percabangan) ===");
        KalkulatorOngkirKaku kaku = new KalkulatorOngkirKaku();
        for (String layanan : List.of("reguler", "kilat", "sameday")) {
            System.out.println(String.format("%-9s", layanan) + berat + " kg: "
                    + formatRupiah(kaku.hitung(layanan, berat)));
        }
        System.out.println("Layanan baru dianggap gratis! Method hitung() harus dibongkar dulu.");

        System.out.println();
        System.out.println("=== VERSI SESUAI OCP (satu kelas per layanan) ===");
        KalkulatorOngkir kalkulator = new KalkulatorOngkir();
        List<LayananKirim> daftarLayanan = List.of(
                new LayananReguler(), new LayananKilat(), new LayananSameDay());
        for (LayananKirim layanan : daftarLayanan) {
            int ongkir = kalkulator.hitung(layanan, berat);
            System.out.println(String.format("%-9s", layanan.nama()) + berat + " kg: "
                    + formatRupiah(ongkir));
        }
        System.out.println("Layanan Same Day cukup ditambahkan sebagai kelas baru.");
    }
}

// ------------------------------------------------------------ MELANGGAR OCP
/** Setiap layanan baru memaksa method hitung() dibongkar. */
class KalkulatorOngkirKaku {

    public int hitung(String layanan, int beratKg) {
        if (layanan.equals("reguler")) {
            return 9000 * beratKg;
        } else if (layanan.equals("kilat")) {
            return 15000 * beratKg;
        }
        return 0; // [1] layanan lain belum dikenal: diam-diam dianggap gratis!
    }
}

// -------------------------------------------------------------- SESUAI OCP
/** Kontrak semua layanan pengiriman. */
interface LayananKirim {
    /** Nama layanan untuk ditampilkan. */
    String nama();

    /** Ongkos kirim dalam rupiah untuk berat tertentu. */
    int ongkir(int beratKg);
}

class LayananReguler implements LayananKirim {
    @Override
    public String nama() {
        return "Reguler";
    }

    @Override
    public int ongkir(int beratKg) {
        return 9000 * beratKg;
    }
}

class LayananKilat implements LayananKirim {
    @Override
    public String nama() {
        return "Kilat";
    }

    @Override
    public int ongkir(int beratKg) {
        return 15000 * beratKg;
    }
}

class LayananSameDay implements LayananKirim { // [2] layanan BARU = kelas baru, kode lama aman
    @Override
    public String nama() {
        return "Same Day";
    }

    @Override
    public int ongkir(int beratKg) {
        return 25000 + 5000 * beratKg;
    }
}

/** Tidak pernah menyebut nama layanan apa pun, jadi tidak perlu diubah. */
class KalkulatorOngkir {

    public int hitung(LayananKirim layanan, int beratKg) {
        if (beratKg < 1) { // aturan umum: berat dihitung minimal 1 kg
            beratKg = 1;
        }
        return layanan.ongkir(beratKg); // [3] polimorfisme bekerja di sini
    }
}
