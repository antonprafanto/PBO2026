/*
 * Solusi Soal C1 - Peminjaman Alat Laboratorium
 * Pertemuan 08 - UTS (latihan persiapan, BUKAN soal ujian asli)
 *
 * Ide penyelesaian:
 * - Alat adalah kelas induk. AlatElektronik dan KitPraktikum mewarisinya
 *   (extends), menambah field sendiri, dan meng-override toString().
 * - Besar denda per hari dikirim kelas anak ke konstruktor induk lewat
 *   super(...), jadi hitungDenda() cukup ditulis SEKALI di kelas induk.
 * - Laboratorium menyimpan daftar alat (agregasi: alat dibuat di luar lalu
 *   didaftarkan). Peminjaman juga menyimpan alat yang dipinjam (agregasi:
 *   alat tetap ada setelah peminjaman selesai) dan mengenal Mahasiswa
 *   peminjamnya (asosiasi).
 * - Semua field private dan dibaca lewat getter. Data yang tidak valid
 *   ditolak dengan throw new IllegalArgumentException(...).
 *
 * Catatan nama kelas: pemformat uang di file ini bernama RupiahLab, BUKAN
 * Rupiah. Alasannya, folder java/ ini juga berisi solusi Soal C2 yang punya
 * pemformat sendiri (RupiahToko). Editor seperti VS Code menganggap satu
 * folder sebagai satu proyek, sehingga nama kelas di dalamnya harus unik.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java SoalC1PeminjamanAlat.java
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class SoalC1PeminjamanAlat {

    public static void main(String[] args) {
        Laboratorium lab = siapkanLab();
        lab.tampilkanAlat();
        System.out.println();

        System.out.println("=== DATA TIDAK VALID DITOLAK ===");
        try {
            lab.tambahAlat(new AlatElektronik("A03", "Solder Listrik", 0));
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal menambah alat: " + e.getMessage());
        }
        Mahasiswa ayu = new Mahasiswa("2409106001", "Ayu Lestari");
        Mahasiswa bima = new Mahasiswa("2409106002", "Bima Saputra");
        try {
            lab.buatPeminjaman(ayu, 10);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat peminjaman: " + e.getMessage());
        }
        if (lab.cariAlat("X99") == null) {
            System.out.println("Cari X99: alat tidak ditemukan");
        }
        System.out.println();

        System.out.println("=== PEMINJAMAN ===");
        Peminjaman pinjamAyu = lab.buatPeminjaman(ayu, 3);
        pinjamAyu.tambahAlat(lab.cariAlat("A01"));
        pinjamAyu.tambahAlat(lab.cariAlat("K01"));
        pinjamAyu.cetakBukti();

        Peminjaman pinjamBima = lab.buatPeminjaman(bima, 2);
        try {
            pinjamBima.tambahAlat(lab.cariAlat("A01")); // masih dipinjam Ayu
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal meminjam: " + e.getMessage());
        }
        pinjamBima.tambahAlat(lab.cariAlat("A02"));
        pinjamBima.cetakBukti();
        System.out.println();

        System.out.println("=== SETELAH PEMINJAMAN ===");
        tampilkanStatus(lab);
        System.out.println();

        System.out.println("=== PENGEMBALIAN ===");
        prosesPengembalian(pinjamAyu, 2);
        prosesPengembalian(pinjamBima, 0);
        try {
            prosesPengembalian(pinjamAyu, 1); // sudah dikembalikan sebelumnya
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal mengembalikan: " + e.getMessage());
        }
        System.out.println();

        System.out.println("=== STATUS AKHIR ===");
        tampilkanStatus(lab);
        System.out.println("Peminjaman tercatat: " + lab.jumlahPeminjaman());
    }

    /** Membuat laboratorium beserta empat alat awalnya. */
    static Laboratorium siapkanLab() {
        Laboratorium lab = new Laboratorium("Lab Pemrograman");
        lab.tambahAlat(new AlatElektronik("A01", "Proyektor Portabel", 200));
        lab.tambahAlat(new AlatElektronik("A02", "Laptop Cadangan", 65));
        lab.tambahAlat(new KitPraktikum("K01", "Kit Mikrokontroler", 30));
        lab.tambahAlat(new KitPraktikum("K02", "Kit Sensor IoT", 12));
        return lab;
    }

    /** Mengembalikan semua alat sebuah peminjaman lalu mencetak dendanya. */
    static void prosesPengembalian(Peminjaman peminjaman, int hariTerlambat) {
        int denda = peminjaman.kembalikan(hariTerlambat);
        String keterangan;
        if (hariTerlambat == 0) {
            keterangan = "tepat waktu";
        } else {
            keterangan = "terlambat " + hariTerlambat + " hari";
        }
        System.out.println(peminjaman.getNomor() + " kembali " + keterangan
                + ", denda " + RupiahLab.format(denda));
    }

    static void tampilkanStatus(Laboratorium lab) {
        lab.tampilkanAlat();
        System.out.println("Alat tersedia: " + lab.jumlahAlatTersedia()
                + " dari " + lab.jumlahAlat());
    }
}

