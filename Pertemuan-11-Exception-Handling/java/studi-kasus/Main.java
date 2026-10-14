/*
 * KedaiKita - Pertemuan 11: Exception Handling
 *
 * Yang baru dibanding Pertemuan 10:
 * - KedaiException dan turunannya (StokTidakCukupException,
 *   MenuTidakDitemukanException, PembayaranGagalException).
 * - Kesalahan tidak lagi ditandai dengan null/false, tetapi dengan
 *   exception yang dilempar (throw) lalu ditangkap (try/catch).
 * - Contoh lengkap try / catch / finally.
 *
 * Cara menjalankan (dari dalam folder studi-kasus):
 *     javac *.java
 *     java Main
 */
public class Main {

    /** Membuat kedai beserta lima menu awalnya. */
    public static Kedai siapkanKedai() {
        Kedai kedai = new Kedai("KedaiKita");
        kedai.tambahMenu(new Minuman("M01", "Kopi Susu Gula Aren", 18000, 20, true));
        kedai.tambahMenu(new Minuman("M02", "Es Teh Manis", 8000, 30, true));
        kedai.tambahMenu(new Makanan("M03", "Nasi Goreng Kampung", 25000, 15, 2));
        kedai.tambahMenu(new Makanan("M04", "Mie Goreng Jawa", 23000, 10, 1));
        kedai.tambahMenu(new Makanan("M05", "Pisang Goreng Keju", 15000, 12, 0));
        return kedai;
    }

    public static void main(String[] args) {
        Kedai kedai = siapkanKedai();
        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        Pelanggan siti = new Pelanggan("Siti Aminah", "082198765432");
        Pelanggan rina = new Pelanggan("Rina Marlina", "085312345678");

        System.out.println("=== PESANAN BUDI: MENAMBAH ITEM ===");
        Pesanan pesananBudi = kedai.buatPesanan(budi);
        // Dua array sejajar: kode menu ke-i dipesan sebanyak jumlah ke-i.
        String[] kodePermintaan = {"M01", "M03", "M99", "M04", "M02"};
        int[] jumlahPermintaan = {2, 1, 1, 50, 0};
        for (int i = 0; i < kodePermintaan.length; i++) {
            String kode = kodePermintaan[i];
            int jumlah = jumlahPermintaan[i];
            try {
                Menu menu = kedai.cariMenu(kode);
                pesananBudi.tambahItem(menu, jumlah);
                // Baris ini hanya dijalankan jika dua baris di atasnya
                // berhasil (tidak ada exception yang dilempar).
                System.out.println("  [OK] " + jumlah + " x " + menu.getNama());
            } catch (MenuTidakDitemukanException e) {
                System.out.println("  [GAGAL] " + e.getMessage());
            } catch (StokTidakCukupException e) {
                System.out.println("  [GAGAL] " + e.getMessage());
                System.out.println("          Saran: pesan paling banyak " + e.getTersedia()
                        + " porsi");
            } catch (KedaiException e) { // error kedai lain (misalnya pesanan sudah lunas)
                System.out.println("  [GAGAL] " + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.out.println("  [GAGAL] " + kode + ": " + e.getMessage());
            }
        }
        System.out.println();

        try {
            pesananBudi.bayar(new PembayaranTunai(100000));
        } catch (KedaiException e) {
            System.out.println("  [GAGAL] " + e.getMessage());
        }
        System.out.println();

        System.out.println("=== PESANAN SITI: BAYAR GAGAL, LALU COBA LAGI ===");
        Pesanan pesananSiti = kedai.buatPesanan(siti);
        try {
            pesananSiti.tambahItem(kedai.cariMenu("M02"), 2);
            pesananSiti.tambahItem(kedai.cariMenu("M05"));
            pesananSiti.bayar(new PembayaranQRIS(20000));
        } catch (PembayaranGagalException e) {
            System.out.println("  [GAGAL] " + e.getMessage());
            System.out.println("  Mencoba kartu kredit...");
            try {
                pesananSiti.bayar(new PembayaranKartu("BNI"));
            } catch (KedaiException e2) {
                System.out.println("  [GAGAL LAGI] " + e2.getMessage());
            }
        } catch (KedaiException e) {
            System.out.println("  [GAGAL] " + e.getMessage());
        } finally {
            System.out.println("  [log] proses pesanan Siti selesai");
        }
        System.out.println();

        System.out.println("=== SATU PENANGKAP UNTUK SEMUA ERROR KEDAI ===");
        Pesanan pesananRina = kedai.buatPesanan(rina);
        String[] kodeRina = {"M77", "M04"};
        int[] jumlahRina = {1, 99};
        for (int i = 0; i < kodeRina.length; i++) {
            String kode = kodeRina[i];
            int jumlah = jumlahRina[i];
            try {
                pesananRina.tambahItem(kedai.cariMenu(kode), jumlah);
            } catch (KedaiException e) { // menangkap SEMUA turunan KedaiException
                System.out.println("  Ditolak: " + e.getMessage());
            }
        }
        try {
            pesananBudi.bayar(new PembayaranTunai(100000));
        } catch (KedaiException e) {
            System.out.println("  Ditolak: " + e.getMessage());
        }
        try {
            pesananBudi.tambahItem(kedai.cariMenu("M02"), 1);
        } catch (KedaiException e) {
            System.out.println("  Ditolak: " + e.getMessage());
        }
        System.out.println();

        System.out.println("=== RINGKASAN ===");
        System.out.println(pesananBudi.getNomor() + " (" + budi.getNama() + "): "
                + pesananBudi.getStatus());
        System.out.println(pesananSiti.getNomor() + " (" + siti.getNama() + "): "
                + pesananSiti.getStatus());
        System.out.println(pesananRina.getNomor() + " (" + rina.getNama() + "): "
                + pesananRina.getStatus() + ", " + pesananRina.getDaftarItem().size() + " item");
        kedai.cetak();
    }
}
