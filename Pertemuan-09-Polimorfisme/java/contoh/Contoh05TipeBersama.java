/*
 * Contoh 05 - Java Tidak Mengenal Duck Typing: Butuh Tipe Bersama
 * Pertemuan 09 - Polimorfisme
 *
 * Padanan Java untuk contoh05_duck_typing.py (output-nya sama persis).
 *
 * Di Python, AyamJago, AlarmPonsel, Kentongan, dan BelSekolah boleh tidak
 * punya hubungan apa pun; cukup sama-sama punya method bunyikan().
 * Java lebih ketat: compiler harus YAKIN bahwa setiap objek di dalam List
 * punya method bunyikan(). Caranya, semua kelas diberi TIPE BERSAMA, yaitu
 * kelas induk SumberBunyi.
 *
 * Catatan desain: "ayam jago adalah sumber bunyi" terdengar dipaksakan.
 * Untuk kemampuan bersama seperti "bisa berbunyi", Java punya alat yang lebih
 * tepat, yaitu interface (dibahas di Pertemuan 10).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05TipeBersama.java
 */
import java.util.List;

public class Contoh05TipeBersama {

    static void bangunkanSemua(List<SumberBunyi> daftar) { // [3] tipe bersama wajib disebut
        for (SumberBunyi benda : daftar) {
            String nama = benda.getClass().getSimpleName();
            System.out.println(String.format("%-12s: %s", nama, benda.bunyikan())); // [4]
        }
    }

    public static void main(String[] args) {
        System.out.println("=== PAGI DI ASRAMA ===");
        bangunkanSemua(List.of(new AyamJago(), new AlarmPonsel("05.00"), new Kentongan()));

        System.out.println();
        System.out.println("=== PAGI DI SEKOLAH ===");
        bangunkanSemua(List.of(new BelSekolah(), new AlarmPonsel("06.45")));
    }
}

/** Tipe bersama: "tiket masuk" agar objek-objek berbeda bisa diperlakukan sama. */
class SumberBunyi { // [1]
    public String bunyikan() {
        return "...";
    }
}

class AyamJago extends SumberBunyi { // [2] wajib menyebut induk bersamanya
    @Override
    public String bunyikan() {
        return "Kukuruyuuuk!";
    }
}

class AlarmPonsel extends SumberBunyi {
    private String jam;

    public AlarmPonsel(String jam) {
        this.jam = jam;
    }

    @Override
    public String bunyikan() {
        return "Kriiing! Sudah pukul " + jam;
    }
}

class Kentongan extends SumberBunyi {
    @Override
    public String bunyikan() {
        return "Tung tung tung!";
    }
}

class BelSekolah extends SumberBunyi {
    @Override
    public String bunyikan() {
        return "Teeet! Waktunya masuk kelas";
    }
}
