/*
 * Contoh 08 - Checked dan Unchecked Exception (KHUSUS JAVA)
 * Pertemuan 11 - Exception Handling
 *
 * Java membagi exception menjadi dua kelompok:
 * - CHECKED   : turunan Exception, tetapi BUKAN turunan RuntimeException.
 *               Compiler MEMAKSA kita memilih: tangkap dengan try/catch,
 *               atau umumkan dengan "throws" di kepala method.
 * - UNCHECKED : turunan RuntimeException (misalnya IllegalArgumentException).
 *               Compiler tidak memaksa apa-apa.
 *
 * KelasPenuhException sengaja dibuat checked: kelas kuliah yang penuh adalah
 * situasi WAJAR yang harus dipikirkan setiap pemanggil (misalnya dengan
 * menyarankan kelas paralel). Kapasitas 0 adalah kesalahan pemrogram, jadi
 * cukup IllegalArgumentException (unchecked).
 *
 * Python tidak punya pembagian ini (lihat Jembatan Python - Java).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh08CheckedUnchecked.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh08CheckedUnchecked {

    /** Mendaftarkan beberapa mahasiswa sekaligus. Exception TIDAK ditangkap di sini. */
    static void daftarkanRombongan(KelasKuliah kelas, String[] daftarNama)
            throws KelasPenuhException { // [4] "saya tidak menangani, saya meneruskan"
        for (String nama : daftarNama) {
            kelas.daftar(nama);
            System.out.println(nama + " terdaftar di " + kelas.getKode());
        }
    }

    public static void main(String[] args) {
        System.out.println("=== KRS: CHECKED EXCEPTION WAJIB DITANGANI ===");
        KelasKuliah pboA = new KelasKuliah("PBO-A", 2);
        String[] pendaftar = {"Ayu", "Bima", "Citra"};
        for (String nama : pendaftar) {
            try { // [3] tanpa try/catch ini, program GAGAL DIKOMPILASI
                pboA.daftar(nama);
                System.out.println(nama + " terdaftar di " + pboA.getKode());
            } catch (KelasPenuhException e) {
                System.out.println("Gagal: " + e.getMessage());
                System.out.println("  Saran: pilih kelas paralel lain");
            }
        }

        System.out.println();
        System.out.println("=== MENERUSKAN DENGAN THROWS ===");
        KelasKuliah pboB = new KelasKuliah("PBO-B", 1);
        String[] rombongan = {"Dimas", "Eka"};
        try {
            daftarkanRombongan(pboB, rombongan);
        } catch (KelasPenuhException e) { // [5] ditangkap di pemanggil paling atas
            System.out.println("Gagal: " + e.getMessage());
        }

        System.out.println();
        System.out.println("=== UNCHECKED EXCEPTION ===");
        try { // [6] tidak wajib ditangkap, tetapi boleh
            KelasKuliah pboC = new KelasKuliah("PBO-C", 0);
            System.out.println("Kelas " + pboC.getKode() + " dibuat");
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat kelas: " + e.getMessage());
        }
    }
}

/** Dilempar saat kelas kuliah sudah penuh. CHECKED karena turunan Exception. */
class KelasPenuhException extends Exception { // [1]
    private static final long serialVersionUID = 1L;

    public KelasPenuhException(String kode, int kapasitas) {
        super("Kelas " + kode + " sudah penuh (kapasitas " + kapasitas + " orang)");
    }
}

/** Kelas kuliah dengan kapasitas terbatas. */
class KelasKuliah {
    private String kode;
    private int kapasitas;
    private List<String> peserta;

    public KelasKuliah(String kode, int kapasitas) {
        if (kapasitas <= 0) {
            // unchecked: konstruktor ini tidak perlu menulis "throws"
            throw new IllegalArgumentException("Kapasitas harus lebih dari 0");
        }
        this.kode = kode;
        this.kapasitas = kapasitas;
        this.peserta = new ArrayList<>();
    }

    public String getKode() {
        return kode;
    }

    public void daftar(String nama) throws KelasPenuhException { // [2] wajib diumumkan
        if (peserta.size() >= kapasitas) {
            throw new KelasPenuhException(kode, kapasitas);
        }
        peserta.add(nama);
    }
}
