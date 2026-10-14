/*
 * Solusi Latihan 06 - Dompet Digital dengan Batas Harian
 * Pertemuan 04 - Enkapsulasi
 *
 * Ide penyelesaian:
 * - Ada empat field private: pemilik, saldo, batasHarian, dan
 *   terpakaiHariIni. Tidak ada satu pun yang punya setter.
 * - terpakaiHariIni bahkan tidak punya getter. Dari luar, yang terlihat
 *   hanyalah hasil hitungannya: getSisaBatasHariIni().
 * - Saldo hanya berubah lewat isiSaldo() dan bayar().
 *   bayar() memeriksa TIGA aturan sekaligus: jumlah positif, saldo cukup,
 *   dan tidak melebihi sisa batas hari ini.
 * - gantiHari() adalah satu-satunya cara mengembalikan pemakaian harian ke 0.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan06DompetDigital.java
 */
public class Latihan06DompetDigital {

    public static void main(String[] args) {
        DompetDigital dompet = new DompetDigital("Siti", 100000);

        System.out.println("=== HARI PERTAMA ===");
        tampilkan(dompet);
        dompet.isiSaldo(150000);
        System.out.println("Isi saldo Rp150000 berhasil");
        try {
            dompet.isiSaldo(5000);
        } catch (IllegalArgumentException e) {
            System.out.println("Isi saldo Rp5000 ditolak: " + e.getMessage());
        }
        cobaBayar(dompet, 45000, "makan siang");
        cobaBayar(dompet, 30000, "fotokopi modul");
        cobaBayar(dompet, 40000, "pulsa");
        tampilkan(dompet);

        System.out.println();
        System.out.println("=== HARI KEDUA ===");
        dompet.gantiHari();
        tampilkan(dompet);
        cobaBayar(dompet, 40000, "pulsa");
        cobaBayar(dompet, 50000, "buku");
        cobaBayar(dompet, -10000, "uji coba curang");
        tampilkan(dompet);
    }

    private static void tampilkan(DompetDigital dompet) {
        System.out.println("  Saldo Rp" + dompet.getSaldo() + " | sisa batas hari ini Rp"
                + dompet.getSisaBatasHariIni());
    }

    private static void cobaBayar(DompetDigital dompet, int jumlah, String keterangan) {
        try {
            dompet.bayar(jumlah);
            System.out.println("Bayar Rp" + jumlah + " (" + keterangan + ") berhasil");
        } catch (IllegalArgumentException e) {
            System.out.println("Bayar Rp" + jumlah + " (" + keterangan + ") ditolak: "
                    + e.getMessage());
        }
    }
}

/** Dompet digital dengan batas pembayaran per hari. */
class DompetDigital {
    public static final int ISI_MINIMAL = 10000;

    private String pemilik;
    private int saldo;
    private int batasHarian;
    private int terpakaiHariIni; // tanpa getter dan tanpa setter

    public DompetDigital(String pemilik, int batasHarian) {
        if (batasHarian <= 0) {
            throw new IllegalArgumentException("Batas harian harus lebih dari 0");
        }
        this.pemilik = pemilik;
        this.saldo = 0;
        this.batasHarian = batasHarian;
        this.terpakaiHariIni = 0;
    }

    public String getPemilik() {
        return pemilik;
    }

    public int getSaldo() {
        return saldo;
    }

    public int getBatasHarian() {
        return batasHarian;
    }

    public int getSisaBatasHariIni() {
        return batasHarian - terpakaiHariIni;
    }

    public void isiSaldo(int jumlah) {
        if (jumlah < ISI_MINIMAL) {
            throw new IllegalArgumentException("Isi saldo minimal Rp" + ISI_MINIMAL);
        }
        saldo += jumlah;
    }

    public void bayar(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah pembayaran harus lebih dari 0");
        }
        if (jumlah > saldo) {
            throw new IllegalArgumentException("Saldo tidak cukup (saldo Rp" + saldo + ")");
        }
        if (jumlah > getSisaBatasHariIni()) {
            throw new IllegalArgumentException("Melebihi batas harian (sisa Rp"
                    + getSisaBatasHariIni() + ")");
        }
        saldo -= jumlah;
        terpakaiHariIni += jumlah;
    }

    /** Dipanggil saat hari berganti: pemakaian harian kembali ke 0. */
    public void gantiHari() {
        terpakaiHariIni = 0;
    }
}
