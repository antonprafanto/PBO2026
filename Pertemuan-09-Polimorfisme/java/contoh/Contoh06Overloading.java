/*
 * Contoh 06 - Overloading Method dan Konstruktor
 * Pertemuan 09 - Polimorfisme
 *
 * Overloading = beberapa method (atau konstruktor) dengan NAMA SAMA tetapi
 * DAFTAR PARAMETER BERBEDA (jumlah, tipe, atau urutan tipenya). Compiler
 * memilih versi yang cocok dengan argumen SAAT KOMPILASI, karena itu
 * overloading disebut polimorfisme waktu kompilasi.
 *
 * Bonus: varargs (Buku... daftarBuku) menerima argumen berapa pun jumlahnya,
 * padanan *args di Python.
 * Bandingkan dengan contoh06_pengganti_overloading.py (output-nya sama persis).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06Overloading.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh06Overloading {

    static void tampilkan(String label, List<Buku> hasil) {
        List<String> teksBuku = new ArrayList<>();
        for (Buku buku : hasil) {
            teksBuku.add(buku.toString());
        }
        if (teksBuku.isEmpty()) {
            teksBuku.add("(tidak ada)");
        }
        System.out.println(String.format("%-28s: %s", label, String.join(", ", teksBuku)));
    }

    public static void main(String[] args) {
        System.out.println("=== KONSTRUKTOR DENGAN NILAI BAWAAN ===");
        Perpustakaan pusat = new Perpustakaan(); // [7] memakai konstruktor tanpa parameter
        Perpustakaan pojok = new Perpustakaan("Pojok Baca Informatika");

        System.out.println();
        System.out.println("=== SATU METHOD, JUMLAH ARGUMEN BEBAS ===");
        pusat.tambahBuku(new Buku("Laskar Pelangi", "Andrea Hirata", 2005)); // 1 buku
        pusat.tambahBuku(
                new Buku("Sang Pemimpi", "Andrea Hirata", 2006),
                new Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980),
                new Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009)); // 3 buku sekaligus
        pojok.tambahBuku(); // 0 buku pun boleh

        System.out.println();
        System.out.println("=== SATU NAMA METHOD, BANYAK CARA CARI ===");
        tampilkan("Judul memuat 'Pe'", pusat.cari("Pe")); // [8] cocok dengan cari(String)
        tampilkan("Tahun 1980", pusat.cari(1980)); // cocok dengan cari(int)
        tampilkan("Judul memuat 'a', tahun 2006", pusat.cari("a", 2006)); // cari(String, int)
        tampilkan("Judul memuat 'Kancil'", pusat.cari("Kancil"));
    }
}

/** Data sebuah buku. */
class Buku {
    private String judul;
    private String penulis;
    private int tahun;

    public Buku(String judul, String penulis, int tahun) {
        this.judul = judul;
        this.penulis = penulis;
        this.tahun = tahun;
    }

    public String getJudul() {
        return judul;
    }

    public String getPenulis() {
        return penulis;
    }

    public int getTahun() {
        return tahun;
    }

    @Override
    public String toString() {
        return judul + " (" + tahun + ")";
    }
}

/** Perpustakaan sederhana yang bisa menyimpan dan mencari buku. */
class Perpustakaan {
    private String nama;
    private List<Buku> koleksi;

    public Perpustakaan() { // [1] konstruktor tanpa parameter
        this("Perpustakaan Kampus"); // memanggil konstruktor lain di kelas ini
    }

    public Perpustakaan(String nama) { // [2] overload konstruktor
        this.nama = nama;
        this.koleksi = new ArrayList<>();
        System.out.println(nama + " dibuka");
    }

    public void tambahBuku(Buku... daftarBuku) { // [3] varargs: berapa pun jumlahnya
        for (Buku buku : daftarBuku) { // daftarBuku berupa array berisi semua argumen
            koleksi.add(buku);
        }
        System.out.println(nama + ": " + daftarBuku.length + " buku ditambahkan");
    }

    public List<Buku> cari(String kataKunci) { // [4] cari berdasarkan judul
        return cari(kataKunci, 0);
    }

    public List<Buku> cari(int tahun) { // [5] nama sama, TIPE parameter berbeda
        return cari("", tahun);
    }

    public List<Buku> cari(String kataKunci, int tahun) { // [6] JUMLAH parameter berbeda
        List<Buku> hasil = new ArrayList<>();
        for (Buku buku : koleksi) {
            boolean cocokJudul = buku.getJudul().contains(kataKunci); // "" selalu cocok
            boolean cocokTahun = tahun == 0 || buku.getTahun() == tahun; // 0 = tahun bebas
            if (cocokJudul && cocokTahun) {
                hasil.add(buku);
            }
        }
        return hasil;
    }
}
