"""
Contoh 07 - Kapan Dua Objek Dianggap Sama? (__eq__ dan __hash__)
Pertemuan 12 - Koleksi dan Generics

- Tanpa __eq__, dua objek dianggap sama HANYA jika keduanya objek yang
  sama persis (bawaan dari kelas object).
- Dengan __eq__ + __hash__ berdasarkan NIK, dua objek yang NIK-nya sama
  dianggap sama. Akibatnya set bisa membuang data ganda, dan dict bisa
  dicari memakai objek lain yang NIK-nya sama.
- Aturan wajib: objek yang SAMA (==) harus punya hash yang SAMA.

Cara menjalankan:
    python contoh07_kesamaan_objek.py
"""


class PemilihPolos:
    """Versi A: tanpa __eq__ dan __hash__ (memakai bawaan dari object)."""

    def __init__(self, nik: str, nama: str):
        self._nik = nik
        self._nama = nama


class Pemilih:
    """Versi B: dua pemilih dianggap sama jika NIK-nya sama."""

    def __init__(self, nik: str, nama: str):
        self._nik = nik
        self._nama = nama

    @property
    def nik(self) -> str:
        return self._nik

    @property
    def nama(self) -> str:
        return self._nama

    def __eq__(self, lain) -> bool:  # [1] aturan kesamaan: bandingkan NIK
        if not isinstance(lain, Pemilih):
            return NotImplemented
        return self._nik == lain._nik

    def __hash__(self) -> int:  # [2] hash dari data yang SAMA dengan __eq__
        return hash(self._nik)


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    print("=== VERSI A: TANPA ATURAN KESAMAAN ===")
    a1 = PemilihPolos("6472010000000001", "Budi Santoso")
    a2 = PemilihPolos("6472010000000001", "Budi Santoso")  # data sama, diinput ulang
    print(f"Dianggap sama     : {ya_tidak(a1 == a2)}")  # [3]
    print(f"Isi set           : {len({a1, a2})} pemilih")

    print()
    print("=== VERSI B: SAMA JIKA NIK SAMA ===")
    b1 = Pemilih("6472010000000001", "Budi Santoso")
    b2 = Pemilih("6472010000000001", "Budi Santosa")  # salah ketik nama, NIK sama
    b3 = Pemilih("6472010000000002", "Siti Aminah")
    print(f"Dianggap sama     : {ya_tidak(b1 == b2)}")  # [4] memanggil __eq__
    print(f"Objek sama persis : {ya_tidak(b1 is b2)}")
    print(f"Kode hash sama    : {ya_tidak(hash(b1) == hash(b2))}")
    dpt: set[Pemilih] = set()  # DPT = daftar pemilih tetap
    dpt.add(b1)
    dpt.add(b2)  # [5] NIK sudah ada: diabaikan
    dpt.add(b3)
    print(f"Isi set           : {len(dpt)} pemilih")
    for pemilih in sorted(dpt, key=lambda p: p.nik):  # urutkan dulu sebelum dicetak
        print(f"  {pemilih.nik} {pemilih.nama}")

    print()
    print("=== MENCARI DENGAN OBJEK LAIN YANG NIK-NYA SAMA ===")
    tps: dict[Pemilih, str] = {b1: "TPS 05", b3: "TPS 12"}  # [6] objek sebagai kunci
    pencari = Pemilih("6472010000000002", "Siti A.")  # objek baru, NIK milik Siti
    print(f"Terdaftar di DPT  : {ya_tidak(pencari in dpt)}")  # [7]
    print(f"Lokasi TPS        : {tps[pencari]}")


if __name__ == "__main__":
    main()
