/*
 * Contoh 04 - Simple Factory: Membuat Kendaraan dari Pilihan Teks
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Aplikasi ojek online menerima pilihan berupa TEKS ("motor", "mobil", ...).
 * Tanpa factory, setiap bagian program yang butuh kendaraan menulis if/else
 * yang sama berulang-ulang. Dengan SIMPLE FACTORY, keputusan "kelas mana yang
 * dibuat" dikumpulkan di SATU tempat: KendaraanFactory.buat(jenis).
 *
 * Kode pemanggil cukup mengenal kelas abstrak Kendaraan. Ia tidak perlu tahu
 * nama kelas Motor, Mobil, atau MobilBesar.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04SimpleFactory.java
 */
import java.util.List;

public class Contoh04SimpleFactory {

    public static void main(String[] args) {
        System.out.println("=== PESANAN DARI APLIKASI (JARAK 8 KM) ===");
        for (String pilihan : List.of("motor", "Mobil", "MOBIL BESAR")) {
            Kendaraan kendaraan = KendaraanFactory.buat(pilihan); // [4] cukup kirim teks
            int ongkos = kendaraan.hitungOngkos(8);
            System.out.println(String.format("%-12s -> %-12s ", pilihan, kendaraan.nama())
                    + "maks " + kendaraan.kapasitas() + " penumpang, Rp" + ongkos);
        }

        System.out.println();
        System.out.println("=== PILIHAN TIDAK DIKENAL ===");
        try {
            KendaraanFactory.buat("helikopter");
        } catch (IllegalArgumentException e) { // [5]
            System.out.println("Ditolak: " + e.getMessage());
        }
    }
}

/** Produk abstrak: semua kendaraan yang bisa dipesan. */
abstract class Kendaraan {
    public abstract String nama();

    public abstract int kapasitas();

    public abstract int tarifPerKm();

    public int hitungOngkos(int jarakKm) {
        return tarifPerKm() * jarakKm;
    }
}

class Motor extends Kendaraan {
    @Override
    public String nama() {
        return "Motor";
    }

    @Override
    public int kapasitas() {
        return 1;
    }

    @Override
    public int tarifPerKm() {
        return 2500;
    }
}

class Mobil extends Kendaraan {
    @Override
    public String nama() {
        return "Mobil";
    }

    @Override
    public int kapasitas() {
        return 4;
    }

    @Override
    public int tarifPerKm() {
        return 4000;
    }
}

class MobilBesar extends Kendaraan {
    @Override
    public String nama() {
        return "Mobil Besar";
    }

    @Override
    public int kapasitas() {
        return 6;
    }

    @Override
    public int tarifPerKm() {
        return 5500;
    }
}

/** Simple Factory: SATU tempat yang memutuskan kelas mana yang dibuat. */
class KendaraanFactory {

    public static Kendaraan buat(String jenis) { // [1] tipe kembalian: kelas abstrak
        if (jenis.equalsIgnoreCase("motor")) { // [2] "MOBIL" dan "mobil" dianggap sama
            return new Motor();
        }
        if (jenis.equalsIgnoreCase("mobil")) {
            return new Mobil();
        }
        if (jenis.equalsIgnoreCase("mobil besar")) {
            return new MobilBesar();
        }
        throw new IllegalArgumentException("Jenis kendaraan tidak dikenal: " + jenis); // [3]
    }
}
