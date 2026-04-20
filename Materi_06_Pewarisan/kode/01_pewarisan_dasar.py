"""
Kode Praktik - Materi 06: Pewarisan (Inheritance)
File: 01_pewarisan_dasar.py
Topik: Sintaks dasar, super(), dan method overriding

Jalankan: python 01_pewarisan_dasar.py
"""

# ======================================================================
# BAGIAN 1: Hierarki Pengguna -> Mahasiswa / Dosen
#           Fokus: super() dan override __str__
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Hierarki Pengguna -> Mahasiswa / Dosen")
print("=" * 60)

class Pengguna:
    """Kelas dasar untuk semua civitas akademika."""
    _counter = 0

    def __init__(self, nama, email):
        Pengguna._counter += 1
        self.id     = f"USR-{Pengguna._counter:04d}"
        self.nama   = nama.strip().title()
        self.email  = email.lower()
        self._aktif = True

    def login(self):
        print(f"  [OK] {self.nama} ({self.id}) berhasil login.")

    def logout(self):
        print(f"  [--] {self.nama} logout.")

    def __str__(self):
        status = "Aktif" if self._aktif else "Nonaktif"
        return f"[{self.id}] {self.nama} <{self.email}> [{status}]"


class Mahasiswa(Pengguna):
    """Mahasiswa mewarisi Pengguna dan menambah atribut akademik."""
    def __init__(self, nama, email, nim, prodi):
        super().__init__(nama, email)   # <- panggil __init__ Pengguna
        self.nim   = nim
        self.prodi = prodi
        self._ipk  = 0.0

    @property
    def ipk(self):
        return self._ipk

    @ipk.setter
    def ipk(self, nilai):
        if not (0.0 <= nilai <= 4.0):
            raise ValueError(f"IPK tidak valid: {nilai}")
        self._ipk = round(nilai, 2)

    @property
    def predikat(self):
        if self._ipk >= 3.51: return "Cum Laude"
        if self._ipk >= 3.01: return "Sangat Memuaskan"
        if self._ipk >= 2.76: return "Memuaskan"
        return "Cukup"

    def daftar_krs(self, matkul_list):
        print(f"  [{self.nim}] KRS {self.nama}:")
        for mk in matkul_list:
            print(f"    - {mk}")

    def __str__(self):
        # super().__str__() memanggil __str__ milik Pengguna
        return (f"Mahasiswa | {super().__str__()} | "
                f"NIM: {self.nim} | IPK: {self._ipk:.2f} ({self.predikat})")


class Dosen(Pengguna):
    """Dosen mewarisi Pengguna dan menambah data kepegawaian."""
    def __init__(self, nama, email, nip, jabatan="Asisten Ahli"):
        super().__init__(nama, email)
        self.nip     = nip
        self.jabatan = jabatan
        self._matkul = []

    def tambah_matkul(self, matkul):
        self._matkul.append(matkul)
        print(f"  [+] {self.nama} ditugaskan: {matkul}")

    def ajar(self, matkul, ruangan):
        print(f"  [~] {self.nama} mengajar '{matkul}' di {ruangan}")

    def __str__(self):
        return (f"Dosen | {super().__str__()} | "
                f"NIP: {self.nip} | {self.jabatan}")


# Demo Bagian 1
mhs = Mahasiswa("budi santoso", "budi@unmul.ac.id", "2301001", "Informatika")
mhs.ipk = 3.85
mhs.login()                                   # method DIWARISI dari Pengguna
mhs.daftar_krs(["PBO", "Basis Data"])

dos = Dosen("dr. anton", "anton@unmul.ac.id", "NIP001", "Lektor")
dos.tambah_matkul("PBO")
dos.ajar("PBO", "Lab 2")

print()
print(mhs)
print(dos)
print(f"\nTotal pengguna dibuat: {Pengguna._counter}")


# ======================================================================
# BAGIAN 2: Hierarki Hewan - Method Overriding
#           Satu perintah (info()), banyak bentuk respons
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: Hierarki Hewan - Method Overriding")
print("=" * 60)

