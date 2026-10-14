/*
 * Contoh 05 - Memahami this
 * Pertemuan 02 - Kelas dan Objek
 *
 * this adalah "objek yang sedang menjalankan method ini".
 * - this.email   -> atribut milik objek
 * - email        -> parameter (variabel lokal method)
 * - sapa()       -> memanggil method lain milik objek yang sama
 *                   (boleh juga ditulis this.sapa())
 *
 * Cara menjalankan dari folder java/contoh (Java 11 ke atas):
 *     java Contoh05This.java
 */
public class Contoh05This {

    public static void main(String[] args) {
        Akun akunBudi = new Akun("budi_s", "budi@contoh.id");
        Akun akunSiti = new Akun("siti_a", "siti@contoh.id");

        System.out.println("=== PROFIL AWAL ===");
        akunBudi.tampilkanProfil(); // [3] di dalam method, this = akunBudi
        akunSiti.tampilkanProfil(); //     di dalam method, this = akunSiti

        System.out.println();
        System.out.println("=== BUDI MENGGANTI EMAIL ===");
        akunBudi.gantiEmail("budi.santoso@contoh.id");
        akunBudi.tampilkanProfil();
        akunSiti.tampilkanProfil(); // email Siti tidak ikut berubah
    }
}

/** Akun aplikasi dengan username dan email. */
class Akun {
    String username;
    String email;

    Akun(String username, String email) {
        this.username = username;
        this.email = email;
    }

    void gantiEmail(String email) {
        // [1] this.email = atribut milik objek, email = parameter yang baru diterima
        System.out.println(username + ": email " + this.email + " diganti ke " + email);
        this.email = email;
    }

    String sapa() {
        return "Halo, " + username + "!";
    }

    void tampilkanProfil() {
        System.out.println(this.sapa()); // [2] memanggil method lain milik objek yang sama
        System.out.println("  Email terdaftar: " + email);
    }
}
