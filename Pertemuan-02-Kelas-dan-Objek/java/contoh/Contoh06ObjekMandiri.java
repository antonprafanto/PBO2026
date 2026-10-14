/*
 * Contoh 06 - Setiap Objek Menyimpan Datanya Sendiri
 * Pertemuan 02 - Kelas dan Objek
 *
 * Dua rekening dibuat dari kelas yang sama. Transaksi pada satu rekening
 * tidak memengaruhi rekening lain, karena setiap objek punya atribut sendiri.
 *
 * Cara menjalankan dari folder java/contoh (Java 11 ke atas):
 *     java Contoh06ObjekMandiri.java
 */
public class Contoh06ObjekMandiri {

    public static void main(String[] args) {
        RekeningBank rekeningBudi = new RekeningBank("Budi", 500000);
        RekeningBank rekeningSiti = new RekeningBank("Siti", 750000);

        System.out.println("=== SALDO AWAL ===");
        rekeningBudi.cekSaldo();
        rekeningSiti.cekSaldo();

        System.out.println();
        System.out.println("=== TRANSAKSI ===");
        rekeningBudi.setor(200000);
        rekeningBudi.tarik(1000000);
        rekeningSiti.tarik(250000);

        System.out.println();
        System.out.println("=== SALDO AKHIR ===");
        rekeningBudi.cekSaldo();
        rekeningSiti.cekSaldo();
    }
}

/** Rekening tabungan sederhana. */
class RekeningBank {
    String pemilik;
    int saldo;

    RekeningBank(String pemilik, int saldoAwal) {
        this.pemilik = pemilik;
        this.saldo = saldoAwal;
    }

    void setor(int jumlah) {
        saldo = saldo + jumlah;
        System.out.println(pemilik + " setor Rp" + jumlah);
    }

    void tarik(int jumlah) {
        if (jumlah > saldo) {
            System.out.println(pemilik + " gagal tarik Rp" + jumlah + ": saldo tidak cukup");
        } else {
            saldo = saldo - jumlah;
            System.out.println(pemilik + " tarik Rp" + jumlah);
        }
    }

    void cekSaldo() {
        System.out.println("  Saldo " + pemilik + ": Rp" + saldo);
    }
}
