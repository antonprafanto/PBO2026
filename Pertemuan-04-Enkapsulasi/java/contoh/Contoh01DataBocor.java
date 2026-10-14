/*
 * Contoh 01 - Data Bocor vs Data Terlindungi
 * Pertemuan 04 - Enkapsulasi
 *
 * - TabunganBocor: field saldo tanpa access modifier. Kode di kelas lain
 *   dalam paket yang sama bebas mengubahnya, termasuk membuatnya negatif
 *   atau "menyulap" saldo.
 * - TabunganAman: field saldo diberi private, sehingga hanya kode di DALAM
 *   kelas TabunganAman yang boleh menyentuhnya. Saldo hanya berubah lewat
 *   method setor() dan tarik() yang memeriksa aturan lebih dulu.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01DataBocor.java
 */
public class Contoh01DataBocor {

    public static void main(String[] args) {
        System.out.println("=== TABUNGAN BOCOR ===");
        TabunganBocor bocor = new TabunganBocor("Budi", 500000);
        System.out.println("Saldo awal Budi: Rp" + bocor.saldo);
        bocor.saldo = bocor.saldo - 2000000; // [5] tarik melebihi saldo, tidak dicegah
        System.out.println("Setelah ditarik Rp2000000: Rp" + bocor.saldo);
        bocor.saldo = 999999999; // [6] saldo "disulap" langsung dari luar kelas
        System.out.println("Setelah disulap: Rp" + bocor.saldo);

        System.out.println();
        System.out.println("=== TABUNGAN AMAN ===");
        TabunganAman aman = new TabunganAman("Siti", 500000);
        aman.cekSaldo();
        aman.tarik(2000000); // [7] semua perubahan lewat method, aturan selalu dicek
        aman.setor(-100000);
        aman.setor(250000);
        aman.tarik(100000);
        aman.cekSaldo();
    }
}

/** Tabungan tanpa perlindungan: field saldo bisa diubah siapa saja. */
class TabunganBocor {
    String pemilik;
    int saldo; // [1] tanpa access modifier: kelas lain di paket yang sama bebas mengubahnya

    TabunganBocor(String pemilik, int saldo) {
        this.pemilik = pemilik;
        this.saldo = saldo;
    }
}

/** Tabungan yang menjaga saldonya sendiri. */
class TabunganAman {
    private String pemilik;
    private int saldo; // [2] private: hanya kode di dalam kelas ini yang boleh menyentuhnya

    public TabunganAman(String pemilik, int saldo) {
        this.pemilik = pemilik;
        this.saldo = saldo;
    }

    public void setor(int jumlah) { // [3] pintu resmi untuk menambah saldo
        if (jumlah <= 0) {
            System.out.println("Setor Rp" + jumlah + " ditolak: jumlah harus lebih dari 0");
        } else {
            saldo += jumlah;
            System.out.println("Setor Rp" + jumlah + " berhasil");
        }
    }

    public void tarik(int jumlah) { // [4] pintu resmi untuk mengurangi saldo
        if (jumlah <= 0) {
            System.out.println("Tarik Rp" + jumlah + " ditolak: jumlah harus lebih dari 0");
        } else if (jumlah > saldo) {
            System.out.println("Tarik Rp" + jumlah + " ditolak: saldo tidak cukup");
        } else {
            saldo -= jumlah;
            System.out.println("Tarik Rp" + jumlah + " berhasil");
        }
    }

    public void cekSaldo() {
        System.out.println("  Saldo " + pemilik + ": Rp" + saldo);
    }
}
