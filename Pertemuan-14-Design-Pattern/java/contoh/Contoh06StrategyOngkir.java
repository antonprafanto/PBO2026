/*
 * Contoh 06 - Strategy: Menukar Cara Menghitung Ongkos Kirim
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Satu paket bisa dikirim dengan beberapa layanan: Reguler, Kilat, Hemat.
 * Setiap layanan punya RUMUS ongkir sendiri. Pola STRATEGY membungkus setiap
 * rumus menjadi kelas tersendiri (sebuah "strategi"), lalu objek Pengiriman
 * (context) cukup memanggil strategi yang sedang dipasang.
 *
 * - Ganti layanan  = tukar objek strategi (bisa saat program berjalan).
 * - Layanan baru   = kelas strategi baru; kelas Pengiriman tidak diubah (OCP).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06StrategyOngkir.java
 */
import java.util.List;

public class Contoh06StrategyOngkir {

    public static void main(String[] args) {
        Pengiriman paket = new Pengiriman(2, new OngkirReguler());
        System.out.println("=== PAKET 2 KG DARI SAMARINDA KE BONTANG ===");
        List<StrategiOngkir> daftarStrategi = List.of(new OngkirReguler(),
                new OngkirKilat(), new OngkirHemat());
        for (StrategiOngkir strategi : daftarStrategi) {
            paket.aturStrategi(strategi); // [4] tukar saat program berjalan
            System.out.println(paket.ringkasan());
        }

        System.out.println();
        System.out.println("=== STRATEGI BARU, KELAS Pengiriman TIDAK DIUBAH ===");
        paket.aturStrategi(new OngkirAmbilSendiri()); // [5]
        System.out.println(paket.ringkasan());
    }
}

/** Strategy: kontrak semua cara menghitung ongkos kirim. */
interface StrategiOngkir {
    String nama();

    int hitung(int beratKg);
}

class OngkirReguler implements StrategiOngkir {
    @Override
    public String nama() {
        return "Reguler (3 hari)";
    }

    @Override
    public int hitung(int beratKg) {
        return 8000 * beratKg;
    }
}

/** Lebih mahal per kg, ditambah biaya tetap Rp5000. */
class OngkirKilat implements StrategiOngkir {
    @Override
    public String nama() {
        return "Kilat (besok tiba)";
    }

    @Override
    public int hitung(int beratKg) {
        return 15000 * beratKg + 5000;
    }
}

/** Murah per kg, tetapi berat minimal dihitung 3 kg. */
class OngkirHemat implements StrategiOngkir {
    @Override
    public String nama() {
        return "Hemat (5 hari)";
    }

    @Override
    public int hitung(int beratKg) {
        return 5000 * Math.max(beratKg, 3);
    }
}

/** Context: memakai strategi ongkir tanpa tahu rumus di dalamnya. */
class Pengiriman {
    private int beratKg;
    private StrategiOngkir strategi; // [1] strategi disimpan sebagai field

    Pengiriman(int beratKg, StrategiOngkir strategi) {
        this.beratKg = beratKg;
        this.strategi = strategi;
    }

    public void aturStrategi(StrategiOngkir strategi) { // [2] bisa ditukar
        this.strategi = strategi;
    }

    public int ongkir() {
        return strategi.hitung(beratKg); // [3] didelegasikan
    }

    public String ringkasan() {
        return String.format("%-20s Rp", strategi.nama()) + ongkir();
    }
}

/** Strategi BARU: paket diambil sendiri di gerai, tanpa ongkir. */
class OngkirAmbilSendiri implements StrategiOngkir {
    @Override
    public String nama() {
        return "Ambil di gerai";
    }

    @Override
    public int hitung(int beratKg) {
        return 0;
    }
}
