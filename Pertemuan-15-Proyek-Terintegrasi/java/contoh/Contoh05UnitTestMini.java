/*
 * Contoh 05 - Unit Test Mini dengan "Test Runner" Buatan Sendiri
 * Pertemuan 15 - Proyek Terintegrasi
 *
 * Unit test adalah kode kecil yang memeriksa kode lain secara OTOMATIS.
 * Di industri, programmer Java memakai JUnit. JUnit tidak ikut di dalam JDK
 * (harus diunduh terpisah), jadi di sini kita membuat runner mini sendiri:
 * - setiap pengujian adalah satu method uji...()
 * - samakan(hasil, harapan)     : seperti assertEquals / assertEqual
 * - harusMelempar(jenis, kode)  : seperti assertThrows / assertRaises
 * - uji(nama, kasus)            : menjalankan satu pengujian, mencetak hasilnya
 * Pengganti setUp(): setiap uji meminta keranjang BARU dari pembuatKeranjang.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05UnitTestMini.java
 */
import java.util.ArrayList;
import java.util.List;
import java.util.function.Supplier;

public class Contoh05UnitTestMini {
    private static Supplier<KeranjangBelanja> pembuatKeranjang; // [1] "resep" objek baru
    private static int jumlahLulus;
    private static int jumlahGagal;

    public static void main(String[] args) {
        System.out.println("=== UJI 1: KeranjangBelanja ===");
        jalankanSemuaUji(KeranjangBelanja::new); // [2] uji pada versi yang benar

        System.out.println();
        System.out.println("=== UJI 2: KeranjangBerbug (sengaja diberi bug) ===");
        jalankanSemuaUji(KeranjangBerbug::new); // uji yang SAMA pada versi berbug
    }

    /** Menjalankan semua uji pada keranjang buatan pembuat. */
    static void jalankanSemuaUji(Supplier<KeranjangBelanja> pembuat) {
        pembuatKeranjang = pembuat;
        jumlahLulus = 0;
        jumlahGagal = 0;
        uji("Jumlah barang 0 ditolak", Contoh05UnitTestMini::ujiJumlahNolDitolak);
        uji("Belanja Rp99.000 kena ongkir Rp10.000", Contoh05UnitTestMini::ujiOngkirDiBawahBatas);
        uji("Belanja tepat Rp100.000 gratis ongkir",
                Contoh05UnitTestMini::ujiOngkirGratisTepatDiBatas);
        uji("Subtotal dua barang dijumlahkan", Contoh05UnitTestMini::ujiSubtotalDuaBarang);
        uji("Total = subtotal + ongkir", Contoh05UnitTestMini::ujiTotalTermasukOngkir);
        System.out.println("Hasil: " + jumlahLulus + " lulus, " + jumlahGagal + " gagal");
    }

    // ============================== kasus uji ==============================

    static void ujiJumlahNolDitolak() {
        KeranjangBelanja keranjang = pembuatKeranjang.get(); // [3] objek baru setiap uji
        harusMelempar(IllegalArgumentException.class, () -> keranjang.tambah("Buku tulis", 5000, 0));
    }

    static void ujiOngkirDiBawahBatas() {
        KeranjangBelanja keranjang = pembuatKeranjang.get();
        keranjang.tambah("Kaos", 99000, 1);
        samakan(keranjang.ongkir(), 10000); // [4] hasil, harapan
    }

    static void ujiOngkirGratisTepatDiBatas() {
        KeranjangBelanja keranjang = pembuatKeranjang.get();
        keranjang.tambah("Sepatu", 100000, 1);
        samakan(keranjang.ongkir(), 0);
    }

    static void ujiSubtotalDuaBarang() {
        KeranjangBelanja keranjang = pembuatKeranjang.get();
        keranjang.tambah("Pulpen", 3000, 4);
        keranjang.tambah("Map", 8000, 2);
        samakan(keranjang.subtotal(), 28000);
    }

    static void ujiTotalTermasukOngkir() {
        KeranjangBelanja keranjang = pembuatKeranjang.get();
        keranjang.tambah("Topi", 60000, 1);
        samakan(keranjang.total(), 70000);
    }

    // ===================== alat bantu uji (runner mini) =====================

    /** Isi satu pengujian. Gagal = melempar AssertionError. */
    interface KasusUji {
        void jalankan();
    }

    static void uji(String nama, KasusUji kasus) {
        try {
            kasus.jalankan();
            jumlahLulus++;
            System.out.println("[LULUS] " + nama);
        } catch (AssertionError e) { // [5] pemeriksaan tidak terpenuhi
            jumlahGagal++;
            System.out.println("[GAGAL] " + nama);
            System.out.println("        -> " + e.getMessage());
        } catch (RuntimeException e) { // exception yang tidak diduga
            jumlahGagal++;
            System.out.println("[ERROR] " + nama);
            System.out.println("        -> " + e);
        }
    }

    /** Seperti assertEqual: gagal jika hasil tidak sama dengan harapan. */
    static void samakan(int hasil, int harapan) {
        if (hasil != harapan) {
            throw new AssertionError(hasil + " != " + harapan); // [6]
        }
    }

    /** Seperti assertRaises: gagal jika kode TIDAK melempar exception jenis itu. */
    static void harusMelempar(Class<? extends RuntimeException> jenis, Runnable kode) {
        try {
            kode.run();
        } catch (RuntimeException e) {
            if (jenis.isInstance(e)) { // isInstance = "instanceof" untuk objek Class
                return; // exception yang diharapkan memang dilempar: lulus
            }
            throw e; // exception lain: biarkan dicatat sebagai ERROR
        }
        throw new AssertionError(jenis.getSimpleName() + " not raised");
    }
}

/** Keranjang belanja daring. Gratis ongkir jika belanja minimal Rp100.000. */
class KeranjangBelanja {
    static final int BATAS_GRATIS_ONGKIR = 100000;
    static final int ONGKIR = 10000;

    private List<Integer> daftarSubtotal = new ArrayList<>(); // harga x jumlah per barang

    void tambah(String nama, int harga, int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        daftarSubtotal.add(harga * jumlah);
    }

    int subtotal() {
        int total = 0;
        for (int nilai : daftarSubtotal) {
            total += nilai;
        }
        return total;
    }

    int ongkir() {
        if (subtotal() >= BATAS_GRATIS_ONGKIR) {
            return 0;
        }
        return ONGKIR;
    }

    int total() {
        return subtotal() + ongkir();
    }
}

/** Versi yang SENGAJA diberi bug: memakai > padahal seharusnya >=. */
class KeranjangBerbug extends KeranjangBelanja {
    @Override
    int ongkir() {
        if (subtotal() > BATAS_GRATIS_ONGKIR) { // BUG: tepat 100000 tidak gratis
            return 0;
        }
        return ONGKIR;
    }
}
