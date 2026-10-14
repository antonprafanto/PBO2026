/*
 * Contoh 02 - Asosiasi Berarah dan Multiplisitas
 * Pertemuan 06 - UML Class Diagram
 *
 * Diagram (versi Java, sintaks Mermaid):
 *
 *     PesananOjek "*" --> "1" Penumpang : penumpang
 *     PesananOjek "*" --> "0..1" Pengemudi : pengemudi
 *
 * - Panah --> berarti PesananOjek MENGENAL Penumpang dan Pengemudi.
 *   Navigasinya satu arah: Penumpang tidak menyimpan daftar pesanannya.
 * - "1"    : setiap pesanan WAJIB punya tepat satu penumpang (diisi di konstruktor).
 * - "0..1" : pengemudi boleh belum ada (null) saat pesanan baru dibuat.
 * - "*"    : satu penumpang boleh punya banyak pesanan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02Asosiasi.java
 */
public class Contoh02Asosiasi {

    public static void main(String[] args) {
        Penumpang rina = new Penumpang("Rina");
        Pengemudi joko = new Pengemudi("Pak Joko", "KT 4521 AB");

        PesananOjek pesanan1 = new PesananOjek(rina, "Kampus Unmul Gunung Kelua");
        PesananOjek pesanan2 = new PesananOjek(rina, "Pasar Segiri"); // [5] satu penumpang, dua pesanan

        System.out.println("=== PESANAN BARU ===");
        System.out.println(pesanan1.info());
        System.out.println(pesanan2.info());

        System.out.println();
        System.out.println("=== SETELAH PENGEMUDI DITEMUKAN ===");
        pesanan1.tetapkanPengemudi(joko);
        System.out.println(pesanan1.info());
        System.out.println(pesanan2.info());
    }
}

/** Pengguna aplikasi yang memesan ojek. */
class Penumpang {
    private String nama;

    public Penumpang(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }
}

/** Pengemudi ojek beserta pelat nomor motornya. */
class Pengemudi {
    private String nama;
    private String plat;

    public Pengemudi(String nama, String plat) {
        this.nama = nama;
        this.plat = plat;
    }

    public String getNama() {
        return nama;
    }

    public String getPlat() {
        return plat;
    }
}

/** Satu pesanan ojek: penumpang wajib ada, pengemudi menyusul. */
class PesananOjek {
    private Penumpang penumpang; // [1] multiplisitas 1: diisi saat objek lahir
    private String tujuan;
    private Pengemudi pengemudi; // [2] multiplisitas 0..1: boleh null

    public PesananOjek(Penumpang penumpang, String tujuan) {
        this.penumpang = penumpang;
        this.tujuan = tujuan;
        this.pengemudi = null;
    }

    public void tetapkanPengemudi(Pengemudi pengemudi) {
        this.pengemudi = pengemudi; // [3] tautan ke pengemudi dibuat belakangan
    }

    public String info() {
        String teksPengemudi;
        if (pengemudi == null) { // [4] 0..1 berarti harus siap menghadapi null
            teksPengemudi = "belum ada";
        } else {
            teksPengemudi = pengemudi.getNama() + " (" + pengemudi.getPlat() + ")";
        }
        return penumpang.getNama() + " -> " + tujuan + " | pengemudi: " + teksPengemudi;
    }
}
