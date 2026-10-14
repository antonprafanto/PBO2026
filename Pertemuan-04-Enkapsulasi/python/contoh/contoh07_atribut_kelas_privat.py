"""
Contoh 07 - Atribut Kelas yang Dilindungi
Pertemuan 04 - Enkapsulasi

Atribut KELAS (milik bersama semua objek) juga perlu dilindungi. Jika siapa
saja bisa mengubah penghitung nomor antrean, nomor tiket bisa kembar.

- Penghitung disimpan di atribut kelas _nomor_terakhir (garis bawah = internal).
- Penghitung hanya dinaikkan oleh konstruktor, SETELAH data dinyatakan valid,
  sehingga tidak ada nomor yang "hangus".
- Dari luar, jumlah tiket dibaca lewat @classmethod jumlah_tiket().

Cara menjalankan:
    python contoh07_atribut_kelas_privat.py
"""


class TiketAntrean:
    """Tiket antrean loket. Nomornya dibuat otomatis dan tidak boleh kembar."""

    _nomor_terakhir = 0  # [1] atribut kelas internal, dipakai bersama semua tiket

    def __init__(self, nama):
        if nama.strip() == "":
            raise ValueError("Nama tidak boleh kosong")
        TiketAntrean._nomor_terakhir += 1  # [2] naik HANYA jika data sudah valid
        self._nomor = TiketAntrean._nomor_terakhir
        self._nama = nama

    @classmethod
    def jumlah_tiket(cls):  # [3] "getter" milik kelas, dipanggil lewat nama kelas
        return cls._nomor_terakhir

    @property
    def nomor(self):  # [4] getter boleh menyajikan data dalam format yang rapi
        return f"A{self._nomor:03d}"

    @property
    def nama(self):
        return self._nama


def main():
    print("=== PENGAMBILAN TIKET ===")
    budi = TiketAntrean("Budi")
    print(f"{budi.nomor} - {budi.nama}")
    siti = TiketAntrean("Siti")
    print(f"{siti.nomor} - {siti.nama}")
    try:
        TiketAntrean("")  # [5] ditolak sebelum penghitung dinaikkan
    except ValueError as e:
        print(f"Ditolak: {e}")
    rina = TiketAntrean("Rina")
    print(f"{rina.nomor} - {rina.nama}")  # tetap A003, tidak ada nomor yang terlewat

    print()
    print(f"Jumlah tiket tercetak: {TiketAntrean.jumlah_tiket()}")  # [6]


if __name__ == "__main__":
    main()
