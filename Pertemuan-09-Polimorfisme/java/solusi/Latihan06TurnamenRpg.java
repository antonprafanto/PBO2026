/*
 * Solusi Latihan 06 - Turnamen Mini RPG
 * Pertemuan 09 - Polimorfisme
 *
 * Ide penyelesaian:
 * - serang(lawan) ditulis SEKALI di kelas induk Karakter. Di dalamnya ada DUA
 *   panggilan polimorfik sekaligus:
 *     hitungSerangan()               -> versi milik PENYERANG (this)
 *     lawan.terimaSerangan(damage)   -> versi milik yang DISERANG
 * - Prajurit meng-override terimaSerangan(): damage dikurangi perisai
 *   (minimal tetap 1).
 * - Penyihir meng-override hitungSerangan(): setiap serangan ke-3, ke-6, ...
 *   menjadi bola api (3 kali kekuatan).
 * - Pemanah meng-override terimaSerangan(): setiap serangan ke-2, ke-4, ...
 *   yang mengarah kepadanya berhasil dihindari (damage 0).
 * - Tidak ada angka acak, jadi hasil turnamen selalu sama.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan06TurnamenRpg.java
 */
public class Latihan06TurnamenRpg {
    static final int RONDE_MAKS = 10;

    static void duel(Karakter a, Karakter b) {
        System.out.println("=== DUEL: " + a.getNama() + " (" + a.getClass().getSimpleName()
                + ") vs " + b.getNama() + " (" + b.getClass().getSimpleName() + ") ===");
        for (int ronde = 1; ronde <= RONDE_MAKS; ronde++) {
            System.out.println("Ronde " + ronde);
            a.serang(b);
            if (!b.masihHidup()) {
                break;
            }
            b.serang(a);
            if (!a.masihHidup()) {
                break;
            }
        }
        if (a.masihHidup() && b.masihHidup()) {
            System.out.println("Hasil: seri");
        } else if (a.masihHidup()) {
            System.out.println("Pemenang: " + a.getNama());
        } else {
            System.out.println("Pemenang: " + b.getNama());
        }
    }

    public static void main(String[] args) {
        duel(new Prajurit("Bima", 60, 10, 4), new Penyihir("Sari", 45, 9));
        System.out.println();
        duel(new Penyihir("Sari", 45, 9), new Pemanah("Raka", 50, 8));
    }
}

/** Kelas induk semua karakter. */
class Karakter {
    private String nama;
    private int hp;
    private int kekuatan;

    public Karakter(String nama, int hp, int kekuatan) {
        this.nama = nama;
        this.hp = hp;
        this.kekuatan = kekuatan;
    }

    public String getNama() {
        return nama;
    }

    public int getHp() {
        return hp;
    }

    public int getKekuatan() {
        return kekuatan;
    }

    public boolean masihHidup() {
        return hp > 0;
    }

    public int hitungSerangan() {
        return kekuatan;
    }

    /** Mengurangi HP, lalu mengembalikan damage yang benar-benar diterima. */
    public int terimaSerangan(int damage) {
        hp = Math.max(hp - damage, 0);
        return damage;
    }

    public void serang(Karakter lawan) {
        int damage = hitungSerangan(); // polimorfisme: versi penyerang
        int diterima = lawan.terimaSerangan(damage); // polimorfisme: versi lawan
        System.out.println("  " + nama + " menyerang " + lawan.getNama() + ": " + diterima
                + " damage, HP " + lawan.getNama() + " tinggal " + lawan.getHp());
    }
}

class Prajurit extends Karakter {
    private int perisai;

    public Prajurit(String nama, int hp, int kekuatan, int perisai) {
        super(nama, hp, kekuatan);
        this.perisai = perisai;
    }

    @Override
    public int terimaSerangan(int damage) {
        int dikurangi = Math.max(damage - perisai, 1);
        return super.terimaSerangan(dikurangi); // memperluas versi induk
    }
}

class Penyihir extends Karakter {
    private int jumlahSerangan;

    public Penyihir(String nama, int hp, int kekuatan) {
        super(nama, hp, kekuatan);
        this.jumlahSerangan = 0;
    }

    @Override
    public int hitungSerangan() {
        jumlahSerangan++;
        if (jumlahSerangan % 3 == 0) {
            return getKekuatan() * 3; // bola api
        }
        return getKekuatan();
    }
}

class Pemanah extends Karakter {
    private int jumlahDiserang;

    public Pemanah(String nama, int hp, int kekuatan) {
        super(nama, hp, kekuatan);
        this.jumlahDiserang = 0;
    }

    @Override
    public int terimaSerangan(int damage) {
        jumlahDiserang++;
        if (jumlahDiserang % 2 == 0) {
            return 0; // berhasil menghindar, HP tidak berkurang
        }
        return super.terimaSerangan(damage);
    }
}
