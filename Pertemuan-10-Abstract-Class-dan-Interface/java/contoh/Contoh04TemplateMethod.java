/*
 * Contoh 04 - Template Method: Kerangka Tetap, Detail Diisi Kelas Anak
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * Laporan adalah kelas abstrak dengan method konkret tampilkan(). Method ini
 * menentukan URUTAN langkah yang sama untuk semua laporan (kerangkanya),
 * lalu memanggil method abstrak judul() dan isi() yang diisi kelas anak.
 * penutup() adalah method biasa yang BOLEH di-override (disebut "hook").
 *
 * Pola ini disebut template method. Pola desain lainnya kita bahas di
 * Pertemuan 14.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04TemplateMethod.java
 */
import java.util.List;

public class Contoh04TemplateMethod {

    public static void main(String[] args) {
        List<Laporan> daftar = List.of(
                new LaporanKehadiran("Ayu Lestari", "PBO", 14, 16),
                new LaporanPerpustakaan("OKTOBER", 120, 112));
        System.out.println("=== MENCETAK " + daftar.size() + " LAPORAN ===");
        for (Laporan laporan : daftar) {
            System.out.println();
            laporan.tampilkan(); // [5] satu panggilan, kerangka sama, isi berbeda
        }
    }
}

/** Kelas abstrak untuk semua jenis laporan. */
abstract class Laporan {
    private static final int LEBAR = 40;

    /** Template method. final: kelas anak tidak boleh mengubah kerangkanya. */
    public final void tampilkan() { // [1] urutan langkahnya selalu sama
        System.out.println("=".repeat(LEBAR));
        System.out.println(judul()); // [2] langkah yang diisi kelas anak
        System.out.println("-".repeat(LEBAR));
        for (String baris : isi()) { // [2]
            System.out.println(baris);
        }
        System.out.println("-".repeat(LEBAR));
        System.out.println(penutup()); // [3] hook: sudah punya isi, boleh di-override
        System.out.println("=".repeat(LEBAR));
    }

    /** Judul laporan. */
    public abstract String judul();

    /** Baris-baris isi laporan. */
    public abstract List<String> isi();

    public String penutup() {
        return "Dicetak oleh Sistem Informasi Akademik";
    }
}

/** Rekap kehadiran seorang mahasiswa di satu mata kuliah. */
class LaporanKehadiran extends Laporan {
    private String nama;
    private String mataKuliah;
    private int hadir;
    private int pertemuan;

    public LaporanKehadiran(String nama, String mataKuliah, int hadir, int pertemuan) {
        this.nama = nama;
        this.mataKuliah = mataKuliah;
        this.hadir = hadir;
        this.pertemuan = pertemuan;
    }

    @Override
    public String judul() {
        return "LAPORAN KEHADIRAN " + mataKuliah;
    }

    @Override
    public List<String> isi() {
        int persen = hadir * 100 / pertemuan;
        return List.of(
                "Mahasiswa  : " + nama,
                "Hadir      : " + hadir + " dari " + pertemuan + " pertemuan",
                "Persentase : " + persen + "%");
    }
}

/** Rekap peminjaman buku perpustakaan dalam satu bulan. */
class LaporanPerpustakaan extends Laporan {
    private String bulan;
    private int dipinjam;
    private int dikembalikan;

    public LaporanPerpustakaan(String bulan, int dipinjam, int dikembalikan) {
        this.bulan = bulan;
        this.dipinjam = dipinjam;
        this.dikembalikan = dikembalikan;
    }

    @Override
    public String judul() {
        return "LAPORAN PERPUSTAKAAN BULAN " + bulan;
    }

    @Override
    public List<String> isi() {
        int belum = dipinjam - dikembalikan;
        return List.of(
                "Buku dipinjam      : " + dipinjam,
                "Sudah dikembalikan : " + dikembalikan,
                "Belum dikembalikan : " + belum);
    }

    @Override
    public String penutup() { // [4] meng-override hook
        return "Disahkan oleh Kepala Perpustakaan";
    }
}
