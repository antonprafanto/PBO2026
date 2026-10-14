/*
 * Solusi Latihan 05 - KedaiKita: Strategi Baru DiskonPelajar
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Ide penyelesaian:
 * - DiskonPelajar adalah STRATEGY baru: potongan 10% dari subtotal, tetapi
 *   paling banyak Rp5.000. Kuncinya: Math.min(potongan, MAKSIMAL).
 * - Kelas Keranjang (context) TIDAK diubah sama sekali saat strategi baru
 *   ditambahkan. Inilah OCP (Pertemuan 13) yang diwujudkan oleh pola Strategy.
 * - Pajak 10% dihitung dari subtotal SETELAH dipotong diskon, sama seperti
 *   Pesanan.hitungPajak() di studi kasus.
 *
 * Catatan nama kelas: supaya file ini bisa dijalankan sendiri, kita memakai
 * versi MINI dari kelas studi kasus dengan nama berbeda: MenuKedai (Menu),
 * ItemKeranjang (ItemPesanan), AturanDiskon (Diskon), Keranjang (Pesanan).
 * Folder java/ pertemuan ini sudah punya kelas Menu, Diskon, dan seterusnya
 * (di studi-kasus), dan editor seperti VS Code akan protes "The type ... is
 * already defined" jika ada dua kelas bernama sama. Di salinan studi kasusmu
 * sendiri, cukup buat file DiskonPelajar.java yang meng-implements Diskon.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05DiskonPelajar.java
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Latihan05DiskonPelajar {

    static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    static void bandingkan(String judul, Keranjang keranjang) {
        System.out.println("=== " + judul + " ===");
        System.out.println("Subtotal: " + formatRupiah(keranjang.hitungSubtotal()));
        List<AturanDiskon> daftarStrategi = List.of(new TanpaPotongan(),
                new PotonganHappyHour(), new DiskonPelajar());
        for (AturanDiskon strategi : daftarStrategi) {
            keranjang.aturDiskon(strategi);
            String potongan = formatRupiah(keranjang.hitungPotongan());
            String total = formatRupiah(keranjang.hitungTotal());
            System.out.println(String.format("%-22s potongan %8s, total %8s",
                    strategi.keterangan(), potongan, total));
        }
    }

    public static void main(String[] args) {
        MenuKedai kopi = new MenuKedai("Kopi Susu Gula Aren", 18000, "Minuman");
        MenuKedai esTeh = new MenuKedai("Es Teh Manis", 8000, "Minuman");
        MenuKedai mie = new MenuKedai("Mie Goreng Jawa", 23000, "Makanan");
        MenuKedai pisang = new MenuKedai("Pisang Goreng Keju", 15000, "Makanan");

        Keranjang pesananKecil = new Keranjang();
        pesananKecil.tambah(esTeh, 2);
        pesananKecil.tambah(pisang, 1);
        bandingkan("2 ES TEH MANIS + 1 PISANG GORENG KEJU", pesananKecil);

        System.out.println();
        Keranjang pesananBesar = new Keranjang();
        pesananBesar.tambah(kopi, 2);
        pesananBesar.tambah(mie, 1);
        bandingkan("2 KOPI SUSU GULA AREN + 1 MIE GORENG JAWA", pesananBesar);
    }
}

class MenuKedai {
    private String nama;
    private int harga;
    private String kategori;

    MenuKedai(String nama, int harga, String kategori) {
        this.nama = nama;
        this.harga = harga;
        this.kategori = kategori;
    }

    public String getNama() {
        return nama;
    }

    public int getHarga() {
        return harga;
    }

    public String getKategori() {
        return kategori;
    }
}

class ItemKeranjang {
    private MenuKedai menu;
    private int jumlah;

    ItemKeranjang(MenuKedai menu, int jumlah) {
        this.menu = menu;
        this.jumlah = jumlah;
    }

    public MenuKedai getMenu() {
        return menu;
    }

    public int hitungSubtotal() {
        return menu.getHarga() * jumlah;
    }
}

/** Strategy: kontrak semua aturan diskon (sama dengan Diskon). */
interface AturanDiskon {
    /** Besar potongan dalam rupiah (tidak pernah negatif). */
    int hitungPotongan(List<ItemKeranjang> daftarItem);

    /** Nama singkat aturan diskon. */
    String keterangan();

    static int subtotalDari(List<ItemKeranjang> daftarItem) {
        int total = 0;
        for (ItemKeranjang item : daftarItem) {
            total += item.hitungSubtotal();
        }
        return total;
    }
}

class TanpaPotongan implements AturanDiskon {
    @Override
    public int hitungPotongan(List<ItemKeranjang> daftarItem) {
        return 0;
    }

    @Override
    public String keterangan() {
        return "Tanpa diskon";
    }
}

/** 20% khusus untuk item minuman. */
class PotonganHappyHour implements AturanDiskon {
    @Override
    public int hitungPotongan(List<ItemKeranjang> daftarItem) {
        int totalMinuman = 0;
        for (ItemKeranjang item : daftarItem) {
            if (item.getMenu().getKategori().equals("Minuman")) {
                totalMinuman += item.hitungSubtotal();
            }
        }
        return totalMinuman * 20 / 100;
    }

    @Override
    public String keterangan() {
        return "Happy Hour (minuman)";
    }
}

/** Strategi BARU: potongan 10% untuk pelajar, paling banyak Rp5.000. */
class DiskonPelajar implements AturanDiskon {
    private static final int PERSEN = 10;
    private static final int MAKSIMAL = 5000;

    @Override
    public int hitungPotongan(List<ItemKeranjang> daftarItem) {
        int potongan = AturanDiskon.subtotalDari(daftarItem) * PERSEN / 100;
        return Math.min(potongan, MAKSIMAL); // dibatasi Rp5.000
    }

    @Override
    public String keterangan() {
        return "Pelajar 10%";
    }
}

/** Context (versi mini Pesanan). TIDAK diubah saat strategi baru ditambah. */
class Keranjang {
    private static final int PAJAK_PERSEN = 10;

    private List<ItemKeranjang> daftarItem = new ArrayList<>();
    private AturanDiskon diskon = new TanpaPotongan();

    public void tambah(MenuKedai menu, int jumlah) {
        daftarItem.add(new ItemKeranjang(menu, jumlah));
    }

    public void aturDiskon(AturanDiskon diskon) {
        this.diskon = diskon;
    }

    public int hitungSubtotal() {
        return AturanDiskon.subtotalDari(daftarItem);
    }

    public int hitungPotongan() {
        return diskon.hitungPotongan(new ArrayList<>(daftarItem));
    }

    public int hitungPajak() {
        int dasar = hitungSubtotal() - hitungPotongan();
        return dasar * PAJAK_PERSEN / 100;
    }

    public int hitungTotal() {
        return hitungSubtotal() - hitungPotongan() + hitungPajak();
    }
}
