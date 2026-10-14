/*
 * Contoh 06 - Generalisasi: Pratinjau Pewarisan
 * Pertemuan 06 - UML Class Diagram
 *
 * Diagram (versi Java, sintaks Mermaid):
 *
 *     Karyawan <|-- Barista
 *     Karyawan <|-- Kasir
 *
 * - Segitiga KOSONG menunjuk ke kelas INDUK (Karyawan).
 * - Barista dan Kasir mewarisi isi Karyawan, sehingga di diagram kotak
 *   kelas anak hanya berisi anggota yang BARU.
 * - Sintaks pewarisan selengkapnya (extends, super, override, dan lainnya)
 *   dipelajari di Pertemuan 07. Di sini kita cukup melihat wujud panahnya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06Generalisasi.java
 */
public class Contoh06Generalisasi {

    public static void main(String[] args) {
        Barista dimas = new Barista("Dimas");
        Kasir sari = new Kasir("Sari");

        System.out.println("=== SHIFT PAGI ===");
        System.out.println(dimas.absen()); // [3] method warisan dari Karyawan
        System.out.println(sari.absen());
        System.out.println(dimas.racik("Kopi Susu Gula Aren"));
        System.out.println(sari.terimaUang(50000));

        System.out.println();
        System.out.println("=== PANAH GENERALISASI DI DALAM PROGRAM ===");
        System.out.println("Induk Barista: " + Barista.class.getSuperclass().getSimpleName()); // [4]
        System.out.println("Induk Kasir  : " + Kasir.class.getSuperclass().getSimpleName());
    }
}

/** Data dan perilaku yang dimiliki SEMUA karyawan kafe. */
class Karyawan {
    private String nama;

    public Karyawan(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public String absen() {
        return nama + " sudah absen masuk";
    }
}

/** Karyawan yang meracik minuman. */
class Barista extends Karyawan { // [1] Barista ADALAH Karyawan: panah menunjuk ke induk

    public Barista(String nama) {
        super(nama); // meneruskan nama ke konstruktor Karyawan (detail di Pertemuan 07)
    }

    public String racik(String minuman) { // [2] anggota baru milik Barista
        return getNama() + " meracik " + minuman;
    }
}

/** Karyawan yang menerima pembayaran. */
class Kasir extends Karyawan {

    public Kasir(String nama) {
        super(nama);
    }

    public String terimaUang(int jumlah) {
        return getNama() + " menerima uang Rp" + jumlah;
    }
}
