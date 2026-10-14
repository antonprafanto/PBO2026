/*
 * Solusi Latihan 03 - Peminjaman Buku Perpustakaan
 * Pertemuan 11 - Exception Handling
 *
 * Ide penyelesaian:
 * - Hierarki exception (semuanya checked, karena turunan Exception):
 *       PerpustakaanException                 (induk)
 *       +-- BukuSedangDipinjamException       (data: judul, peminjam)
 *       +-- BatasPinjamException              (data: nama, batas)
 * - Anggota.pinjam() memeriksa dua aturan, lalu melempar exception yang
 *   sesuai. Data tambahan di exception dipakai penangkap untuk memberi saran.
 * - Anggota.kembalikan() melempar PerpustakaanException (induknya langsung)
 *   karena kesalahan ini tidak butuh jenis khusus.
 * - Urutan catch: yang spesifik di atas. cobaKembalikan() cukup menangkap
 *   induknya, PerpustakaanException.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03PeminjamanBuku.java
 */
import java.util.ArrayList;
import java.util.List;

public class Latihan03PeminjamanBuku {

    static void cobaPinjam(Anggota anggota, Buku buku) {
        try {
            anggota.pinjam(buku);
            System.out.println(anggota.getNama() + " meminjam '" + buku.getJudul() + "'");
        } catch (BukuSedangDipinjamException e) {
            System.out.println("Gagal: " + e.getMessage());
            System.out.println("  Saran: tunggu sampai " + e.getPeminjam() + " mengembalikannya");
        } catch (BatasPinjamException e) {
            System.out.println("Gagal: " + e.getMessage());
            System.out.println("  Saran: kembalikan dulu salah satu dari " + e.getBatas()
                    + " buku");
        }
    }

    static void cobaKembalikan(Anggota anggota, Buku buku) {
        try {
            anggota.kembalikan(buku);
            System.out.println(anggota.getNama() + " mengembalikan '" + buku.getJudul() + "'");
        } catch (PerpustakaanException e) {
            System.out.println("Gagal: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        Buku laskar = new Buku("Laskar Pelangi");
        Buku bumi = new Buku("Bumi Manusia");
        Buku negeri = new Buku("Negeri 5 Menara");
        Anggota ayu = new Anggota("Ayu", 2);
        Anggota bima = new Anggota("Bima", 2);

        System.out.println("=== PEMINJAMAN BUKU ===");
        cobaPinjam(ayu, laskar);
        cobaPinjam(ayu, bumi);
        cobaPinjam(ayu, negeri); // melewati batas 2 buku
        cobaPinjam(bima, laskar); // sedang dipinjam Ayu

        System.out.println();
        System.out.println("=== PENGEMBALIAN ===");
        cobaKembalikan(bima, bumi); // Bima tidak meminjam buku ini
        cobaKembalikan(ayu, laskar);
        cobaPinjam(bima, laskar); // sekarang berhasil
    }
}

/** Induk semua error perpustakaan. */
class PerpustakaanException extends Exception {
    private static final long serialVersionUID = 1L;

    public PerpustakaanException(String pesan) {
        super(pesan);
    }
}

/** Dilempar saat buku yang diminta sedang dipinjam orang lain. */
class BukuSedangDipinjamException extends PerpustakaanException {
    private static final long serialVersionUID = 1L;

    private String judul;
    private String peminjam;

    public BukuSedangDipinjamException(String judul, String peminjam) {
        super("Buku '" + judul + "' sedang dipinjam oleh " + peminjam);
        this.judul = judul;
        this.peminjam = peminjam;
    }

    public String getJudul() {
        return judul;
    }

    public String getPeminjam() {
        return peminjam;
    }
}

/** Dilempar saat anggota sudah meminjam sebanyak batas maksimal. */
class BatasPinjamException extends PerpustakaanException {
    private static final long serialVersionUID = 1L;

    private String nama;
    private int batas;

    public BatasPinjamException(String nama, int batas) {
        super(nama + " sudah meminjam " + batas + " buku (batas maksimal)");
        this.nama = nama;
        this.batas = batas;
    }

    public String getNama() {
        return nama;
    }

    public int getBatas() {
        return batas;
    }
}

/** Buku perpustakaan. Menyimpan nama peminjamnya (null jika tersedia). */
class Buku {
    private String judul;
    private String peminjam;

    public Buku(String judul) {
        this.judul = judul;
        this.peminjam = null;
    }

    public String getJudul() {
        return judul;
    }

    public String getPeminjam() {
        return peminjam;
    }

    /** Mencatat nama peminjam. null berarti buku sudah kembali. */
    public void catatPeminjam(String nama) {
        this.peminjam = nama;
    }
}

/** Anggota perpustakaan dengan batas jumlah pinjaman. */
class Anggota {
    private String nama;
    private int batas;
    private List<Buku> pinjaman;

    public Anggota(String nama, int batas) {
        this.nama = nama;
        this.batas = batas;
        this.pinjaman = new ArrayList<>();
    }

    public String getNama() {
        return nama;
    }

    // throws boleh berisi lebih dari satu jenis, dipisah koma. Menulis jenis
    // yang tepat (bukan induknya) memberi tahu pemanggil apa saja yang bisa terjadi.
    public void pinjam(Buku buku)
            throws BukuSedangDipinjamException, BatasPinjamException {
        if (buku.getPeminjam() != null) {
            throw new BukuSedangDipinjamException(buku.getJudul(), buku.getPeminjam());
        }
        if (pinjaman.size() >= batas) {
            throw new BatasPinjamException(nama, batas);
        }
        buku.catatPeminjam(nama); // baru dicatat setelah lolos semua aturan
        pinjaman.add(buku);
    }

    public void kembalikan(Buku buku) throws PerpustakaanException {
        if (!pinjaman.contains(buku)) {
            throw new PerpustakaanException(nama + " tidak sedang meminjam '"
                    + buku.getJudul() + "'");
        }
        buku.catatPeminjam(null);
        pinjaman.remove(buku);
    }
}
