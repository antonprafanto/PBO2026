/*
 * Solusi Latihan 03 - Akun Pengguna dengan Password
 * Pertemuan 04 - Enkapsulasi
 *
 * Ide penyelesaian:
 * - username: read-only (hanya getter).
 * - password disimpan di field private dan SENGAJA tidak diberi getter.
 *   Dari luar, password hanya bisa DICOCOKKAN lewat cekPassword(),
 *   tidak pernah bisa dibaca.
 * - Password hanya bisa diganti lewat gantiPassword(lama, baru), dan hanya
 *   jika password lama benar.
 * - Aturan "minimal 8 karakter" dipakai di dua tempat (konstruktor dan
 *   gantiPassword), jadi ditulis sekali di method private periksaPassword().
 *   Method private hanya bisa dipanggil dari dalam kelas ini.
 *
 * Catatan: di aplikasi sungguhan, password TIDAK PERNAH disimpan sebagai teks
 * asli, melainkan diubah dulu dengan fungsi hash. Di latihan ini kita
 * sederhanakan agar fokus pada enkapsulasi.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03AkunPengguna.java
 */
public class Latihan03AkunPengguna {

    public static void main(String[] args) {
        System.out.println("=== MEMBUAT AKUN ===");
        AkunPengguna akun = new AkunPengguna("ayu_unmul", "rahasia123");
        System.out.println("Akun " + akun.getUsername() + " berhasil dibuat");
        try {
            new AkunPengguna("bima_unmul", "12345");
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat akun: " + e.getMessage());
        }

        System.out.println();
        System.out.println("=== LOGIN ===");
        cobaLogin(akun, "salah123");
        cobaLogin(akun, "rahasia123");

        System.out.println();
        System.out.println("=== GANTI PASSWORD ===");
        try {
            akun.gantiPassword("tebak-tebak", "kopiSusu2026");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        try {
            akun.gantiPassword("rahasia123", "kopi");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        akun.gantiPassword("rahasia123", "kopiSusu2026");
        System.out.println("Password berhasil diganti");
        cobaLogin(akun, "rahasia123");
        cobaLogin(akun, "kopiSusu2026");
    }

    private static void cobaLogin(AkunPengguna akun, String password) {
        String hasil;
        if (akun.cekPassword(password)) {
            hasil = "berhasil";
        } else {
            hasil = "gagal";
        }
        System.out.println("Login " + akun.getUsername() + " dengan '" + password + "': " + hasil);
    }
}

/** Akun aplikasi. Password tersimpan tersembunyi dan tidak punya getter. */
class AkunPengguna {
    public static final int PANJANG_MINIMAL = 8;

    private String username;
    private String password; // tidak ada getter untuk field ini

    public AkunPengguna(String username, String password) {
        periksaPassword(password); // ditolak di sini jika terlalu pendek
        this.username = username;
        this.password = password;
    }

    public String getUsername() {
        return username;
    }

    /** Method internal: menolak password yang terlalu pendek. */
    private void periksaPassword(String password) {
        if (password.length() < PANJANG_MINIMAL) {
            throw new IllegalArgumentException("Password minimal " + PANJANG_MINIMAL + " karakter");
        }
    }

    /** true jika password cocok. Password asli tidak pernah dikeluarkan. */
    public boolean cekPassword(String password) {
        return this.password.equals(password);
    }

    public void gantiPassword(String passwordLama, String passwordBaru) {
        if (!cekPassword(passwordLama)) {
            throw new IllegalArgumentException("Password lama salah");
        }
        periksaPassword(passwordBaru);
        this.password = passwordBaru;
    }
}
