/*
 * Contoh 04 - ISP: Interface Kecil Lebih Baik daripada Interface Gemuk
 * Pertemuan 13 - Prinsip SOLID
 *
 * Versi MELANGGAR: interface PerangkatKasir "gemuk" (tiga kemampuan sekaligus).
 * PrinterBluetooth hanya bisa mencetak, tetapi dipaksa menulis dua method
 * palsu yang melempar exception.
 *
 * Versi SESUAI ISP: kontrak dipecah menjadi PencetakStruk, PemindaiBarcode,
 * dan LaciUang. Setiap perangkat hanya meng-implements interface yang
 * benar-benar sesuai kemampuannya. KasirLengkap meng-implements ketiganya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04Isp.java
 */
import java.util.List;

public class Contoh04Isp {

    public static void main(String[] args) {
        System.out.println("=== VERSI MELANGGAR ISP (interface gemuk) ===");
        List<PerangkatKasir> perangkatLama = List.of(new MesinKasirLengkap(), new PrinterBluetooth());
        for (PerangkatKasir perangkat : perangkatLama) {
            perangkat.cetakStruk("Terima kasih!");
            try {
                System.out.println("Hasil pindai: " + perangkat.pindaiBarcode());
            } catch (UnsupportedOperationException e) {
                System.out.println("[KEJUTAN] " + e.getMessage());
            }
        }

        System.out.println();
        System.out.println("=== VERSI SESUAI ISP (interface kecil) ===");
        KasirLengkap kasir = new KasirLengkap();
        List<PencetakStruk> pencetak = List.of(kasir, new PrinterThermal()); // [5]
        List<PemindaiBarcode> pemindai = List.of(kasir, new PemindaiGenggam());
        System.out.println("-- semua PencetakStruk --");
        for (PencetakStruk alat : pencetak) {
            alat.cetakStruk("Terima kasih!");
        }
        System.out.println("-- semua PemindaiBarcode --");
        for (PemindaiBarcode alat : pemindai) {
            System.out.println("Hasil pindai: " + alat.pindaiBarcode());
        }
        System.out.println("Setiap perangkat hanya berjanji sebanyak kemampuannya.");
    }
}

// ------------------------------------------------------------ MELANGGAR ISP
/** Kontrak GEMUK: siapa pun yang meng-implements-nya wajib bisa tiga hal. */
interface PerangkatKasir {
    void cetakStruk(String teks);

    String pindaiBarcode();

    void bukaLaci();
}

class MesinKasirLengkap implements PerangkatKasir {
    @Override
    public void cetakStruk(String teks) {
        System.out.println("[Mesin Kasir] mencetak: " + teks);
    }

    @Override
    public String pindaiBarcode() {
        return "8991234567890";
    }

    @Override
    public void bukaLaci() {
        System.out.println("[Mesin Kasir] laci terbuka");
    }
}

class PrinterBluetooth implements PerangkatKasir {
    @Override
    public void cetakStruk(String teks) {
        System.out.println("[Printer Bluetooth] mencetak: " + teks);
    }

    @Override
    public String pindaiBarcode() { // [1] method palsu: dipaksa ada
        throw new UnsupportedOperationException("Printer Bluetooth tidak punya pemindai barcode");
    }

    @Override
    public void bukaLaci() { // method palsu kedua
        throw new UnsupportedOperationException("Printer Bluetooth tidak punya laci uang");
    }
}

// -------------------------------------------------------------- SESUAI ISP
/** Kontrak kecil: bisa mencetak struk. */
interface PencetakStruk { // [2] tiga kontrak kecil, masing-masing satu kemampuan
    void cetakStruk(String teks);
}

/** Kontrak kecil: bisa memindai barcode. */
interface PemindaiBarcode {
    String pindaiBarcode();
}

/** Kontrak kecil: punya laci uang. */
interface LaciUang {
    void bukaLaci();
}

class KasirLengkap implements PencetakStruk, PemindaiBarcode, LaciUang { // [3]
    @Override
    public void cetakStruk(String teks) {
        System.out.println("[Mesin Kasir] mencetak: " + teks);
    }

    @Override
    public String pindaiBarcode() {
        return "8991234567890";
    }

    @Override
    public void bukaLaci() {
        System.out.println("[Mesin Kasir] laci terbuka");
    }
}

class PrinterThermal implements PencetakStruk { // [4] cukup satu kontrak, tanpa method palsu
    @Override
    public void cetakStruk(String teks) {
        System.out.println("[Printer Thermal] mencetak: " + teks);
    }
}

class PemindaiGenggam implements PemindaiBarcode {
    @Override
    public String pindaiBarcode() {
        return "8997654321098";
    }
}
