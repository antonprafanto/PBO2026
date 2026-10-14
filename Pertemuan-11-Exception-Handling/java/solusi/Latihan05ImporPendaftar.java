/*
 * Solusi Latihan 05 - Impor Data Pendaftar Lomba
 * Pertemuan 11 - Exception Handling
 *
 * Ide penyelesaian:
 * - BarisDataException membawa nomorBaris dan alasan. Pesannya sudah memuat
 *   nomor baris sehingga penangkap cukup mencetak getMessage().
 * - bacaPendaftar() memeriksa satu baris dari yang paling mendasar:
 *   jumlah kolom -> nama -> umur angka -> rentang umur. Kesalahan apa pun
 *   diubah menjadi BarisDataException, jadi pemanggil cukup menangkap SATU
 *   jenis.
 * - NumberFormatException dari parseInt() dibungkus dengan
 *   new BarisDataException(..., e) (exception chaining) sehingga penyebab
 *   aslinya tetap tersimpan dan bisa diambil dengan getCause().
 * - Java tidak punya blok else: baris yang lolos dicatat di AKHIR blok try.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05ImporPendaftar.java
 */
import java.util.ArrayList;
import java.util.List;

public class Latihan05ImporPendaftar {
    static final int UMUR_MIN = 17;
    static final int UMUR_MAKS = 25;

    /** Mengubah satu baris "nama;umur" menjadi Pendaftar. */
    static Pendaftar bacaPendaftar(int nomorBaris, String teks) throws BarisDataException {
        String[] bagian = teks.split(";");
        if (bagian.length != 2) {
            throw new BarisDataException(nomorBaris, "format harus nama;umur");
        }
        String nama = bagian[0].trim();
        String teksUmur = bagian[1].trim();
        if (nama.isEmpty()) {
            throw new BarisDataException(nomorBaris, "nama tidak boleh kosong");
        }
        int umur;
        try {
            umur = Integer.parseInt(teksUmur);
        } catch (NumberFormatException e) {
            throw new BarisDataException(nomorBaris, "umur '" + teksUmur + "' bukan angka", e);
        }
        if (umur < UMUR_MIN || umur > UMUR_MAKS) {
            throw new BarisDataException(nomorBaris, "umur " + umur + " di luar syarat "
                    + UMUR_MIN + "-" + UMUR_MAKS + " tahun");
        }
        return new Pendaftar(nama, umur);
    }

    public static void main(String[] args) {
        String[] data = {
            "Ayu Lestari;20",
            "Bima Saputra",
            "Citra Dewi;dua puluh",
            ";19",
            "Dimas Pratama;30",
            "Eka Putri;18",
            "Fajar Nugraha;21;Samarinda"
        };
        List<Pendaftar> peserta = new ArrayList<>();
        int jumlahDitolak = 0;

        System.out.println("=== IMPOR DATA PENDAFTAR LOMBA DEBAT ===");
        for (int nomor = 1; nomor <= data.length; nomor++) {
            try {
                Pendaftar pendaftar = bacaPendaftar(nomor, data[nomor - 1]);
                peserta.add(pendaftar);
                System.out.println("[OK] Baris " + nomor + ": " + pendaftar);
            } catch (BarisDataException e) {
                jumlahDitolak++;
                System.out.println("[DITOLAK] " + e.getMessage());
                if (e.getCause() != null) {
                    System.out.println("          (penyebab asli: kesalahan konversi angka)");
                }
            }
        }

        System.out.println();
        System.out.println("Diterima: " + peserta.size() + ", ditolak: " + jumlahDitolak);
        System.out.println("Daftar peserta:");
        for (Pendaftar pendaftar : peserta) {
            System.out.println("- " + pendaftar);
        }
    }
}

/** Kesalahan pada satu baris data. Menyimpan nomor barisnya. */
class BarisDataException extends Exception {
    private static final long serialVersionUID = 1L;

    private int nomorBaris;
    private String alasan;

    public BarisDataException(int nomorBaris, String alasan) {
        super("Baris " + nomorBaris + ": " + alasan);
        this.nomorBaris = nomorBaris;
        this.alasan = alasan;
    }

    public BarisDataException(int nomorBaris, String alasan, Throwable penyebab) {
        super("Baris " + nomorBaris + ": " + alasan, penyebab);
        this.nomorBaris = nomorBaris;
        this.alasan = alasan;
    }

    public int getNomorBaris() {
        return nomorBaris;
    }

    public String getAlasan() {
        return alasan;
    }
}

/** Pendaftar lomba yang datanya sudah lolos pemeriksaan. */
class Pendaftar {
    private String nama;
    private int umur;

    public Pendaftar(String nama, int umur) {
        this.nama = nama;
        this.umur = umur;
    }

    @Override
    public String toString() {
        return nama + " (" + umur + " tahun)";
    }
}
