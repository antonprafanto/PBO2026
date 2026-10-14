/*
 * Contoh 01 - Dependensi: Memakai Objek Lain Sebentar
 * Pertemuan 05 - Relasi Antar Kelas
 *
 * Penumpang MEMAKAI objek Ojek hanya selama method pesanOjek() berjalan.
 * Objek Ojek datang lewat parameter dan TIDAK disimpan sebagai field.
 * Hubungan "memakai sebentar" seperti ini disebut dependensi.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01Dependensi.java
 */
public class Contoh01Dependensi {

    public static void main(String[] args) {
        Penumpang ayu = new Penumpang("Ayu");
        Ojek ojekRudi = new Ojek("Pak Rudi", "KT 4521 AB", 2500);
        Ojek ojekDedi = new Ojek("Bang Dedi", "KT 3317 CD", 2500);

        System.out.println("=== PERJALANAN 1 ===");
        ayu.pesanOjek(ojekRudi, "Kampus Gunung Kelua", 4); // [5]

        System.out.println();
        System.out.println("=== PERJALANAN 2 ===");
        ayu.pesanOjek(ojekDedi, "Tepian Mahakam", 6); // ojek lain pun bisa

        System.out.println();
        System.out.println("=== RINGKASAN ===");
        System.out.println("Ayu sudah " + ayu.getJumlahPerjalanan() + " kali naik ojek");
        System.out.println("Total ongkos: Rp" + ayu.getTotalOngkos());
    }
}

/** Ojek daring yang bisa mengantar penumpang. */
class Ojek {
    private String pengemudi;
    private String plat;
    private int tarifPerKm;

    public Ojek(String pengemudi, String plat, int tarifPerKm) {
        this.pengemudi = pengemudi;
        this.plat = plat;
        this.tarifPerKm = tarifPerKm;
    }

    /** Mengantar penumpang, lalu mengembalikan ongkosnya. */
    public int antar(String tujuan, int jarakKm) {
        System.out.println("  " + pengemudi + " (" + plat + ") mengantar ke " + tujuan);
        return jarakKm * tarifPerKm;
    }
}

/** Penumpang yang memesan ojek. Ia TIDAK menyimpan objek Ojek. */
class Penumpang {
    private String nama;
    private int jumlahPerjalanan; // [1] yang diingat hanya angka-angka ini
    private int totalOngkos;

    public Penumpang(String nama) {
        this.nama = nama;
        this.jumlahPerjalanan = 0;
        this.totalOngkos = 0;
    }

    public int getJumlahPerjalanan() {
        return jumlahPerjalanan;
    }

    public int getTotalOngkos() {
        return totalOngkos;
    }

    public void pesanOjek(Ojek ojek, String tujuan, int jarakKm) { // [2]
        System.out.println(nama + " memesan ojek, jarak " + jarakKm + " km");
        int ongkos = ojek.antar(tujuan, jarakKm); // [3] memakai objek Ojek
        jumlahPerjalanan++;
        totalOngkos += ongkos;
        System.out.println("  Ongkos: Rp" + ongkos);
        // [4] method selesai: parameter ojek dilepas, tidak disimpan di field
    }
}
