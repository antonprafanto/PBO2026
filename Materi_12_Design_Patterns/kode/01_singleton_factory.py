"""
Kode Praktik - Materi 12: Pola Desain (Design Patterns)
File: 01_singleton_factory.py
Topik: Singleton Pattern dan Factory Pattern

Jalankan: python 01_singleton_factory.py
"""

# ======================================================================
# BAGIAN 1: Singleton Pattern
#           Fokus: Hanya satu instance di seluruh aplikasi
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Singleton Pattern")
print("=" * 60)

# --- Anti-pattern: Multiple instances ---
print("\n-- Demo Anti-Pattern: Multiple database connections --")

class DatabaseJelek:
    """
    [JELEK] Setiap create instance baru = koneksi baru.
    Inefficient!
    """
    def __init__(self):
        self.connection_id = id(self)
        print(f"  [DB] Creating connection {self.connection_id}...")
    
    def query(self, sql):
        return f"Executing on {self.connection_id}: {sql}"

db1 = DatabaseJelek()
db2 = DatabaseJelek()
db3 = DatabaseJelek()

print(f"  db1 is db2? {db1 is db2}")  # False -- berbeda instance!
print(f"  Total connections: 3 (wasteful)")

# --- Pattern: Singleton dengan __new__ ---
print("\n-- Pattern: Singleton dengan __new__ --")

class DatabaseSingleton:
    """
    [BAIK] Hanya satu instance di seluruh aplikasi.
    Efficient!
    """
    _instance = None
    
    def __new__(cls):
        """__new__ dipanggil sebelum __init__, kontrol instantiation."""
        if cls._instance is None:
            print("  [DB] Creating FIRST database connection...")
            cls._instance = super().__new__(cls)
            cls._instance.connection_id = id(cls._instance)
        else:
            print("  [DB] Reusing existing connection...")
        return cls._instance
    
    def query(self, sql):
        return f"Executing on {self.connection_id}: {sql}"

db1 = DatabaseSingleton()
db2 = DatabaseSingleton()
db3 = DatabaseSingleton()

print(f"  db1 is db2? {db1 is db2}")  # True -- sama instance!
print(f"  Total connections: 1 (efficient)")

# --- Decorator Singleton (alternative) ---
print("\n-- Alternative: Singleton dengan decorator --")

def singleton(cls):
    """Decorator untuk convert class menjadi singleton."""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            print(f"  [LOG] Creating first {cls.__name__} instance...")
            instances[cls] = cls(*args, **kwargs)
        else:
            print(f"  [LOG] Reusing {cls.__name__} instance...")
        return instances[cls]
    
    return get_instance

@singleton
class Logger:
    """
    [PATTERN] Logger menggunakan decorator singleton.
    Hanya satu logger di seluruh aplikasi!
    """
    def __init__(self):
        self.logs = []
    
    def log(self, message):
        self.logs.append(message)
        print(f"  [LOG] {message}")

log1 = Logger()
log2 = Logger()
log3 = Logger()

print(f"  log1 is log2? {log1 is log2}")  # True -- sama instance!
print(f"  Total loggers: 1 (efficient)")

# ======================================================================
# BAGIAN 2: Factory Pattern
#           Fokus: Centralize object creation logic
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 2: Factory Pattern")
print("=" * 60)

# --- Anti-pattern: Scattered creation logic ---
print("\n-- Demo Anti-Pattern: Hardcoded creation di mana-mana --")

class NotifikasiEmail:
    def kirim(self, pesan):
        return f"Email: {pesan}"

class NotifikasiSMS:
    def kirim(self, pesan):
        return f"SMS: {pesan}"

class NotifikasiPush:
    def kirim(self, pesan):
        return f"Push: {pesan}"

def kirim_notifikasi_jelek(tipe, pesan):
    """
    [JELEK] Logic creation tersebar -- sulit maintain.
    """
    if tipe == "email":
        notif = NotifikasiEmail()
    elif tipe == "sms":
        notif = NotifikasiSMS()
    elif tipe == "push":
        notif = NotifikasiPush()
    else:
        raise ValueError(f"Unknown type: {tipe}")
    
    return notif.kirim(pesan)

print("  " + kirim_notifikasi_jelek("email", "Welcome!"))
print("  " + kirim_notifikasi_jelek("sms", "OTP 123456"))

# --- Pattern: Simple Factory ---
print("\n-- Pattern: Simple Factory --")

class NotifikasiFactory:
    """
    [BAIK] Centralized factory untuk create notifikasi.
    """
    @staticmethod
    def create(tipe):
        """Factory method -- centralized creation logic."""
        if tipe == "email":
            return NotifikasiEmail()
        elif tipe == "sms":
            return NotifikasiSMS()
        elif tipe == "push":
            return NotifikasiPush()
        else:
            raise ValueError(f"Unknown type: {tipe}")

notif = NotifikasiFactory.create("email")
print("  " + notif.kirim("Welcome!"))

notif = NotifikasiFactory.create("sms")
print("  " + notif.kirim("OTP 123456"))

# --- Pattern: Factory Method Pattern ---
print("\n-- Pattern: Factory Method Pattern (polymorphic) --")

class NotifikasiProducer:
    """
    [PATTERN] Base class dengan factory method.
    Subclass define bagaimana create notifikasi-nya.
    """
    def create_notifikasi(self):
        """Factory method -- subclass override."""
        raise NotImplementedError
    
    def kirim_dengan_retry(self, pesan, max_retry=3):
        """Template -- gunakan factory method untuk flexibility."""
        for attempt in range(max_retry):
            try:
                notif = self.create_notifikasi()
                return notif.kirim(pesan)
            except Exception as e:
                if attempt == max_retry - 1:
                    print(f"  [ERROR] Failed after {max_retry} attempts")
                    raise
                print(f"  [RETRY] Attempt {attempt + 1} failed, retrying...")

class ProduserEmail(NotifikasiProducer):
    """Concrete producer untuk email."""
    def create_notifikasi(self):
        return NotifikasiEmail()

class ProduserSMS(NotifikasiProducer):
    """Concrete producer untuk SMS."""
    def create_notifikasi(self):
        return NotifikasiSMS()

class ProduserPush(NotifikasiProducer):
    """Concrete producer untuk push."""
    def create_notifikasi(self):
        return NotifikasiPush()

def kirim_ke_user(producer: NotifikasiProducer, pesan):
    """Polymorphic -- work dengan any producer."""
    return producer.kirim_dengan_retry(pesan)

print("  Kirim email:")
print("  " + kirim_ke_user(ProduserEmail(), "Welcome to platform!"))

print("  Kirim SMS:")
print("  " + kirim_ke_user(ProduserSMS(), "Your OTP is 123456"))

print("  Kirim push:")
print("  " + kirim_ke_user(ProduserPush(), "New grade available"))

print()
print("Bagian 1-2 selesai! Pattern Singleton dan Factory demonstrated.")
