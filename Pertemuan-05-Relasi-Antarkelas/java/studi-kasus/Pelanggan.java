/*
 * File Pelanggan.java: kelas Pelanggan (sama seperti Pertemuan 04, kini di file sendiri).
 *
 * Kelas ini tidak punya method main, jadi tidak bisa dijalankan sendiri.
 * Yang dijalankan adalah kelas Main (lihat Main.java).
 */

/** Pelanggan KedaiKita. Poin hanya berubah lewat method resmi. */
public class Pelanggan {
    private String nama;
    private String noHp;
    private int poin;

    public Pelanggan(String nama, String noHp) {
        this.nama = nama;
        this.noHp = noHp;
        this.poin = 0;
    }

    public String getNama() {
        return nama;
    }

    public String getNoHp() {
        return noHp;
    }

    public int getPoin() {
        return poin;
    }

    public void tambahPoin(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Poin yang ditambahkan harus lebih dari 0");
        }
        poin += jumlah;
    }

    /** Menukar poin menjadi potongan harga. 1 poin = Rp1.000. */
    public int tukarPoin(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Poin yang ditukar harus lebih dari 0");
        }
        if (jumlah > poin) {
            throw new IllegalArgumentException("Poin tidak cukup (sisa " + poin + ")");
        }
        poin -= jumlah;
        return jumlah * 1000;
    }

    @Override
    public String toString() {
        return nama + " (" + noHp + ") - " + poin + " poin";
    }
}
