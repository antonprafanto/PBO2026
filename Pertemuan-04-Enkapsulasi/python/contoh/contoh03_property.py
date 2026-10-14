"""
Contoh 03 - Property: Getter dan Setter ala Python
Pertemuan 04 - Enkapsulasi

- @property mengubah method menjadi "atribut" yang bisa DIBACA (getter).
- @volume.setter membuat method yang otomatis dijalankan saat atribut
  DIISI (setter). Di sinilah data diperiksa sebelum disimpan.
- Data yang tidak valid ditolak dengan raise ValueError(...).
- try/except hanya kita intip sekilas untuk menangkap penolakan tersebut
  (bahasan lengkapnya di Pertemuan 11).

Cara menjalankan:
    python contoh03_property.py
"""


class Televisi:
    """Televisi dengan volume 0 sampai 100."""

    def __init__(self, merek):
        self._merek = merek
        self._volume = 10  # volume awal setiap TV baru

    @property
    def merek(self):  # [1] getter: dijalankan saat kita MEMBACA tv.merek
        return self._merek

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, nilai):  # [2] setter: dijalankan saat kita MENGISI tv.volume
        if nilai < 0 or nilai > 100:
            raise ValueError(f"Volume harus 0-100, bukan {nilai}")  # [3] tolak!
        self._volume = nilai  # [4] simpan ke atribut internal (bergaris bawah)


def main():
    tv = Televisi("Polytron")
    print("=== TV BARU DINYALAKAN ===")
    print(f"Merek : {tv.merek}")  # [5] dibaca seperti atribut, tanpa tanda kurung
    print(f"Volume: {tv.volume}")

    print()
    print("=== MENGATUR VOLUME ===")
    tv.volume = 25  # [6] terlihat seperti mengisi atribut, padahal setter yang bekerja
    print(f"Volume diatur ke 25, sekarang {tv.volume}")
    tv.volume += 10  # [7] getter membaca 25, lalu setter menyimpan 35
    print(f"Volume dinaikkan 10, sekarang {tv.volume}")

    print()
    print("=== DATA TIDAK VALID DITOLAK ===")
    try:  # [8] intip sekilas: "coba jalankan; jika ditolak, tangkap"
        tv.volume = 150
        print("Baris ini tidak pernah tercetak")
    except ValueError as e:
        print(f"Ditolak: {e}")
    print(f"Volume tetap {tv.volume}")


if __name__ == "__main__":
    main()
