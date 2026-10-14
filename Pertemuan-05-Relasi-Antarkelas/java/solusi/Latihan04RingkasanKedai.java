/*
 * Solusi Latihan 04 - Ringkasan Penjualan KedaiKita
 * Pertemuan 05 - Relasi Antarkelas
 *
 * Ide penyelesaian:
 * - jumlahPorsi() di Pesanan: jumlahkan getJumlah() dari setiap ItemPesanan.
 * - getDaftarPesanan() di Kedai: kembalikan SALINAN list pesanan.
 * - totalPendapatan() di Kedai: Kedai bertanya ke setiap Pesanan lewat
 *   hitungTotal(), dan setiap Pesanan bertanya ke ItemPesanan miliknya.
 *
 * Catatan nama kelas: di studi kasus, kelas-kelas ini tersebar di beberapa
 * file (Menu.java, Pesanan.java, ...). Agar solusi ini bisa dijalankan sebagai
 * SATU file, kelas yang dibutuhkan disalin ke sini dalam versi ringkas dan
 * diberi akhiran "Ringkas" (MenuRingkas, PesananRingkas, ...). Alasannya,
 * folder java/ pertemuan ini sudah punya kelas Menu, Pesanan, dan Kedai di
 * studi-kasus. Editor seperti VS Code menganggap satu folder sebagai satu
 * proyek dan akan protes "The type Menu is already defined" jika ada dua
 * kelas bernama sama. Di proyekmu sendiri, cukup tambahkan method baru ke
 * Pesanan.java dan Kedai.java.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04RingkasanKedai.java
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Latihan04RingkasanKedai {

    public static void main(String[] args) {
        KedaiRingkas kedai = new KedaiRingkas("KedaiKita");
        kedai.tambahMenu(new MenuRingkas("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20));
        kedai.tambahMenu(new MenuRingkas("M02", "Es Teh Manis", 8000, "Minuman", 30));
        kedai.tambahMenu(new MenuRingkas("M03", "Nasi Goreng Kampung", 25000, "Makanan", 15));
        kedai.tambahMenu(new MenuRingkas("M04", "Mie Goreng Jawa", 23000, "Makanan", 10));
        kedai.tambahMenu(new MenuRingkas("M05", "Pisang Goreng Keju", 15000, "Makanan", 12));
        PelangganRingkas budi = new PelangganRingkas("Budi Santoso", "081234567890");
        PelangganRingkas siti = new PelangganRingkas("Siti Aminah", "082198765432");

        PesananRingkas pesananBudi = kedai.buatPesanan(budi);
        pesananBudi.tambahItem(kedai.cariMenu("M01"), 2);
        pesananBudi.tambahItem(kedai.cariMenu("M03"), 1);
        PesananRingkas pesananSiti = kedai.buatPesanan(siti);
        pesananSiti.tambahItem(kedai.cariMenu("M02"), 2);
        pesananSiti.tambahItem(kedai.cariMenu("M05"), 1);

        System.out.println("=== RINGKASAN PESANAN ===");
        for (PesananRingkas pesanan : kedai.getDaftarPesanan()) {
            String total = formatRupiah(pesanan.hitungTotal());
            System.out.println(pesanan.getNomor() + " - " + pesanan.getPelanggan().getNama()
                    + ": " + pesanan.jumlahPorsi() + " porsi, " + total);
        }
        System.out.println("Total pendapatan " + kedai.getNama() + ": "
                + formatRupiah(kedai.totalPendapatan()));

        System.out.println();
        System.out.println("=== SALINAN TIDAK MERUSAK CATATAN ===");
        List<PesananRingkas> salinan = kedai.getDaftarPesanan();
        salinan.clear();
        System.out.println("Salinan dikosongkan, pesanan tercatat tetap " + kedai.jumlahPesanan());
    }

    /** Mengubah 18000 menjadi "Rp18.000" (padanan Rupiah.format di studi kasus). */
    static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

/** Versi ringkas kelas Menu dari studi kasus. */
class MenuRingkas {
    private String kode;
    private String nama;
    private int harga;
    private String kategori;
    private int stok;

