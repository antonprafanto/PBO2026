/*
 * File Kedai.java: kelas Kedai, "pusat" yang menyimpan menu dan mencatat pesanan.
 *
 * Relasi yang terlihat di sini:
 * - Kedai o-- Menu    : AGREGASI (menu dibuat di luar lalu didaftarkan ke kedai;
 *                       menu bisa tetap ada walau tidak terdaftar di kedai)
 * - Kedai --> Pesanan : ASOSIASI (kedai mencatat pesanan-pesanan yang dibuat)
 *
 * Yang baru di Pertemuan 11: cariMenu() tidak lagi mengembalikan null,
 * tetapi melempar MenuTidakDitemukanException bila kode tidak terdaftar.
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

    /**
     * Mengembalikan objek Menu dengan kode tertentu.
     *
     * Melempar MenuTidakDitemukanException jika kode tidak terdaftar.
     */
    public Menu cariMenu(String kode) throws MenuTidakDitemukanException {
        for (Menu menu : daftarMenu) {
            if (menu.getKode().equals(kode)) {
                return menu;
            }
        }
        throw new MenuTidakDitemukanException(kode);
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
