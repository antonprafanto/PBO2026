/*
 * Contoh 06 - Kelas Akar Object dan instanceof
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * - Kelas yang tidak menulis extends otomatis mewarisi kelas akar Object.
 *   Dari Object-lah setiap kelas mendapat toString() dan equals() bawaan.
 * - objek instanceof Kelas menjawab: "apakah objek ini termasuk Kelas itu
 *   (atau turunannya)?"
 * - KelasB.class.isAssignableFrom(KelasA.class) menjawab: "apakah KelasA
 *   turunan KelasB?" (padanan issubclass di Python; jarang dipakai).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06KelasAkarDanCekTipe.java
 */
public class Contoh06KelasAkarDanCekTipe {

    public static void main(String[] args) {
        AlatMusik gitar = new Gitar("gitar akustik"); // variabel bertipe induk, objeknya Gitar
        AlatMusik drum = new Drum("drum elektrik");

        System.out.println("=== TEKS OBJEK ===");
        System.out.println(gitar); // [3] memanggil toString() warisan dari AlatMusik
        System.out.println(drum);

        System.out.println();
        System.out.println("=== CEK TIPE OBJEK ===");
        System.out.println("gitar adalah Gitar?        " + yaTidak(gitar instanceof Gitar)); // [4]
        System.out.println("gitar adalah AlatMusik?    " + yaTidak(gitar instanceof AlatMusik));
        System.out.println("gitar adalah Drum?         " + yaTidak(gitar instanceof Drum));
        System.out.println("gitar termasuk kelas akar? " + yaTidak(gitar instanceof Object));
        System.out.println("Kelas persis gitar: " + gitar.getClass().getSimpleName()); // [5]
        System.out.println("Kelas persis gitar = AlatMusik? "
                + yaTidak(gitar.getClass() == AlatMusik.class));

        System.out.println();
        System.out.println("=== CEK HUBUNGAN KELAS ===");
        System.out.println("Gitar turunan AlatMusik? "
                + yaTidak(AlatMusik.class.isAssignableFrom(Gitar.class))); // [6]
        System.out.println("AlatMusik turunan Gitar? "
                + yaTidak(Gitar.class.isAssignableFrom(AlatMusik.class)));

        System.out.println();
        System.out.println("=== KESAMAAN BAWAAN DARI KELAS AKAR ===");
        AlatMusik kembaran = new Gitar("gitar akustik"); // isi sama, tetapi objek berbeda
        System.out.println("gitar sama dengan kembarannya? "
                + yaTidak(gitar.equals(kembaran))); // [7] equals() warisan Object
        System.out.println("gitar sama dengan dirinya?     " + yaTidak(gitar.equals(gitar)));
    }

    static String yaTidak(boolean nilai) {
        return nilai ? "ya" : "tidak";
    }
}

/** Kelas induk semua alat musik. */
class AlatMusik { // [1] tidak menulis extends -> otomatis mewarisi Object
    private String nama;

    public AlatMusik(String nama) {
        this.nama = nama;
    }

    @Override // [2] override toString() bawaan Object
    public String toString() {
        return "Alat musik " + nama;
    }
}

/** Gitar adalah AlatMusik. Hanya punya konstruktor yang meneruskan nama. */
class Gitar extends AlatMusik {
    public Gitar(String nama) {
        super(nama);
    }
}

/** Drum adalah AlatMusik. Hanya punya konstruktor yang meneruskan nama. */
class Drum extends AlatMusik {
    public Drum(String nama) {
        super(nama);
    }
}
