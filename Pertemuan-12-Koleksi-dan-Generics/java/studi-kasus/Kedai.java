/*
 * File Kedai.java: kelas Kedai, "pusat" yang menyimpan menu dan mencatat pesanan.
 *
 * Yang baru di Pertemuan 12:
 * - Menu disimpan dalam MAP (kode -> Menu), bukan list. Mencari menu
 *   berdasarkan kode jadi langsung, tanpa perlu memeriksa satu per satu,
 *   dan kode ganda bisa ditolak. LinkedHashMap dipakai agar urutan menu
 *   tetap sesuai urutan saat ditambahkan.
 * - Method baru: semuaMenu(), menuBerdasarkanKategori(),
 *   daftarKategori() (memakai SET), dan riwayatPesanan().
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

/** Kedai yang punya daftar menu dan catatan pesanan. */
public class Kedai implements DapatDicetak {
    private String nama;
    private Map<String, Menu> daftarMenu; // kode -> objek Menu
    private List<Pesanan> riwayatPesanan;

    public Kedai(String nama) {
        this.nama = nama;
        this.daftarMenu = new LinkedHashMap<>();
        this.riwayatPesanan = new ArrayList<>();
    }

    public String getNama() {
        return nama;
    }

    public void tambahMenu(Menu menu) {
        if (daftarMenu.containsKey(menu.getKode())) {
            throw new IllegalArgumentException("Kode " + menu.getKode() + " sudah dipakai");
        }
        daftarMenu.put(menu.getKode(), menu);
    }

    /**
     * Mengembalikan Menu berdasarkan kode.
     *
     * Melempar MenuTidakDitemukanException jika kode tidak terdaftar.
     */
    public Menu cariMenu(String kode) throws MenuTidakDitemukanException {
        if (!daftarMenu.containsKey(kode)) {
            throw new MenuTidakDitemukanException(kode);
        }
        return daftarMenu.get(kode);
    }

    /** Salinan daftar menu, urut sesuai urutan saat ditambahkan. */
    public List<Menu> semuaMenu() {
        return new ArrayList<>(daftarMenu.values());
    }

    public List<Menu> menuBerdasarkanKategori(String kategori) {
        List<Menu> hasil = new ArrayList<>();
        for (Menu menu : daftarMenu.values()) {
            if (menu.getKategori().equals(kategori)) {
                hasil.add(menu);
            }
        }
        return hasil;
    }

    /** Kategori unik (tanpa duplikat), diurutkan abjad. */
    public List<String> daftarKategori() {
        Set<String> kategoriUnik = new HashSet<>();
        for (Menu menu : daftarMenu.values()) {
            kategoriUnik.add(menu.getKategori());
        }
        List<String> hasil = new ArrayList<>(kategoriUnik);
        Collections.sort(hasil); // urutan isi HashSet tidak tentu, jadi diurutkan dulu
        return hasil;
    }

    public int jumlahMenu() {
        return daftarMenu.size();
    }

    public Pesanan buatPesanan(Pelanggan pelanggan) {
        Pesanan pesanan = new Pesanan(pelanggan);
        riwayatPesanan.add(pesanan);
        return pesanan;
    }

    public List<Pesanan> riwayatPesanan() {
        return new ArrayList<>(riwayatPesanan);
    }

    public int jumlahPesanan() {
        return riwayatPesanan.size();
    }

    /** Mencetak daftar menu (memenuhi kontrak DapatDicetak). */
    @Override
    public void cetak() {
        System.out.println("=== MENU " + nama + " ===");
        for (Menu menu : daftarMenu.values()) {
            System.out.println(menu);
        }
    }
}
