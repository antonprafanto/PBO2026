/*
 * File Menu.java: kelas Menu (sama seperti Pertemuan 04, kini di file sendiri).
 *
 * Perubahan kecil: penghitung jumlah menu (atribut static) dihapus,
 * karena sekarang tugas menghitung menu dipegang oleh kelas Kedai.
 * Konstruktor tanpa stok juga dihapus karena tidak dipakai lagi, dan
 * setHarga() kini diberi kata kunci final (alasannya ada di dekat method itu).
 *
 * Kelas ini tidak punya method main, jadi tidak bisa dijalankan sendiri.
 * Yang dijalankan adalah kelas Main (lihat Main.java).
 */

/** Satu menu KedaiKita. Datanya dilindungi dan hanya diubah lewat method. */
public class Menu {
    private String kode;
    private String nama;
    private int harga;
    private String kategori;
    private int stok;

    public Menu(String kode, String nama, int harga, String kategori, int stok) {
        if (stok < 0) {
            throw new IllegalArgumentException("Stok tidak boleh negatif");
        }
        this.kode = kode;
        this.nama = nama;
        this.kategori = kategori;
        this.stok = stok;
        setHarga(harga); // lewat setter, jadi ikut divalidasi
    }

    public String getKode() {
        return kode;
    }

    public String getNama() {
        return nama;
    }

    public String getKategori() {
        return kategori;
    }

    public int getStok() {
        return stok;
    }

    public int getHarga() {
        return harga;
    }

    // final: setter ini tidak bisa di-override oleh kelas anak (Pertemuan 07),
    // sehingga aman dipanggil dari konstruktor.
    public final void setHarga(int harga) {
        if (harga <= 0) {
            throw new IllegalArgumentException("Harga harus lebih dari 0");
        }
        this.harga = harga;
    }

    public void tambahStok(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        stok += jumlah;
    }

    public void kurangiStok(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        if (jumlah > stok) {
            throw new IllegalArgumentException("Stok " + nama + " tidak cukup (sisa " + stok + ")");
        }
        stok -= jumlah;
    }

    public int hitungTotal(int jumlah) {
        return harga * jumlah;
    }

    public int hargaSetelahDiskon(int persen) {
        int potongan = harga * persen / 100;
        return harga - potongan;
    }

    public boolean stokCukup(int jumlah) {
        return stok >= jumlah;
    }

    @Override
    public String toString() {
        return "[" + kode + "] " + nama + " (" + kategori + ") - "
                + Rupiah.format(harga) + " | stok " + stok;
    }
}
