/*
 * Contoh 04 - Urutan Konstruktor dan Pewarisan Bertingkat (Multilevel)
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * Tiga tingkat: Perangkat -> Komputer -> Laptop.
 * Setiap konstruktor mencetak pesan SETELAH memanggil konstruktor induknya,
 * sehingga kita bisa melihat urutannya: bagian induk selalu selesai lebih dulu.
 * Laptop juga bisa memakai method dari SEMUA tingkat di atasnya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04UrutanKonstruktor.java
 */
public class Contoh04UrutanKonstruktor {

    public static void main(String[] args) {
        System.out.println("=== MEMBUAT LAPTOP (3 TINGKAT) ===");
        Laptop laptop = new Laptop("Lenovo", 16, 8); // [4]

        System.out.println();
        System.out.println("=== MEMBUAT KOMPUTER (2 TINGKAT) ===");
        new Komputer("Dell", 32); // [5] hanya dua bagian yang disiapkan

        System.out.println();
        System.out.println("=== METHOD DARI SETIAP TINGKAT ===");
        System.out.println(laptop.nyalakan()); // [6] warisan dari "kakek" (Perangkat)
        System.out.println(laptop.jalankan("VS Code")); // warisan dari induk (Komputer)
        System.out.println(laptop.cekBaterai()); // milik Laptop sendiri
    }
}

/** Tingkat 1: semua perangkat elektronik. */
class Perangkat {
    private String merek;

    public Perangkat(String merek) {
        // [1] di sini Java diam-diam memanggil super() milik Object
        this.merek = merek;
        System.out.println("  Bagian Perangkat selesai: merek " + merek);
    }

    public String nyalakan() {
        return merek + " dinyalakan";
    }
}

/** Tingkat 2: Komputer adalah Perangkat. */
class Komputer extends Perangkat {
    private int ramGb;

    public Komputer(String merek, int ramGb) {
        super(merek); // [2] minta induk menyiapkan bagiannya dulu
        this.ramGb = ramGb;
        System.out.println("  Bagian Komputer selesai: RAM " + ramGb + " GB");
    }

    public String jalankan(String program) {
        return program + " berjalan dengan RAM " + ramGb + " GB";
    }
}

/** Tingkat 3: Laptop adalah Komputer, dan karena itu juga Perangkat. */
class Laptop extends Komputer {
    private int bateraiJam;

    public Laptop(String merek, int ramGb, int bateraiJam) {
        super(merek, ramGb); // [3] induk langsung Laptop adalah Komputer
        this.bateraiJam = bateraiJam;
        System.out.println("  Bagian Laptop selesai: baterai " + bateraiJam + " jam");
    }

    public String cekBaterai() {
        return "Baterai tahan " + bateraiJam + " jam";
    }
}
