/*
 * Contoh 07 - Overload Dipilih saat Kompilasi, Override Dipilih saat Berjalan
 * Pertemuan 09 - Polimorfisme
 *
 * Contoh ini KHUSUS Java (Python tidak punya overloading).
 *
 * - OVERLOAD: Resepsionis punya dua method sambut(...). Compiler memilih
 *   versinya SAAT KOMPILASI berdasarkan TIPE VARIABEL argumen.
 * - OVERRIDE: TamuVip meng-override fasilitas(). Versinya dipilih SAAT
 *   PROGRAM BERJALAN berdasarkan OBJEK yang sebenarnya.
 *
 * Perhatikan tamu Rina: variabelnya bertipe Tamu, objeknya TamuVip.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh07OverloadVsOverride.java
 */
public class Contoh07OverloadVsOverride {

    public static void main(String[] args) {
        Resepsionis resepsionis = new Resepsionis();
        Tamu budi = new Tamu("Budi");
        TamuVip siti = new TamuVip("Siti");
        Tamu rina = new TamuVip("Rina"); // [1] tipe variabel Tamu, objeknya TamuVip

        System.out.println("=== OVERLOAD: DIPILIH SAAT KOMPILASI ===");
        System.out.println(resepsionis.sambut(budi));
        System.out.println(resepsionis.sambut(siti));
        System.out.println(resepsionis.sambut(rina)); // [2] melihat tipe VARIABEL rina

        System.out.println();
        System.out.println("=== OVERRIDE: DIPILIH SAAT BERJALAN ===");
        System.out.println(budi.getNama() + ": " + budi.fasilitas());
        System.out.println(siti.getNama() + ": " + siti.fasilitas());
        System.out.println(rina.getNama() + ": " + rina.fasilitas()); // [3] melihat OBJEK rina
    }
}

/** Tamu hotel biasa. */
class Tamu {
    private String nama;

    public Tamu(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public String fasilitas() {
        return "kamar standar";
    }
}

/** Tamu VIP meng-override fasilitas(). */
class TamuVip extends Tamu {
    public TamuVip(String nama) {
        super(nama);
    }

    @Override
    public String fasilitas() {
        return "kamar suite dan sarapan";
    }
}

/** Resepsionis punya dua method sambut(): ini OVERLOADING. */
class Resepsionis {
    public String sambut(Tamu tamu) { // [4] versi untuk tipe Tamu
        return "sambut(Tamu)    dipakai untuk " + tamu.getNama();
    }

    public String sambut(TamuVip tamu) { // [5] versi untuk tipe TamuVip
        return "sambut(TamuVip) dipakai untuk " + tamu.getNama();
    }
}
