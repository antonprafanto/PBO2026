/*
 * Contoh 07 - Atribut Kelas (static) yang Dilindungi
 * Pertemuan 04 - Enkapsulasi
 *
 * Atribut KELAS (static, milik bersama semua objek) juga perlu dilindungi.
 * Jika siapa saja bisa mengubah penghitung nomor antrean, nomor tiket bisa kembar.
 *
 * - Penghitung disimpan di field private static nomorTerakhir.
 * - Penghitung hanya dinaikkan oleh konstruktor, SETELAH data dinyatakan valid,
 *   sehingga tidak ada nomor yang "hangus".
 * - Dari luar, jumlah tiket dibaca lewat getter static getJumlahTiket().
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh07AtributKelasPrivat.java
 */
public class Contoh07AtributKelasPrivat {

    public static void main(String[] args) {
        System.out.println("=== PENGAMBILAN TIKET ===");
        TiketAntrean budi = new TiketAntrean("Budi");
        System.out.println(budi.getNomor() + " - " + budi.getNama());
        TiketAntrean siti = new TiketAntrean("Siti");
        System.out.println(siti.getNomor() + " - " + siti.getNama());
        try {
            new TiketAntrean(""); // [5] ditolak sebelum penghitung dinaikkan
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        TiketAntrean rina = new TiketAntrean("Rina");
        System.out.println(rina.getNomor() + " - " + rina.getNama()); // tetap A003

        System.out.println();
        System.out.println("Jumlah tiket tercetak: " + TiketAntrean.getJumlahTiket()); // [6]
        // TiketAntrean.nomorTerakhir = 0; // [7] jika tanda // dihapus: error kompilasi
    }
}

/** Tiket antrean loket. Nomornya dibuat otomatis dan tidak boleh kembar. */
class TiketAntrean {
    private static int nomorTerakhir = 0; // [1] milik kelas, private: tak bisa diubah dari luar

    private int nomor;
    private String nama;

    public TiketAntrean(String nama) {
        if (nama.isBlank()) {
            throw new IllegalArgumentException("Nama tidak boleh kosong");
        }
        TiketAntrean.nomorTerakhir += 1; // [2] naik HANYA jika data sudah valid
        this.nomor = TiketAntrean.nomorTerakhir;
        this.nama = nama;
    }

    public static int getJumlahTiket() { // [3] getter static: dipanggil lewat nama kelas
        return nomorTerakhir;
    }

    public String getNomor() { // [4] getter boleh menyajikan data dalam format yang rapi
        return String.format("A%03d", nomor);
    }

    public String getNama() {
        return nama;
    }
}
