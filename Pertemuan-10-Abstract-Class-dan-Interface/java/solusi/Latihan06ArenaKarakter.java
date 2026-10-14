/*
 * Solusi Latihan 06 - Arena Karakter: Kelas Abstrak + Interface
 * Pertemuan 10 - Abstract Class dan Interface
 *
 * Ide penyelesaian:
 * - Karakter adalah kelas abstrak (is-a): menyimpan nama dan HP, punya method
 *   konkret terimaSerangan(), pulihkan(), masihHidup(), dan serang().
 * - serang() adalah template method: aturan "yang tumbang tidak bisa
 *   menyerang" ditulis sekali, lalu besar serangan ditanyakan ke method
 *   abstrak kekuatanSerangan() milik kelas anak.
 * - BisaMenyembuhkan adalah interface (can-do). Penyihir (sebuah Karakter)
 *   dan RamuanObat (BUKAN Karakter) sama-sama meng-implements-nya, sehingga
 *   fasePenyembuhan() bisa memakai keduanya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan06ArenaKarakter.java
 */
import java.util.List;

public class Latihan06ArenaKarakter {

    public static void fasePenyembuhan(List<BisaMenyembuhkan> daftar, Karakter target) {
        for (BisaMenyembuhkan penyembuh : daftar) {
            penyembuh.sembuhkan(target);
        }
    }

    public static void main(String[] args) {
        Ksatria arga = new Ksatria("Arga");
        Pemanah laras = new Pemanah("Laras");
        Penyihir mira = new Penyihir("Mira");
        List<Karakter> semua = List.of(arga, laras, mira);

        System.out.println("=== PARA KARAKTER ===");
        for (Karakter karakter : semua) {
            System.out.println(karakter);
        }

        System.out.println();
        System.out.println("=== RONDE 1 ===");
        arga.serang(laras);
        laras.serang(arga);
        mira.serang(laras);

        System.out.println();
        System.out.println("=== RONDE 2 ===");
        arga.serang(laras);
        laras.serang(arga);
        mira.serang(arga);

        System.out.println();
        System.out.println("=== FASE PENYEMBUHAN UNTUK ARGA ===");
        RamuanObat ramuan = new RamuanObat(50);
        fasePenyembuhan(List.of(mira, ramuan), arga);
        ramuan.sembuhkan(mira);

        System.out.println();
        System.out.println("=== STATUS AKHIR ===");
        for (Karakter karakter : semua) {
            System.out.println(karakter);
        }
    }
}

/** Kelas abstrak untuk semua karakter di arena. */
abstract class Karakter {
    private String nama;
    private int hpMaks;
    private int hp;

    protected Karakter(String nama, int hpMaks) {
        this.nama = nama;
        this.hpMaks = hpMaks;
        this.hp = hpMaks;
    }

    public String getNama() {
        return nama;
    }

    public int getHp() {
        return hp;
    }

    /** Nama peran, misalnya "Ksatria". */
    public abstract String peran();

    /** Besar HP lawan yang berkurang setiap kali menyerang. */
    public abstract int kekuatanSerangan();

    public boolean masihHidup() {
        return hp > 0;
    }

    public void terimaSerangan(int jumlah) {
        hp = Math.max(0, hp - jumlah);
    }

    /** Menambah HP tanpa melewati HP maksimal. Mengembalikan HP yang naik. */
    public int pulihkan(int jumlah) {
        int sebelum = hp;
        hp = Math.min(hpMaks, hp + jumlah);
        return hp - sebelum;
    }

    /** Template method: urutan dan aturannya sama untuk semua peran. */
    public final void serang(Karakter lawan) {
        if (!masihHidup()) {
            System.out.println(nama + " sudah tumbang dan tidak bisa menyerang");
            return;
        }
        int kekuatan = kekuatanSerangan();
        lawan.terimaSerangan(kekuatan);
        System.out.println(nama + " menyerang " + lawan.getNama() + ": -" + kekuatan
                + " HP (sisa " + lawan.getHp() + ")");
    }

    @Override
    public String toString() {
        String teks = peran() + " " + nama + ": HP " + hp + "/" + hpMaks;
        if (!masihHidup()) {
            teks += " (tumbang)";
        }
        return teks;
    }
}

/** Kontrak: bisa memulihkan HP sebuah karakter. */
interface BisaMenyembuhkan {
    void sembuhkan(Karakter target);
}

/** Ksatria: HP besar, serangan sedang. */
class Ksatria extends Karakter {

    public Ksatria(String nama) {
        super(nama, 100);
    }

    @Override
    public String peran() {
        return "Ksatria";
    }

    @Override
    public int kekuatanSerangan() {
        return 20;
    }
}

/** Pemanah: HP sedang, serangan kecil. */
class Pemanah extends Karakter {

    public Pemanah(String nama) {
        super(nama, 60);
    }

    @Override
    public String peran() {
        return "Pemanah";
    }

    @Override
    public int kekuatanSerangan() {
        return 15;
    }
}

/** Penyihir: HP kecil, serangan besar, dan bisa menyembuhkan. */
class Penyihir extends Karakter implements BisaMenyembuhkan {

    public Penyihir(String nama) {
        super(nama, 50);
    }

    @Override
    public String peran() {
        return "Penyihir";
    }

    @Override
    public int kekuatanSerangan() {
        return 25;
    }

    @Override
    public void sembuhkan(Karakter target) {
        int naik = target.pulihkan(30);
        System.out.println("Penyihir " + getNama() + " menyembuhkan " + target.getNama()
                + ": +" + naik + " HP");
    }
}

/** Ramuan sekali pakai. Bukan Karakter, tetapi BisaMenyembuhkan. */
class RamuanObat implements BisaMenyembuhkan {
    private int kekuatan;
    private boolean sudahDipakai;

    public RamuanObat(int kekuatan) {
        this.kekuatan = kekuatan;
        this.sudahDipakai = false;
    }

    @Override
    public void sembuhkan(Karakter target) {
        if (sudahDipakai) {
            System.out.println("Ramuan Obat sudah habis");
            return;
        }
        sudahDipakai = true;
        int naik = target.pulihkan(kekuatan);
        System.out.println("Ramuan Obat menyembuhkan " + target.getNama() + ": +" + naik + " HP");
    }
}