/** Kelas utilitas: mengubah 30000 menjadi "Rp30.000". */
class RupiahLab {
    public static String format(int angka) {
        // Locale.US agar pemisah ribuan selalu koma, lalu diganti titik.
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

/** Peminjam alat. Datanya hanya bisa dibaca dari luar (read-only). */
class Mahasiswa {
    private String nim;
    private String nama;

    public Mahasiswa(String nim, String nama) {
        this.nim = nim;
        this.nama = nama;
    }

    public String getNim() {
        return nim;
    }

    public String getNama() {
        return nama;
    }

    @Override
    public String toString() {
        return nama + " (" + nim + ")";
    }
}

/** Kelas induk: data dan perilaku yang dimiliki SEMUA alat lab. */
class Alat {
    private String kode;
    private String nama;
    private int dendaPerHari;
    private boolean tersedia;

    public Alat(String kode, String nama, int dendaPerHari) {
        if (dendaPerHari <= 0) {
            throw new IllegalArgumentException("Denda per hari harus lebih dari 0");
        }
        this.kode = kode;
        this.nama = nama;
        this.dendaPerHari = dendaPerHari;
        this.tersedia = true; // [1] alat baru selalu tersedia
    }

    public String getKode() {
        return kode;
    }

    public String getNama() {
        return nama;
    }

    public int getDendaPerHari() {
        return dendaPerHari;
    }

    public boolean isTersedia() {
        return tersedia;
    }

    /** Pintu resmi untuk mengubah status menjadi dipinjam. */
    public void pinjamkan() {
        if (!tersedia) {
            throw new IllegalArgumentException(nama + " sedang dipinjam"); // [2]
        }
        tersedia = false;
    }

    public void terimaKembali() {
        tersedia = true;
    }

    public int hitungDenda(int hariTerlambat) {
        return dendaPerHari * hariTerlambat;
    }

    @Override
    public String toString() {
        String status = tersedia ? "tersedia" : "dipinjam";
        return "[" + kode + "] " + nama + " - " + status;
    }
}

/** Alat yang memakai listrik. Tambahan: daya dalam watt. */
class AlatElektronik extends Alat {
    private static final int DENDA_PER_HARI = 10000; // Rupiah

    private int dayaWatt;

    public AlatElektronik(String kode, String nama, int dayaWatt) {
        super(kode, nama, DENDA_PER_HARI); // [3] konstruktor induk, WAJIB baris pertama
        if (dayaWatt <= 0) {
            throw new IllegalArgumentException("Daya harus lebih dari 0 watt");
        }
        this.dayaWatt = dayaWatt;
    }

    public int getDayaWatt() {
        return dayaWatt;
    }

    @Override
    public String toString() {
        // [4] override: pakai teks dari induk, lalu tambahkan info daya
        return super.toString() + " | " + dayaWatt + " watt";
    }
}

/** Satu kotak kit berisi banyak komponen. Tambahan: jumlah komponen. */
class KitPraktikum extends Alat {
    private static final int DENDA_PER_HARI = 5000; // Rupiah

    private int jumlahKomponen;

    public KitPraktikum(String kode, String nama, int jumlahKomponen) {
        super(kode, nama, DENDA_PER_HARI);
        if (jumlahKomponen < 1) {
            throw new IllegalArgumentException("Jumlah komponen minimal 1");
        }
        this.jumlahKomponen = jumlahKomponen;
    }

    public int getJumlahKomponen() {
        return jumlahKomponen;
    }

    @Override
    public String toString() {
        return super.toString() + " | " + jumlahKomponen + " komponen";
    }
}

/** Satu transaksi: siapa meminjam, alat apa saja, dan berapa lama. */
class Peminjaman {
    private static final int MAKS_HARI_PINJAM = 7;
    private static final int LEBAR_BUKTI = 40;
    private static int nomorTerakhir = 0; // [5] milik kelas: penghitung nomor otomatis

    private String nomor;
    private Mahasiswa peminjam;
    private int lamaHari;
    private List<Alat> daftarAlat;
    private boolean selesai;

    public Peminjaman(Mahasiswa peminjam, int lamaHari) {
        if (lamaHari < 1 || lamaHari > MAKS_HARI_PINJAM) {
            throw new IllegalArgumentException(
                    "Lama pinjam harus 1 sampai " + MAKS_HARI_PINJAM + " hari");
        }
        nomorTerakhir++; // [6] bertambah HANYA jika data valid
        this.nomor = String.format("PJ%03d", nomorTerakhir); // PJ001, PJ002, ...
        this.peminjam = peminjam; // [7] asosiasi: menyimpan referensi Mahasiswa
        this.lamaHari = lamaHari;
        this.daftarAlat = new ArrayList<>(); // [8] agregasi: alat dibuat di luar
        this.selesai = false;
    }

    public String getNomor() {
        return nomor;
    }

    public Mahasiswa getPeminjam() {
        return peminjam;
    }

    public int getLamaHari() {
        return lamaHari;
    }

    public boolean isSelesai() {
        return selesai;
    }

    /** Mengembalikan SALINAN list, agar isi asli tidak diubah dari luar. */
    public List<Alat> getDaftarAlat() {
        return new ArrayList<>(daftarAlat);
    }

    public void tambahAlat(Alat alat) {
        if (selesai) {
            throw new IllegalArgumentException("Peminjaman " + nomor + " sudah selesai");
        }
        alat.pinjamkan(); // [9] gagal (exception) jika alat sedang dipinjam
        daftarAlat.add(alat);
    }

    /** Menerima kembali semua alat lalu MENGEMBALIKAN total denda. */
    public int kembalikan(int hariTerlambat) {
        if (selesai) {
            throw new IllegalArgumentException("Peminjaman " + nomor + " sudah selesai");
        }
        if (hariTerlambat < 0) {
            throw new IllegalArgumentException("Hari terlambat tidak boleh negatif");
        }
        int totalDenda = 0;
        for (Alat alat : daftarAlat) { // [10] mengirim pesan ke setiap alat
            alat.terimaKembali();
            totalDenda += alat.hitungDenda(hariTerlambat);
        }
        selesai = true;
        return totalDenda;
    }

    public void cetakBukti() {
        String garis = "=".repeat(LEBAR_BUKTI);
        System.out.println(garis);
        System.out.println("BUKTI PEMINJAMAN " + nomor);
        System.out.println(garis);
        System.out.println("Peminjam : " + peminjam);
        System.out.println("Lama     : " + lamaHari + " hari");
        System.out.println("-".repeat(LEBAR_BUKTI));
        System.out.println(String.format("%-30s%10s", "Alat", "Denda/hari"));
        for (Alat alat : daftarAlat) {
            String label = "[" + alat.getKode() + "] " + alat.getNama();
            System.out.println(String.format("%-30s%10s", label,
                    RupiahLab.format(alat.getDendaPerHari())));
        }
        System.out.println("-".repeat(LEBAR_BUKTI));
        System.out.println("Jumlah alat: " + daftarAlat.size());
        System.out.println(garis);
    }
}

/** Lab yang punya daftar alat dan catatan peminjaman. */
class Laboratorium {
    private String nama;
    private List<Alat> daftarAlat; // agregasi
    private List<Peminjaman> daftarPeminjaman; // asosiasi (catatan)

    public Laboratorium(String nama) {
        this.nama = nama;
        this.daftarAlat = new ArrayList<>();
        this.daftarPeminjaman = new ArrayList<>();
    }

    public String getNama() {
        return nama;
    }

    public void tambahAlat(Alat alat) {
        daftarAlat.add(alat);
    }

    /** Mengembalikan objek Alat dengan kode tertentu, atau null. */
    public Alat cariAlat(String kode) {
        for (Alat alat : daftarAlat) {
            if (alat.getKode().equals(kode)) { // String dibandingkan dengan equals
                return alat;
            }
        }
        return null;
    }

    public Peminjaman buatPeminjaman(Mahasiswa peminjam, int lamaHari) {
        Peminjaman peminjaman = new Peminjaman(peminjam, lamaHari); // gagal jika lamaHari salah
        daftarPeminjaman.add(peminjaman);
        return peminjaman;
    }

    public int jumlahAlat() {
        return daftarAlat.size();
    }

    public int jumlahAlatTersedia() {
        int jumlah = 0;
        for (Alat alat : daftarAlat) {
            if (alat.isTersedia()) {
                jumlah++;
            }
        }
        return jumlah;
    }

    public int jumlahPeminjaman() {
        return daftarPeminjaman.size();
    }

    public void tampilkanAlat() {
        System.out.println("=== ALAT " + nama + " ===");
        for (Alat alat : daftarAlat) {
            System.out.println(alat); // memanggil toString() milik kelas anak
        }
    }
}
