/*
 * Solusi Soal C1 - Sistem Pemesanan Tiket Bioskop
 * Pertemuan 16 - UAS (latihan persiapan, BUKAN soal ujian asli)
 *
 * Konsep yang dipakai:
 * - Kelas abstrak Tiket dengan tiga kelas anak: TiketReguler, TiketVIP,
 *   dan TiketPelajar.
 * - Polimorfisme: Jadwal dan Bioskop cukup memanggil tiket.hitungHarga()
 *   dan tiket.jenis() tanpa memeriksa jenis tiketnya.
 * - Exception buatan sendiri: BioskopException (CHECKED, turunan Exception)
 *   dan tiga turunannya. KursiSudahTerjualException membawa data tambahan.
 * - Koleksi: LinkedHashMap (kode jadwal -> Jadwal), TreeMap (kode kursi ->
 *   Tiket, otomatis urut kunci), List, dan Comparator untuk laporan terurut.
 * - Bonus: TiketFactory (pola Factory sederhana dari Pertemuan 14).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java SoalC1TiketBioskop.java
 */
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.TreeMap;

public class SoalC1TiketBioskop {

    // Setiap permintaan: {kode jadwal, jenis tiket, kode kursi, nama pemesan}
    static final String[][] DAFTAR_PERMINTAAN = {
        {"J02", "reguler", "A1", "Budi Santoso"},
        {"J02", "VIP", "A2", "Siti Aminah"},
        {"J02", "pelajar", "A1", "Rina Marlina"},
        {"J02", "pelajar", "A3", "Rina Marlina"},
        {"J03", "vip", "D1", "Andi Wijaya"},
        {"J03", "vip", "C5", "Andi Wijaya"},
        {"J05", "reguler", "A1", "Dimas Pratama"},
        {"J01", "premium", "B2", "Dimas Pratama"},
        {"J01", "vip", "B2", "Dimas Pratama"},
        {"J01", "reguler", "B3", "Ayu Lestari"},
        {"J01", "reguler", "B4", "Bima Saputra"},
        {"J03", "pelajar", "C4", "Citra Dewi"},
        {"J02", "reguler", "B1", "Eko Prasetyo"}
    };

    /** Membuat bioskop beserta tiga jadwal tayang hari ini. */
    static Bioskop siapkanBioskop() {
        Bioskop bioskop = new Bioskop("BioskopKita");
        bioskop.tambahJadwal(new Jadwal("J01", "Rindu di Tepian", "13:00", 1, 30000));
        bioskop.tambahJadwal(new Jadwal("J02", "Mahakam Biru", "16:00", 2, 40000));
        bioskop.tambahJadwal(new Jadwal("J03", "Detektif Kampus", "19:00", 1, 50000));
        return bioskop;
    }

    // main boleh melempar BioskopException karena cariJadwal("J02") di bawah
    // dipanggil di luar try (seperti versi Python). J02 pasti ada; jika tidak,
    // program berhenti dan Java menampilkan stack trace.
    public static void main(String[] args) throws BioskopException {
        Bioskop bioskop = siapkanBioskop();
        System.out.println("=== JADWAL TAYANG " + bioskop.getNama() + " ===");
        for (Jadwal jadwal : bioskop.semuaJadwal()) {
            System.out.println(jadwal);
        }
        System.out.println();

        System.out.println("=== PEMESANAN TIKET ===");
        for (String[] permintaan : DAFTAR_PERMINTAAN) {
            String kodeJadwal = permintaan[0];
            try {
                Tiket tiket = bioskop.pesan(kodeJadwal, permintaan[1], permintaan[2],
                        permintaan[3]);
                // Java tidak punya "else" pada try: baris sukses ditulis di dalam try
                String harga = Rupiah.format(tiket.hitungHarga());
                System.out.println("[OK]    " + kodeJadwal + "/" + tiket.getKodeKursi() + " "
                        + tiket.jenis() + " untuk " + tiket.getPemesan() + ": " + harga);
            } catch (KursiSudahTerjualException e) { // [9] yang spesifik ditulis dulu
                System.out.println("[GAGAL] " + e.getMessage());
                System.out.println("        Saran: pilih kursi lain, masih ada "
                        + e.getSisaKursi() + " kursi kosong");
            } catch (BioskopException e) { // [10] semua error bioskop yang lain
                System.out.println("[GAGAL] " + e.getMessage());
            } catch (IllegalArgumentException e) { // jenis tiket tidak dikenal
                System.out.println("[GAGAL] " + e.getMessage());
            }
        }
        System.out.println();

        Jadwal jadwal = bioskop.cariJadwal("J02");
        System.out.println("=== TIKET TERJUAL " + jadwal.getKode() + ": " + jadwal.getJudul()
                + " ===");
        for (Tiket tiket : jadwal.daftarTiket()) {
            System.out.println(tiket); // toString() milik Tiket memanggil method anak
        }
        List<String> kosong = jadwal.kursiKosong();
        System.out.println("Kursi kosong (" + kosong.size() + "): " + String.join(", ", kosong));
        System.out.println();

        System.out.println("=== LAPORAN PENDAPATAN PER FILM ===");
        List<Jadwal> laporan = bioskop.laporanPerFilm();
        for (int i = 0; i < laporan.size(); i++) {
            Jadwal j = laporan.get(i);
            System.out.println(String.format("%d. %-18s%2d tiket%12s", i + 1, j.getJudul(),
                    j.jumlahTerjual(), Rupiah.format(j.pendapatan())));
        }
        System.out.println("Total pendapatan: " + Rupiah.format(bioskop.totalPendapatan()));
        System.out.println();

        System.out.println("=== REKAP PER JENIS TIKET ===");
        Map<String, Integer> pendapatanJenis = bioskop.pendapatanPerJenis();
        for (Map.Entry<String, Integer> entri : bioskop.jumlahPerJenis().entrySet()) {
            String jenis = entri.getKey();
            System.out.println(String.format("%-9s%2d tiket%12s", jenis, entri.getValue(),
                    Rupiah.format(pendapatanJenis.get(jenis))));
        }
    }
}

