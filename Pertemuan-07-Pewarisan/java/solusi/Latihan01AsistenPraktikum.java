/*
 * Solusi Latihan 01 - Mahasiswa dan Asisten Praktikum
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * Ide penyelesaian:
 * 1. Mahasiswa adalah kelas induk: menyimpan NIM dan nama, punya perkenalan().
 * 2. AsistenPraktikum extends Mahasiswa. Konstruktornya memanggil
 *    super(nim, nama) di baris PERTAMA, lalu mengisi field praktikum.
 * 3. perkenalan() TIDAK ditulis ulang di AsistenPraktikum, tetapi tetap bisa
 *    dipanggil karena diwarisi dari Mahasiswa.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan01AsistenPraktikum.java
 */
public class Latihan01AsistenPraktikum {

    public static void main(String[] args) {
        Mahasiswa bima = new Mahasiswa("2409106002", "Bima Saputra");
        AsistenPraktikum ayu = new AsistenPraktikum("2309106001", "Ayu Lestari",
                "Pemrograman Berorientasi Objek");

        System.out.println("=== MAHASISWA BIASA ===");
        System.out.println(bima.perkenalan());

        System.out.println();
        System.out.println("=== ASISTEN PRAKTIKUM ===");
        System.out.println(ayu.perkenalan()); // method warisan dari Mahasiswa
        System.out.println(ayu.tugas()); // method tambahan milik AsistenPraktikum
        String jawaban = (ayu instanceof Mahasiswa) ? "ya" : "tidak";
        System.out.println(ayu.getNama() + " termasuk Mahasiswa? " + jawaban);
    }
}

/** Mahasiswa dengan NIM dan nama. */
class Mahasiswa {
    private String nim;
    private String nama;

    public Mahasiswa(String nim, String nama) {
        this.nim = nim;
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public String perkenalan() {
        return "Halo, saya " + nama + " (NIM " + nim + ")";
    }
}

/** Mahasiswa yang juga menjadi asisten sebuah praktikum. */
class AsistenPraktikum extends Mahasiswa {
    private String praktikum; // field tambahan

    public AsistenPraktikum(String nim, String nama, String praktikum) {
        super(nim, nama); // bagian Mahasiswa diisi oleh Mahasiswa
        this.praktikum = praktikum;
    }

    public String tugas() {
        // field nama milik induk bersifat private, jadi dibaca lewat getter warisan
        return getNama() + " mengasisteni praktikum " + praktikum;
    }
}
