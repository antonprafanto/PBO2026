/*
 * Solusi Latihan 02 - Diskon Ulang Tahun (OCP + LSP)
 * Pertemuan 13 - Prinsip SOLID
 *
 * Ide penyelesaian:
 * - Aturan diskon baru = kelas BARU yang meng-implements interface diskon.
 *   Kelas pesanan, kelas diskon lain, dan pencetak struk TIDAK diubah (OCP).
 * - DiskonUlangTahun: gratis 1 porsi menu TERMURAH di dalam pesanan.
 * - Menepati janji Diskon (LSP): potongan tidak pernah negatif, tidak pernah
 *   melebihi subtotal, dan pesanan kosong tidak membuat program error.
 *
 * Agar file ini bisa dijalankan sendiri, kelas-kelas studi kasus yang
 * dibutuhkan disalin dalam versi RINGKAS. Satu-satunya kelas yang BARU adalah
 * DiskonUlangTahun.
 *
 * Catatan nama kelas: folder java/ pertemuan ini sudah punya Menu, ItemPesanan,
 * Pelanggan, Diskon, TanpaDiskon, dan Pesanan (di studi-kasus).
 * Nama kelas di dalam satu folder harus unik, jadi salinan ringkasnya diberi
 * akhiran "Mini" (MenuMini, DiskonMini, PesananMini, ...). Di proyekmu sendiri,
 * cukup buat file DiskonUlangTahun.java berisi "implements Diskon".
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02DiskonUlangTahun.java
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Latihan02DiskonUlangTahun {

    static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    static void cetakStruk(PesananMini pesanan) {
        System.out.println("Pesanan " + pesanan.getPelanggan().getNama());
        for (ItemPesananMini item : pesanan.getDaftarItem()) {
            String kiri = item.getJumlah() + " x " + item.getMenu().getNama();
            System.out.println(String.format("%-30s%10s", kiri, formatRupiah(item.hitungSubtotal())));
        }
        System.out.println(String.format("%-30s%10s", "Subtotal", formatRupiah(pesanan.hitungSubtotal())));
        int potongan = pesanan.hitungPotongan();
        if (potongan > 0) {
            String kiri = "Diskon " + pesanan.getDiskon().keterangan();
            System.out.println(String.format("%-30s%10s", kiri, "-" + formatRupiah(potongan)));
        }
        System.out.println(String.format("%-30s%10s", "TOTAL", formatRupiah(pesanan.hitungTotal())));
    }

    public static void main(String[] args) {
        MenuMini esTeh = new MenuMini("Es Teh Manis", 8000);
        MenuMini nasiGoreng = new MenuMini("Nasi Goreng Kampung", 25000);
        MenuMini pisang = new MenuMini("Pisang Goreng Keju", 15000);

        System.out.println("=== SITI BERULANG TAHUN ===");
        PesananMini pesananSiti = new PesananMini(new PelangganMini("Siti Aminah"));
        pesananSiti.tambahItem(esTeh, 2);
        pesananSiti.tambahItem(pisang, 1);
        pesananSiti.aturDiskon(new DiskonUlangTahun()); // cukup objek diskon baru
        cetakStruk(pesananSiti);

        System.out.println();
        System.out.println("=== BUDI BERULANG TAHUN, PESAN SATU MENU ===");
        PesananMini pesananBudi = new PesananMini(new PelangganMini("Budi Santoso"));
        pesananBudi.tambahItem(nasiGoreng, 1);
        pesananBudi.aturDiskon(new DiskonUlangTahun());
        cetakStruk(pesananBudi);


        System.out.println();
        System.out.println("=== PESANAN KOSONG (UJI LSP) ===");
        PesananMini kosong = new PesananMini(new PelangganMini("Andi Wijaya"));
        kosong.aturDiskon(new DiskonUlangTahun());
        System.out.println("Potongan: " + formatRupiah(kosong.hitungPotongan())
                + ", total: " + formatRupiah(kosong.hitungTotal()));
    }
}

// ------------------------------- salinan RINGKAS dari studi kasus (tidak diubah)
class MenuMini {
    private String nama;
    private int harga;

    public MenuMini(String nama, int harga) {
        this.nama = nama;
        this.harga = harga;
    }

    public String getNama() {
        return nama;
    }

    public int getHarga() {
        return harga;
    }
}

class ItemPesananMini {
    private MenuMini menu;
    private int jumlah;

    public ItemPesananMini(MenuMini menu, int jumlah) {
        this.menu = menu;
        this.jumlah = jumlah;
    }

    public MenuMini getMenu() {
        return menu;
    }

    public int getJumlah() {
        return jumlah;
    }

    public int hitungSubtotal() {
        return menu.getHarga() * jumlah;
    }
}

class PelangganMini {
    private String nama;

    public PelangganMini(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }
}

interface DiskonMini {
    /** Besar potongan dalam rupiah (tidak pernah negatif). */
    int hitungPotongan(List<ItemPesananMini> daftarItem, PelangganMini pelanggan);

    /** Nama singkat diskon untuk ditampilkan di struk. */
    String keterangan();

    static int subtotalDari(List<ItemPesananMini> daftarItem) {
        int total = 0;
        for (ItemPesananMini item : daftarItem) {
            total += item.hitungSubtotal();
        }
        return total;
    }
}

class TanpaDiskonMini implements DiskonMini {
    @Override
    public int hitungPotongan(List<ItemPesananMini> daftarItem, PelangganMini pelanggan) {
        return 0;
    }

    @Override
    public String keterangan() {
        return "Tanpa diskon";
    }
}

class PesananMini {
    private PelangganMini pelanggan;
    private List<ItemPesananMini> daftarItem = new ArrayList<>();
    private DiskonMini diskon = new TanpaDiskonMini();

    public PesananMini(PelangganMini pelanggan) {
        this.pelanggan = pelanggan;
    }

    public PelangganMini getPelanggan() {
        return pelanggan;
    }

    public List<ItemPesananMini> getDaftarItem() {
        return new ArrayList<>(daftarItem);
    }

    public DiskonMini getDiskon() {
        return diskon;
    }

    public void tambahItem(MenuMini menu, int jumlah) {
        daftarItem.add(new ItemPesananMini(menu, jumlah));
    }

    public void aturDiskon(DiskonMini diskon) {
        this.diskon = diskon;
    }

    public int hitungSubtotal() {
        return DiskonMini.subtotalDari(daftarItem);
    }

    public int hitungPotongan() {
        return diskon.hitungPotongan(new ArrayList<>(daftarItem), pelanggan);
    }

    public int hitungTotal() {
        return hitungSubtotal() - hitungPotongan();
    }
}

// ------------------------------------------------------------------- KELAS BARU
/** Hadiah ulang tahun: gratis 1 porsi menu termurah di dalam pesanan. */
class DiskonUlangTahun implements DiskonMini {

    @Override
    public int hitungPotongan(List<ItemPesananMini> daftarItem, PelangganMini pelanggan) {
        if (daftarItem.isEmpty()) { // pesanan kosong: potongan 0, bukan error (LSP)
            return 0;
        }
        int termurah = daftarItem.get(0).getMenu().getHarga();
        for (ItemPesananMini item : daftarItem) {
            if (item.getMenu().getHarga() < termurah) {
                termurah = item.getMenu().getHarga();
            }
        }
        return termurah; // selalu >= 0 dan tidak melebihi subtotal
    }

    @Override
    public String keterangan() {
        return "Ulang Tahun";
    }
}
