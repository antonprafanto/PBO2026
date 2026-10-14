/*
 * Contoh 04 - Perpustakaan Mini (pasangan contoh package Python)
 * Pertemuan 15 - Proyek Terintegrasi
 *
 * Versi Python contoh ini memecah kelas-kelasnya ke dalam package
 * perpustakaan/ (beberapa file). Versi Java ini sengaja tetap SATU FILE,
 * karena perintah "java NamaFile.java" hanya bisa menjalankan satu file.
 * Hasilnya sama persis dengan versi Python.
 *
 * Bagaimana jika kelas-kelas ini dijadikan package Java sungguhan?
 * - setiap kelas pindah ke file sendiri di folder perpustakaan/,
 * - baris pertama setiap file: package perpustakaan;
 * - kelas yang dipakai dari luar package diberi public,
 * - kompilasi: javac -d out perpustakaan/*.java Contoh04PaketMini.java
 * Contoh lengkapnya adalah studi kasus KedaiKita (folder src/kedaikita/).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04PaketMini.java
 */
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Contoh04PaketMini {

    public static void main(String[] args) {
        Katalog katalog = new Katalog();
        katalog.tambah(new Buku("B01", "Laskar Pelangi", "Andrea Hirata"));
        katalog.tambah(new Buku("B02", "Bumi Manusia", "Pramoedya Ananta Toer"));
        katalog.tambah(new Buku("B03", "Negeri 5 Menara", "Ahmad Fuadi"));

        System.out.println("=== KATALOG PERPUSTAKAAN MINI ===");
        for (Buku buku : katalog.semua()) {
            System.out.println(buku);
        }

        System.out.println();
        System.out.println("=== MEMINJAM BUKU ===");
        for (String kode : List.of("B02", "B02", "B09")) { // pinjam B02 dua kali, lalu kode asal
            try {
                Buku buku = katalog.cari(kode);
                buku.pinjam();
                System.out.println(kode + ": berhasil dipinjam");
            } catch (PerpustakaanException e) { // menangkap semua error milik "package"
                System.out.println(kode + ": gagal, " + e.getMessage());
            }
        }

        System.out.println();
        System.out.println("=== KATALOG SETELAH PEMINJAMAN ===");
        for (Buku buku : katalog.semua()) {
            System.out.println(buku);
        }
    }
}

/** Induk semua error perpustakaan (checked exception). */
class PerpustakaanException extends Exception {
    private static final long serialVersionUID = 1L;

    PerpustakaanException(String pesan) {
        super(pesan);
    }
}

/** Dilempar saat kode buku tidak terdaftar di katalog. */
class BukuTidakDitemukanException extends PerpustakaanException {
    private static final long serialVersionUID = 1L;

    BukuTidakDitemukanException(String kode) {
        super("buku dengan kode " + kode + " tidak ditemukan");
    }
}

/** Dilempar saat buku yang sedang dipinjam ingin dipinjam lagi. */
class BukuSedangDipinjamException extends PerpustakaanException {
    private static final long serialVersionUID = 1L;

    BukuSedangDipinjamException(String judul) {
        super("buku '" + judul + "' sedang dipinjam");
    }
}

/** Satu buku di perpustakaan. Status pinjam hanya berubah lewat method. */
class Buku {
    private String kode;
    private String judul;
    private String penulis;
    private boolean dipinjam;

    Buku(String kode, String judul, String penulis) {
        this.kode = kode;
        this.judul = judul;
        this.penulis = penulis;
        this.dipinjam = false;
    }

    String getKode() {
        return kode;
    }

    void pinjam() throws BukuSedangDipinjamException {
        if (dipinjam) {
            throw new BukuSedangDipinjamException(judul);
        }
        dipinjam = true;
    }

    void kembalikan() {
        dipinjam = false;
    }

    @Override
    public String toString() {
        String status = dipinjam ? "dipinjam" : "tersedia";
        return "[" + kode + "] " + judul + " - " + penulis + " (" + status + ")";
    }
}

/** Daftar buku perpustakaan, dicari berdasarkan kode. */
class Katalog {
    private Map<String, Buku> daftar = new LinkedHashMap<>(); // kode -> Buku, urut saat ditambah

    void tambah(Buku buku) {
        daftar.put(buku.getKode(), buku);
    }

    Buku cari(String kode) throws BukuTidakDitemukanException {
        if (!daftar.containsKey(kode)) {
            throw new BukuTidakDitemukanException(kode);
        }
        return daftar.get(kode);
    }

    List<Buku> semua() {
        return new ArrayList<>(daftar.values());
    }
}
