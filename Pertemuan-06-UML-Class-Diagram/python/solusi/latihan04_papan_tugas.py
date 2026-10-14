"""
Solusi Latihan 04 - Dari Diagram ke Kode: Papan Tugas Kelompok
Pertemuan 06 - UML Class Diagram

Ide penyelesaian (baca diagram baris demi baris):
- Proyek "1" *-- "*" Tugas      -> KOMPOSISI: objek Tugas dibuat DI DALAM
                                   tambah_tugas(), lalu disimpan di list.
- Tugas "*" --> "0..1" Anggota  -> ASOSIASI 0..1: atribut _penanggung_jawab
                                   bernilai None sampai tugas ditugaskan.
- -cari(nomor) Tugas [0..1]     -> method PRIVAT pembantu (_cari), boleh
                                   mengembalikan None.
- +progres() int                -> persen bilangan bulat:
                                   jumlah_selesai * 100 // jumlah_tugas.
- Getter di diagram (getNomor, getNama) ditulis sebagai property di Python.

Cara menjalankan:
    python latihan04_papan_tugas.py
"""


class Anggota:
    """Anggota kelompok."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama


class Tugas:
    """Satu tugas di papan. Boleh belum punya penanggung jawab."""

    def __init__(self, nomor: int, judul: str):
        self._nomor = nomor
        self._judul = judul
        self._selesai = False
        self._penanggung_jawab: Anggota | None = None  # multiplisitas 0..1

    @property
    def nomor(self) -> int:
        return self._nomor

    def tugaskan_ke(self, anggota: Anggota):
        self._penanggung_jawab = anggota

    def tandai_selesai(self):
        self._selesai = True

    def sudah_selesai(self) -> bool:
        return self._selesai

    def baris(self) -> str:
        if self._penanggung_jawab is None:
            pj = "-"
        else:
            pj = self._penanggung_jawab.nama
        if self._selesai:
            status = "SELESAI"
        else:
            status = "proses"
        return f"[{self._nomor}] {self._judul:<26}{pj:<8}{status}"


class Proyek:
    """Proyek kelompok yang tersusun atas tugas-tugas."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_tugas: list[Tugas] = []

    def tambah_tugas(self, judul: str):
        nomor = len(self._daftar_tugas) + 1
        self._daftar_tugas.append(Tugas(nomor, judul))  # komposisi: dibuat di sini

    def _cari(self, nomor: int) -> Tugas | None:
        for tugas in self._daftar_tugas:
            if tugas.nomor == nomor:
                return tugas
        return None

    def tugaskan(self, nomor: int, anggota: Anggota):
        tugas = self._cari(nomor)
        if tugas is None:
            print(f"Tugas nomor {nomor} tidak ada")
        else:
            tugas.tugaskan_ke(anggota)

    def selesaikan(self, nomor: int):
        tugas = self._cari(nomor)
        if tugas is None:
            print(f"Tugas nomor {nomor} tidak ada")
        else:
            tugas.tandai_selesai()

    def progres(self) -> int:
        if not self._daftar_tugas:
            return 0
        jumlah_selesai = 0
        for tugas in self._daftar_tugas:
            if tugas.sudah_selesai():
                jumlah_selesai += 1
        return jumlah_selesai * 100 // len(self._daftar_tugas)

    def cetak_papan(self):
        print(f"=== PAPAN TUGAS: {self._nama} ===")
        for tugas in self._daftar_tugas:
            print(tugas.baris())
        print(f"Progres: {self.progres()}%")


def main():
    ayu = Anggota("Ayu")
    bima = Anggota("Bima")

    proyek = Proyek("Aplikasi Kasir")
    proyek.tambah_tugas("Gambar diagram kelas")
    proyek.tambah_tugas("Tulis kelas Menu")
    proyek.tambah_tugas("Tulis kelas Pesanan")
    proyek.tambah_tugas("Uji semua fitur")

    proyek.tugaskan(1, ayu)
    proyek.tugaskan(2, bima)
    proyek.selesaikan(1)
    proyek.cetak_papan()

    print()
    proyek.tugaskan(3, ayu)
    proyek.selesaikan(2)
    proyek.selesaikan(3)
    proyek.tugaskan(9, bima)
    proyek.cetak_papan()


if __name__ == "__main__":
    main()
