/*
 * Solusi Latihan 04 - KedaiKita: Menolak Kode Menu Ganda
 * Pertemuan 11 - Exception Handling
 *
 * Ide penyelesaian:
 * - MenuSudahAdaException adalah turunan exception induk KedaiKita, sama
 *   seperti MenuTidakDitemukanException. Ia membawa data kode dan namaLama
 *   (nama menu yang sudah lebih dulu memakai kode itu).
 * - tambahMenu() memeriksa semua menu yang sudah terdaftar. Jika kodenya
 *   sama, lempar MenuSudahAdaException SEBELUM menu baru dimasukkan ke list.
 *   Karena checked, tambahMenu() wajib menulis "throws".
 * - main() menangkap exception itu dan memberi pesan yang ramah.
 *
 * Catatan nama kelas: folder java/ pertemuan ini sudah punya kelas Menu,
 * Kedai, dan KedaiException (di studi-kasus). Agar VS Code tidak protes
 * "The type ... is already defined", solusi ini memakai SALINAN RINGKAS
 * dengan nama lain:
 *     MenuKedai          = salinan ringkas Menu
 *     KedaiKopi          = salinan ringkas Kedai
 *     KedaiKopiException = pengganti KedaiException (induk exception)
 * Di proyek KedaiKita-mu, cukup buat file MenuSudahAdaException.java berisi
 * "public class MenuSudahAdaException extends KedaiException", lalu ubah
 * tambahMenu() di Kedai.java.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04MenuSudahAda.java
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Latihan04MenuSudahAda {

    public static void main(String[] args) {
        KedaiKopi kedai = new KedaiKopi("KedaiKita");
        MenuKedai[] menuBaru = {
            new MenuKedai("M01", "Kopi Susu Gula Aren", 18000),
            new MenuKedai("M02", "Es Teh Manis", 8000),
            new MenuKedai("M03", "Nasi Goreng Kampung", 25000),
            new MenuKedai("M04", "Mie Goreng Jawa", 23000),
            new MenuKedai("M05", "Pisang Goreng Keju", 15000),
            new MenuKedai("M02", "Es Jeruk", 10000), // kode ganda
            new MenuKedai("M06", "Teh Tarik", 12000),
            new MenuKedai("M06", "Kopi Tubruk", 12000) // kode ganda
        };

        System.out.println("=== MENAMBAH MENU ===");
        for (MenuKedai menu : menuBaru) {
            try {
                kedai.tambahMenu(menu);
                System.out.println("[OK] " + menu);
            } catch (MenuSudahAdaException e) {
                System.out.println("[GAGAL] " + e.getMessage());
                System.out.println("        " + menu.getNama()
                        + " tidak ditambahkan, pilih kode selain " + e.getKode());
            }
        }
        System.out.println("Jumlah menu terdaftar: " + kedai.jumlahMenu());
    }
}

/** Pengganti KedaiException: induk semua error khusus KedaiKita. */
class KedaiKopiException extends Exception {
    private static final long serialVersionUID = 1L;

    public KedaiKopiException(String pesan) {
        super(pesan);
    }
}

/** Dilempar saat kode menu yang didaftarkan sudah dipakai menu lain. */
class MenuSudahAdaException extends KedaiKopiException {
    private static final long serialVersionUID = 1L;

    private String kode;
    private String namaLama;

    public MenuSudahAdaException(String kode, String namaLama) {
        super("Kode " + kode + " sudah dipakai oleh " + namaLama);
        this.kode = kode;
        this.namaLama = namaLama;
    }

    public String getKode() {
        return kode;
    }

    public String getNamaLama() {
        return namaLama;
    }
}

/** Salinan ringkas kelas Menu dari studi kasus. */
class MenuKedai {
    private String kode;
    private String nama;
    private int harga;

    public MenuKedai(String kode, String nama, int harga) {
        this.kode = kode;
        this.nama = nama;
        this.harga = harga;
    }

    public String getKode() {
        return kode;
    }

    public String getNama() {
        return nama;
    }

    /** Mengubah 18000 menjadi "Rp18.000" (pengganti Rupiah.format). */
    static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    @Override
    public String toString() {
        return "[" + kode + "] " + nama + " - " + formatRupiah(harga);
    }
}

/** Salinan ringkas kelas Kedai dari studi kasus. */
class KedaiKopi {
    private String nama;
    private List<MenuKedai> daftarMenu;

    public KedaiKopi(String nama) {
        this.nama = nama;
        this.daftarMenu = new ArrayList<>();
    }

    public String getNama() {
        return nama;
    }

    /** Mendaftarkan menu. Melempar MenuSudahAdaException jika kodenya ganda. */
    public void tambahMenu(MenuKedai menu) throws MenuSudahAdaException {
        for (MenuKedai terdaftar : daftarMenu) {
            if (terdaftar.getKode().equals(menu.getKode())) {
                throw new MenuSudahAdaException(menu.getKode(), terdaftar.getNama());
            }
        }
        daftarMenu.add(menu);
    }

    public int jumlahMenu() {
        return daftarMenu.size();
    }
}
