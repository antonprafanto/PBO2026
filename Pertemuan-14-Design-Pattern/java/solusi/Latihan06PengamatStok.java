/*
 * Solusi Latihan 06 - KedaiKita: PengamatStok (Observer Baru)
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Ide penyelesaian:
 * - PengamatStok adalah OBSERVER baru. Ia hanya bereaksi saat status pesanan
 *   menjadi LUNAS; status lain diabaikan.
 * - Ia memakai gaya PULL: menerima objek pesanan, lalu MENARIK sendiri data
 *   yang dibutuhkan (daftar item dan stok setiap menu).
 * - Jika stok sebuah menu <= batas, cetak peringatan.
 * - Kelas pesanan (subject) TIDAK diubah: pengamat baru cukup didaftarkan
 *   lewat tambahPengamat().
 *
 * Catatan nama kelas: supaya file ini bisa dijalankan sendiri, kita memakai
 * versi MINI dari kelas studi kasus dengan nama berbeda: MenuStok (Menu),
 * BarisPesanan (ItemPesanan), PesananKedai (Pesanan), PengamatStatus
 * (PengamatPesanan), LayarPesanan (mirip LayarDapur). Nama aslinya sudah
 * dipakai di folder studi-kasus, dan VS Code akan protes jika ada dua kelas
 * bernama sama di folder java/ yang sama.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan06PengamatStok.java
 */
import java.util.ArrayList;
import java.util.List;

public class Latihan06PengamatStok {

    static String isiPesanan(PesananKedai pesanan) {
        List<String> teks = new ArrayList<>();
        for (BarisPesanan baris : pesanan.getDaftarBaris()) {
            teks.add(baris.toString());
        }
        return String.join(", ", teks);
    }

    public static void main(String[] args) {
        MenuStok kopi = new MenuStok("Kopi Susu Gula Aren", 20);
        MenuStok nasiGoreng = new MenuStok("Nasi Goreng Kampung", 6);
        MenuStok pisangGoreng = new MenuStok("Pisang Goreng Keju", 5);
        LayarPesanan layar = new LayarPesanan();
        PengamatStok pengamatStok = new PengamatStok(5);

        PesananKedai p001 = new PesananKedai("P001");
        p001.tambahItem(kopi, 2);
        p001.tambahItem(nasiGoreng, 3);
        p001.tambahPengamat(layar);
        p001.tambahPengamat(pengamatStok); // pengamat baru cukup didaftarkan
        System.out.println("=== PESANAN P001 ===");
        System.out.println("Isi: " + isiPesanan(p001));
        p001.ubahStatus("LUNAS"); // di studi kasus, bayar() yang memanggil ini
        p001.ubahStatus("DIPROSES");

        System.out.println();
        PesananKedai p002 = new PesananKedai("P002");
        p002.tambahItem(kopi, 1);
        p002.tambahItem(pisangGoreng, 1);
        p002.tambahPengamat(layar);
        p002.tambahPengamat(pengamatStok);
        System.out.println("=== PESANAN P002 ===");
        System.out.println("Isi: " + isiPesanan(p002));
        p002.ubahStatus("LUNAS");

        System.out.println();
        System.out.println("=== SISA STOK ===");
        for (MenuStok menu : List.of(kopi, nasiGoreng, pisangGoreng)) {
            System.out.println(String.format("%-20s%3d porsi", menu.getNama(), menu.getStok()));
        }
    }
}

class MenuStok {
    private String nama;
    private int stok;

    MenuStok(String nama, int stok) {
        this.nama = nama;
        this.stok = stok;
    }

    public String getNama() {
        return nama;
    }

    public int getStok() {
        return stok;
    }

    public void kurangiStok(int jumlah) {
        if (jumlah > stok) {
            throw new IllegalArgumentException("Stok " + nama + " tidak cukup");
        }
        stok -= jumlah;
    }
}

class BarisPesanan {
    private MenuStok menu;
    private int jumlah;

    BarisPesanan(MenuStok menu, int jumlah) {
        this.menu = menu;
        this.jumlah = jumlah;
    }

    public MenuStok getMenu() {
        return menu;
    }

    @Override
    public String toString() {
        return jumlah + " x " + menu.getNama();
    }
}

/** Observer: diberi tahu setiap kali status pesanan berubah. */
interface PengamatStatus {
    /** Pesanan mengirim DIRINYA SENDIRI (gaya pull). */
    void perbarui(PesananKedai pesanan);
}

/** Subject (versi mini Pesanan). */
class PesananKedai {
    private String nomor;
    private List<BarisPesanan> daftarBaris = new ArrayList<>();
    private String status = "BARU";
    private List<PengamatStatus> daftarPengamat = new ArrayList<>();

    PesananKedai(String nomor) {
        this.nomor = nomor;
    }

    public String getNomor() {
        return nomor;
    }

    public String getStatus() {
        return status;
    }

    public List<BarisPesanan> getDaftarBaris() {
        return new ArrayList<>(daftarBaris);
    }

    public void tambahItem(MenuStok menu, int jumlah) {
        menu.kurangiStok(jumlah); // stok berkurang saat item ditambahkan
        daftarBaris.add(new BarisPesanan(menu, jumlah));
    }

    public void tambahPengamat(PengamatStatus pengamat) {
        daftarPengamat.add(pengamat);
    }

    public void ubahStatus(String statusBaru) {
        status = statusBaru;
        for (PengamatStatus pengamat : daftarPengamat) {
            pengamat.perbarui(this);
        }
    }
}

/** Pengamat lama: menampilkan setiap perubahan status. */
class LayarPesanan implements PengamatStatus {
    @Override
    public void perbarui(PesananKedai pesanan) {
        System.out.println("  [LAYAR] " + pesanan.getNomor() + " -> " + pesanan.getStatus());
    }
}

/** Pengamat BARU: memberi peringatan saat stok menu menipis. */
class PengamatStok implements PengamatStatus {
    private int batas;

    PengamatStok(int batas) {
        this.batas = batas;
    }

    @Override
    public void perbarui(PesananKedai pesanan) {
        if (!pesanan.getStatus().equals("LUNAS")) { // hanya peduli saat pesanan lunas
            return;
        }
        for (BarisPesanan baris : pesanan.getDaftarBaris()) { // PULL: tarik data dari pesanan
            MenuStok menu = baris.getMenu();
            if (menu.getStok() <= batas) {
                System.out.println("  [STOK] Peringatan: " + menu.getNama() + " tinggal "
                        + menu.getStok() + " porsi");
            }
        }
    }
}
