/*
 * Solusi Latihan 03 - Paket Kiriman
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Ide penyelesaian:
 * - Dua konstruktor (overloading): dengan layanan, atau tanpa layanan.
 *   Konstruktor tanpa layanan meneruskan ke konstruktor lengkap dengan
 *   this(..., "REG"), jadi layanan bawaannya "REG".
 * - beratKg() membulatkan berat ke ATAS dengan rumus int
 *   (beratGram + 999) / 1000. Contoh: 1200 gram -> 2 kg, 500 gram -> 1 kg.
 * - ongkir() memakai beratKg(). Teks layanan dibandingkan dengan .equals(),
 *   BUKAN dengan ==.
 * - toString() menyusun teks satu baris berisi semua data paket dan ongkirnya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03PaketKiriman.java
 */
public class Latihan03PaketKiriman {

    public static void main(String[] args) {
        Paket paket1 = new Paket("PKT001", "Balikpapan", 1200); // layanan bawaan: REG
        Paket paket2 = new Paket("PKT002", "Bontang", 500, "KILAT");
        Paket paket3 = new Paket("PKT003", "Tenggarong", 2100);

        System.out.println("=== DAFTAR PAKET ===");
        System.out.println(paket1);
        System.out.println(paket2);
        System.out.println(paket3);
        int total = paket1.ongkir() + paket2.ongkir() + paket3.ongkir();
        System.out.println("Total ongkir: Rp" + total);
    }
}

/** Paket kiriman dengan ongkos kirim berdasarkan berat dan layanan. */
class Paket {
    String resi;
    String tujuan;
    int beratGram;
    String layanan;

    Paket(String resi, String tujuan, int beratGram, String layanan) {
        this.resi = resi;
        this.tujuan = tujuan;
        this.beratGram = beratGram;
        this.layanan = layanan;
    }

    Paket(String resi, String tujuan, int beratGram) {
        this(resi, tujuan, beratGram, "REG");
    }

    /** Berat dibulatkan ke atas ke kilogram terdekat. */
    int beratKg() {
        return (beratGram + 999) / 1000;
    }

    int ongkir() {
        int tarif;
        if (layanan.equals("KILAT")) {
            tarif = 15000;
        } else {
            tarif = 9000;
        }
        return beratKg() * tarif;
    }

    @Override
    public String toString() {
        return "[" + resi + "] " + tujuan + ", " + beratGram + " gram, "
                + layanan + " - ongkir Rp" + ongkir();
    }
}
