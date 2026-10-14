"""
Contoh 01 - Singleton: Satu Objek Konfigurasi untuk Seluruh Program
Pertemuan 14 - Design Pattern Dasar

Pola SINGLETON menjamin sebuah kelas hanya punya SATU objek, dan objek itu
diambil lewat satu pintu yang sama: Konfigurasi.get_instance().

- Atribut kelas _instance menyimpan satu-satunya objek.
- get_instance() membuat objek saat PERTAMA kali diminta (lazy), lalu
  selalu mengembalikan objek yang sama.
- __init__ diberi penjaga yang menolak pembuatan objek kedua.

Cara menjalankan:
    python contoh01_singleton_konfigurasi.py
"""


class Konfigurasi:
    """Pengaturan aplikasi yang harus SAMA di semua bagian program."""

    _instance = None  # [1] atribut kelas: tempat satu-satunya objek

    def __init__(self):
        if Konfigurasi._instance is not None:  # [2] penjaga objek kedua
            raise RuntimeError("Konfigurasi adalah Singleton. "
                               "Gunakan Konfigurasi.get_instance()")
        print("  (objek Konfigurasi dibuat)")
        self._data = {"bahasa": "Indonesia", "tema": "terang"}

    @classmethod
    def get_instance(cls) -> "Konfigurasi":  # [3] satu-satunya pintu masuk
        if cls._instance is None:  # [4] dibuat hanya saat pertama diminta
            cls._instance = cls()
        return cls._instance

    def ambil(self, kunci: str) -> str:
        return self._data[kunci]

    def ubah(self, kunci: str, nilai: str):
        self._data[kunci] = nilai


def halaman_beranda():
    konfigurasi = Konfigurasi.get_instance()  # [5] tanpa parameter tambahan
    print(f"Beranda: bahasa {konfigurasi.ambil('bahasa')}, "
          f"tema {konfigurasi.ambil('tema')}")


def halaman_profil():
    konfigurasi = Konfigurasi.get_instance()
    print(f"Profil : bahasa {konfigurasi.ambil('bahasa')}, "
          f"tema {konfigurasi.ambil('tema')}")


def halaman_pengaturan():
    print("Pengguna memilih tema gelap di halaman Pengaturan")
    Konfigurasi.get_instance().ubah("tema", "gelap")  # [6]


def main():
    print("=== MEMINTA KONFIGURASI DUA KALI ===")
    print("Permintaan pertama:")
    a = Konfigurasi.get_instance()
    print("Permintaan kedua:")
    b = Konfigurasi.get_instance()
    sama = "ya" if a is b else "tidak"  # [7] is: objek yang sama?
    print(f"a dan b objek yang sama? {sama}")

    print()
    print("=== SEMUA HALAMAN MEMBACA PENGATURAN YANG SAMA ===")
    halaman_beranda()
    halaman_profil()

    print()
    print("=== DIUBAH DI SATU TEMPAT, TERLIHAT DI SEMUA TEMPAT ===")
    halaman_pengaturan()
    halaman_beranda()
    halaman_profil()


if __name__ == "__main__":
    main()
