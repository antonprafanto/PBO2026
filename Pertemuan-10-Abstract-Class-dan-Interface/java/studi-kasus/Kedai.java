/*
 * File Kedai.java: kelas Kedai, "pusat" yang menyimpan menu dan mencatat pesanan.
 *
 * Relasi yang terlihat di sini:
 * - Kedai o-- Menu    : AGREGASI (menu dibuat di luar lalu didaftarkan ke kedai;
 *                       menu bisa tetap ada walau tidak terdaftar di kedai)
 * - Kedai --> Pesanan : ASOSIASI (kedai mencatat pesanan-pesanan yang dibuat)
 *
 * Yang baru di Pertemuan 10: Kedai meng-implements interface DapatDicetak,
 * sehingga tampilkanMenu() diganti nama menjadi cetak().
 */

import java.util.ArrayList;
import java.util.List;

/** Kedai yang punya daftar menu dan catatan pesanan. */
public class Kedai implements DapatDicetak {
    private String nama;
    private List<Menu> daftarMenu;
    private List<Pesanan> daftarPesanan;

    public Kedai(String nama) {
        this.nama = nama;
        this.daftarMenu = new ArrayList<>();
        this.daftarPesanan = new ArrayList<>();
    }

    public String getNama() {
        return nama;
    }

    public void tambahMenu(Menu menu) {
        daftarMenu.add(menu);
    }

    /** Mengembalikan objek Menu dengan kode tertentu, atau null jika tidak ada. */
    public Menu cariMenu(String kode) {
        for (Menu menu : daftarMenu) {
            if (menu.getKode().equals(kode)) {
                return menu;
            }
        }
        return null;
    }

    public int jumlahMenu() {
        return daftarMenu.size();
    }

    public Pesanan buatPesanan(Pelanggan pelanggan) {
        Pesanan pesanan = new Pesanan(pelanggan);
        daftarPesanan.add(pesanan);
        return pesanan;
    }

    public int jumlahPesanan() {
        return daftarPesanan.size();
    }

    /** Mencetak daftar menu (memenuhi kontrak DapatDicetak). */
    @Override
    public void cetak() {
        System.out.println("=== MENU " + nama + " ===");
        for (Menu menu : daftarMenu) {
            System.out.println(menu);
        }
    }
}
