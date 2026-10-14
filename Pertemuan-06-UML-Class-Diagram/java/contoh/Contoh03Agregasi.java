/*
 * Contoh 03 - Agregasi: Bagian yang Bisa Hidup Sendiri
 * Pertemuan 06 - UML Class Diagram
 *
 * Diagram (versi Java, sintaks Mermaid):
 *
 *     KelasKuliah "*" o-- "*" Mahasiswa : peserta
 *
 * - Belah ketupat KOSONG (o--) ada di sisi KelasKuliah (si "keseluruhan").
 * - Objek Mahasiswa dibuat DI LUAR kelas kuliah, lalu dikirim lewat parameter.
 * - Satu mahasiswa boleh ikut banyak kelas kuliah, dan tetap ada walaupun
 *   sebuah kelas kuliah sudah selesai.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03Agregasi.java
 */

import java.util.ArrayList;
import java.util.List;

public class Contoh03Agregasi {

    public static void main(String[] args) {
        Mahasiswa ayu = new Mahasiswa("2409106001", "Ayu Lestari"); // [4] bagian dibuat di luar
        Mahasiswa bima = new Mahasiswa("2409106002", "Bima Saputra");
        Mahasiswa citra = new Mahasiswa("2409106003", "Citra Dewi");

        KelasKuliah pbo = new KelasKuliah("Pemrograman Berorientasi Objek", 2);
        KelasKuliah basisData = new KelasKuliah("Basis Data", 40);

        System.out.println("=== PENDAFTARAN KELAS PBO ===");
        for (Mahasiswa mhs : List.of(ayu, bima, citra)) {
            if (pbo.tambahPeserta(mhs)) {
                System.out.println(mhs.getNama() + " masuk kelas " + pbo.getNamaMk());
            } else {
                System.out.println(mhs.getNama() + " gagal: kelas " + pbo.getNamaMk() + " penuh");
            }
        }
        basisData.tambahPeserta(ayu); // [5] Ayu ikut dua kelas sekaligus
        basisData.tambahPeserta(citra);

        System.out.println();
        System.out.println("=== PESERTA BASIS DATA ===");
        for (Mahasiswa mhs : basisData.daftarPeserta()) {
            System.out.println(mhs.getNim() + " " + mhs.getNama());
        }
        if (pbo.daftarPeserta().get(0) == basisData.daftarPeserta().get(0)) {
            System.out.println("Ayu di kelas PBO dan di kelas Basis Data adalah objek yang SAMA");
        }

        System.out.println();
        System.out.println("=== KELAS PBO SELESAI ===");
        pbo = null; // [6] si keseluruhan dibubarkan
        System.out.println(ayu.getNama() + " tetap ada, NIM " + ayu.getNim());
        System.out.println("Peserta Basis Data masih " + basisData.daftarPeserta().size() + " orang");
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

    public String getNim() {
        return nim;
    }

    public String getNama() {
        return nama;
    }
}

/** Kelas kuliah yang menampung mahasiswa sampai kapasitas tertentu. */
class KelasKuliah {
    private String namaMk;
    private int kapasitas;
    private List<Mahasiswa> peserta; // [1] list berisi referensi Mahasiswa

    public KelasKuliah(String namaMk, int kapasitas) {
        this.namaMk = namaMk;
        this.kapasitas = kapasitas;
        this.peserta = new ArrayList<>();
    }

    public String getNamaMk() {
        return namaMk;
    }

    public boolean tambahPeserta(Mahasiswa mahasiswa) { // [2] bagian datang dari luar
        if (peserta.size() >= kapasitas) {
            return false;
        }
        peserta.add(mahasiswa);
        return true;
    }

    public List<Mahasiswa> daftarPeserta() {
        return new ArrayList<>(peserta); // [3] salinan list, isi asli tetap aman
    }
}
