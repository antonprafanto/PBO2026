"""
============================================================
    MATERI 04 - Enkapsulasi
    File: 01_akses_modifier.py
    Topik: Public, Protected, Private & Name Mangling
============================================================
"""

print("=" * 58)
print("  MATERI 04 - Enkapsulasi")
print("  01_akses_modifier.py")
print("=" * 58)


# ------------------------------------------------------------
# BAGIAN 1: Tiga Tingkat Akses
# ------------------------------------------------------------

print("\n--- 1. Tiga Tingkat Akses ---")


class KaryawanInfo:
    """Demonstrasi tiga tingkat akses di Python."""

    perusahaan = "PT Nusantara Digital"   # atribut kelas (public)

    def __init__(self, nama, departemen, gaji, pin_akses):
        # PUBLIC  : diakses bebas dari mana saja
        self.nama        = nama
        self.departemen  = departemen

        # PROTECTED: konvensi "hanya internal & subkelas"
        self._gaji       = gaji

        # PRIVATE  : name mangling — _KaryawanInfo__pin_akses
        self.__pin_akses = pin_akses

    def info_publik(self):
        """Informasi yang boleh dilihat semua orang."""
        return f"{self.nama} | {self.departemen}"

    def info_internal(self):
        """Informasi yang hanya digunakan secara internal."""
        return f"{self.nama} | Gaji: Rp {self._gaji:,.0f}"

    def verifikasi_pin(self, pin):
        """Cara yang benar mengakses data private."""
        return self.__pin_akses == pin


k = KaryawanInfo("Anton Prafanto", "Engineering", 12_000_000, "1234")

# Public — akses bebas
print(f"Nama      : {k.nama}")
print(f"Departemen: {k.departemen}")
print(f"Info publik: {k.info_publik()}")

# Protected — bisa, tapi melanggar konvensi
print(f"\n[Protected] _gaji = {k._gaji:,.0f}  <- bisa, tapi jangan!")

# Private — tidak bisa langsung
try:
    print(k.__pin_akses)
except AttributeError as e:
    print(f"\n[Private] akses langsung __pin_akses: AttributeError! -> {e}")

# Cara yang BENAR: gunakan method yang disediakan kelas
print(f"\nVerifikasi PIN '1234': {k.verifikasi_pin('1234')}")   # True
print(f"Verifikasi PIN '9999': {k.verifikasi_pin('9999')}")   # False


# ------------------------------------------------------------
# BAGIAN 2: Name Mangling — Melihat di Balik Layar
# ------------------------------------------------------------

print("\n--- 2. Name Mangling ---")


class AkunBank:
    def __init__(self, pemilik, saldo, pin):
        self.pemilik  = pemilik       # public
        self._saldo   = saldo         # protected
        self.__pin    = pin           # private → _AkunBank__pin

    def info(self):
        return f"{self.pemilik} | Saldo: Rp {self._saldo:,.0f}"


akun = AkunBank("Budi", 5_000_000, "4321")

# Lihat semua atribut objek
print("Atribut objek (via __dict__):")
for k_attr, v_attr in akun.__dict__.items():
    print(f"  {k_attr!r:30} = {v_attr!r}")

# Name mangling: __pin tersimpan sebagai _AkunBank__pin
print(f"\nAkses via name mangling : {akun._AkunBank__pin}")  # 4321
print("(Ini adalah jalan darurat - JANGAN gunakan dalam kode nyata!)")


# ------------------------------------------------------------
# BAGIAN 3: Protected di Konteks Pewarisan
# Protected masuk akal diakses oleh SUBKELAS
# ------------------------------------------------------------

print("\n--- 3. Protected dalam Pewarisan ---")


class Kendaraan:
    def __init__(self, merk, tahun, harga_dasar):
        self.merk         = merk      # public
        self.tahun        = tahun     # public
        self._harga_dasar = harga_dasar  # protected — subkelas perlu ini

    def info(self):
        return f"{self.merk} ({self.tahun})"


class Mobil(Kendaraan):
    def __init__(self, merk, tahun, harga_dasar, tipe):
        super().__init__(merk, tahun, harga_dasar)
        self.tipe = tipe

    def harga_jual(self, diskon_persen=0):
        """Subkelas mengakses _harga_dasar dari induknya — ini wajar."""
        diskon = self._harga_dasar * diskon_persen / 100
        return self._harga_dasar - diskon

    def info(self):
        return f"{super().info()} [{self.tipe}] | Rp {self.harga_jual():,.0f}"


class Motor(Kendaraan):
    def __init__(self, merk, tahun, harga_dasar, cc):
        super().__init__(merk, tahun, harga_dasar)
        self.cc = cc

    def harga_jual(self, diskon_persen=0):
        diskon = self._harga_dasar * diskon_persen / 100
        return self._harga_dasar - diskon


mobil = Mobil("Toyota Avanza", 2024, 280_000_000, "Manual")
motor = Motor("Honda Vario",   2024,  25_000_000, 150)

print(mobil.info())
print(f"Harga setelah diskon 10%: Rp {mobil.harga_jual(diskon_persen=10):,.0f}")
print(f"Motor harga jual: Rp {motor.harga_jual():,.0f}")


# ------------------------------------------------------------
# BAGIAN 4: Private mencegah Konflik Nama di Pewarisan
# ------------------------------------------------------------

print("\n--- 4. Private mencegah Konflik di Pewarisan ---")


class Induk:
    def __init__(self):
        self.__data = "data milik Induk"   # _Induk__data

    def info(self):
        return f"Induk.__data = '{self.__data}'"


class Anak(Induk):
    def __init__(self):
        super().__init__()
        self.__data = "data milik Anak"    # _Anak__data — BERBEDA, tidak konflik!

    def info_anak(self):
        return f"Anak.__data  = '{self.__data}'"


obj = Anak()
print(obj.info())         # Induk: 'data milik Induk'
print(obj.info_anak())    # Anak:  'data milik Anak'
print("Keduanya independen — tidak saling menimpa berkat name mangling!")
print(f"Atribut di memory: {list(obj.__dict__.keys())}")


print("\n[OK] Selesai: 01_akses_modifier.py")
