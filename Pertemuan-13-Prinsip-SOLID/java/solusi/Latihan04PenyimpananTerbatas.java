/*
 * Solusi Latihan 04 - Penyimpanan Terbatas untuk Kedai (DIP)
 * Pertemuan 13 - Prinsip SOLID
 *
 * Ide penyelesaian:
 * - PenyimpananTerbatas adalah kelas BARU yang meng-implements interface
 *   penyimpanan. Ia hanya menyimpan N pesanan TERAKHIR; jika penuh, pesanan
 *   terlama dibuang.
 * - Kelas kedai tidak diubah sedikit pun. Ia tetap menerima "apa saja yang
 *   memenuhi kontrak penyimpanan" lewat konstruktor (dependency injection).
 * - Jenis penyimpanan dipilih di main(), satu-satunya tempat yang perlu tahu.
 * - Maksimal kurang dari 1 tidak masuk akal, jadi ditolak sejak objek dibuat.
 *
 * Catatan nama kelas: folder java/ pertemuan ini sudah punya Pesanan,
 * PenyimpananPesanan, PenyimpananMemori, dan Kedai (di studi-kasus). Nama kelas
 * di dalam satu folder harus unik, jadi salinan ringkasnya diberi akhiran
 * "Ringkas". Di proyekmu sendiri, cukup buat file PenyimpananTerbatas.java
 * berisi "implements PenyimpananPesanan".
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04PenyimpananTerbatas.java
 */
import java.util.ArrayList;
import java.util.List;

public class Latihan04PenyimpananTerbatas {

    /** Membuat empat pesanan, lalu menampilkan isi riwayat kedai. */
    static void layaniPelanggan(KedaiRingkas kedai) {
        for (String nama : List.of("Budi Santoso", "Siti Aminah", "Rina Marlina", "Andi Wijaya")) {
            kedai.buatPesanan(nama);
        }
        System.out.println("Pesanan tersimpan: " + kedai.jumlahPesanan());
        for (PesananRingkas pesanan : kedai.riwayatPesanan()) {
            System.out.println("  " + pesanan.getNomor() + "  " + pesanan.getNamaPelanggan());
        }
    }

    public static void main(String[] args) {
        System.out.println("=== KEDAI DENGAN PENYIMPANAN MEMORI (TANPA BATAS) ===");
        layaniPelanggan(new KedaiRingkas("KedaiKita", new PenyimpananMemoriRingkas()));

        System.out.println();
        System.out.println("=== KEDAI DENGAN PENYIMPANAN TERBATAS (MAKSIMAL 2) ===");
        layaniPelanggan(new KedaiRingkas("KedaiKita", new PenyimpananTerbatas(2)));

        System.out.println();
        System.out.println("=== MAKSIMAL YANG TIDAK MASUK AKAL ===");
        try {
            new PenyimpananTerbatas(0);
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
    }
}

// ------------------------------- salinan RINGKAS dari studi kasus (tidak diubah)
/** Versi ringkas: cukup nomor otomatis dan nama pelanggan. */
class PesananRingkas {
    private static int nomorTerakhir = 0; // static: penomoran berlanjut untuk semua kedai

    private String nomor;
    private String namaPelanggan;

    public PesananRingkas(String namaPelanggan) {
        nomorTerakhir++;
        this.nomor = String.format("P%03d", nomorTerakhir);
        this.namaPelanggan = namaPelanggan;
    }

    public String getNomor() {
        return nomor;
    }

    public String getNamaPelanggan() {
        return namaPelanggan;
    }
}

interface PenyimpananRingkas {
    void simpan(PesananRingkas pesanan);

    List<PesananRingkas> semua();

    default int jumlah() {
        return semua().size();
    }
}

class PenyimpananMemoriRingkas implements PenyimpananRingkas {
    private List<PesananRingkas> data = new ArrayList<>();

    @Override
    public void simpan(PesananRingkas pesanan) {
        data.add(pesanan);
    }

    @Override
    public List<PesananRingkas> semua() {
        return new ArrayList<>(data);
    }
}

class KedaiRingkas {
    private String nama;
    private PenyimpananRingkas penyimpanan; // bergantung pada ABSTRAKSI

    public KedaiRingkas(String nama, PenyimpananRingkas penyimpanan) {
        this.nama = nama;
        this.penyimpanan = penyimpanan;
    }

    public String getNama() {
        return nama;
    }

    public PesananRingkas buatPesanan(String namaPelanggan) {
        PesananRingkas pesanan = new PesananRingkas(namaPelanggan);
        penyimpanan.simpan(pesanan);
        return pesanan;
    }

    public List<PesananRingkas> riwayatPesanan() {
        return penyimpanan.semua();
    }

    public int jumlahPesanan() {
        return penyimpanan.jumlah();
    }
}

// ------------------------------------------------------------------- KELAS BARU
/** Hanya menyimpan N pesanan TERAKHIR. Pesanan terlama dibuang. */
class PenyimpananTerbatas implements PenyimpananRingkas {
    private int maksimal;
    private List<PesananRingkas> data = new ArrayList<>();

    public PenyimpananTerbatas(int maksimal) {
        if (maksimal < 1) {
            throw new IllegalArgumentException("Maksimal pesanan harus minimal 1");
        }
        this.maksimal = maksimal;
    }

    @Override
    public void simpan(PesananRingkas pesanan) {
        data.add(pesanan);
        if (data.size() > maksimal) {
            data.remove(0); // buang pesanan yang paling lama
        }
    }

    @Override
    public List<PesananRingkas> semua() {
        return new ArrayList<>(data); // jumlah() cukup memakai versi default
    }
}
