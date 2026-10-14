/*
 * Solusi Latihan 02 - Akun dan Akun Premium
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * Ide penyelesaian:
 * - AkunPremium extends Akun dan menambah field masa aktif (bulan).
 * - info() di-override (@Override): ambil teks versi induk dengan super.info(),
 *   lalu tambahkan keterangan premium.
 * - batasUnggahMb() di-override: hasil versi induk dikali 10, sehingga jika
 *   batas akun biasa berubah, batas akun premium otomatis ikut menyesuaikan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02AkunPremium.java
 */
public class Latihan02AkunPremium {

    public static void main(String[] args) {
        Akun budi = new Akun("budi_s", "budi@contoh.id");
        AkunPremium siti = new AkunPremium("siti_a", "siti@contoh.id", 6);

        System.out.println("=== DAFTAR AKUN ===");
        System.out.println(budi.info());
        System.out.println(siti.info());

        System.out.println();
        System.out.println("=== BATAS UNGGAH ===");
        System.out.println(budi.getUsername() + ": " + budi.batasUnggahMb() + " MB");
        System.out.println(siti.getUsername() + ": " + siti.batasUnggahMb() + " MB");
    }
}

/** Akun biasa di sebuah aplikasi penyimpanan berkas. */
class Akun {
    private String username;
    private String email;

    public Akun(String username, String email) {
        this.username = username;
        this.email = email;
    }

    public String getUsername() {
        return username;
    }

    public String info() {
        return username + " <" + email + ">";
    }

    public int batasUnggahMb() {
        return 100;
    }
}

/** Akun berbayar dengan batas unggah 10 kali lipat. */
class AkunPremium extends Akun {
    private int masaAktifBulan;

    public AkunPremium(String username, String email, int masaAktifBulan) {
        super(username, email);
        this.masaAktifBulan = masaAktifBulan;
    }

    @Override // versi induk + keterangan premium
    public String info() {
        return super.info() + " [PREMIUM " + masaAktifBulan + " bulan]";
    }

    @Override // memakai hasil versi induk
    public int batasUnggahMb() {
        return super.batasUnggahMb() * 10;
    }
}
