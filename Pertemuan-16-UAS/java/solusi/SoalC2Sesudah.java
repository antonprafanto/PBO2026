/*
 * Solusi Soal C2 (kode SESUDAH refactor) - Kasir Laundry
 * Pertemuan 16 - UAS (latihan persiapan, BUKAN soal ujian asli)
 *
 * Refactor = mengubah STRUKTUR kode tanpa mengubah PERILAKU-nya.
 * Output program ini SAMA PERSIS dengan SoalC2Sebelum.java.
 *
 * Pembagian tugas setelah refactor:
 *     KatalogLayanan + Layanan -> menyimpan tarif (Map), menolak layanan asing
 *     PesananLaundry           -> data satu order + hitungan subtotal/potongan/total
 *     Promo + 3 kelas          -> aturan promo yang bisa ditukar (pola STRATEGY)
 *     NotaLaundry              -> menyusun teks nota (SRP)
 *     Pengirim + PengirimWhatsApp -> mengirim pesan (ISP: kontrak kecil)
 *     LaporanHarian            -> menyusun laporan harian (SRP)
 *     KasirLaundry             -> mengatur alur kerja; menerima Pengirim lewat
 *                                 konstruktor (DIP, dependency injection)
 *
 * Catatan nama kelas: kelas format uang di file ini bernama RupiahLaundry,
 * BUKAN Rupiah, karena SoalC1TiketBioskop.java di folder yang sama sudah
 * punya kelas Rupiah. Editor seperti VS Code menganggap satu folder sebagai
 * satu proyek dan akan protes "The type Rupiah is already defined".
 *
 * Di proyek sungguhan, setiap kelas sebaiknya punya file sendiri (seperti
 * KedaiKita Pertemuan 13). Di sini dibuat satu file agar mudah dijalankan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java SoalC2Sesudah.java
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public class SoalC2Sesudah {

    static KatalogLayanan siapkanKatalog() {
        KatalogLayanan katalog = new KatalogLayanan();
        katalog.tambah(new Layanan("cuci kering", 6000));
        katalog.tambah(new Layanan("cuci setrika", 8000));
        katalog.tambah(new Layanan("setrika saja", 5000));
        return katalog;
    }

    /** Lapisan tampilan: memanggil kasir dan menampilkan pesan bila ditolak. */
    static void terima(KasirLaundry kasir, Pelanggan pelanggan, String namaLayanan,
            int berat, Promo promo) {
        try {
            kasir.terimaCucian(pelanggan, namaLayanan, berat, promo);
        } catch (LayananTidakTersediaException e) {
            System.out.println("[DITOLAK] " + e.getMessage());
        }
        System.out.println();
    }

    public static void main(String[] args) {
        KasirLaundry kasir = new KasirLaundry(siapkanKatalog(), new PengirimWhatsApp()); // [6]
        terima(kasir, new Pelanggan("Budi Santoso", "081234567890"), "cuci setrika", 4,
                new PromoMember());
        terima(kasir, new Pelanggan("Siti Aminah", "082198765432"), "cuci kering", 6,
                new PromoGratisSatuKg());
        terima(kasir, new Pelanggan("Rina Marlina", "085312345678"), "setrika saja", 3,
                new PromoGratisSatuKg());
        terima(kasir, new Pelanggan("Andi Wijaya", "087711223344"), "dry clean", 2,
                new TanpaPromo());
        terima(kasir, new Pelanggan("Dimas Pratama", "081355577799"), "cuci setrika", 5,
                new TanpaPromo());
        System.out.println(new LaporanHarian(kasir.riwayat()).buatTeks());
    }
}

