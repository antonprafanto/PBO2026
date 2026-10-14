package kedaikita;

/*
 * File Kedai.java: kelas Kedai, "pusat" yang menyimpan menu dan mencatat pesanan.
 *
 * Yang berubah di Pertemuan 13 (DIP - Dependency Inversion):
 * - Kedai tidak lagi membuat list riwayat sendiri. Tempat penyimpanan
 *   pesanan "disuntikkan" lewat konstruktor (dependency injection) dan
 *   bertipe abstrak PenyimpananPesanan. Kedai tidak peduli apakah pesanan
 *   disimpan di memori, di file, atau di database.
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
    private PenyimpananPesanan penyimpanan; // bergantung pada ABSTRAKSI

    public Kedai(String nama, PenyimpananPesanan penyimpanan) {
        this.nama = nama;
        this.daftarMenu = new LinkedHashMap<>();
        this.penyimpanan = penyimpanan;
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
        penyimpanan.simpan(pesanan);
        return pesanan;
    }

    public List<Pesanan> riwayatPesanan() {
        return penyimpanan.semua();
    }

    public int jumlahPesanan() {
        return penyimpanan.jumlah();
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
