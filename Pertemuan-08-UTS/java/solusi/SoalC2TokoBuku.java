/*
 * Solusi Soal C2 - Toko Buku Daring
 * Pertemuan 08 - UTS (latihan persiapan, BUKAN soal ujian asli)
 *
 * Ide penyelesaian:
 * - Produk adalah kelas induk untuk semua barang yang dijual. Buku dan
 *   AlatTulis mewarisinya (extends), menambah field sendiri, dan
 *   meng-override toString().
 * - Harga dijaga oleh setter (harus > 0). Stok hanya berubah lewat method
 *   kurangiStok() yang menolak permintaan melebihi stok.
 * - Pesanan MEMBUAT objek ItemPesanan di dalam tambahItem() (komposisi).
 *   TokoBuku menyimpan produk yang dibuat di luar (agregasi). Pesanan
 *   mengenal Pelanggan pemesannya (asosiasi).
 * - Ongkir dihitung dari total berat (dibulatkan ke atas per kg) dan gratis
 *   bila subtotal mencapai batas tertentu.
 *
 * Catatan nama kelas: pemformat uang di file ini bernama RupiahToko, BUKAN
 * Rupiah, karena folder java/ ini juga berisi solusi Soal C1 (RupiahLab).
 * Nama kelas di dalam satu folder proyek harus unik.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java SoalC2TokoBuku.java
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class SoalC2TokoBuku {

    public static void main(String[] args) {
        TokoBuku toko = siapkanToko();
        toko.tampilkanKatalog();
        System.out.println();

        System.out.println("=== DATA TIDAK VALID DITOLAK ===");
        try {
            toko.tambahProduk(new Buku("B09", "Buku Tanpa Harga", 0, 5, 300, "Anonim"));
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal menambah produk: " + e.getMessage());
        }
        Produk bumiManusia = toko.cariProduk("B02");
        try {
            bumiManusia.setHarga(-5000);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal mengubah harga: " + e.getMessage());
        }
        System.out.println("Harga " + bumiManusia.getNama() + " tetap "
                + RupiahToko.format(bumiManusia.getHarga()));
        if (toko.cariProduk("B99") == null) {
            System.out.println("Cari B99: produk tidak ditemukan");
        }
        System.out.println();

        System.out.println("=== PESANAN ===");
        Pelanggan siti = new Pelanggan("Siti Aminah", "siti@contoh.id");
        Pelanggan budi = new Pelanggan("Budi Santoso", "budi@contoh.id");

        Pesanan pesananSiti = toko.buatPesanan(siti);
        pesananSiti.tambahItem(toko.cariProduk("B01"), 2);
        pesananSiti.tambahItem(toko.cariProduk("T01"), 2);
        pesananSiti.cetakInvoice();

        Pesanan pesananBudi = toko.buatPesanan(budi);
        try {
            pesananBudi.tambahItem(toko.cariProduk("B03"), 3); // stok hanya 2
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal menambah item: " + e.getMessage());
        }
        try {
            pesananBudi.tambahItem(toko.cariProduk("T02"), 0);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal menambah item: " + e.getMessage());
        }
        pesananBudi.tambahItem(toko.cariProduk("B03"), 2);
        pesananBudi.tambahItem(toko.cariProduk("T02"), 3);
        pesananBudi.cetakInvoice();
        System.out.println();

        System.out.println("=== RINGKASAN ===");
        toko.tampilkanKatalog();
        System.out.println("Jumlah pesanan : " + toko.jumlahPesanan());
        System.out.println("Total penjualan: " + RupiahToko.format(toko.totalPenjualan()));
    }

    /** Membuat toko beserta lima produk awalnya. */
    static TokoBuku siapkanToko() {
        TokoBuku toko = new TokoBuku("PustakaKita");
        toko.tambahProduk(new Buku("B01", "Laskar Pelangi", 95000, 5, 350,
                "Andrea Hirata"));
        toko.tambahProduk(new Buku("B02", "Bumi Manusia", 120000, 3, 600,
                "Pramoedya Ananta Toer"));
        toko.tambahProduk(new Buku("B03", "Negeri 5 Menara", 89000, 2, 450,
                "Ahmad Fuadi"));
        toko.tambahProduk(new AlatTulis("T01", "Pulpen Gel", 8000, 50, 10, "hitam"));
        toko.tambahProduk(new AlatTulis("T02", "Map Plastik", 5000, 40, 60, "biru"));
        return toko;
    }
}

