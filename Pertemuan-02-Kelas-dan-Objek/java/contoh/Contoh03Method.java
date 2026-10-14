/*
 * Contoh 03 - Method: Perilaku Sebuah Objek
 * Pertemuan 02 - Kelas dan Objek
 *
 * Method adalah fungsi yang "menempel" pada objek. Method bisa membaca dan
 * mengubah atribut milik objeknya sendiri.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03Method.java
 */
public class Contoh03Method {

    public static void main(String[] args) {
        Lampu lampuKamar = new Lampu("kamar");
        Lampu lampuDapur = new Lampu("dapur");

        System.out.println("=== KONDISI AWAL ===");
        lampuKamar.tampilkanStatus(); // [4] memanggil method
        lampuDapur.tampilkanStatus();

        System.out.println();
        System.out.println("=== SETELAH DIOPERASIKAN ===");
        lampuKamar.nyalakan();
        lampuKamar.tampilkanStatus();
        lampuDapur.tampilkanStatus(); // lampu dapur tidak terpengaruh
        lampuKamar.matikan();
        lampuKamar.tampilkanStatus();
    }
}

/** Lampu yang bisa dinyalakan dan dimatikan. */
class Lampu {
    String ruangan;
    boolean menyala;

    Lampu(String ruangan) {
        this.ruangan = ruangan;
        this.menyala = false; // [1] nilai awal tidak harus dari parameter
    }

    void nyalakan() { // [2] method yang mengubah atribut
        menyala = true;
        System.out.println("Lampu " + ruangan + " dinyalakan");
    }

    void matikan() {
        menyala = false;
        System.out.println("Lampu " + ruangan + " dimatikan");
    }

    void tampilkanStatus() { // [3] method yang hanya membaca atribut
        if (menyala) {
            System.out.println("Status lampu " + ruangan + ": MENYALA");
        } else {
            System.out.println("Status lampu " + ruangan + ": PADAM");
        }
    }
}
