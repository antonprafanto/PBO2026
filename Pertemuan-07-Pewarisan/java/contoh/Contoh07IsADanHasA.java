/*
 * Contoh 07 - is-a atau has-a? Kapan TIDAK Memakai Pewarisan
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * Dua rancangan untuk "mobil dan mesinnya":
 * - KELIRU : MobilKeliru extends Mesin  -> "mobil ADALAH mesin" (janggal).
 * - TEPAT  : MobilTepat menyimpan objek Mesin sebagai field
 *            -> "mobil PUNYA mesin" (has-a, seperti relasi di Pertemuan 05).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh07IsADanHasA.java
 */
public class Contoh07IsADanHasA {

    public static void main(String[] args) {
        System.out.println("=== RANCANGAN KELIRU: MOBIL MEWARISI MESIN ===");
        MobilKeliru avanza = new MobilKeliru("Avanza", 1300);
        System.out.println(avanza.jalan());
        System.out.println("Avanza adalah Mesin? " + yaTidak(avanza instanceof Mesin)
                + " (janggal!)");

        System.out.println();
        System.out.println("=== RANCANGAN TEPAT: MOBIL PUNYA MESIN ===");
        MobilTepat xenia = new MobilTepat("Xenia", new Mesin(1300));
        System.out.println(xenia.jalan());
        xenia.gantiMesin(new Mesin(1500));
        System.out.println("Setelah ganti mesin -> " + xenia.jalan());
    }

    static String yaTidak(boolean nilai) {
        return nilai ? "ya" : "tidak";
    }
}

/** Mesin kendaraan dengan kapasitas tertentu (cc). */
class Mesin {
    private int cc;

    public Mesin(int cc) {
        this.cc = cc;
    }

    public String hidupkan() {
        return "Mesin " + cc + " cc menyala";
    }
}

/** Rancangan keliru: mobil mewarisi mesin hanya demi memakai hidupkan(). */
class MobilKeliru extends Mesin { // [1] KELIRU: mobil dianggap "adalah" mesin
    private String nama;

    public MobilKeliru(String nama, int cc) {
        super(cc);
        this.nama = nama;
    }

    public String jalan() {
        return nama + ": " + hidupkan();
    }
}

/** Rancangan tepat: mobil MENYIMPAN objek Mesin sebagai field. */
class MobilTepat { // [2] TEPAT: mobil "punya" mesin
    private String nama;
    private Mesin mesin; // [3] has-a: field berisi objek lain

    public MobilTepat(String nama, Mesin mesin) {
        this.nama = nama;
        this.mesin = mesin;
    }

    public String jalan() {
        return nama + ": " + mesin.hidupkan(); // [4] tugas diteruskan ke objek mesin
    }

    public void gantiMesin(Mesin mesinBaru) { // [5] bagiannya bisa diganti
        this.mesin = mesinBaru;
    }
}
