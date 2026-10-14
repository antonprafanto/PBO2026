/*
 * Solusi Latihan 04 - Observer Stok Gudang Menipis
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Ide penyelesaian:
 * - Gudang adalah SUBJECT: menyimpan stok (LinkedHashMap) dan daftar pengamat.
 * - Setiap kali barang diambil dan sisanya di bawah BATAS_MINIMUM, gudang
 *   memanggil stokMenipis(namaBarang, sisa) milik SEMUA pengamat.
 *   Datanya langsung dikirim sebagai argumen (gaya PUSH).
 * - Dua pengamat yang berbeda jenis: Pemasok dan AdminGudang. Gudang tidak
 *   peduli jenisnya, cukup tahu bahwa keduanya PengamatGudang.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04ObserverGudang.java
 */
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Latihan04ObserverGudang {

    public static void main(String[] args) {
        Gudang gudang = new Gudang("Gudang Sembako");
        gudang.isiStok("Beras", 50);
        gudang.isiStok("Gula", 20);
        gudang.isiStok("Minyak", 15);
        AdminGudang admin = new AdminGudang();
        gudang.tambahPengamat(new Pemasok("Pak Rahman"));
        gudang.tambahPengamat(admin);

        System.out.println("=== TRANSAKSI GUDANG (BATAS MINIMUM " + Gudang.BATAS_MINIMUM
                + ") ===");
        gudang.ambil("Beras", 30);
        gudang.ambil("Gula", 12);
        gudang.ambil("Minyak", 3);
        gudang.ambil("Gula", 5);

        System.out.println();
        System.out.println("=== RINGKASAN ===");
        System.out.println("Peringatan yang dicatat admin: " + admin.jumlahPeringatan());
    }
}

/** Observer: ingin diberi tahu saat stok sebuah barang menipis. */
interface PengamatGudang {
    void stokMenipis(String namaBarang, int sisa);
}

class Pemasok implements PengamatGudang {
    private String nama;

    Pemasok(String nama) {
        this.nama = nama;
    }

    @Override
    public void stokMenipis(String namaBarang, int sisa) {
        System.out.println("  [Pemasok " + nama + "] Siap mengirim " + namaBarang
                + " tambahan");
    }
}

class AdminGudang implements PengamatGudang {
    private int jumlahPeringatan = 0;

    @Override
    public void stokMenipis(String namaBarang, int sisa) {
        jumlahPeringatan++;
        System.out.println("  [Admin] Catat: stok " + namaBarang + " tinggal " + sisa);
    }

    public int jumlahPeringatan() {
        return jumlahPeringatan;
    }
}

/** Subject: memberi kabar ke semua pengamat saat stok menipis. */
class Gudang {
    public static final int BATAS_MINIMUM = 10;

    private String nama;
    private Map<String, Integer> stok = new LinkedHashMap<>();
    private List<PengamatGudang> daftarPengamat = new ArrayList<>();

    Gudang(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public void tambahPengamat(PengamatGudang pengamat) {
        daftarPengamat.add(pengamat);
    }

    public void isiStok(String namaBarang, int jumlah) {
        stok.put(namaBarang, stok.getOrDefault(namaBarang, 0) + jumlah);
    }

    public void ambil(String namaBarang, int jumlah) {
        if (jumlah > stok.get(namaBarang)) {
            throw new IllegalArgumentException("Stok " + namaBarang + " tidak cukup");
        }
        int sisa = stok.get(namaBarang) - jumlah;
        stok.put(namaBarang, sisa);
        System.out.println("Ambil " + jumlah + " " + namaBarang + ", sisa " + sisa);
        if (sisa < BATAS_MINIMUM) {
            beriKabar(namaBarang, sisa);
        }
    }

    private void beriKabar(String namaBarang, int sisa) {
        for (PengamatGudang pengamat : daftarPengamat) {
            pengamat.stokMenipis(namaBarang, sisa);
        }
    }
}
