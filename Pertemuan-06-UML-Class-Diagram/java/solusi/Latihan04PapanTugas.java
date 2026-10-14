/*
 * Solusi Latihan 04 - Dari Diagram ke Kode: Papan Tugas Kelompok
 * Pertemuan 06 - UML Class Diagram
 *
 * Ide penyelesaian (baca diagram baris demi baris):
 * - Proyek "1" *-- "*" Tugas      -> KOMPOSISI: objek Tugas dibuat DI DALAM
 *                                    tambahTugas(), lalu disimpan di List.
 * - Tugas "*" --> "0..1" Anggota  -> ASOSIASI 0..1: field penanggungJawab
 *                                    bernilai null sampai tugas ditugaskan.
 * - -cari(nomor) Tugas [0..1]     -> method PRIVATE pembantu, boleh
 *                                    mengembalikan null.
 * - +progres() int                -> persen bilangan bulat:
 *                                    jumlahSelesai * 100 / jumlahTugas.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04PapanTugas.java
 */

import java.util.ArrayList;
import java.util.List;

public class Latihan04PapanTugas {

    public static void main(String[] args) {
        Anggota ayu = new Anggota("Ayu");
        Anggota bima = new Anggota("Bima");

        Proyek proyek = new Proyek("Aplikasi Kasir");
        proyek.tambahTugas("Gambar diagram kelas");
        proyek.tambahTugas("Tulis kelas Menu");
        proyek.tambahTugas("Tulis kelas Pesanan");
        proyek.tambahTugas("Uji semua fitur");

        proyek.tugaskan(1, ayu);
        proyek.tugaskan(2, bima);
        proyek.selesaikan(1);
        proyek.cetakPapan();

        System.out.println();
        proyek.tugaskan(3, ayu);
        proyek.selesaikan(2);
        proyek.selesaikan(3);
        proyek.tugaskan(9, bima);
        proyek.cetakPapan();
    }
}

/** Anggota kelompok. */
class Anggota {
    private String nama;

    public Anggota(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }
}

/** Satu tugas di papan. Boleh belum punya penanggung jawab. */
class Tugas {
    private int nomor;
    private String judul;
    private boolean selesai;
    private Anggota penanggungJawab; // multiplisitas 0..1: boleh null

    public Tugas(int nomor, String judul) {
        this.nomor = nomor;
        this.judul = judul;
        this.selesai = false;
        this.penanggungJawab = null;
    }

    public int getNomor() {
        return nomor;
    }

    public void tugaskanKe(Anggota anggota) {
        this.penanggungJawab = anggota;
    }

    public void tandaiSelesai() {
        this.selesai = true;
    }

    public boolean sudahSelesai() {
        return selesai;
    }

    public String baris() {
        String pj;
        if (penanggungJawab == null) {
            pj = "-";
        } else {
            pj = penanggungJawab.getNama();
        }
        String status;
        if (selesai) {
            status = "SELESAI";
        } else {
            status = "proses";
        }
        return "[" + nomor + "] " + String.format("%-26s%-8s", judul, pj) + status;
    }
}

/** Proyek kelompok yang tersusun atas tugas-tugas. */
class Proyek {
    private String nama;
    private List<Tugas> daftarTugas;

    public Proyek(String nama) {
        this.nama = nama;
        this.daftarTugas = new ArrayList<>();
    }

    public void tambahTugas(String judul) {
        int nomor = daftarTugas.size() + 1;
        daftarTugas.add(new Tugas(nomor, judul)); // komposisi: dibuat di sini
    }

    private Tugas cari(int nomor) {
        for (Tugas tugas : daftarTugas) {
            if (tugas.getNomor() == nomor) {
                return tugas;
            }
        }
        return null;
    }

    public void tugaskan(int nomor, Anggota anggota) {
        Tugas tugas = cari(nomor);
        if (tugas == null) {
            System.out.println("Tugas nomor " + nomor + " tidak ada");
        } else {
            tugas.tugaskanKe(anggota);
        }
    }

    public void selesaikan(int nomor) {
        Tugas tugas = cari(nomor);
        if (tugas == null) {
            System.out.println("Tugas nomor " + nomor + " tidak ada");
        } else {
            tugas.tandaiSelesai();
        }
    }

    public int progres() {
        if (daftarTugas.isEmpty()) {
            return 0;
        }
        int jumlahSelesai = 0;
        for (Tugas tugas : daftarTugas) {
            if (tugas.sudahSelesai()) {
                jumlahSelesai++;
            }
        }
        return jumlahSelesai * 100 / daftarTugas.size();
    }

    public void cetakPapan() {
        System.out.println("=== PAPAN TUGAS: " + nama + " ===");
        for (Tugas tugas : daftarTugas) {
            System.out.println(tugas.baris());
        }
        System.out.println("Progres: " + progres() + "%");
    }
}
