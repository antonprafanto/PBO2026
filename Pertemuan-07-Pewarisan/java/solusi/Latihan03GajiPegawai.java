/*
 * Solusi Latihan 03 - Gaji Pegawai Tetap dan Pegawai Kontrak
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * Ide penyelesaian:
 * - Pegawai (induk) menyimpan NIP, nama, dan gaji pokok. hitungGaji() versi
 *   induk mengembalikan gaji pokok saja.
 * - PegawaiTetap dan PegawaiKontrak meng-override hitungGaji(): keduanya
 *   memakai super.hitungGaji() lalu menambahkan komponen milik masing-masing.
 * - toString() juga di-override agar jenis pegawai ikut tampil.
 * - Saat perulangan memanggil p.hitungGaji(), setiap objek otomatis memakai
 *   versi miliknya sendiri (bahasan lengkapnya di Pertemuan 09: Polimorfisme).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03GajiPegawai.java
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Latihan03GajiPegawai {
    private static final int LEBAR_SLIP = 44;

    public static void main(String[] args) {
        List<Pegawai> daftarPegawai = new ArrayList<>();
        daftarPegawai.add(new PegawaiTetap("198703", "Andi Wijaya", 6000000, 1500000));
        daftarPegawai.add(new PegawaiKontrak("200105", "Rina Marlina", 4400000, 20));
        daftarPegawai.add(new PegawaiKontrak("199912", "Dodi Pratama", 4500000, 0));

        System.out.println("=== SLIP GAJI OKTOBER 2026 ===");
        int total = 0;
        for (Pegawai pegawai : daftarPegawai) {
            int gaji = pegawai.hitungGaji();
            total += gaji;
            System.out.println(String.format("%-30s%14s", pegawai.toString(), formatRupiah(gaji)));
        }
        System.out.println("-".repeat(LEBAR_SLIP));
        System.out.println(String.format("%-30s%14s", "Total gaji", formatRupiah(total)));
    }

    /** Mengubah 7500000 menjadi "Rp7.500.000". */
    static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

/** Kelas induk semua pegawai. */
class Pegawai {
    private String nip;
    private String nama;
    private int gajiPokok;

    public Pegawai(String nip, String nama, int gajiPokok) {
        if (gajiPokok <= 0) {
            throw new IllegalArgumentException("Gaji pokok harus lebih dari 0");
        }
        this.nip = nip;
        this.nama = nama;
        this.gajiPokok = gajiPokok;
    }

    public int hitungGaji() {
        return gajiPokok;
    }

    @Override
    public String toString() {
        return nip + " " + nama;
    }
}

/** Pegawai tetap: gaji pokok ditambah tunjangan bulanan. */
class PegawaiTetap extends Pegawai {
    private int tunjangan;

    public PegawaiTetap(String nip, String nama, int gajiPokok, int tunjangan) {
        super(nip, nama, gajiPokok);
        this.tunjangan = tunjangan;
    }

    @Override
    public int hitungGaji() {
        return super.hitungGaji() + tunjangan;
    }

    @Override
    public String toString() {
        return super.toString() + " (tetap)";
    }
}

/** Pegawai kontrak: gaji pokok ditambah upah lembur per jam. */
class PegawaiKontrak extends Pegawai {
    private static final int UPAH_LEMBUR_PER_JAM = 40000; // Rupiah

    private int jamLembur;

    public PegawaiKontrak(String nip, String nama, int gajiPokok, int jamLembur) {
        super(nip, nama, gajiPokok); // WAJIB paling awal, validasi ditulis sesudahnya
        if (jamLembur < 0) {
            throw new IllegalArgumentException("Jam lembur tidak boleh negatif");
        }
        this.jamLembur = jamLembur;
    }

    @Override
    public int hitungGaji() {
        return super.hitungGaji() + jamLembur * UPAH_LEMBUR_PER_JAM;
    }

    @Override
    public String toString() {
        return super.toString() + " (kontrak)";
    }
}
