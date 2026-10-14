/*
 * Solusi Latihan 04 - Kartu Perpustakaan
 * Pertemuan 04 - Enkapsulasi
 *
 * Ide penyelesaian:
 * - Penghitung anggota disimpan di field private static jumlahAnggota.
 *   Penghitung naik hanya SETELAH nama dinyatakan valid, sehingga nomor
 *   anggota tidak pernah terlewat. Dibaca lewat getter static getJumlahAnggota().
 * - nomor, nama, dan dipinjam bersifat read-only (hanya getter).
 * - Jumlah buku yang dipinjam hanya berubah lewat pinjam() dan kembalikan(),
 *   dua "pintu resmi" yang menjaga aturan batas pinjam.
 * - Versi sederhana: kita hanya menghitung JUMLAH buku, belum mencatat judulnya
 *   satu per satu (daftar objek dibahas di Pertemuan 05).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04KartuPerpustakaan.java
 */
public class Latihan04KartuPerpustakaan {

    public static void main(String[] args) {
        System.out.println("=== PENDAFTARAN ANGGOTA ===");
        KartuPerpustakaan ayu = new KartuPerpustakaan("Ayu Lestari");
        System.out.println(ayu.getNomor() + " " + ayu.getNama());
        KartuPerpustakaan bima = new KartuPerpustakaan("Bima Saputra");
        System.out.println(bima.getNomor() + " " + bima.getNama());
        try {
            new KartuPerpustakaan("   ");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        KartuPerpustakaan citra = new KartuPerpustakaan("Citra Dewi");
        System.out.println(citra.getNomor() + " " + citra.getNama());
        System.out.println("Jumlah anggota: " + KartuPerpustakaan.getJumlahAnggota());

        System.out.println();
        System.out.println("=== PEMINJAMAN BUKU ===");
        ayu.pinjam("Laskar Pelangi");
        ayu.pinjam("Bumi Manusia");
        ayu.pinjam("Negeri 5 Menara");
        try {
            ayu.pinjam("Sang Pemimpi");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        ayu.kembalikan("Bumi Manusia");
        ayu.pinjam("Sang Pemimpi");
        try {
            bima.kembalikan("Laskar Pelangi");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
    }
}

/** Kartu anggota perpustakaan kampus. */
class KartuPerpustakaan {
    public static final int BATAS_PINJAM = 3;
    private static int jumlahAnggota = 0; // atribut kelas, private

    private String nomor;
    private String nama;
    private int dipinjam;

    public KartuPerpustakaan(String nama) {
        if (nama.isBlank()) {
            throw new IllegalArgumentException("Nama anggota tidak boleh kosong");
        }
        KartuPerpustakaan.jumlahAnggota += 1; // naik hanya jika nama valid
        this.nomor = String.format("AGT-%03d", KartuPerpustakaan.jumlahAnggota);
        this.nama = nama;
        this.dipinjam = 0;
    }

    public static int getJumlahAnggota() {
        return jumlahAnggota;
    }

    public String getNomor() {
        return nomor;
    }

    public String getNama() {
        return nama;
    }

    public int getDipinjam() {
        return dipinjam;
    }

    public void pinjam(String judul) {
        if (dipinjam >= BATAS_PINJAM) {
            throw new IllegalArgumentException(nama + " sudah mencapai batas "
                    + BATAS_PINJAM + " buku");
        }
        dipinjam += 1;
        System.out.println(nama + " meminjam '" + judul + "' (" + dipinjam + "/"
                + BATAS_PINJAM + ")");
    }

    public void kembalikan(String judul) {
        if (dipinjam == 0) {
            throw new IllegalArgumentException(nama + " tidak sedang meminjam buku");
        }
        dipinjam -= 1;
        System.out.println(nama + " mengembalikan '" + judul + "' (" + dipinjam + "/"
                + BATAS_PINJAM + ")");
    }
}