class Hewan:
    def __init__(self, nama, jenis):
        self.nama  = nama
        self.jenis = jenis

    def suara(self):
        """Method induk - akan di-override oleh anak."""
        return "[diam]"

    def gerak(self):
        """Method induk - bisa di-override."""
        return "bergerak"

    def info(self):
        """Method induk - menggunakan suara() dan gerak() yang ter-override."""
        print(f"  {self.jenis}: {self.nama}")
        print(f"    Suara : {self.suara()}")
        print(f"    Gerak : {self.gerak()}")


class Anjing(Hewan):
    def __init__(self, nama, ras):
        super().__init__(nama, "Anjing")
        self.ras = ras

    def suara(self):
        return "Guk! Guk!"

    def gerak(self):
        return "berlari dengan 4 kaki"

    def info(self):
        super().info()                        # jalankan info() milik Hewan dulu
        print(f"    Ras   : {self.ras}")      # tambahkan baris extra


class Kucing(Hewan):
    def __init__(self, nama):
        super().__init__(nama, "Kucing")

    def suara(self):
        return "Meow~"

    def gerak(self):
        return "berjalan anggun"


class Ikan(Hewan):
    def __init__(self, nama, spesies):
        super().__init__(nama, "Ikan")
        self.spesies = spesies

    def suara(self):
        return "... (diam di bawah air)"

    def gerak(self):
        return "berenang dengan sirip"

    def info(self):
        super().info()
        print(f"    Spesies: {self.spesies}")


# Karena semua punya method info(), kita bisa loop tanpa tahu tipe persisnya
hewan_list = [
    Anjing("Rex",   "German Shepherd"),
    Kucing("Kitty"),
    Ikan("Nemo",    "Clownfish"),
    Anjing("Buddy", "Labrador"),
]

print("\n  Daftar Hewan:")
for h in hewan_list:
    h.info()
    print()


# ======================================================================
# BAGIAN 3: Hierarki Karyawan - Override + super() untuk Perluas
# ======================================================================
print("=" * 60)
print("BAGIAN 3: Karyawan -> Manajer -> Direktur")
print("=" * 60)

class Karyawan:
    def __init__(self, nama, nip, gaji_pokok):
        self.nama       = nama
        self.nip        = nip
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

    def info(self):
        print(f"\n  [{self.nip}] {self.nama}")
        print(f"    Gaji Pokok: Rp {self.gaji_pokok:>12,.0f}")


class Manajer(Karyawan):
    def __init__(self, nama, nip, gaji_pokok, bonus, jumlah_bawahan=0):
        super().__init__(nama, nip, gaji_pokok)
        self.bonus          = bonus
        self.jumlah_bawahan = jumlah_bawahan

    def hitung_gaji(self):
        return super().hitung_gaji() + self.bonus   # perluas induk

    def info(self):
        super().info()                              # panggil info() milik induk
        print(f"    Jabatan   : Manajer")
        print(f"    Bonus     : Rp {self.bonus:>12,.0f}")
        print(f"    Bawahan   : {self.jumlah_bawahan} orang")


class Direktur(Manajer):
    def __init__(self, nama, nip, gaji_pokok, bonus, tunjangan, divisi):
        super().__init__(nama, nip, gaji_pokok, bonus)
        self.tunjangan = tunjangan
        self.divisi    = divisi

    def hitung_gaji(self):
        return super().hitung_gaji() + self.tunjangan   # perluas Manajer

    def info(self):
        # Memanggil info() tidak di-super dari Manajer agar Direktur 
        # tidak mencetak 'Jabatan : Manajer'. 
        # Ini mencontohkan kapan kita TIDAK memakai super() jika tidak cocok.
        print(f"\n  [{self.nip}] {self.nama}")
        print(f"    Gaji Pokok: Rp {self.gaji_pokok:>12,.0f}")
        print(f"    Bonus     : Rp {self.bonus:>12,.0f}")
        print(f"    Jabatan   : Direktur")
        print(f"    Tunjangan : Rp {self.tunjangan:>12,.0f}")
        print(f"    Divisi    : {self.divisi}")


k = Karyawan("Andi",  "K001", 5_000_000)
m = Manajer( "Budi",  "M001", 10_000_000, 3_000_000, 8)
d = Direktur("Citra", "D001", 20_000_000, 8_000_000, 5_000_000, "Teknologi")

for pegawai in [k, m, d]:
    pegawai.info()
    print(f"    Total Gaji: Rp {pegawai.hitung_gaji():>12,.0f}")

print()
