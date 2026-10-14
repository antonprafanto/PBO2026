/*
 * Contoh 01 - Satu Perintah, Banyak Bentuk
 * Pertemuan 09 - Polimorfisme
 *
 * Kucing, Anjing, dan Bebek meng-override method bersuara() milik Hewan.
 * Perintahnya SAMA (hewan.bersuara()), tetapi hasilnya BERBEDA, tergantung
 * objek apa yang sebenarnya ditunjuk oleh variabel. Ikan tidak meng-override,
 * jadi Ikan memakai versi milik induknya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01SatuPerintahBanyakBentuk.java
 */
import java.util.List;

public class Contoh01SatuPerintahBanyakBentuk {

    static void suruhBersuara(Hewan hewan) { // [3] parameter bertipe kelas induk
        String jenis = hewan.getClass().getSimpleName();
        System.out.println(hewan.getNama() + " si " + jenis + ": " + hewan.bersuara()); // [4]
    }

    public static void main(String[] args) {
        System.out.println("=== SATU VARIABEL, BERGANTI OBJEK ===");
        Hewan hewan = new Kucing("Oyen"); // [5] tipe variabel Hewan, objeknya Kucing
        System.out.println(hewan.bersuara());
        hewan = new Anjing("Bruno"); // sekarang menunjuk objek Anjing
        System.out.println(hewan.bersuara()); // baris yang sama persis, hasilnya berbeda

        System.out.println();
        System.out.println("=== SATU PERINTAH UNTUK SEMUA HEWAN ===");
        List<Hewan> kebun = List.of(new Kucing("Oyen"), new Anjing("Bruno"),
                new Bebek("Kuning"), new Ikan("Koki")); // [6]
        for (Hewan satwa : kebun) {
            suruhBersuara(satwa);
        }
    }
}

/** Kelas induk semua hewan. */
class Hewan {
    private String nama;

    public Hewan(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public String bersuara() {
        return "(diam saja)"; // [1] versi umum milik induk
    }
}

class Kucing extends Hewan {
    public Kucing(String nama) {
        super(nama);
    }

    @Override // [2] override: versi khusus kucing
    public String bersuara() {
        return "Meong!";
    }
}

class Anjing extends Hewan {
    public Anjing(String nama) {
        super(nama);
    }

    @Override
    public String bersuara() {
        return "Guk guk!";
    }
}

class Bebek extends Hewan {
    public Bebek(String nama) {
        super(nama);
    }

    @Override
    public String bersuara() {
        return "Kwek kwek!";
    }
}

/** Ikan tidak meng-override bersuara(), jadi memakai versi Hewan. */
class Ikan extends Hewan {
    public Ikan(String nama) {
        super(nama);
    }
}
