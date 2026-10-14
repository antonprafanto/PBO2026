/*
 * File Kedai.java: kelas Kedai, "pusat" yang menyimpan menu dan mencatat pesanan.
 *
 * Relasi yang terlihat di sini:
 * - Kedai o-- Menu    : AGREGASI (menu dibuat di luar lalu didaftarkan ke kedai;
 *                       menu bisa tetap ada walau tidak terdaftar di kedai)
 * - Kedai --> Pesanan : ASOSIASI (kedai mencatat pesanan-pesanan yang dibuat)
 */

import java.util.ArrayList;
import java.util.List;

/** Kedai yang punya daftar menu dan catatan pesanan. */
public class Kedai {
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

    public void tampilkanMenu() {
        System.out.println("=== MENU " + nama + " ===");
        for (Menu menu : daftarMenu) {
            System.out.println(menu);
        }
    }
}
