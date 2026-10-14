/*
 * Solusi Latihan 02 - Rumah Pintar: Mode Tidur
 * Pertemuan 09 - Polimorfisme
 *
 * Ide penyelesaian:
 * - status() di-override oleh Lampu dan AC, jadi menampilkan status semua
 *   perangkat cukup dengan satu perulangan (polimorfisme).
 * - Mode tidur butuh method KHUSUS: redupkan() hanya milik Lampu, aturSuhu()
 *   hanya milik AC. Lewat variabel bertipe Perangkat, compiler tidak
 *   mengizinkan method itu dipanggil. Karena itu jenis objek diperiksa dulu
 *   dengan instanceof, lalu di-downcast. Perangkat lain cukup dimatikan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02RumahPintar.java
 */
import java.util.List;

public class Latihan02RumahPintar {

    static void tampilkanStatus(List<Perangkat> daftar) {
        for (Perangkat perangkat : daftar) {
            System.out.println(perangkat.status()); // polimorfisme: tanpa cek jenis
        }
    }

    static void modeTidur(List<Perangkat> daftar) {
        for (Perangkat perangkat : daftar) {
            if (perangkat instanceof Lampu) { // cek jenis dulu ...
                Lampu lampu = (Lampu) perangkat; // ... lalu downcasting
                lampu.redupkan(10);
            } else if (perangkat instanceof AC) {
                AC ac = (AC) perangkat;
                ac.aturSuhu(26);
            } else {
                perangkat.matikan();
            }
        }
    }

    public static void main(String[] args) {
        List<Perangkat> rumah = List.of(
                new Lampu("Lampu Kamar"),
                new AC("AC Kamar", 20),
                new Televisi("Televisi"),
                new Lampu("Lampu Teras"));
        System.out.println("=== SEBELUM MODE TIDUR ===");
        tampilkanStatus(rumah);

        System.out.println();
        System.out.println("=== MODE TIDUR DIAKTIFKAN ===");
        modeTidur(rumah);

        System.out.println();
        System.out.println("=== SESUDAH MODE TIDUR ===");
        tampilkanStatus(rumah);
    }
}

/** Kelas induk semua perangkat rumah pintar. */
class Perangkat {
    private String nama;
    private boolean menyala;

    public Perangkat(String nama) {
        this.nama = nama;
        this.menyala = true;
    }

    public String getNama() {
        return nama;
    }

    public boolean isMenyala() {
        return menyala;
    }

    public void matikan() {
        menyala = false;
        System.out.println(nama + " dimatikan");
    }

    public String status() {
        String keadaan = menyala ? "menyala" : "mati";
        return nama + ": " + keadaan;
    }
}

class Lampu extends Perangkat {
    private int kecerahan;

    public Lampu(String nama) { // tanpa kecerahan: bawaan 100%
        this(nama, 100);
    }

    public Lampu(String nama, int kecerahan) {
        super(nama);
        this.kecerahan = kecerahan;
    }

    public void redupkan(int persen) { // method KHUSUS lampu
        kecerahan = persen;
        System.out.println(getNama() + " diredupkan ke " + persen + "%");
    }

    @Override
    public String status() {
        if (!isMenyala()) {
            return super.status();
        }
        return getNama() + ": menyala " + kecerahan + "%";
    }
}

class AC extends Perangkat {
    private int suhu;

    public AC(String nama, int suhu) {
        super(nama);
        this.suhu = suhu;
    }

    public void aturSuhu(int derajat) { // method KHUSUS AC
        suhu = derajat;
        System.out.println(getNama() + " diatur ke " + derajat + " derajat");
    }

    @Override
    public String status() {
        if (!isMenyala()) {
            return super.status();
        }
        return getNama() + ": menyala " + suhu + " derajat";
    }
}

/** Televisi tidak punya method khusus dan tidak meng-override status(). */
class Televisi extends Perangkat {
    public Televisi(String nama) {
        super(nama);
    }
}
