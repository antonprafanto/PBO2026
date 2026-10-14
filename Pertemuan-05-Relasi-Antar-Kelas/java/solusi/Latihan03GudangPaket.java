/*
 * Solusi Latihan 03 - Gudang Paket dan Kurir
 * Pertemuan 05 - Relasi Antar Kelas
 *
 * Relasi yang dipakai:
 * - Gudang o-- Paket  : agregasi (paket datang dari luar lalu diterima gudang)
 * - Paket --> Kurir   : asosiasi 0..1 (paket baru belum punya kurir = null)
 *
 * Ide penyelesaian:
 * - cariPaket() mengembalikan objek Paket, atau null jika resi tidak ada.
 *   tugaskanKurir() WAJIB memeriksa null sebelum memakai hasilnya.
 * - Menghitung paket milik seorang kurir: bandingkan referensinya dengan
 *   operator == (objek kurir yang SAMA, bukan sekadar nama yang sama).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03GudangPaket.java
 */
import java.util.ArrayList;
import java.util.List;

public class Latihan03GudangPaket {

    public static void main(String[] args) {
        Gudang gudang = new Gudang("Gudang Samarinda");
        gudang.terima(new Paket("SMD001", "Jl. Juanda", 2));
        gudang.terima(new Paket("SMD002", "Jl. Pahlawan", 5));
        gudang.terima(new Paket("SMD003", "Jl. Antasari", 1));
        Kurir joko = new Kurir("Joko");
        Kurir wawan = new Kurir("Wawan");

        System.out.println("=== PAKET MASUK ===");
        gudang.tampilkan();

        System.out.println();
        System.out.println("=== PENUGASAN KURIR ===");
        gudang.tugaskanKurir("SMD001", joko);
        gudang.tugaskanKurir("SMD003", joko);
        gudang.tugaskanKurir("SMD009", wawan);
        gudang.tugaskanKurir("SMD002", wawan);

        System.out.println();
        System.out.println("=== STATUS AKHIR ===");
        gudang.tampilkan();
        System.out.println("Paket yang dibawa " + joko.getNama() + ": "
                + gudang.jumlahPaketKurir(joko));
        System.out.println("Paket yang dibawa " + wawan.getNama() + ": "
                + gudang.jumlahPaketKurir(wawan));
    }
}

/** Kurir pengantar paket. */
class Kurir {
    private String nama;

    public Kurir(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }
}

/** Paket kiriman. Kurirnya boleh belum ditentukan (0..1). */
class Paket {
    private String resi;
    private String tujuan;
    private int beratKg;
    private Kurir kurir;

    public Paket(String resi, String tujuan, int beratKg) {
        this.resi = resi;
        this.tujuan = tujuan;
        this.beratKg = beratKg;
        this.kurir = null; // belum ada kurir
    }

    public String getResi() {
        return resi;
    }

    public Kurir getKurir() {
        return kurir;
    }

    public void tugaskan(Kurir kurir) {
        this.kurir = kurir;
    }

    @Override
    public String toString() {
        String namaKurir;
        if (kurir == null) {
            namaKurir = "belum ada";
        } else {
            namaKurir = kurir.getNama();
        }
        return resi + " ke " + tujuan + ", " + beratKg + " kg - kurir: " + namaKurir;
    }
}

/** Gudang yang menampung paket-paket sebelum diantar. */
class Gudang {
    private String nama;
    private List<Paket> daftarPaket;

    public Gudang(String nama) {
        this.nama = nama;
        this.daftarPaket = new ArrayList<>();
    }

    public void terima(Paket paket) {
        daftarPaket.add(paket);
    }

    public Paket cariPaket(String resi) {
        for (Paket paket : daftarPaket) {
            if (paket.getResi().equals(resi)) {
                return paket;
            }
        }
        return null;
    }

    public void tugaskanKurir(String resi, Kurir kurir) {
        Paket paket = cariPaket(resi);
        if (paket == null) { // periksa dulu, jangan langsung dipakai
            System.out.println("Gagal: paket " + resi + " tidak ditemukan");
            return;
        }
        paket.tugaskan(kurir);
        System.out.println(resi + " diantar oleh " + kurir.getNama());
    }

    public int jumlahPaketKurir(Kurir kurir) {
        int jumlah = 0;
        for (Paket paket : daftarPaket) {
            if (paket.getKurir() == kurir) { // objek kurir yang sama
                jumlah++;
            }
        }
        return jumlah;
    }

    public void tampilkan() {
        System.out.println(nama + " (" + daftarPaket.size() + " paket):");
        for (Paket paket : daftarPaket) {
            System.out.println("- " + paket);
        }
    }
}