/** Kelas utilitas format uang: 18000 -> "Rp18.000". */
class Rupiah {
    static String format(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

// ------------------------------------------------------------ exception
/** Induk semua error BioskopKita. CHECKED: wajib ditangkap atau dideklarasikan. */
class BioskopException extends Exception {
    public BioskopException(String pesan) {
        super(pesan);
    }
}

/** Dilempar saat kode jadwal tidak terdaftar. */
class JadwalTidakDitemukanException extends BioskopException {
    private final String kodeJadwal;

    public JadwalTidakDitemukanException(String kodeJadwal) {
        super("Jadwal " + kodeJadwal + " tidak ditemukan");
        this.kodeJadwal = kodeJadwal;
    }

    public String getKodeJadwal() {
        return kodeJadwal;
    }
}

/** Dilempar saat kode kursi tidak ada di studio. */
class KursiTidakAdaException extends BioskopException {
    private final String kodeKursi;
    private final int studio;

    public KursiTidakAdaException(String kodeKursi, int studio) {
        super("Kursi " + kodeKursi + " tidak ada di Studio " + studio);
        this.kodeKursi = kodeKursi;
        this.studio = studio;
    }

    public String getKodeKursi() {
        return kodeKursi;
    }

    public int getStudio() {
        return studio;
    }
}

/** Dilempar saat kursi sudah dipesan orang lain. */
class KursiSudahTerjualException extends BioskopException {
    private final String kodeKursi;
    private final String judul;
    private final int sisaKursi; // [2] data tambahan untuk penangkap error

    public KursiSudahTerjualException(String kodeKursi, String judul, int sisaKursi) {
        super("Kursi " + kodeKursi + " untuk " + judul + " sudah terjual"); // [1]
        this.kodeKursi = kodeKursi;
        this.judul = judul;
        this.sisaKursi = sisaKursi;
    }

    public String getKodeKursi() {
        return kodeKursi;
    }

    public String getJudul() {
        return judul;
    }

    public int getSisaKursi() {
        return sisaKursi;
    }
}

// ---------------------------------------------------------------- tiket
/** Kelas abstrak: kerangka untuk semua jenis tiket. */
abstract class Tiket {
    private final String kodeKursi;
    private final String pemesan;
    private final int hargaDasar;

    public Tiket(String kodeKursi, String pemesan, int hargaDasar) {
        this.kodeKursi = kodeKursi;
        this.pemesan = pemesan;
        this.hargaDasar = hargaDasar;
    }

    public String getKodeKursi() {
        return kodeKursi;
    }

    public String getPemesan() {
        return pemesan;
    }

    public int getHargaDasar() {
        return hargaDasar;
    }

    /** Nama jenis tiket, misalnya "Reguler". */
    public abstract String jenis(); // [3] method abstrak: WAJIB diisi kelas anak

    /** Harga akhir tiket dalam rupiah (bilangan bulat). */
    public abstract int hitungHarga();

    @Override
    public String toString() { // [4] method konkret yang memanggil method abstrak
        String harga = Rupiah.format(hitungHarga());
        return String.format("%-4s%-9s%-16s%10s", kodeKursi, jenis(), pemesan, harga);
    }
}

/** Tiket reguler: harganya sama dengan harga dasar jadwal. */
class TiketReguler extends Tiket {
    public TiketReguler(String kodeKursi, String pemesan, int hargaDasar) {
        super(kodeKursi, pemesan, hargaDasar);
    }

    @Override
    public String jenis() {
        return "Reguler";
    }

    @Override
    public int hitungHarga() {
        return getHargaDasar();
    }
}

/** Kursi sofa + popcorn: harga dasar ditambah biaya tetap. */
class TiketVIP extends Tiket {
    static final int TAMBAHAN = 25000;

    public TiketVIP(String kodeKursi, String pemesan, int hargaDasar) {
        super(kodeKursi, pemesan, hargaDasar);
    }

    @Override
    public String jenis() {
        return "VIP";
    }

    @Override
    public int hitungHarga() {
        return getHargaDasar() + TAMBAHAN;
    }
}

/** Tiket pelajar/mahasiswa: diskon 20% dari harga dasar. */
class TiketPelajar extends Tiket {
    static final int DISKON_PERSEN = 20;

    public TiketPelajar(String kodeKursi, String pemesan, int hargaDasar) {
        super(kodeKursi, pemesan, hargaDasar);
    }

    @Override
    public String jenis() {
        return "Pelajar";
    }

    @Override
    public int hitungHarga() {
        int potongan = getHargaDasar() * DISKON_PERSEN / 100;
        return getHargaDasar() - potongan;
    }
}

/** Factory sederhana: membuat objek Tiket dari pilihan berupa teks. */
class TiketFactory {
    static Tiket buat(String jenis, String kodeKursi, String pemesan, int hargaDasar) {
        // "VIP", "vip", dan "Vip" dianggap sama. Locale.ROOT membuat aturan huruf
        // kecilnya sama di semua komputer, apa pun bahasa sistem operasinya.
        String pilihan = jenis.toLowerCase(Locale.ROOT);
        if (pilihan.equals("reguler")) {
            return new TiketReguler(kodeKursi, pemesan, hargaDasar);
        }
        if (pilihan.equals("vip")) {
            return new TiketVIP(kodeKursi, pemesan, hargaDasar);
        }
        if (pilihan.equals("pelajar")) {
            return new TiketPelajar(kodeKursi, pemesan, hargaDasar);
        }
        throw new IllegalArgumentException("Jenis tiket '" + jenis + "' tidak dikenal");
    }
}

// --------------------------------------------------------------- jadwal
/** Satu jadwal tayang: film, jam, studio, harga dasar, dan kursi terjual. */
class Jadwal {
    static final String BARIS = "ABC";
    static final int KURSI_PER_BARIS = 5;

    private final String kode;
    private final String judul;
    private final String jam;
    private final int studio;
    private final int hargaDasar;
    private final List<String> semuaKursi = new ArrayList<>(); // A1..A5, B1..B5, C1..C5
    // [5] kode kursi -> Tiket. TreeMap selalu urut berdasarkan kunci (A1, A2, ...)
    private final Map<String, Tiket> terjual = new TreeMap<>();

    public Jadwal(String kode, String judul, String jam, int studio, int hargaDasar) {
        if (hargaDasar <= 0) {
            throw new IllegalArgumentException("Harga dasar harus lebih dari 0");
        }
        this.kode = kode;
        this.judul = judul;
        this.jam = jam;
        this.studio = studio;
        this.hargaDasar = hargaDasar;
        for (char baris : BARIS.toCharArray()) {
            for (int nomor = 1; nomor <= KURSI_PER_BARIS; nomor++) {
                semuaKursi.add(baris + String.valueOf(nomor));
            }
        }
    }

    public String getKode() {
        return kode;
    }

    public String getJudul() {
        return judul;
    }

    public int getHargaDasar() {
        return hargaDasar;
    }

    /** Menyimpan tiket. Melempar exception jika kursi tidak ada/sudah terjual. */
    public void tambahTiket(Tiket tiket) throws KursiTidakAdaException,
            KursiSudahTerjualException {
        String kursi = tiket.getKodeKursi();
        if (!semuaKursi.contains(kursi)) {
            throw new KursiTidakAdaException(kursi, studio);
        }
        if (terjual.containsKey(kursi)) { // [6] cek kunci Map
            throw new KursiSudahTerjualException(kursi, judul, kursiKosong().size());
        }
        terjual.put(kursi, tiket);
    }

    public List<String> kursiKosong() {
        List<String> hasil = new ArrayList<>();
        for (String kursi : semuaKursi) {
            if (!terjual.containsKey(kursi)) {
                hasil.add(kursi);
            }
        }
        return hasil;
    }

    /** Tiket terjual, sudah urut kode kursi karena memakai TreeMap. */
    public List<Tiket> daftarTiket() {
        return new ArrayList<>(terjual.values());
    }

    public int jumlahTerjual() {
        return terjual.size();
    }

    public int pendapatan() {
        int total = 0;
        for (Tiket tiket : terjual.values()) {
            total += tiket.hitungHarga(); // [7] polimorfisme
        }
        return total;
    }

    @Override
    public String toString() {
        return String.format("%s  %s  Studio %d  %-18s%10s", kode, jam, studio, judul,
                Rupiah.format(hargaDasar));
    }
}

// -------------------------------------------------------------- bioskop
/** Bioskop yang menyimpan jadwal tayang dan melayani pemesanan. */
class Bioskop {
    private final String nama;
    // kode jadwal -> Jadwal. LinkedHashMap menjaga urutan saat dimasukkan.
    private final Map<String, Jadwal> daftarJadwal = new LinkedHashMap<>();

    public Bioskop(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public void tambahJadwal(Jadwal jadwal) {
        if (daftarJadwal.containsKey(jadwal.getKode())) {
            throw new IllegalArgumentException("Kode jadwal " + jadwal.getKode()
                    + " sudah dipakai");
        }
        daftarJadwal.put(jadwal.getKode(), jadwal);
    }

    public Jadwal cariJadwal(String kode) throws JadwalTidakDitemukanException {
        if (!daftarJadwal.containsKey(kode)) {
            throw new JadwalTidakDitemukanException(kode);
        }
        return daftarJadwal.get(kode);
    }

    /** Memesan satu tiket. Urutan pemeriksaan: jadwal, jenis, kursi. */
    public Tiket pesan(String kodeJadwal, String jenis, String kodeKursi, String pemesan)
            throws BioskopException { // mencakup ketiga turunannya
        Jadwal jadwal = cariJadwal(kodeJadwal);
        Tiket tiket = TiketFactory.buat(jenis, kodeKursi, pemesan, jadwal.getHargaDasar());
        jadwal.tambahTiket(tiket);
        return tiket;
    }

    public List<Jadwal> semuaJadwal() {
        return new ArrayList<>(daftarJadwal.values());
    }

    public List<Tiket> semuaTiket() {
        List<Tiket> hasil = new ArrayList<>();
        for (Jadwal jadwal : daftarJadwal.values()) {
            hasil.addAll(jadwal.daftarTiket());
        }
        return hasil;
    }

    public int totalPendapatan() {
        int total = 0;
        for (Jadwal jadwal : daftarJadwal.values()) {
            total += jadwal.pendapatan();
        }
        return total;
    }

    /** Pendapatan terbesar dulu; jika sama, judul A-Z. */
    public List<Jadwal> laporanPerFilm() {
        List<Jadwal> hasil = new ArrayList<>(daftarJadwal.values());
        hasil.sort(Comparator.comparing(Jadwal::pendapatan).reversed()
                .thenComparing(Jadwal::getJudul)); // [8]
        return hasil;
    }

    /** Jenis tiket -> banyak tiket terjual. TreeMap: urut nama jenis. */
    public Map<String, Integer> jumlahPerJenis() {
        Map<String, Integer> hasil = new TreeMap<>();
        for (Tiket tiket : semuaTiket()) {
            hasil.put(tiket.jenis(), hasil.getOrDefault(tiket.jenis(), 0) + 1);
        }
        return hasil;
    }

    /** Jenis tiket -> total pendapatan. TreeMap: urut nama jenis. */
    public Map<String, Integer> pendapatanPerJenis() {
        Map<String, Integer> hasil = new TreeMap<>();
        for (Tiket tiket : semuaTiket()) {
            hasil.put(tiket.jenis(), hasil.getOrDefault(tiket.jenis(), 0)
                    + tiket.hitungHarga());
        }
        return hasil;
    }
}
