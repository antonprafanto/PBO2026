/*
 * Contoh 03 - Getter dan Setter dengan Validasi
 * Pertemuan 04 - Enkapsulasi
 *
 * - Getter (getVolume()) adalah method public untuk MEMBACA field private.
 * - Setter (setVolume(...)) adalah method public untuk MENGUBAH field private.
 *   Di sinilah data diperiksa sebelum disimpan.
 * - Data yang tidak valid ditolak dengan throw new IllegalArgumentException(...).
 * - try/catch hanya kita intip sekilas untuk menangkap penolakan tersebut
 *   (bahasan lengkapnya di Pertemuan 11).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03GetterSetter.java
 */
public class Contoh03GetterSetter {

    public static void main(String[] args) {
        Televisi tv = new Televisi("Polytron");
        System.out.println("=== TV BARU DINYALAKAN ===");
        System.out.println("Merek : " + tv.getMerek()); // [5] membaca lewat getter
        System.out.println("Volume: " + tv.getVolume());

        System.out.println();
        System.out.println("=== MENGATUR VOLUME ===");
        tv.setVolume(25); // [6] mengubah lewat setter
        System.out.println("Volume diatur ke 25, sekarang " + tv.getVolume());
        tv.setVolume(tv.getVolume() + 10); // [7] baca dulu (25), lalu simpan 35
        System.out.println("Volume dinaikkan 10, sekarang " + tv.getVolume());

        System.out.println();
        System.out.println("=== DATA TIDAK VALID DITOLAK ===");
        try { // [8] intip sekilas: "coba jalankan; jika ditolak, tangkap"
            tv.setVolume(150);
            System.out.println("Baris ini tidak pernah tercetak");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        System.out.println("Volume tetap " + tv.getVolume());
    }
}

/** Televisi dengan volume 0 sampai 100. */
class Televisi {
    private String merek;
    private int volume;

    public Televisi(String merek) {
        this.merek = merek;
        this.volume = 10; // volume awal setiap TV baru
    }

    public String getMerek() { // [1] getter: mengembalikan nilai field private
        return merek;
    }

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) { // [2] setter: menerima nilai baru lewat parameter
        if (volume < 0 || volume > 100) {
            throw new IllegalArgumentException("Volume harus 0-100, bukan " + volume); // [3]
        }
        this.volume = volume; // [4] baru disimpan setelah lolos pemeriksaan
    }
}
