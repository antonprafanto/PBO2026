/*
 * Contoh 05 - finally (dan Pengganti else)
 * Pertemuan 11 - Exception Handling
 *
 * Bentuk lengkap try di Java:
 *     try     { kode yang mungkin gagal }
 *     catch   { dijalankan jika GAGAL (dan jenis exception-nya cocok) }
 *     finally { SELALU dijalankan, berhasil maupun gagal }
 *
 * Java TIDAK punya blok else seperti Python. Kode yang hanya boleh berjalan
 * jika semuanya berhasil cukup ditulis di AKHIR blok try.
 *
 * finally cocok untuk "bersih-bersih": mematikan alat, menutup file, dan
 * sejenisnya. Di contoh ini, proyektor harus SELALU dimatikan setelah
 * presentasi, apa pun yang terjadi.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05Finally.java
 */
public class Contoh05Finally {

    static void presentasi(Proyektor proyektor, String namaFile) {
        proyektor.nyalakan();
        try {
            proyektor.tampilkan(namaFile); // [1] bisa gagal
            System.out.println("  Presentasi lancar, terima kasih!"); // [3] hanya jika berhasil
        } catch (IllegalArgumentException e) { // [2] hanya menangani IllegalArgumentException
            System.out.println("  Gagal presentasi: " + e.getMessage());
        } finally { // [4] SELALU dijalankan
            proyektor.matikan();
        }
    }

    public static void main(String[] args) {
        Proyektor proyektor = new Proyektor("R301");

        System.out.println("=== PRESENTASI 1: LANCAR ===");
        presentasi(proyektor, "laporan-akhir.pdf");

        System.out.println();
        System.out.println("=== PRESENTASI 2: FILE SALAH ===");
        presentasi(proyektor, "laporan-akhir.docx");

        System.out.println();
        System.out.println("=== PRESENTASI 3: LAMPU PUTUS ===");
        proyektor.rusakkanLampu();
        try {
            presentasi(proyektor, "laporan-akhir.pdf"); // [5]
        } catch (IllegalStateException e) { // [6] ditangkap oleh pemanggil
            System.out.println("Ditangani di main: " + e.getMessage());
        }
    }
}

/** Proyektor ruang kelas yang hanya bisa menampilkan file PDF. */
class Proyektor {
    private String ruang;
    private boolean lampuPutus;

    public Proyektor(String ruang) {
        this.ruang = ruang;
        this.lampuPutus = false;
    }

    /** Simulasi kerusakan: lampu proyektor putus. */
    public void rusakkanLampu() {
        lampuPutus = true;
    }

    public void nyalakan() {
        System.out.println("  Proyektor " + ruang + " menyala");
    }

    public void matikan() {
        System.out.println("  Proyektor " + ruang + " dimatikan");
    }

    public void tampilkan(String namaFile) {
        if (lampuPutus) {
            throw new IllegalStateException("lampu proyektor putus");
        }
        if (!namaFile.endsWith(".pdf")) {
            throw new IllegalArgumentException("file " + namaFile + " bukan PDF");
        }
        System.out.println("  Menampilkan " + namaFile);
    }
}
