"""
============================================================
    MATERI 03 — Atribut dan Method
    File: 02_classmethod.py
    Topik: @classmethod — Cara Kerja dan Kegunaannya
============================================================
"""

# ─────────────────────────────────────────────────────────
# BAGIAN 1: Dasar @classmethod
# Parameter pertama: cls (kelas itu sendiri, bukan objek)
# Bisa akses & ubah atribut KELAS
# ─────────────────────────────────────────────────────────

print("=" * 55)
print("  1. DASAR @classmethod")
print("=" * 55)


class Server:
    nama_aplikasi = "SiDigital"
    versi         = "1.0.0"
    mode          = "production"

    def __init__(self, host, port):
        self.host = host
        self.port = port

    # Instance method biasa
    def alamat(self):
        return f"{self.host}:{self.port}"

    # Class method — akses atribut kelas via cls
    @classmethod
    def info_aplikasi(cls):
        print(f"Aplikasi : {cls.nama_aplikasi} v{cls.versi}")
        print(f"Mode     : {cls.mode}")

    @classmethod
    def ubah_mode(cls, mode_baru):
        cls.mode = mode_baru
        print(f"Mode diubah ke: {cls.mode}")


server1 = Server("localhost", 8000)
server2 = Server("192.168.1.100", 80)

print(f"Alamat server1: {server1.alamat()}")
print(f"Alamat server2: {server2.alamat()}")

Server.info_aplikasi()

Server.ubah_mode("development")
Server.info_aplikasi()


# ─────────────────────────────────────────────────────────
# BAGIAN 2: Factory Method — Kegunaan Utama @classmethod
# Cara alternatif membuat objek dari format data berbeda
# ─────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("  2. FACTORY METHOD")
print("=" * 55)


class Mahasiswa:
    universitas = "Universitas Mulawarman"

    def __init__(self, nama, nim, semester, ipk):
        self.nama     = nama
        self.nim      = nim
        self.semester = semester
        self.ipk      = ipk

    # ── Factory Methods ───────────────────────────────────
    @classmethod
    def dari_csv(cls, baris):
        """Buat Mahasiswa dari baris CSV: 'nama,nim,semester,ipk'"""
        nama, nim, semester, ipk = baris.split(",")
        return cls(nama.strip(), nim.strip(), int(semester), float(ipk))

    @classmethod
    def dari_dict(cls, data: dict):
        """Buat Mahasiswa dari dictionary."""
        return cls(
            data["nama"],
            data["nim"],
            data.get("semester", 1),
            data.get("ipk", 0.0)
        )

    @classmethod
    def mahasiswa_baru(cls, nama, nim):
        """Buat mahasiswa baru: semester 1, IPK 0.0."""
        return cls(nama, nim, semester=1, ipk=0.0)

    def info(self):
        print(f"  [{self.nim}] {self.nama:<20} | Sem {self.semester} | IPK {self.ipk:.2f}")


# Cara 1: Konstruktor biasa
mhs1 = Mahasiswa("Andi Wijaya", "2301001", 5, 3.80)

# Cara 2: dari CSV
mhs2 = Mahasiswa.dari_csv("Budi Santoso, 2301002, 3, 3.75")

# Cara 3: dari dictionary (misal dari JSON / database)
data_json = {"nama": "Citra Dewi", "nim": "2301003", "semester": 4, "ipk": 3.65}
mhs3 = Mahasiswa.dari_dict(data_json)

# Cara 4: mahasiswa baru (satu baris, tanpa parameter semester & ipk)
mhs4 = Mahasiswa.mahasiswa_baru("Deni Kurniawan", "2301004")

print("Daftar Mahasiswa:")
for m in [mhs1, mhs2, mhs3, mhs4]:
    m.info()


# ─────────────────────────────────────────────────────────
# BAGIAN 3: @classmethod pada Hierarki Kelas
# cls mengacu ke kelas yang MEMANGGIL method, bukan kelas induk
# (manfaat ini sangat terasa saat ada Pewarisan — Materi 06)
# ─────────────────────────────────────────────────────────

print("\n" + "=" * 55)
print("  3. @classmethod pada Hierarki (preview Inheritance)")
print("=" * 55)


class Kendaraan:
    jenis = "Kendaraan Umum"

    def __init__(self, merk, tahun):
        self.merk  = merk
        self.tahun = tahun

    @classmethod
    def buat_default(cls):
        """Factory: buat kendaraan dengan nilai default."""
        return cls("Unknown", 2020)   # cls -> Mobil/Motor jika dipanggil dari sana

    def info(self):
        print(f"  [{self.__class__.jenis}] {self.merk} ({self.tahun})")


class Mobil(Kendaraan):
    jenis = "Mobil"


class Motor(Kendaraan):
    jenis = "Motor"


# Karena cls dinamis, buat_default() di subclass mengembalikan tipe yang benar
m_default = Mobil.buat_default()    # -> cls = Mobil
k_default = Motor.buat_default()    # -> cls = Motor

m_default.info()   # [Mobil] Unknown (2020)
k_default.info()   # [Motor] Unknown (2020)

mobil = Mobil("Toyota", 2023)
motor = Motor("Honda",  2024)
mobil.info()   # [Mobil] Toyota (2023)
motor.info()   # [Motor] Honda (2024)


print("\n[OK] Selesai: 02_classmethod.py")
