/*
 * Contoh 04 - Komposisi: Bagian yang Dibuat oleh Keseluruhan
 * Pertemuan 06 - UML Class Diagram
 *
 * Diagram (versi Java, sintaks Mermaid):
 *
 *     Gedung "1" *-- "1..*" Lantai : daftarLantai
 *
 * - Belah ketupat PENUH (*--) ada di sisi Gedung (si "keseluruhan").
 * - Objek Lantai dibuat DI DALAM konstruktor Gedung dan tidak pernah
 *   diserahkan ke luar. Lantai tidak punya arti tanpa gedungnya.
 * - Multiplisitas "1..*": gedung minimal punya satu lantai. Aturan ini
 *   dijaga oleh konstruktor Gedung.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04Komposisi.java
 */

import java.util.ArrayList;
import java.util.List;

public class Contoh04Komposisi {

    public static void main(String[] args) {
        Gedung gedung = new Gedung("Gedung Informatika", 3); // [4] hanya data mentah yang dikirim
        gedung.tambahRuangan(1, "Lobi");
        gedung.tambahRuangan(1, "Ruang Dosen");
        gedung.tambahRuangan(2, "Lab Pemrograman");
        gedung.tambahRuangan(2, "Lab Jaringan");
        gedung.cetakDenah();
        System.out.println("Jumlah lantai: " + gedung.jumlahLantai());

        System.out.println();
        System.out.println("=== MENCOBA GEDUNG TANPA LANTAI ===");
        try {
            new Gedung("Gedung Khayalan", 0);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat gedung: " + e.getMessage());
        }
    }
}

/** Satu lantai gedung beserta nama-nama ruangannya. */
class Lantai {
    private int nomor;
    private List<String> ruangan;

    public Lantai(int nomor) {
        this.nomor = nomor;
        this.ruangan = new ArrayList<>();
    }

    public void tambahRuangan(String nama) {
        ruangan.add(nama);
    }

    public String deskripsi() {
        if (ruangan.isEmpty()) {
            return "Lantai " + nomor + ": (kosong)";
        }
        return "Lantai " + nomor + ": " + String.join(", ", ruangan);
    }
}

/** Gedung yang tersusun atas lantai-lantai. */
class Gedung {
    private String nama;
    private List<Lantai> daftarLantai;

    public Gedung(String nama, int jumlahLantai) {
        if (jumlahLantai < 1) { // [1] menjaga multiplisitas 1..*
            throw new IllegalArgumentException("Gedung minimal punya 1 lantai");
        }
        this.nama = nama;
        this.daftarLantai = new ArrayList<>();
        for (int nomor = 1; nomor <= jumlahLantai; nomor++) {
            daftarLantai.add(new Lantai(nomor)); // [2] bagian dibuat OLEH gedung
        }
    }

    public void tambahRuangan(int nomorLantai, String namaRuangan) {
        Lantai lantai = daftarLantai.get(nomorLantai - 1);
        lantai.tambahRuangan(namaRuangan); // [3] gedung meneruskan perintah
    }

    public int jumlahLantai() {
        return daftarLantai.size();
    }

    public void cetakDenah() {
        System.out.println("=== DENAH " + nama + " ===");
        for (Lantai lantai : daftarLantai) {
            System.out.println(lantai.deskripsi());
        }
    }
}