/** Kelas utilitas: mengubah 206000 menjadi "Rp206.000". */
class RupiahToko {
    public static String format(int angka) {
        // Locale.US agar pemisah ribuan selalu koma, lalu diganti titik.
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

/** Pembeli di toko daring. Datanya read-only dari luar. */
class Pelanggan {
    private String nama;
    private String email;

    public Pelanggan(String nama, String email) {
        this.nama = nama;
        this.email = email;
    }

    public String getNama() {
        return nama;
    }

    public String getEmail() {
        return email;
    }

    @Override
    public String toString() {
        return nama + " (" + email + ")";
    }
}

/** Kelas induk: data dan perilaku yang dimiliki SEMUA produk toko. */
class Produk {
    private String kode;
    private String nama;
    private int harga;
    private int stok;
    private int beratGram;

    public Produk(String kode, String nama, int harga, int stok, int beratGram) {
        if (stok < 0) {
            throw new IllegalArgumentException("Stok tidak boleh negatif");
        }
        if (beratGram <= 0) {
            throw new IllegalArgumentException("Berat harus lebih dari 0 gram");
        }
        this.kode = kode;
        this.nama = nama;
        this.stok = stok;
        this.beratGram = beratGram;
        setHarga(harga); // [1] lewat setter, jadi ikut divalidasi
    }

    public String getKode() {
        return kode;
    }

    public String getNama() {
        return nama;
    }

    public int getStok() {
        return stok;
    }

    public int getBeratGram() {
        return beratGram;
    }

    public int getHarga() {
        return harga;
    }

    public void setHarga(int nilai) {
        if (nilai <= 0) {
            // [2] ditolak SEBELUM field diubah, jadi harga lama tetap aman
            throw new IllegalArgumentException("Harga harus lebih dari 0");
        }
        this.harga = nilai;
    }

    public boolean stokCukup(int jumlah) {
        return stok >= jumlah;
    }

    /** Satu-satunya pintu untuk mengurangi stok. */
    public void kurangiStok(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        if (!stokCukup(jumlah)) {
            throw new IllegalArgumentException(
                    "Stok " + nama + " tidak cukup (sisa " + stok + ")");
        }
        stok -= jumlah;
    }

    @Override
    public String toString() {
        return "[" + kode + "] " + nama + " - " + RupiahToko.format(harga) + " | stok " + stok;
    }
}

/** Produk berupa buku. Tambahan: penulis. */
class Buku extends Produk {
    private String penulis;

    public Buku(String kode, String judul, int harga, int stok, int beratGram,
            String penulis) {
        super(kode, judul, harga, stok, beratGram); // [3]
        this.penulis = penulis;
    }

    public String getPenulis() {
        return penulis;
    }

    @Override
    public String toString() {
        // [4] override: pakai teks dari induk, lalu tambahkan nama penulis
        return super.toString() + " | penulis " + penulis;
    }
}

/** Produk berupa alat tulis. Tambahan: warna. */
class AlatTulis extends Produk {
    private String warna;

    public AlatTulis(String kode, String nama, int harga, int stok, int beratGram,
            String warna) {
        super(kode, nama, harga, stok, beratGram);
        this.warna = warna;
    }

    public String getWarna() {
        return warna;
    }

    @Override
    public String toString() {
        return super.toString() + " | warna " + warna;
    }
}

/** Satu baris pesanan: produk apa dan berapa banyak. */
class ItemPesanan {
    private Produk produk;
    private int jumlah;

    public ItemPesanan(Produk produk, int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        this.produk = produk; // menyimpan REFERENSI ke objek Produk
        this.jumlah = jumlah;
    }

    public Produk getProduk() {
        return produk;
    }

    public int getJumlah() {
        return jumlah;
    }

    public int hitungSubtotal() {
        return produk.getHarga() * jumlah;
    }

    public int hitungBerat() {
        return produk.getBeratGram() * jumlah;
    }

    @Override
    public String toString() {
        return jumlah + " x " + produk.getNama();
    }
}

/** Satu pesanan milik seorang pelanggan, berisi beberapa ItemPesanan. */
class Pesanan {
    private static final int ONGKIR_PER_KG = 10000; // Rupiah per kilogram
    private static final int BATAS_GRATIS_ONGKIR = 200000; // subtotal minimal ongkir gratis
    private static final int LEBAR_INVOICE = 40;
    private static int nomorTerakhir = 0; // milik kelas: untuk nomor otomatis

    private String nomor;
    private Pelanggan pelanggan;
    private List<ItemPesanan> daftarItem;

    public Pesanan(Pelanggan pelanggan) {
        nomorTerakhir++;
        this.nomor = String.format("INV%03d", nomorTerakhir); // INV001, INV002, ...
        this.pelanggan = pelanggan; // asosiasi
        this.daftarItem = new ArrayList<>(); // komposisi
    }

    public String getNomor() {
        return nomor;
    }

    public Pelanggan getPelanggan() {
        return pelanggan;
    }

    /** Mengembalikan SALINAN list, agar isi asli tidak diubah dari luar. */
    public List<ItemPesanan> getDaftarItem() {
        return new ArrayList<>(daftarItem);
    }

    public void tambahItem(Produk produk, int jumlah) {
        ItemPesanan item = new ItemPesanan(produk, jumlah); // [5] item dibuat OLEH pesanan
        produk.kurangiStok(jumlah); // [6] gagal (exception) jika stok kurang
        daftarItem.add(item); // [7] hanya disimpan jika semua lolos
    }

    public int hitungSubtotal() {
        int subtotal = 0;
        for (ItemPesanan item : daftarItem) {
            subtotal += item.hitungSubtotal();
        }
        return subtotal;
    }

    /** Total berat dalam kg, DIBULATKAN KE ATAS (1080 gram -> 2 kg). */
    public int hitungBeratKg() {
        int beratGram = 0;
        for (ItemPesanan item : daftarItem) {
            beratGram += item.hitungBerat();
        }
        return (beratGram + 999) / 1000; // [8] pembulatan ke atas tanpa double
    }

    public int hitungOngkir() {
        if (hitungSubtotal() >= BATAS_GRATIS_ONGKIR) {
            return 0;
        }
        return hitungBeratKg() * ONGKIR_PER_KG;
    }

    public int hitungTotal() {
        return hitungSubtotal() + hitungOngkir();
    }

    public void cetakInvoice() {
        String garis = "=".repeat(LEBAR_INVOICE);
        System.out.println(garis);
        System.out.println("INVOICE " + nomor);
        System.out.println(garis);
        System.out.println("Pelanggan : " + pelanggan);
        System.out.println("-".repeat(LEBAR_INVOICE));
        for (ItemPesanan item : daftarItem) {
            String subtotal = RupiahToko.format(item.hitungSubtotal());
            System.out.println(String.format("%-30s%10s", item.toString(), subtotal));
        }
        System.out.println("-".repeat(LEBAR_INVOICE));
        System.out.println(String.format("%-30s%10s", "Subtotal",
                RupiahToko.format(hitungSubtotal())));
        int ongkir = hitungOngkir();
        String teksOngkir = (ongkir == 0) ? "GRATIS" : RupiahToko.format(ongkir);
        String labelOngkir = "Ongkir (" + hitungBeratKg() + " kg)";
        System.out.println(String.format("%-30s%10s", labelOngkir, teksOngkir));
        System.out.println(String.format("%-30s%10s", "TOTAL",
                RupiahToko.format(hitungTotal())));
        System.out.println(garis);
    }
}

/** Toko daring yang punya katalog produk dan catatan pesanan. */
class TokoBuku {
    private String nama;
    private List<Produk> daftarProduk; // agregasi
    private List<Pesanan> daftarPesanan; // asosiasi (catatan)

    public TokoBuku(String nama) {
        this.nama = nama;
        this.daftarProduk = new ArrayList<>();
        this.daftarPesanan = new ArrayList<>();
    }

    public String getNama() {
        return nama;
    }

    public void tambahProduk(Produk produk) {
        daftarProduk.add(produk);
    }

    /** Mengembalikan objek Produk dengan kode tertentu, atau null. */
    public Produk cariProduk(String kode) {
        for (Produk produk : daftarProduk) {
            if (produk.getKode().equals(kode)) {
                return produk;
            }
        }
        return null;
    }

    public Pesanan buatPesanan(Pelanggan pelanggan) {
        Pesanan pesanan = new Pesanan(pelanggan);
        daftarPesanan.add(pesanan);
        return pesanan;
    }

    public int jumlahPesanan() {
        return daftarPesanan.size();
    }

    public int totalPenjualan() {
        int total = 0;
        for (Pesanan pesanan : daftarPesanan) {
            total += pesanan.hitungTotal();
        }
        return total;
    }

    public void tampilkanKatalog() {
        System.out.println("=== KATALOG " + nama + " ===");
        for (Produk produk : daftarProduk) {
            System.out.println(produk); // memanggil toString() milik kelas anak
        }
    }
}
