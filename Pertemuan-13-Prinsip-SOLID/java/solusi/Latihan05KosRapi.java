/*
 * Solusi Latihan 05 - Membongkar KosSerbaBisa (SRP + refactoring)
 * Pertemuan 13 - Prinsip SOLID
 *
 * Ide penyelesaian:
 * - KosSerbaBisa punya empat tugas. Setiap tugas kini punya kelasnya sendiri:
 *     Kamar             -> data satu kamar (nomor, penghuni, sewa)
 *     PenghitungTagihan -> aturan denda dan total tagihan
 *     PencetakKuitansi  -> format kuitansi
 *     BukuKas           -> catatan pembayaran dan pemasukan
 * - PengelolaKos hanya mengatur URUTAN kerja. Rekan kerjanya disuntikkan lewat
 *   konstruktor, sehingga mudah diganti (misalnya pencetak kuitansi versi lain).
 * - Sengaja TIDAK dibuat interface untuk setiap kelas: program sekecil ini
 *   belum membutuhkannya (ingat YAGNI). Abstraksi bisa ditambahkan saat perlu.
 * - Refactor = perilaku tidak berubah: output program ini SAMA PERSIS dengan
 *   output KosSerbaBisa. Buktikan dengan fc (Windows) atau diff (macOS/Linux).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05KosRapi.java
 */
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public class Latihan05KosRapi {

    static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    public static void main(String[] args) {
        BukuKas bukuKas = new BukuKas();
        PengelolaKos kos = new PengelolaKos(new PenghitungTagihan(), new PencetakKuitansi(), bukuKas);
        kos.tambahKamar(new Kamar("A1", "Ayu", 750000));
        kos.tambahKamar(new Kamar("A2", "Bima", 750000));
        kos.tambahKamar(new Kamar("B1", "Citra", 900000));

        kos.bayar("A1", 0);
        kos.bayar("B1", 3);
        kos.bayar("A2", 14);
        System.out.println("Kamar lunas: " + bukuKas.jumlahTransaksi()
                + ", pemasukan: " + formatRupiah(bukuKas.pemasukan()));
    }
}

/** Data satu kamar kos. */
class Kamar {
    private String nomor;
    private String penghuni;
    private int sewa;

    public Kamar(String nomor, String penghuni, int sewa) {
        this.nomor = nomor;
        this.penghuni = penghuni;
        this.sewa = sewa;
    }

    public String getNomor() {
        return nomor;
    }

    public String getPenghuni() {
        return penghuni;
    }

    public int getSewa() {
        return sewa;
    }
}

/** Satu-satunya tempat aturan denda keterlambatan. */
class PenghitungTagihan {
    private static final int DENDA_PER_HARI = 10000;
    private static final int DENDA_MAKSIMAL = 100000;

    public int denda(int hariTerlambat) {
        if (hariTerlambat <= 0) {
            return 0;
        }
        return Math.min(hariTerlambat * DENDA_PER_HARI, DENDA_MAKSIMAL);
    }

    public int total(Kamar kamar, int hariTerlambat) {
        return kamar.getSewa() + denda(hariTerlambat);
    }
}

/** Satu-satunya tempat format kuitansi. */
class PencetakKuitansi {

    public void cetak(Kamar kamar, int hariTerlambat, int denda, int total) {
        System.out.println("KUITANSI KOS MAWAR - KAMAR " + kamar.getNomor());
        System.out.println("Penghuni : " + kamar.getPenghuni());
        System.out.println("Sewa     : " + Latihan05KosRapi.formatRupiah(kamar.getSewa()));
        if (denda > 0) {
            System.out.println("Denda    : " + Latihan05KosRapi.formatRupiah(denda)
                    + " (" + hariTerlambat + " hari)");
        }
        System.out.println("Total    : " + Latihan05KosRapi.formatRupiah(total));
        System.out.println("-".repeat(30));
    }
}

/** Mencatat setiap pembayaran yang masuk. */
class BukuKas {
    private List<Integer> daftarTotal = new ArrayList<>();

    public void catat(int total) {
        daftarTotal.add(total);
    }

    public int jumlahTransaksi() {
        return daftarTotal.size();
    }

    public int pemasukan() {
        int jumlah = 0;
        for (int total : daftarTotal) {
            jumlah += total;
        }
        return jumlah;
    }
}

/** Koordinator: mengatur urutan kerja, detailnya diserahkan ke rekan kerja. */
class PengelolaKos {
    private Map<String, Kamar> daftarKamar = new LinkedHashMap<>();
    private PenghitungTagihan penghitung;
    private PencetakKuitansi pencetak;
    private BukuKas bukuKas;

    public PengelolaKos(PenghitungTagihan penghitung, PencetakKuitansi pencetak, BukuKas bukuKas) {
        this.penghitung = penghitung;
        this.pencetak = pencetak;
        this.bukuKas = bukuKas;
    }

    public void tambahKamar(Kamar kamar) {
        daftarKamar.put(kamar.getNomor(), kamar);
    }

    public void bayar(String nomor, int hariTerlambat) {
        Kamar kamar = daftarKamar.get(nomor);
        int denda = penghitung.denda(hariTerlambat);
        int total = penghitung.total(kamar, hariTerlambat);
        pencetak.cetak(kamar, hariTerlambat, denda, total);
        bukuKas.catat(total);
    }
}
