/*
 * File Menu.java: kelas induk Menu. Dua kelas anaknya, Makanan dan Minuman,
 * ada di file Makanan.java dan Minuman.java.
 *
 * Hierarki pewarisan:
 *         Menu            <- kelas induk (superclass)
 *        /    \
 *   Makanan  Minuman      <- kelas anak (subclass)
 *
 * Makanan dan Minuman MEWARISI semua atribut dan method Menu, lalu:
 * - menambah atribut khusus (levelPedas / dingin),
 * - meng-override toString() agar informasinya lebih lengkap.
 *
 * Yang baru di Pertemuan 12: Menu meng-override equals() dan hashCode(), serta
 * meng-implements interface Comparable<Menu>:
 * - equals() dan hashCode() : dua Menu dianggap SAMA jika kodenya sama
 *                             (dibutuhkan agar Menu bisa dipakai di HashSet/HashMap
 *                             dengan benar)
 * - compareTo()             : urutan alami berdasarkan harga, sehingga
 *                             Collections.sort(daftarMenu) otomatis urut dari
 *                             yang termurah
 */

/** Kelas induk: data dan perilaku yang dimiliki SEMUA jenis menu. */
public class Menu implements Comparable<Menu> {
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

    public void kurangiStok(int jumlah) throws StokTidakCukupException {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        if (jumlah > stok) {
            throw new StokTidakCukupException(nama, jumlah, stok);
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

    @Override
    public boolean equals(Object lain) {
        if (!(lain instanceof Menu)) {
            return false; // bukan Menu (atau null): pasti tidak sama
        }
        Menu menuLain = (Menu) lain;
        return kode.equals(menuLain.kode);
    }

    @Override
    public int hashCode() {
        return kode.hashCode();
    }

    /** Urutan alami: harga termurah dulu; jika harga sama, urut kode. */
    @Override
    public int compareTo(Menu lain) {
        if (harga != lain.harga) {
            return Integer.compare(harga, lain.harga);
        }
        return kode.compareTo(lain.kode);
    }
}