    public MenuRingkas(String kode, String nama, int harga, String kategori, int stok) {
        this.kode = kode;
        this.nama = nama;
        this.harga = harga;
        this.kategori = kategori;
        this.stok = stok;
    }

    public String getKode() {
        return kode;
    }

    public int getHarga() {
        return harga;
    }

    public String getKategori() {
        return kategori;
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
}

/** Versi ringkas kelas Pelanggan dari studi kasus. */
class PelangganRingkas {
    private String nama;
    private String noHp;

    public PelangganRingkas(String nama, String noHp) {
        this.nama = nama;
        this.noHp = noHp;
    }

    public String getNama() {
        return nama;
    }

    public String getNoHp() {
        return noHp;
    }
}

/** Satu baris pesanan: menu apa dan berapa porsi. */
class ItemPesananRingkas {
    private MenuRingkas menu;
    private int jumlah;

    public ItemPesananRingkas(MenuRingkas menu, int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        this.menu = menu;
        this.jumlah = jumlah;
    }

    public int getJumlah() {
        return jumlah;
    }

    public int hitungSubtotal() {
        return menu.getHarga() * jumlah;
    }
}

/** Pesanan milik seorang pelanggan, berisi beberapa item. */
class PesananRingkas {
    private static int nomorTerakhir = 0;

    private String nomor;
    private PelangganRingkas pelanggan;
    private List<ItemPesananRingkas> daftarItem;

    public PesananRingkas(PelangganRingkas pelanggan) {
        nomorTerakhir++;
        this.nomor = String.format("P%03d", nomorTerakhir);
        this.pelanggan = pelanggan;
        this.daftarItem = new ArrayList<>();
    }

    public String getNomor() {
        return nomor;
    }

    public PelangganRingkas getPelanggan() {
        return pelanggan;
    }

    public void tambahItem(MenuRingkas menu, int jumlah) {
        ItemPesananRingkas item = new ItemPesananRingkas(menu, jumlah);
        menu.kurangiStok(jumlah);
        daftarItem.add(item);
    }

    public int hitungTotal() {
        int total = 0;
        for (ItemPesananRingkas item : daftarItem) {
            total += item.hitungSubtotal();
        }
        return total;
    }

    public int jumlahPorsi() { // BARU
        int porsi = 0;
        for (ItemPesananRingkas item : daftarItem) {
            porsi += item.getJumlah();
        }
        return porsi;
    }
}

/** Kedai yang punya daftar menu dan catatan pesanan. */
class KedaiRingkas {
    private String nama;
    private List<MenuRingkas> daftarMenu;
    private List<PesananRingkas> daftarPesanan;

    public KedaiRingkas(String nama) {
        this.nama = nama;
        this.daftarMenu = new ArrayList<>();
        this.daftarPesanan = new ArrayList<>();
    }

    public String getNama() {
        return nama;
    }

    /** BARU: mengembalikan SALINAN list, agar catatan asli tidak diubah dari luar. */
    public List<PesananRingkas> getDaftarPesanan() {
        return new ArrayList<>(daftarPesanan);
    }

    public void tambahMenu(MenuRingkas menu) {
        daftarMenu.add(menu);
    }

    public MenuRingkas cariMenu(String kode) {
        for (MenuRingkas menu : daftarMenu) {
            if (menu.getKode().equals(kode)) {
                return menu;
            }
        }
        return null;
    }

    public PesananRingkas buatPesanan(PelangganRingkas pelanggan) {
        PesananRingkas pesanan = new PesananRingkas(pelanggan);
        daftarPesanan.add(pesanan);
        return pesanan;
    }

    public int jumlahPesanan() {
        return daftarPesanan.size();
    }

    public int totalPendapatan() { // BARU
        int total = 0;
        for (PesananRingkas pesanan : daftarPesanan) {
            total += pesanan.hitungTotal(); // Kedai -> Pesanan -> ItemPesanan
        }
        return total;
    }
}
