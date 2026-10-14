/*
 * Contoh 05 - Dependensi: Memakai Sementara
 * Pertemuan 06 - UML Class Diagram
 *
 * Diagram (versi Java, sintaks Mermaid):
 *
 *     Motor ..> SPBU : isiBensin
 *
 * - Garis PUTUS-PUTUS dengan panah (..>) berarti Motor BERGANTUNG pada SPBU:
 *   Motor memakai SPBU hanya selama method isiBensin() berjalan.
 * - SPBU datang sebagai PARAMETER dan tidak disimpan sebagai field,
 *   jadi setelah method selesai, motor tidak lagi "mengenal" SPBU itu.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05Dependensi.java
 */
public class Contoh05Dependensi {

    public static void main(String[] args) {
        SPBU spbuJuanda = new SPBU("SPBU Jl. Juanda", 10000);
        SPBU spbuPahlawan = new SPBU("SPBU Jl. Pahlawan", 12500);
        Motor motor = new Motor("KT 3344 XY", 5);

        System.out.println("=== ISI BENSIN ===");
        int total = 0;
        total += motor.isiBensin(spbuJuanda, 3); // [4] SPBU dikirim saat dibutuhkan
        total += motor.isiBensin(spbuPahlawan, 4); // hanya muat 2 liter lagi
        System.out.println(motor.info());
        System.out.println("Total biaya: Rp" + total);
    }
}

/** Stasiun pengisian bahan bakar. Harga per liter hanya contoh. */
class SPBU {
    private String nama;
    private int hargaPerLiter;

    public SPBU(String nama, int hargaPerLiter) {
        this.nama = nama;
        this.hargaPerLiter = hargaPerLiter;
    }

    public String getNama() {
        return nama;
    }

    public int getHargaPerLiter() {
        return hargaPerLiter;
    }
}

/** Motor dengan tangki bensin (dalam liter, bilangan bulat). */
class Motor {
    private String plat;
    private int kapasitasTangki;
    private int isiTangki;

    public Motor(String plat, int kapasitasTangki) {
        this.plat = plat;
        this.kapasitasTangki = kapasitasTangki;
        this.isiTangki = 0;
    }

    public int isiBensin(SPBU spbu, int liter) { // [1] SPBU hanya parameter
        int ruangKosong = kapasitasTangki - isiTangki;
        int literMasuk = Math.min(liter, ruangKosong); // tangki tidak bisa melebihi kapasitas
        isiTangki += literMasuk;
        int biaya = literMasuk * spbu.getHargaPerLiter(); // [2] memakai data milik SPBU
        System.out.println(plat + " isi " + literMasuk + " liter di " + spbu.getNama()
                + ", bayar Rp" + biaya);
        return biaya; // [3] selesai: motor tidak menyimpan SPBU
    }

    public String info() {
        return plat + ": tangki " + isiTangki + "/" + kapasitasTangki + " liter";
    }
}