/** Satu-satunya tempat aturan format uang (DRY): 8000 -> "Rp8.000". */
class RupiahLaundry {
    static String format(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

/** Dilempar saat layanan yang diminta tidak ada di katalog (checked). */
class LayananTidakTersediaException extends Exception {
    private final String namaLayanan;

    public LayananTidakTersediaException(String namaLayanan) {
        super("Layanan '" + namaLayanan + "' tidak tersedia");
        this.namaLayanan = namaLayanan;
    }

    public String getNamaLayanan() {
        return namaLayanan;
    }
}

// --------------------------------------------------------------- data dasar
/** Satu jenis layanan beserta tarifnya per kg. */
class Layanan {
    private final String nama;
    private final int tarifPerKg;

    public Layanan(String nama, int tarifPerKg) {
        if (tarifPerKg <= 0) {
            throw new IllegalArgumentException("Tarif harus lebih dari 0");
        }
        this.nama = nama;
        this.tarifPerKg = tarifPerKg;
    }

    public String getNama() {
        return nama;
    }

    public int getTarifPerKg() {
        return tarifPerKg;
    }
}

/** Daftar layanan. Layanan baru cukup DIDAFTARKAN, tanpa mengubah kode (OCP). */
class KatalogLayanan {
    // [1] nama layanan -> Layanan. HashMap cukup karena katalog hanya dipakai
    //     untuk MENCARI, tidak pernah dicetak berurutan.
    private final Map<String, Layanan> daftar = new HashMap<>();

    public void tambah(Layanan layanan) {
        daftar.put(layanan.getNama(), layanan);
    }

    public Layanan cari(String nama) throws LayananTidakTersediaException {
        if (!daftar.containsKey(nama)) {
            throw new LayananTidakTersediaException(nama); // [2] bukan lagi print + return
        }
        return daftar.get(nama);
    }
}

/** Data pelanggan: nama dan nomor HP. */
class Pelanggan {
    private final String nama;
    private final String noHp;

    public Pelanggan(String nama, String noHp) {
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

// ------------------------------------------------------- promo (STRATEGY)
/** Strategi promo. Promo baru = kelas baru; kelas lain tidak diubah (OCP). */
interface Promo {
    /** Besar potongan dalam rupiah. Tidak pernah negatif (LSP). */
    int hitungPotongan(PesananLaundry pesanan); // [3]

    /** Nama promo untuk dicetak di nota. */
    String keterangan();
}

class TanpaPromo implements Promo {
    @Override
    public int hitungPotongan(PesananLaundry pesanan) {
        return 0;
    }

    @Override
    public String keterangan() {
        return "Tanpa promo";
    }
}

/** Member mendapat potongan 10% dari subtotal. */
class PromoMember implements Promo {
    static final int PERSEN = 10;

    @Override
    public int hitungPotongan(PesananLaundry pesanan) {
        return pesanan.subtotal() * PERSEN / 100;
    }

    @Override
    public String keterangan() {
        return "Member " + PERSEN + "%";
    }
}

/** Cucian minimal 5 kg: gratis 1 kg (potongan = tarif 1 kg). */
class PromoGratisSatuKg implements Promo {
    static final int MINIMAL_BERAT = 5;

    @Override
    public int hitungPotongan(PesananLaundry pesanan) {
        if (pesanan.getBerat() < MINIMAL_BERAT) {
            return 0;
        }
        return pesanan.getLayanan().getTarifPerKg();
    }

    @Override
    public String keterangan() {
        return "Gratis 1 kg";
    }
}

// ------------------------------------------------------------------ pesanan
/** Satu order cucian: hanya data dan perhitungan harga (SRP). */
class PesananLaundry {
    private final String kode;
    private final Pelanggan pelanggan;
    private final Layanan layanan;
    private final int berat;
    private final Promo promo;

    public PesananLaundry(String kode, Pelanggan pelanggan, Layanan layanan, int berat,
            Promo promo) {
        if (berat <= 0) {
            throw new IllegalArgumentException("Berat harus lebih dari 0");
        }
        this.kode = kode;
        this.pelanggan = pelanggan;
        this.layanan = layanan;
        this.berat = berat;
        this.promo = promo;
    }

    public String getKode() {
        return kode;
    }

    public Pelanggan getPelanggan() {
        return pelanggan;
    }

    public Layanan getLayanan() {
        return layanan;
    }

    public int getBerat() {
        return berat;
    }

    public Promo getPromo() {
        return promo;
    }

    public int subtotal() {
        return layanan.getTarifPerKg() * berat;
    }

    public int potongan() {
        return promo.hitungPotongan(this); // [4] diserahkan ke strategi
    }

    public int total() {
        return subtotal() - potongan();
    }
}

// --------------------------------------------------------- tampilan (SRP)
/** Menyusun teks nota untuk satu pesanan. Hanya berubah jika format nota berubah. */
class NotaLaundry {
    static final int LEBAR_NOTA = 36;

    private final PesananLaundry pesanan;

    public NotaLaundry(PesananLaundry pesanan) {
        this.pesanan = pesanan;
    }

    private static String baris(String kiri, String kanan) {
        return String.format("%-24s%12s", kiri, kanan);
    }

    public String buatTeks() {
        PesananLaundry p = pesanan;
        String garis = "=".repeat(LEBAR_NOTA);
        String tarif = RupiahLaundry.format(p.getLayanan().getTarifPerKg());
        List<String> hasil = new ArrayList<>();
        hasil.add(garis);
        hasil.add("LAUNDRY BERSIH KILAT");
        hasil.add(garis);
        hasil.add("No. Order : " + p.getKode());
        hasil.add("Pelanggan : " + p.getPelanggan().getNama());
        hasil.add("Layanan   : " + p.getLayanan().getNama());
        hasil.add("Berat     : " + p.getBerat() + " kg x " + tarif);
        hasil.add("-".repeat(LEBAR_NOTA));
        hasil.add(baris("Subtotal", RupiahLaundry.format(p.subtotal())));
        if (p.potongan() > 0) {
            hasil.add(baris("Promo " + p.getPromo().keterangan(),
                    "-" + RupiahLaundry.format(p.potongan())));
        }
        hasil.add(baris("TOTAL", RupiahLaundry.format(p.total())));
        hasil.add(garis);
        // Baris disambung dengan pemisah baris milik sistem operasi, sama dengan
        // yang dipakai println: "\r\n" di Windows, "\n" di macOS/Linux. Dengan
        // begitu output-nya sama persis byte demi byte dengan SoalC2Sebelum.java
        // di semua sistem operasi (penting saat membandingkan dengan fc/diff).
        return String.join(System.lineSeparator(), hasil);
    }
}

/** Menyusun laporan harian dari daftar pesanan (SRP). */
class LaporanHarian {
    private final List<PesananLaundry> daftarPesanan;

    public LaporanHarian(List<PesananLaundry> daftarPesanan) {
        this.daftarPesanan = daftarPesanan;
    }

    public String buatTeks() {
        List<String> hasil = new ArrayList<>();
        hasil.add("=== LAPORAN HARIAN ===");
        int totalBerat = 0;
        int pendapatan = 0;
        for (PesananLaundry p : daftarPesanan) {
            hasil.add(String.format("%s  %-16s%3d kg%12s", p.getKode(),
                    p.getPelanggan().getNama(), p.getBerat(), RupiahLaundry.format(p.total())));
            totalBerat += p.getBerat();
            pendapatan += p.total();
        }
        hasil.add("Jumlah order : " + daftarPesanan.size());
        hasil.add("Total berat  : " + totalBerat + " kg");
        hasil.add("Pendapatan   : " + RupiahLaundry.format(pendapatan));
        return String.join(System.lineSeparator(), hasil); // lihat NotaLaundry
    }
}

// ----------------------------------------------------- pengiriman (ISP, DIP)
/** Kontrak kecil: cukup satu method untuk mengirim pesan (ISP). */
interface Pengirim {
    void kirim(String noHp, String pesan);
}

/** Simulasi WhatsApp: pesan dicetak ke layar. */
class PengirimWhatsApp implements Pengirim {
    @Override
    public void kirim(String noHp, String pesan) {
        System.out.println("[WA ke " + noHp + "] " + pesan);
    }
}

// ------------------------------------------------------ alur kerja kasir
/** Mengatur alur kerja kasir dengan memakai kelas-kelas di atas. */
class KasirLaundry {
    private final KatalogLayanan katalog;
    private final Pengirim pengirim; // bergantung pada ABSTRAKSI (DIP)
    private final List<PesananLaundry> riwayat = new ArrayList<>();
    private int nomorTerakhir = 0;

    public KasirLaundry(KatalogLayanan katalog, Pengirim pengirim) { // [5]
        this.katalog = katalog;
        this.pengirim = pengirim;
    }

    /** Melempar LayananTidakTersediaException jika layanan tidak dikenal. */
    public PesananLaundry terimaCucian(Pelanggan pelanggan, String namaLayanan, int berat,
            Promo promo) throws LayananTidakTersediaException {
        Layanan layanan = katalog.cari(namaLayanan); // dicek SEBELUM nomor dibuat
        nomorTerakhir++;
        String kode = String.format("L%03d", nomorTerakhir);
        PesananLaundry pesanan = new PesananLaundry(kode, pelanggan, layanan, berat, promo);
        System.out.println(new NotaLaundry(pesanan).buatTeks());
        pengirim.kirim(pelanggan.getNoHp(), "Halo " + pelanggan.getNama() + ", cucian " + kode
                + " sudah kami terima. Total " + RupiahLaundry.format(pesanan.total()) + ".");
        riwayat.add(pesanan);
        return pesanan;
    }

    public List<PesananLaundry> riwayat() {
        return new ArrayList<>(riwayat);
    }
}
