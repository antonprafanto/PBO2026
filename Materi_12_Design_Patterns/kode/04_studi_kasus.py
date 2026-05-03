"""
Kode Praktik - Materi 12: Pola Desain (Design Patterns)
File: 04_studi_kasus.py
Topik: Sistem akademik dengan multiple patterns

Jalankan: python 04_studi_kasus.py
"""

from abc import ABC, abstractmethod

# ======================================================================
# STUDI KASUS: Sistem Akademik Kompleks dengan Patterns
# ======================================================================
print("=" * 60)
print("STUDI KASUS: Sistem Akademik dengan Multiple Patterns")
print("=" * 60)

# ===== Singleton: Hanya satu Logger untuk seluruh sistem =====

def singleton(cls):
    """Decorator untuk singleton."""
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    """[SINGLETON] Hanya satu logger instance."""
    def __init__(self):
        self.logs = []
    
    def log(self, message):
        self.logs.append(message)
        print(f"  [LOG] {message}")

# ===== Factory: Create different notification types =====

class Notifikasi(ABC):
    @abstractmethod
    def kirim(self, pesan):
        pass

class NotifikasiEmail(Notifikasi):
    def kirim(self, pesan):
        return f"Email: {pesan}"

class NotifikasiSMS(Notifikasi):
    def kirim(self, pesan):
        return f"SMS: {pesan}"

class NotifikasiFactory:
    """[FACTORY] Centralize notifikasi creation."""
    @staticmethod
    def create(tipe):
        if tipe == "email":
            return NotifikasiEmail()
        elif tipe == "sms":
            return NotifikasiSMS()
        else:
            raise ValueError(f"Unknown type: {tipe}")

# ===== Observer: Event-driven notifikasi =====

class Subject:
    """[OBSERVER] Subject untuk emit events."""
    def __init__(self):
        self._observers = []
    
    def subscribe(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

class Observer(ABC):
    @abstractmethod
    def update(self, event):
        pass

class NotifikasiObserver(Observer):
    """[OBSERVER] Listen ke events dan kirim notifikasi."""
    def __init__(self, channel):
        self.channel = channel
        self.logger = Logger()  # Singleton logger
    
    def update(self, event):
        notif = NotifikasiFactory.create(self.channel)  # Factory
        message = notif.kirim(event.get("message", ""))
        self.logger.log(f"Notifikasi {self.channel}: {message}")

# ===== Decorator: MataKuliah dengan optional features =====

class MataKuliah:
    """[DECORATOR] Core matakuliah."""
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks
    
    def harga(self):
        return self.sks * 100_000
    
    def deskripsi(self):
        return f"{self.kode} | {self.nama} ({self.sks} SKS)"

class MataKuliahDecorator(MataKuliah):
    """[DECORATOR] Base decorator."""
    def __init__(self, matkul):
        self.matkul = matkul
    
    def harga(self):
        return self.matkul.harga()
    
    def deskripsi(self):
        return self.matkul.deskripsi()
    
    def __getattr__(self, name):
        return getattr(self.matkul, name)

class DenganPraktik(MataKuliahDecorator):
    """[DECORATOR] Add praktik."""
    def harga(self):
        return super().harga() + 200_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Praktik"

class DenganLab(MataKuliahDecorator):
    """[DECORATOR] Add lab."""
    def harga(self):
        return super().harga() + 300_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Lab"

# ===== Sistem Akademik Lengkap =====

class Mahasiswa(Subject):
    """[OBSERVER SUBJECT] Mahasiswa yang emit events."""
    def __init__(self, nim, nama):
        super().__init__()
        self.nim = nim
        self.nama = nama
        self.nilai = {}
        self.logger = Logger()  # Singleton logger
    
    def input_nilai(self, kode_mk, nilai):
        """Input nilai -- emit event untuk observers."""
        self.nilai[kode_mk] = nilai
        self.notify({
            "tipe": "nilai_input",
            "nim": self.nim,
            "nama": self.nama,
            "kode_mk": kode_mk,
            "nilai": nilai,
            "message": f"Nilai {self.nama} untuk {kode_mk} = {nilai}"
        })
        self.logger.log(f"Nilai input: {self.nama} ({kode_mk}) = {nilai}")

class SistemAkademik:
    """[FACADE] Main sistem akademik -- use semua patterns."""
    def __init__(self):
        self.logger = Logger()  # Singleton
        self.mahasiswa_dict = {}
        self.matakuliah_dict = {}
    
    def register_mahasiswa(self, nim, nama):
        mhs = Mahasiswa(nim, nama)
        self.mahasiswa_dict[nim] = mhs
        self.logger.log(f"Mahasiswa registered: {nama}")
        return mhs
    
    def create_matakuliah(self, kode, nama, sks, features=None):
        """Factory untuk matakuliah dengan optional features."""
        mk = MataKuliah(kode, nama, sks)
        
        if features:
            for feature in features:
                if feature == "praktik":
                    mk = DenganPraktik(mk)
                elif feature == "lab":
                    mk = DenganLab(mk)
        
        self.matakuliah_dict[kode] = mk
        self.logger.log(f"MataKuliah created: {mk.deskripsi()}")
        return mk
    
    def subscribe_notification(self, nim, channel):
        """Subscribe mahasiswa ke channel notifikasi."""
        mhs = self.mahasiswa_dict.get(nim)
        if mhs:
            observer = NotifikasiObserver(channel)
            mhs.subscribe(observer)
            self.logger.log(f"Notifikasi {channel} subscribed untuk {nim}")
    
    def input_nilai_mahasiswa(self, nim, kode_mk, nilai):
        """Input nilai -- trigger observer notifications."""
        mhs = self.mahasiswa_dict.get(nim)
        if mhs:
            mhs.input_nilai(kode_mk, nilai)

# ===== Demo =====

print("\n-- Setup sistem akademik --")
sistem = SistemAkademik()

# Register mahasiswa
print("\n-- Register mahasiswa --")
mhs1 = sistem.register_mahasiswa("2301001", "Budi Santoso")
mhs2 = sistem.register_mahasiswa("2301042", "Sari Dewi")

# Create matakuliah dengan optional features
print("\n-- Create matakuliah --")
mk1 = sistem.create_matakuliah("IF204", "Pemrograman Python", 3, ["praktik"])
mk2 = sistem.create_matakuliah("IF301", "Keamanan Informasi", 4, ["praktik", "lab"])

# Subscribe notifikasi
print("\n-- Subscribe notifikasi --")
sistem.subscribe_notification("2301001", "email")
sistem.subscribe_notification("2301001", "sms")
sistem.subscribe_notification("2301042", "email")

# Input nilai -- trigger observer notifications
print("\n-- Input nilai (trigger observers) --")
sistem.input_nilai_mahasiswa("2301001", "IF204", 85)
sistem.input_nilai_mahasiswa("2301042", "IF301", 92)

# Check harga matakuliah
print("\n-- Harga matakuliah dengan decorator features --")
print(f"  {mk1.deskripsi()}: Rp {mk1.harga()}")
print(f"  {mk2.deskripsi()}: Rp {mk2.harga()}")

# Singleton logger
print("\n-- Semua aktivitas logged di singleton logger --")
logger = Logger()
print(f"  Total logs: {len(logger.logs)}")

print()
print("Studi kasus selesai!")
print("Patterns used:")
print("  - Singleton: Logger")
print("  - Factory: NotifikasiFactory")
print("  - Observer: Mahasiswa (subject) + NotifikasiObserver")
print("  - Decorator: MataKuliah dengan DenganPraktik + DenganLab")
