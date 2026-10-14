/*
 * Contoh 03 - Agregasi: Kumpulan Objek yang Bisa Hidup Sendiri
 * Pertemuan 05 - Relasi Antar Kelas
 *
 * Tim MENGUMPULKAN objek Pemain yang dibuat di luar tim. Satu pemain boleh
 * ikut dua tim, dan pemain tetap ada walaupun salah satu timnya bubar.
 * Contoh ini juga memperkenalkan ArrayList: wadah yang ukurannya bisa
 * bertambah (berbeda dengan array biasa).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03Agregasi.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh03Agregasi {

    public static void main(String[] args) {
        Pemain andi = new Pemain("Andi", "kiper"); // [4] pemain lahir lebih dulu, tanpa tim
        Pemain bayu = new Pemain("Bayu", "anchor");
        Pemain candra = new Pemain("Candra", "pivot");
        Tim timKelas = new Tim("Tim Kelas TI-A");
        Tim timFakultas = new Tim("Tim Fakultas");

        System.out.println("=== MEMBENTUK TIM ===");
        timKelas.rekrut(andi);
        timKelas.rekrut(bayu);
        timKelas.rekrut(candra);
        timFakultas.rekrut(bayu); // [5] satu pemain boleh ikut dua tim

        System.out.println();
        timKelas.tampilkan();
        timFakultas.tampilkan();

        System.out.println();
        System.out.println("=== TIM KELAS DIBUBARKAN ===");
        timKelas = null; // [6] objek tim dilepas, pemain tidak ikut hilang
        System.out.println("Pemain tetap ada: " + andi + ", " + bayu + ", " + candra);
        timFakultas.tampilkan();
    }
}

/** Pemain futsal. Ia bisa ada tanpa tim mana pun. */
class Pemain {
    private String nama;
    private String posisi;

    public Pemain(String nama, String posisi) {
        this.nama = nama;
        this.posisi = posisi;
    }

    public String getNama() {
        return nama;
    }

    @Override
    public String toString() {
        return nama + " (" + posisi + ")";
    }
}

/** Tim futsal yang mengumpulkan pemain-pemain yang sudah ada. */
class Tim {
    private String nama;
    private List<Pemain> daftarPemain; // [1] "list berisi Pemain"

    public Tim(String nama) {
        this.nama = nama;
        this.daftarPemain = new ArrayList<>(); // list kosong: 0 pemain
    }

    public void rekrut(Pemain pemain) { // [2] menerima OBJEK yang sudah jadi
        daftarPemain.add(pemain);
        System.out.println(pemain.getNama() + " bergabung dengan " + nama);
    }

    public int jumlahPemain() {
        return daftarPemain.size();
    }

    public void tampilkan() {
        System.out.println(nama + " (" + jumlahPemain() + " pemain):");
        for (int i = 0; i < daftarPemain.size(); i++) { // [3] indeks mulai dari 0
            Pemain pemain = daftarPemain.get(i);
            System.out.println("  " + (i + 1) + ". " + pemain);
        }
    }
}
