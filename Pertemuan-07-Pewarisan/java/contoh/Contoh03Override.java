/*
 * Contoh 03 - Override: Menimpa Method Induk (dan Tetap Memakai Versi Induk)
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * TiketVIP mewarisi Tiket, lalu MENIMPA (override) dua method: info() dan
 * hitungBayar(). Anotasi @Override meminta compiler memeriksa bahwa method itu
 * memang ada di induk. Di dalam versi barunya, TiketVIP tetap memakai hasil
 * versi induk lewat super.namaMethod(), sehingga rumusnya tidak ditulis ulang.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03Override.java
 */
public class Contoh03Override {

    public static void main(String[] args) {
        Tiket reguler = new Tiket("Festival Musik Kampus", 50000);
        TiketVIP vip = new TiketVIP("Festival Musik Kampus", 120000, "kursi depan dan kaus");

        System.out.println("=== INFO TIKET ===");
        System.out.println(reguler.info()); // [5] objek Tiket -> versi Tiket
        System.out.println(vip.info()); // [5] objek TiketVIP -> versi TiketVIP

        System.out.println();
        System.out.println("=== BAYAR UNTUK 3 ORANG ===");
        System.out.println("Reguler: Rp" + reguler.hitungBayar(3));
        System.out.println("VIP    : Rp" + vip.hitungBayar(3));
        System.out.println("Acara  : " + vip.getAcara()); // [6] getter warisan
    }
}

/** Tiket reguler sebuah acara. */
class Tiket {
    private String acara;
    private int harga;

    public Tiket(String acara, int harga) {
        this.acara = acara;
        this.harga = harga;
    }

    public String getAcara() {
        return acara;
    }

    public String info() {
        return "Tiket " + acara + " - Rp" + harga;
    }

    public int hitungBayar(int jumlah) {
        return harga * jumlah;
    }
}

/** Tiket VIP: punya fasilitas dan ada biaya layanan per orang. */
class TiketVIP extends Tiket {
    private static final int BIAYA_LAYANAN_VIP = 25000; // per orang, dalam Rupiah

    private String fasilitas;

    public TiketVIP(String acara, int harga, String fasilitas) {
        super(acara, harga);
        this.fasilitas = fasilitas;
    }

    @Override // [1] override: nama, parameter, dan tipe kembalian sama dengan induk
    public String info() {
        return super.info() + " | VIP: " + fasilitas; // [2] versi induk + tambahan
    }

    @Override // [3] override kedua
    public int hitungBayar(int jumlah) {
        int hargaDasar = super.hitungBayar(jumlah); // [4] hitungan versi induk
        return hargaDasar + BIAYA_LAYANAN_VIP * jumlah;
    }
}
