/*
 * Contoh 06 - Mengembalikan Salinan List
 * Pertemuan 05 - Relasi Antarkelas
 *
 * Dua garasi berkapasitas 2 motor. GarasiBocor menyerahkan list ASLI-nya
 * ke luar, sehingga aturan kapasitas bisa dilewati. GarasiAman hanya
 * menyerahkan SALINAN list, sehingga isi garasi tetap terjaga.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06SalinanList.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh06SalinanList {

    public static void main(String[] args) {
        System.out.println("=== GARASI BOCOR ===");
        GarasiBocor bocor = new GarasiBocor(2);
        bocor.parkir(new Motor("KT 1111 AA"));
        bocor.parkir(new Motor("KT 2222 BB"));
        bocor.parkir(new Motor("KT 3333 CC"));
        List<Motor> daftar = bocor.getDaftarMotor(); // [3] kode luar memegang list ASLI
        daftar.add(new Motor("KT 3333 CC")); // [4] menyelinap, kapasitas dilewati
        bocor.tampilkan();

        System.out.println();
        System.out.println("=== GARASI AMAN ===");
        GarasiAman aman = new GarasiAman(2);
        aman.parkir(new Motor("KT 1111 AA"));
        aman.parkir(new Motor("KT 2222 BB"));
        aman.parkir(new Motor("KT 3333 CC"));
        daftar = aman.getDaftarMotor(); // [5] kode luar hanya memegang salinan
        daftar.add(new Motor("KT 3333 CC")); // yang bertambah hanya salinannya
        aman.tampilkan();
        System.out.println("Isi salinan di luar: " + daftar.size() + " motor");
    }
}

/** Motor dengan nomor plat. */
class Motor {
    private String plat;

    public Motor(String plat) {
        this.plat = plat;
    }

    public String getPlat() {
        return plat;
    }
}

/** Garasi yang membocorkan list aslinya. */
class GarasiBocor {
    private int kapasitas;
    private List<Motor> daftarMotor;

    public GarasiBocor(int kapasitas) {
        this.kapasitas = kapasitas;
        this.daftarMotor = new ArrayList<>();
    }

    public void parkir(Motor motor) {
        if (daftarMotor.size() >= kapasitas) {
            System.out.println("Ditolak: garasi penuh, " + motor.getPlat() + " tidak bisa masuk");
            return;
        }
        daftarMotor.add(motor);
        System.out.println(motor.getPlat() + " masuk garasi");
    }

    public List<Motor> getDaftarMotor() {
        return daftarMotor; // [1] list ASLI diserahkan ke luar
    }

    public void tampilkan() {
        System.out.println("Isi garasi (" + daftarMotor.size() + "/" + kapasitas + "):");
        for (Motor motor : daftarMotor) {
            System.out.println("- " + motor.getPlat());
        }
    }
}

/** Garasi yang hanya menyerahkan salinan list. */
class GarasiAman {
    private int kapasitas;
    private List<Motor> daftarMotor;

    public GarasiAman(int kapasitas) {
        this.kapasitas = kapasitas;
        this.daftarMotor = new ArrayList<>();
    }

    public void parkir(Motor motor) {
        if (daftarMotor.size() >= kapasitas) {
            System.out.println("Ditolak: garasi penuh, " + motor.getPlat() + " tidak bisa masuk");
            return;
        }
        daftarMotor.add(motor);
        System.out.println(motor.getPlat() + " masuk garasi");
    }

    public List<Motor> getDaftarMotor() {
        return new ArrayList<>(daftarMotor); // [2] yang diserahkan hanya SALINAN
    }

    public void tampilkan() {
        System.out.println("Isi garasi (" + daftarMotor.size() + "/" + kapasitas + "):");
        for (Motor motor : daftarMotor) {
            System.out.println("- " + motor.getPlat());
        }
    }
}
