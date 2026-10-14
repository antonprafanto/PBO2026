/*
 * Solusi Latihan 05 - Perpustakaan Mini
 * Pertemuan 05 - Relasi Antar Kelas
 *
 * Relasi yang dipakai:
 * - Perpustakaan o-- Buku        : agregasi (buku dibuat di luar, lalu didaftarkan)
 * - Perpustakaan *-- Peminjaman  : komposisi (peminjaman dibuat OLEH perpustakaan)
 * - Peminjaman --> Buku, Anggota : asosiasi (peminjaman mengenal buku dan peminjamnya)
 * - Perpustakaan ..> Anggota     : dependensi (anggota hanya datang lewat parameter)
 *
 * Ide penyelesaian:
 * - Status "sedang dipinjam" TIDAK disimpan di Buku. Status itu dicari dari
 *   daftar peminjaman yang masih aktif, sehingga datanya tidak pernah ganda.
 * - cariBuku() mengembalikan Buku atau null, dan pemanggilnya selalu
 *   memeriksa null lebih dulu.
 * - Membandingkan buku dan anggota memakai operator == (objek yang SAMA).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05Perpustakaan.java
 */
import java.util.ArrayList;
import java.util.List;

public class Latihan05Perpustakaan {

    public static void main(String[] args) {
        Perpustakaan perpustakaan = new Perpustakaan("Pojok Baca TI");
        perpustakaan.tambahBuku(new Buku("B01", "Laskar Pelangi"));
        perpustakaan.tambahBuku(new Buku("B02", "Bumi Manusia"));
        perpustakaan.tambahBuku(new Buku("B03", "Negeri 5 Menara"));
        Anggota ayu = new Anggota("Ayu");
        Anggota bima = new Anggota("Bima");

        System.out.println("=== KOLEKSI AWAL ===");
        perpustakaan.tampilkanKoleksi();

        System.out.println();
        System.out.println("=== PEMINJAMAN ===");
        perpustakaan.pinjam("B01", ayu);
        perpustakaan.pinjam("B02", ayu);
        perpustakaan.pinjam("B03", ayu);
        perpustakaan.pinjam("B02", bima);
        perpustakaan.pinjam("B99", bima);
        perpustakaan.pinjam("B03", bima);

        System.out.println();
        System.out.println("=== PENGEMBALIAN ===");
        perpustakaan.kembalikan("B01");
        perpustakaan.kembalikan("B01");

        System.out.println();
        System.out.println("=== KOLEKSI AKHIR ===");
        perpustakaan.tampilkanKoleksi();

        System.out.println();
        System.out.println("=== RIWAYAT ===");
        perpustakaan.tampilkanRiwayat();
    }
}

/** Satu buku di koleksi perpustakaan. */
class Buku {
    private String kode;
    private String judul;

    public Buku(String kode, String judul) {
        this.kode = kode;
        this.judul = judul;
    }

    public String getKode() {
        return kode;
    }

    public String getJudul() {
        return judul;
    }
}

/** Anggota perpustakaan. */
class Anggota {
    private String nama;

    public Anggota(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }
}

/** Catatan satu kali peminjaman: buku apa, oleh siapa, masih aktif atau tidak. */
class Peminjaman {
    private Buku buku;
    private Anggota anggota;
    private boolean aktif;

    public Peminjaman(Buku buku, Anggota anggota) {
        this.buku = buku;
        this.anggota = anggota;
        this.aktif = true;
    }

    public Buku getBuku() {
        return buku;
    }

    public Anggota getAnggota() {
        return anggota;
    }

    public boolean isAktif() {
        return aktif;
    }

    public void selesaikan() {
        aktif = false;
    }

    @Override
    public String toString() {
        String status;
        if (aktif) {
            status = "aktif";
        } else {
            status = "selesai";
        }
        return buku.getJudul() + " oleh " + anggota.getNama() + " (" + status + ")";
    }
}

/** Perpustakaan yang punya koleksi buku dan riwayat peminjaman. */
class Perpustakaan {
    private static final int BATAS_PINJAM = 2; // paling banyak 2 buku per anggota

    private String nama;
    private List<Buku> koleksi;
    private List<Peminjaman> riwayat;

    public Perpustakaan(String nama) {
        this.nama = nama;
        this.koleksi = new ArrayList<>();
        this.riwayat = new ArrayList<>();
    }

    public void tambahBuku(Buku buku) {
        koleksi.add(buku);
    }

    public Buku cariBuku(String kode) {
        for (Buku buku : koleksi) {
            if (buku.getKode().equals(kode)) {
                return buku;
            }
        }
        return null;
    }

    /** Peminjaman yang masih berjalan untuk buku ini, atau null. */
    private Peminjaman peminjamanAktif(Buku buku) {
        for (Peminjaman peminjaman : riwayat) {
            if (peminjaman.isAktif() && peminjaman.getBuku() == buku) {
                return peminjaman;
            }
        }
        return null;
    }

    private int jumlahDipinjam(Anggota anggota) {
        int jumlah = 0;
        for (Peminjaman peminjaman : riwayat) {
            if (peminjaman.isAktif() && peminjaman.getAnggota() == anggota) {
                jumlah++;
            }
        }
        return jumlah;
    }

    public void pinjam(String kode, Anggota anggota) {
        Buku buku = cariBuku(kode);
        if (buku == null) {
            System.out.println("Gagal: buku " + kode + " tidak ditemukan");
            return;
        }
        Peminjaman sedang = peminjamanAktif(buku);
        if (sedang != null) {
            System.out.println("Gagal: " + buku.getJudul() + " sedang dipinjam "
                    + sedang.getAnggota().getNama());
            return;
        }
        if (jumlahDipinjam(anggota) >= BATAS_PINJAM) {
            System.out.println("Gagal: " + anggota.getNama() + " sudah meminjam "
                    + BATAS_PINJAM + " buku");
            return;
        }
        riwayat.add(new Peminjaman(buku, anggota)); // dibuat OLEH perpustakaan
        System.out.println(anggota.getNama() + " meminjam " + buku.getJudul());
    }

    public void kembalikan(String kode) {
        Buku buku = cariBuku(kode);
        if (buku == null) {
            System.out.println("Gagal: buku " + kode + " tidak ditemukan");
            return;
        }
        Peminjaman sedang = peminjamanAktif(buku);
        if (sedang == null) {
            System.out.println("Gagal: " + buku.getJudul() + " tidak sedang dipinjam");
            return;
        }
        sedang.selesaikan();
        System.out.println(sedang.getAnggota().getNama() + " mengembalikan " + buku.getJudul());
    }

    public void tampilkanKoleksi() {
        System.out.println("Koleksi " + nama + ":");
        for (Buku buku : koleksi) {
            Peminjaman sedang = peminjamanAktif(buku);
            String status;
            if (sedang == null) {
                status = "tersedia";
            } else {
                status = "dipinjam " + sedang.getAnggota().getNama();
            }
            System.out.println("- [" + buku.getKode() + "] " + buku.getJudul() + ": " + status);
        }
    }

    public void tampilkanRiwayat() {
        System.out.println("Riwayat peminjaman:");
        for (int i = 0; i < riwayat.size(); i++) {
            System.out.println("  " + (i + 1) + ". " + riwayat.get(i));
        }
    }
}
