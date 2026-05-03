"""
Kode Praktik - Materi 12: Pola Desain (Design Patterns)
File: 03_decorator.py
Topik: Decorator Pattern

Jalankan: python 03_decorator.py
"""

from abc import ABC, abstractmethod

# ======================================================================
# BAGIAN 1: Decorator Pattern
#           Fokus: Add behavior dynamically tanpa inheritance explosion
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Decorator Pattern")
print("=" * 60)

# --- Anti-pattern: Inheritance explosion ---
print("\n-- Demo Anti-Pattern: Too many subclasses --")

class MataKuliahBase:
    """Base class untuk matakuliah."""
    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks
    
    def harga(self):
        """Base harga = SKS * tarif per SKS."""
        return self.sks * 100_000
    
    def deskripsi(self):
        return f"{self.nama} ({self.sks} SKS)"

# Kalau mau kombinasi fitur (dengan praktik, lab, ujian online, dll)
# Inheritance nightmare!
class Regular(MataKuliahBase):
    pass

class DenganPraktik(MataKuliahBase):
    def harga(self):
        return super().harga() + 200_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Praktik"

class DenganPraktikDanLab(MataKuliahBase):
    def harga(self):
        return super().harga() + 200_000 + 300_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Praktik + Lab"

class DenganPraktikDanLabDanUjianOnline(MataKuliahBase):
    def harga(self):
        return super().harga() + 200_000 + 300_000 + 150_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Praktik + Lab + Ujian Online"

# Nightmare kombinatorial! 2^4 = 16 kombinasi untuk 4 features!

print("  Inheritance approach:")
print(f"  - Regular: Rp {Regular('Python', 3).harga()}")
print(f"  - DenganPraktik: Rp {DenganPraktik('Python', 3).harga()}")
print(f"  - DenganPraktikDanLab: Rp {DenganPraktikDanLab('Python', 3).harga()}")
print(f"  - Problem: N kombinasi = N subclasses!")

# --- Pattern: Decorator Pattern ---
print("\n-- Pattern: Decorator Pattern (composition) --")

class MataKuliah:
    """[PATTERN] Core matakuliah -- simple."""
    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks
    
    def harga(self):
        return self.sks * 100_000
    
    def deskripsi(self):
        return f"{self.nama} ({self.sks} SKS)"

class MataKuliahDecorator(MataKuliah):
    """
    [PATTERN] Base decorator -- wraps MataKuliah.
    Subclass add specific behavior.
    """
    def __init__(self, matkul: MataKuliah):
        self.matkul = matkul
    
    def harga(self):
        """Default: pass through ke wrapped object."""
        return self.matkul.harga()
    
    def deskripsi(self):
        """Default: pass through ke wrapped object."""
        return self.matkul.deskripsi()

class DenganPraktikDecorator(MataKuliahDecorator):
    """[PATTERN] Decorator -- add praktik."""
    def harga(self):
        return super().harga() + 200_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Praktik"

class DenganLabDecorator(MataKuliahDecorator):
    """[PATTERN] Decorator -- add lab."""
    def harga(self):
        return super().harga() + 300_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Lab"

class DenganUjianOnlineDecorator(MataKuliahDecorator):
    """[PATTERN] Decorator -- add ujian online."""
    def harga(self):
        return super().harga() + 150_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Ujian Online"

class DenganBukuDecorator(MataKuliahDecorator):
    """[PATTERN] Decorator -- provide buku."""
    def harga(self):
        return super().harga() + 100_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Buku"

# Penggunaan -- composable!
print("  Decorator approach:")

mk1 = MataKuliah("Pemrograman Python", 3)
print(f"  - Regular: Rp {mk1.harga()}")

mk2 = MataKuliah("Pemrograman Python", 3)
mk2 = DenganPraktikDecorator(mk2)
print(f"  - Dengan Praktik: Rp {mk2.harga()}")

mk3 = MataKuliah("Pemrograman Python", 3)
mk3 = DenganPraktikDecorator(mk3)
mk3 = DenganLabDecorator(mk3)
print(f"  - Dengan Praktik + Lab: Rp {mk3.harga()}")

mk4 = MataKuliah("Pemrograman Python", 3)
mk4 = DenganPraktikDecorator(mk4)
mk4 = DenganLabDecorator(mk4)
mk4 = DenganUjianOnlineDecorator(mk4)
mk4 = DenganBukuDecorator(mk4)
print(f"  - Dengan Praktik + Lab + Ujian Online + Buku: Rp {mk4.harga()}")

print(f"\n  Deskripsi lengkap:")
print(f"  {mk4.deskripsi()}")

# --- Pattern: Python Decorator Syntax ---
print("\n-- Alternative: Python function decorators --")

def dengan_praktik_func(matkul_func):
    """Decorator function -- wrap matakuliah function."""
    def wrapper():
        base_harga = matkul_func()
        return base_harga + 200_000
    return wrapper

def dengan_lab_func(matkul_func):
    """Decorator function -- wrap matakuliah function."""
    def wrapper():
        base_harga = matkul_func()
        return base_harga + 300_000
    return wrapper

@dengan_lab_func
@dengan_praktik_func
def harga_python():
    """Base harga Pemrograman Python."""
    return 300_000

print(f"  Python dengan praktik + lab: Rp {harga_python()}")

# --- Skenario real: HTTP middleware ---
print("\n-- Real-world: HTTP middleware dengan decorators --")

class Request:
    """Represent HTTP request."""
    def __init__(self, url, method="GET"):
        self.url = url
        self.method = method
        self.headers = {}
        self.body = ""

class ResponseDecorator:
    """[PATTERN] Base decorator untuk HTTP response handling."""
    def __init__(self, handler):
        self.handler = handler
    
    def process(self, request):
        return self.handler.process(request)

class AuthenticationDecorator(ResponseDecorator):
    """[PATTERN] Middleware -- check authentication."""
    def process(self, request):
        print(f"  [AUTH] Checking authentication for {request.url}...")
        if "Authorization" not in request.headers:
            return {"status": 401, "message": "Unauthorized"}
        return self.handler.process(request)

class LoggingDecorator(ResponseDecorator):
    """[PATTERN] Middleware -- log request."""
    def process(self, request):
        print(f"  [LOG] {request.method} {request.url}")
        return self.handler.process(request)

class CompressingDecorator(ResponseDecorator):
    """[PATTERN] Middleware -- compress response."""
    def process(self, request):
        result = self.handler.process(request)
        result["compressed"] = True
        print(f"  [COMPRESS] Response compressed")
        return result

class BaseHandler:
    """[PATTERN] Base handler -- process request."""
    def process(self, request):
        return {"status": 200, "message": "OK"}

# Composable middleware stack!
handler = BaseHandler()
handler = LoggingDecorator(handler)
handler = AuthenticationDecorator(handler)
handler = CompressingDecorator(handler)

request = Request("/api/mahasiswa/2301001")
request.headers["Authorization"] = "Bearer token123"

print("\n-- HTTP request processing with decorators --")
response = handler.process(request)
print(f"  Response: {response}")

print()
print("Bagian 1 selesai! Decorator Pattern demonstrated.")
print("Key benefits:")
print("  - No subclass explosion: N decorators, not 2^N subclasses")
print("  - Flexible composition: Stack decorators at runtime")
print("  - Single responsibility: Each decorator does one thing")
print("  - Easy to test: Can test each decorator independently")
