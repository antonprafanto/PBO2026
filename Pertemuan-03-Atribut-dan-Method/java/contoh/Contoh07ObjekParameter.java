/*
 * Contoh 07 - Objek sebagai Parameter
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Saat sebuah objek dikirim ke method, yang dikirim adalah salinan
 * REFERENSI-nya, bukan salinan objeknya. Karena itu method bisa MENGUBAH
 * objek tersebut, dan perubahannya tetap terlihat setelah method selesai.
 * Bandingkan dengan mengirim angka (int) biasa.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh07ObjekParameter.java
 */
public class Contoh07ObjekParameter {

    // Method static milik kelas utama: bisa dipanggil langsung dari main.
    static void tambahBonusAngka(int saldo) { // [4] menerima ANGKA (salinan nilainya)
        saldo = saldo + 5000; // hanya mengubah variabel milik method ini
        System.out.println("  (di dalam: Rp" + saldo + ")");
    }

    static void tambahBonusDompet(DompetDigital dompet) { // [5] menerima OBJEK
        dompet.saldo = dompet.saldo + 5000; // mengubah objek milik pemanggil
        System.out.println("  (di dalam: Rp" + dompet.saldo + ")");
    }

    public static void main(String[] args) {
        DompetDigital dompetBudi = new DompetDigital("Budi", 100000);
        DompetDigital dompetSiti = new DompetDigital("Siti", 20000);

        System.out.println("=== TRANSFER ANTARDOMPET ===");
        dompetBudi.transfer(dompetSiti, 30000); // [6] objek dompetSiti dikirim
        dompetSiti.transfer(dompetBudi, 75000);
        System.out.println("Saldo Budi: Rp" + dompetBudi.saldo);
        System.out.println("Saldo Siti: Rp" + dompetSiti.saldo);

        System.out.println();
        System.out.println("=== MENGIRIM ANGKA vs MENGIRIM OBJEK ===");
        int saldoTunai = 10000;
        tambahBonusAngka(saldoTunai);
        System.out.println("Saldo tunai sesudahnya      : Rp" + saldoTunai); // [7] tidak berubah
        tambahBonusDompet(dompetSiti);
        System.out.println("Saldo dompet Siti sesudahnya: Rp" + dompetSiti.saldo); // [8] berubah
    }
}

/** Dompet digital (e-wallet) dengan saldo dalam rupiah. */
class DompetDigital {
    String pemilik;
    int saldo;

    DompetDigital(String pemilik, int saldo) {
        this.pemilik = pemilik;
        this.saldo = saldo;
    }

    boolean saldoCukup(int jumlah) { // [1] method boolean: jawabannya ya atau tidak
        return saldo >= jumlah;
    }

    void transfer(DompetDigital tujuan, int jumlah) { // [2] tujuan berisi objek lain
        if (!saldoCukup(jumlah)) {
            System.out.println("Transfer gagal: saldo " + pemilik + " tidak cukup");
            return;
        }
        saldo = saldo - jumlah;
        tujuan.saldo = tujuan.saldo + jumlah; // [3] mengubah objek yang dikirim
        System.out.println(pemilik + " transfer Rp" + jumlah + " ke " + tujuan.pemilik);
    }
}
