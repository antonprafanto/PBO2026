/*
 * Contoh 05 - Multiplisitas dan Mencari Objek
 * Pertemuan 05 - Relasi Antar Kelas
 *
 * Grup belajar punya TEPAT SATU ketua (multiplisitas 1) dan MINIMAL SATU
 * anggota (multiplisitas 1..*). Kelas GrupBelajar sendiri yang menjaga
 * aturan itu. Method cariAnggota() mengembalikan objek Peserta, atau null
 * jika tidak ditemukan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05Multiplisitas.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh05Multiplisitas {

    public static void main(String[] args) {
        Peserta ayu = new Peserta("2409106001", "Ayu");
        Peserta bima = new Peserta("2409106002", "Bima");
        Peserta citra = new Peserta("2409106003", "Citra");

        System.out.println("=== GRUP BARU ===");
        GrupBelajar grup = new GrupBelajar("Grup PBO", ayu);
        grup.tampilkan();

        System.out.println();
        System.out.println("=== GRUP TANPA KETUA ===");
        try {
            new GrupBelajar("Grup Hantu", null); // [7] sengaja melanggar aturan
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat grup: " + e.getMessage());
        }

        System.out.println();
        System.out.println("=== MENAMBAH ANGGOTA ===");
        grup.tambahAnggota(bima);
        grup.tambahAnggota(citra);
        grup.tampilkan();

        System.out.println();
        System.out.println("=== MENCARI ANGGOTA ===");
        String[] daftarNim = {"2409106002", "2409106099"};
        for (String nim : daftarNim) {
            Peserta hasil = grup.cariAnggota(nim);
            if (hasil == null) {
                System.out.println("Cari " + nim + ": tidak ditemukan");
            } else {
                System.out.println("Cari " + nim + ": " + hasil);
            }
        }

        System.out.println();
        System.out.println("=== MENGELUARKAN ANGGOTA ===");
        grup.keluarkan("2409106099");
        grup.keluarkan("2409106001");
        grup.keluarkan("2409106003");
        grup.tampilkan();
    }
}

/** Mahasiswa peserta grup belajar. */
class Peserta {
    private String nim;
    private String nama;

    public Peserta(String nim, String nama) {
        this.nim = nim;
        this.nama = nama;
    }

    public String getNim() {
        return nim;
    }

    public String getNama() {
        return nama;
    }

    @Override
    public String toString() {
        return nama + " (" + nim + ")";
    }
}

/** Grup belajar: tepat 1 ketua dan minimal 1 anggota. */
class GrupBelajar {
    private String nama;
    private Peserta ketua;
    private List<Peserta> daftarAnggota;

    public GrupBelajar(String nama, Peserta ketua) {
        if (ketua == null) { // [1] multiplisitas 1: ketua wajib ada
            throw new IllegalArgumentException("Grup wajib punya ketua");
        }
        this.nama = nama;
        this.ketua = ketua;
        this.daftarAnggota = new ArrayList<>();
        this.daftarAnggota.add(ketua); // [2] 1..*: sudah 1 anggota
    }

    public void tambahAnggota(Peserta peserta) {
        daftarAnggota.add(peserta);
    }

    public Peserta cariAnggota(String nim) { // [3]
        for (Peserta peserta : daftarAnggota) {
            if (peserta.getNim().equals(nim)) {
                return peserta;
            }
        }
        return null; // [4] sudah diperiksa semua, tidak ketemu
    }

    public void keluarkan(String nim) {
        Peserta peserta = cariAnggota(nim);
        if (peserta == null) { // [5] periksa null sebelum memakai hasilnya
            System.out.println("Gagal: NIM " + nim + " bukan anggota " + nama);
        } else if (peserta == ketua) { // [6] ketua tidak boleh keluar
            System.out.println("Gagal: " + peserta.getNama()
                    + " adalah ketua, tidak bisa dikeluarkan");
        } else {
            daftarAnggota.remove(peserta);
            System.out.println(peserta.getNama() + " keluar dari " + nama);
        }
    }

    public void tampilkan() {
        System.out.println(nama + " - ketua: " + ketua.getNama());
        System.out.println("Anggota (" + daftarAnggota.size() + " orang):");
        for (Peserta peserta : daftarAnggota) {
            System.out.println("- " + peserta);
        }
    }
}
