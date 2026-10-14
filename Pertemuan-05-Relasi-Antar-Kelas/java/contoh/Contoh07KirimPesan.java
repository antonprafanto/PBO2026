/*
 * Contoh 07 - Objek Saling Mengirim Pesan
 * Pertemuan 05 - Relasi Antar Kelas
 *
 * Menarik uang tunai melibatkan tiga objek yang bekerja sama:
 *     MesinAtm --> KartuAtm --> Rekening
 * Setiap objek hanya mengerjakan bagiannya sendiri, lalu meneruskan pesan
 * ke objek yang ia kenal. Baris berawalan [NamaKelas] menunjukkan objek
 * mana yang sedang bekerja.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh07KirimPesan.java
 */
public class Contoh07KirimPesan {

    public static void main(String[] args) {
        Rekening rekeningAyu = new Rekening("Ayu", 500000);
        KartuAtm kartuAyu = new KartuAtm("123456", rekeningAyu);
        MesinAtm mesin = new MesinAtm(1000000);

        System.out.println("=== TRANSAKSI 1: BERHASIL ===");
        mesin.tarikTunai(kartuAyu, "123456", 200000); // [5]

        System.out.println();
        System.out.println("=== TRANSAKSI 2: PIN SALAH ===");
        mesin.tarikTunai(kartuAyu, "111111", 100000);

        System.out.println();
        System.out.println("=== TRANSAKSI 3: SALDO TIDAK CUKUP ===");
        mesin.tarikTunai(kartuAyu, "123456", 400000);

        System.out.println();
        System.out.println("=== SETELAH TRANSAKSI ===");
        System.out.println("Saldo rekening Ayu: Rp" + rekeningAyu.getSaldo());
        System.out.println("Uang di mesin     : Rp" + mesin.getUangTersedia());
    }
}

/** Rekening bank yang menjaga saldonya sendiri. */
class Rekening {
    private String pemilik;
    private int saldo;

    public Rekening(String pemilik, int saldo) {
        this.pemilik = pemilik;
        this.saldo = saldo;
    }

    public int getSaldo() {
        return saldo;
    }

    public boolean tarik(int jumlah) {
        if (jumlah > saldo) {
            System.out.println("    [Rekening] saldo tidak cukup (sisa Rp" + saldo + ")");
            return false;
        }
        saldo -= jumlah;
        System.out.println("    [Rekening] saldo " + pemilik + " kini Rp" + saldo);
        return true;
    }
}

/** Kartu ATM yang MENGENAL rekeningnya (asosiasi). */
class KartuAtm {
    private String pin;
    private Rekening rekening; // [1] kartu menyimpan referensi rekening

    public KartuAtm(String pin, Rekening rekening) {
        this.pin = pin;
        this.rekening = rekening;
    }

    public boolean otorisasi(String pin, int jumlah) {
        if (!pin.equals(this.pin)) {
            System.out.println("  [KartuAtm] PIN salah");
            return false;
        }
        System.out.println("  [KartuAtm] PIN cocok, teruskan ke rekening");
        return rekening.tarik(jumlah); // [2] pesan diteruskan ke Rekening
    }
}

/** Mesin ATM yang MEMAKAI kartu selama transaksi (dependensi). */
class MesinAtm {
    private int uangTersedia;

    public MesinAtm(int uangTersedia) {
        this.uangTersedia = uangTersedia;
    }

    public int getUangTersedia() {
        return uangTersedia;
    }

    public void tarikTunai(KartuAtm kartu, String pin, int jumlah) { // [3]
        System.out.println("[MesinAtm] permintaan tarik Rp" + jumlah);
        if (jumlah > uangTersedia) {
            System.out.println("[MesinAtm] uang di mesin tidak cukup");
            return;
        }
        if (kartu.otorisasi(pin, jumlah)) { // [4] pesan dikirim ke KartuAtm
            uangTersedia -= jumlah;
            System.out.println("[MesinAtm] silakan ambil uang Rp" + jumlah);
        } else {
            System.out.println("[MesinAtm] transaksi dibatalkan");
        }
    }
}
