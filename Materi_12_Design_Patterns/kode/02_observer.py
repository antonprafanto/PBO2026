"""
Kode Praktik - Materi 12: Pola Desain (Design Patterns)
File: 02_observer.py
Topik: Observer Pattern

Jalankan: python 02_observer.py
"""

# ======================================================================
# BAGIAN 1: Observer Pattern
#           Fokus: Event-driven, loosely coupled communication
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Observer Pattern")
print("=" * 60)

# --- Anti-pattern: Tight coupling ---
print("\n-- Demo Anti-Pattern: Hardcoded dependencies --")

class MahasiswaJelek:
    """
    [JELEK] Hardcode tahu siapa yang perlu notify.
    Tight coupling!
    """
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.nilai = 0
    
    def update_nilai(self, nilai):
        self.nilai = nilai
        
        # Hardcode notify siapa aja -- tight coupling!
        print(f"  [HARDCODED] Notifying OrangTua...")
        print(f"  [HARDCODED] Notifying Dosen...")
        print(f"  [HARDCODED] Notifying AdminAkademik...")
        # Problem: jika ada observer baru, harus modify class ini!

mhs = MahasiswaJelek("2301001", "Budi Santoso")
mhs.update_nilai(85)

# --- Pattern: Observer Pattern ---
print("\n-- Pattern: Observer Pattern (event-driven) --")

class Subject:
    """
    [PATTERN] Base class untuk object yang emit events.
    Manage list of observers.
    """
    def __init__(self):
        self._observers = []
    
    def subscribe(self, observer):
        """Subscribe observer untuk events."""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"  [SUBSCRIBE] {observer.__class__.__name__} subscribed")
    
    def unsubscribe(self, observer):
        """Unsubscribe observer."""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"  [UNSUBSCRIBE] {observer.__class__.__name__} unsubscribed")
    
    def notify(self, event):
        """Notify all observers tentang event."""
        for observer in self._observers:
            observer.update(event)

class Observer:
    """[PATTERN] Base class untuk observer."""
    def update(self, event):
        raise NotImplementedError

class Mahasiswa(Subject):
    """
    [PATTERN] Mahasiswa = Subject yang emit events.
    Tidak perlu tahu siapa observernya.
    """
    def __init__(self, nim, nama):
        super().__init__()
        self.nim = nim
        self.nama = nama
        self.nilai = 0
    
    def update_nilai(self, nilai):
        self.nilai = nilai
        # Just notify -- don't care who listens!
        self.notify({
            "tipe": "nilai_diupdate",
            "nim": self.nim,
            "nama": self.nama,
            "nilai": nilai
        })
    
    def update_status(self, status):
        self.status = status
        # Another event type -- observers can listen if they want
        self.notify({
            "tipe": "status_diubah",
            "nim": self.nim,
            "nama": self.nama,
            "status": status
        })

class OrangTuaObserver(Observer):
    """[PATTERN] Observer -- interested in nilai events."""
    def __init__(self, nama):
        self.nama = nama
    
    def update(self, event):
        if event["tipe"] == "nilai_diupdate":
            print(f"  [ORANGTUA {self.nama}] Nilai {event['nama']} = {event['nilai']}")
        elif event["tipe"] == "status_diubah":
            print(f"  [ORANGTUA {self.nama}] Status {event['nama']} = {event['status']}")

class DosenObserver(Observer):
    """[PATTERN] Observer -- interested in nilai untuk statistik."""
    def update(self, event):
        if event["tipe"] == "nilai_diupdate":
            print(f"  [DOSEN] Update statistik {event['nim']}, nilai = {event['nilai']}")

class AdminAkademikObserver(Observer):
    """[PATTERN] Observer -- interested in status untuk audit."""
    def update(self, event):
        if event["tipe"] == "status_diubah":
            print(f"  [ADMIN] Record perubahan status {event['nim']} -> {event['status']}")

class BeasiswaObserver(Observer):
    """[PATTERN] Observer -- interested in nilai untuk evaluasi."""
    def update(self, event):
        if event["tipe"] == "nilai_diupdate":
            nilai = event["nilai"]
            if nilai < 70:
                print(f"  [BEASISWA] WARNING: {event['nama']} nilai rendah = {nilai}")
            else:
                print(f"  [BEASISWA] OK: {event['nama']} maintain nilai = {nilai}")

# Penggunaan
print("\n-- Setup observers --")
mhs = Mahasiswa("2301001", "Budi Santoso")

# Subscribe observers
orangtua = OrangTuaObserver("Bapak Santoso")
dosen = DosenObserver()
admin = AdminAkademikObserver()
beasiswa = BeasiswaObserver()

mhs.subscribe(orangtua)
mhs.subscribe(dosen)
mhs.subscribe(admin)
mhs.subscribe(beasiswa)

print("\n-- Event: Nilai diupdate --")
mhs.update_nilai(85)

print("\n-- Event: Status diubah --")
mhs.update_status("CUTI_SEMENTARA")

print("\n-- Mahasiswa lain --")
mhs2 = Mahasiswa("2301042", "Sari Dewi")
mhs2.subscribe(orangtua)
mhs2.subscribe(beasiswa)

mhs2.update_nilai(65)

# --- Dynamic subscription ---
print("\n-- Dynamic unsubscribe --")
mhs.unsubscribe(admin)
print("-- Nilai diupdate lagi (admin tidak akan notified) --")
mhs.update_nilai(90)

print()
print("Bagian 1 selesai! Observer Pattern demonstrated.")
print("Key benefits:")
print("  - Mahasiswa tidak tahu siapa observernya")
print("  - Bisa add/remove observers at runtime")
print("  - Easy to add new observer types tanpa modify Mahasiswa")
