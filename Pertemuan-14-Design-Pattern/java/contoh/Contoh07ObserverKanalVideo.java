/*
 * Contoh 07 - Observer: Berlangganan Kanal Video
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Pola OBSERVER punya dua peran:
 * - SUBJECT (KanalVideo): menyimpan daftar pengamat, lalu memberi kabar ke
 *   SEMUA pengamat setiap kali ada kejadian (video baru diunggah).
 * - OBSERVER (PengamatKanal): siapa pun yang ingin diberi kabar. Bisa
 *   penonton, bisa pencatat statistik, bisa apa saja yang ditambahkan kelak.
 *
 * Kanal tidak perlu tahu jenis pengamatnya. Ia cukup memanggil perbarui().
 * Di contoh ini, data kejadian (nama kanal dan judul) DIKIRIM langsung ke
 * pengamat. Gaya ini disebut PUSH.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh07ObserverKanalVideo.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh07ObserverKanalVideo {

    public static void main(String[] args) {
        KanalVideo kanal = new KanalVideo("Belajar PBO");
        Penonton ayu = new Penonton("Ayu");
        Penonton bima = new Penonton("Bima");
        kanal.langganan(ayu);
        kanal.langganan(bima);
        kanal.langganan(new PencatatStatistik());

        System.out.println("=== VIDEO PERTAMA (3 PENGAMAT) ===");
        kanal.unggahVideo("Kelas dan Objek");

        System.out.println();
        System.out.println("=== BIMA BERHENTI BERLANGGANAN ===");
        kanal.berhentiLangganan(bima); // [5]
        kanal.unggahVideo("Design Pattern Dasar");
    }
}

/** Observer: kontrak untuk siapa pun yang ingin diberi kabar video baru. */
interface PengamatKanal {
    void perbarui(String namaKanal, String judul);
}

class Penonton implements PengamatKanal {
    private String nama;

    Penonton(String nama) {
        this.nama = nama;
    }

    @Override
    public void perbarui(String namaKanal, String judul) {
        System.out.println("  [HP " + nama + "] Video baru dari " + namaKanal + ": " + judul);
    }
}

/** Pengamat jenis lain: bukan penonton, tetapi boleh ikut berlangganan. */
class PencatatStatistik implements PengamatKanal {
    private int jumlahVideo = 0;

    @Override
    public void perbarui(String namaKanal, String judul) {
        jumlahVideo++;
        System.out.println("  [STATISTIK] " + namaKanal + " sudah mengunggah "
                + jumlahVideo + " video");
    }
}

/** Subject: menyimpan daftar pengamat dan memberi kabar ke semuanya. */
class KanalVideo {
    private String nama;
    private List<PengamatKanal> daftarPengamat = new ArrayList<>(); // [1]

    KanalVideo(String nama) {
        this.nama = nama;
    }

    public void langganan(PengamatKanal pengamat) { // [2]
        daftarPengamat.add(pengamat);
    }

    public void berhentiLangganan(PengamatKanal pengamat) {
        daftarPengamat.remove(pengamat);
    }

    public void unggahVideo(String judul) {
        System.out.println(nama + " mengunggah: " + judul);
        beriKabar(judul); // [3] kejadian -> semua pengamat diberi tahu
    }

    private void beriKabar(String judul) {
        for (PengamatKanal pengamat : daftarPengamat) { // [4] tidak peduli jenisnya
            pengamat.perbarui(nama, judul);
        }
    }
}
