/*
 * Contoh 06 - Refactoring Aman: Struktur Berubah, Perilaku Tetap
 * Pertemuan 13 - Prinsip SOLID
 *
 * DendaLama menghitung denda keterlambatan perpustakaan. Kodenya benar, tetapi
 * rumus yang sama ditulis tiga kali (melanggar DRY: Don't Repeat Yourself).
 *
 * DendaBaru adalah hasil refactor: rumusnya ditulis SEKALI di AturanDenda,
 * dan setiap jenis pustaka cukup didaftarkan dengan tarif dan batas maksimalnya.
 *
 * Bagian main() membuktikan refactor itu aman: kedua versi dijalankan dengan
 * banyak kasus, lalu hasilnya dibandingkan satu per satu.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06RefactorAman.java
 */
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public class Contoh06RefactorAman {

    static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    public static void main(String[] args) {
        DendaLama lama = new DendaLama();
        DendaBaru baru = new DendaBaru();
        List<String> jenisKasus = List.of("buku", "buku", "buku", "majalah", "majalah",
                "referensi", "referensi", "komik"); // [5] daftar kasus uji
        List<Integer> hariKasus = List.of(0, 3, 25, 4, 30, 2, 12, 5);

        System.out.println("=== MEMBANDINGKAN SEBELUM DAN SESUDAH REFACTOR ===");
        System.out.println(String.format("%-10s%4s%10s%10s   hasil", "jenis", "hari", "lama", "baru"));
        int jumlahSama = 0;
        for (int i = 0; i < jenisKasus.size(); i++) {
            String jenis = jenisKasus.get(i);
            int hari = hariKasus.get(i);
            int hasilLama = lama.hitung(jenis, hari);
            int hasilBaru = baru.hitung(jenis, hari);
            String status;
            if (hasilLama == hasilBaru) { // [6] bukti: hasil harus sama persis
                jumlahSama++;
                status = "sama";
            } else {
                status = "BEDA";
            }
            System.out.println(String.format("%-10s%4s%10s%10s   %s", jenis, hari,
                    formatRupiah(hasilLama), formatRupiah(hasilBaru), status));
        }

        System.out.println("Kasus diuji: " + jenisKasus.size() + ", sama: " + jumlahSama
                + ", beda: " + (jenisKasus.size() - jumlahSama));
        if (jumlahSama == jenisKasus.size()) {
            System.out.println("Kesimpulan: refactor aman, perilaku tidak berubah.");
        } else {
            System.out.println("Kesimpulan: ADA perilaku yang berubah, periksa lagi!");
        }
    }
}

// ---------------------------------------------------------- SEBELUM REFACTOR
class DendaLama {

    public int hitung(String jenis, int hariTerlambat) {
        if (jenis.equals("buku")) {
            if (hariTerlambat <= 0) {
                return 0;
            }
            int denda = hariTerlambat * 1000;
            if (denda > 20000) {
                denda = 20000;
            }
            return denda;
        } else if (jenis.equals("majalah")) { // [1] pola yang sama ditulis ulang...
            if (hariTerlambat <= 0) {
                return 0;
            }
            int denda = hariTerlambat * 500;
            if (denda > 10000) {
                denda = 10000;
            }
            return denda;
        } else if (jenis.equals("referensi")) { // ...dan ditulis ulang lagi
            if (hariTerlambat <= 0) {
                return 0;
            }
            int denda = hariTerlambat * 5000;
            if (denda > 50000) {
                denda = 50000;
            }
            return denda;
        }
        return 0;
    }
}

// ---------------------------------------------------------- SESUDAH REFACTOR
/** Satu rumus denda untuk semua jenis pustaka. */
class AturanDenda {
    private int tarifPerHari;
    private int dendaMaksimal;

    public AturanDenda(int tarifPerHari, int dendaMaksimal) {
        this.tarifPerHari = tarifPerHari;
        this.dendaMaksimal = dendaMaksimal;
    }

    public int hitung(int hariTerlambat) { // [2] rumus ditulis SEKALI
        if (hariTerlambat <= 0) {
            return 0;
        }
        return Math.min(hariTerlambat * tarifPerHari, dendaMaksimal);
    }
}

class DendaBaru {
    private Map<String, AturanDenda> aturan = new LinkedHashMap<>();

    public DendaBaru() {
        aturan.put("buku", new AturanDenda(1000, 20000)); // [3] jenis baru cukup ditambah satu baris
        aturan.put("majalah", new AturanDenda(500, 10000));
        aturan.put("referensi", new AturanDenda(5000, 50000));
    }

    public int hitung(String jenis, int hariTerlambat) {
        if (!aturan.containsKey(jenis)) {
            return 0; // [4] perilaku lama dipertahankan, termasuk yang ini
        }
        return aturan.get(jenis).hitung(hariTerlambat);
    }
}
