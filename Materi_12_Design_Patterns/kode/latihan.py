"""
Latihan - Materi 12: Pola Desain (Design Patterns)
File: latihan.py

Petunjuk:
- Lengkapi setiap bagian yang bertanda # TODO:
- Jalankan file ini untuk memverifikasi jawaban Anda
- Jangan ubah bagian yang tidak ditandai TODO
- Semua assert harus lulus tanpa AssertionError

Kaitan dengan Materi:
- SOAL 1 berkaitan dengan materi.md Bagian 2 (Singleton Pattern)
- SOAL 2 berkaitan dengan materi.md Bagian 3 (Factory Pattern)
- SOAL 3 berkaitan dengan materi.md Bagian 5 (Decorator Pattern)
"""

from abc import ABC, abstractmethod

print("=" * 60)
print("LATIHAN MATERI 12: Pola Desain (Design Patterns)")
print("=" * 60)

# ======================================================================
# SOAL 1 (*Mudah): Implement Singleton Pattern
# (Lihat materi.md Bagian 2 untuk teori Singleton)
# ======================================================================
print()
print("SOAL 1: Implement Singleton Pattern")
print("-" * 40)

# Diberikan: Problem dengan multiple instances
class ConfigurationJelek:
    """
    [JELEK] Setiap instantiate buat config baru.
    Jika ada yang ubah config, yang lain tidak tahu!
    """
    def __init__(self):
        self.debug_mode = False
        self.database_url = "localhost"
    
    def set_debug(self, value):
        self.debug_mode = value
    
    def get_debug(self):
        return self.debug_mode

# TODO: Buat class Configuration sebagai Singleton
#       Gunakan __new__ method atau decorator singleton
#       - Hanya satu instance di seluruh aplikasi
#       - Set debug_mode dengan setter
#       - Get debug_mode dengan getter
class Configuration:
    pass  # TODO: implementasikan sebagai singleton


# ==> PENGUJIAN SOAL 1
print("  Pengujian Soal 1...")

try:
    config1 = Configuration()
    config1.set_debug(True)
    
    config2 = Configuration()
    assert config2.get_debug() == True, "Config tidak shared!"
    
    assert config1 is config2, "Bukan singleton!"
    print("  [OK] Configuration singleton OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  Configuration: {err}")

try:
    config3 = Configuration()
    assert config3 is config1, "Masih buat instance baru!"
    print("  [OK] Singleton verified (3 references = 1 instance)")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  Singleton verification: {err}")


# ======================================================================
# SOAL 2 (**Sedang): Implement Factory Pattern
# (Lihat materi.md Bagian 3 untuk teori Factory)
# ======================================================================
print()
print("SOAL 2: Implement Factory Pattern")
print("-" * 40)

# Diberikan: Interface untuk validasi berbeda
class Validator(ABC):
    @abstractmethod
    def validate(self, value):
        """Return True jika valid, False jika tidak."""
        pass

class ValidatorEmail(Validator):
    """Validate email format."""
    def validate(self, value):
        return "@" in value and "." in value

class ValidatorNumber(Validator):
    """Validate numeric value."""
    def validate(self, value):
        try:
            float(value)
            return True
        except:
            return False

class ValidatorLength(Validator):
    """Validate string length."""
    def __init__(self, min_len=0, max_len=100):
        self.min_len = min_len
        self.max_len = max_len
    
    def validate(self, value):
        return self.min_len <= len(str(value)) <= self.max_len

# TODO: Buat class ValidatorFactory dengan factory method
#       - static method create(validator_type, **kwargs) -> Validator
#       - Supported types: "email", "number", "length"
#       - Untuk "length", pass min_len dan max_len ke constructor
class ValidatorFactory:
    pass  # TODO: implementasikan


# ==> PENGUJIAN SOAL 2
print("  Pengujian Soal 2...")

try:
    email_validator = ValidatorFactory.create("email")
    assert email_validator.validate("user@example.com") == True
    assert email_validator.validate("invalid-email") == False
    print("  [OK] Email validator OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  Email validator: {err}")

try:
    num_validator = ValidatorFactory.create("number")
    assert num_validator.validate("123") == True
    assert num_validator.validate("abc") == False
    print("  [OK] Number validator OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  Number validator: {err}")

try:
    len_validator = ValidatorFactory.create("length", min_len=3, max_len=10)
    assert len_validator.validate("hello") == True
    assert len_validator.validate("a") == False
    assert len_validator.validate("this is way too long") == False
    print("  [OK] Length validator OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  Length validator: {err}")


# ======================================================================
# SOAL 3 (***Sulit): Implement Decorator Pattern
# (Lihat materi.md Bagian 5 untuk teori Decorator)
# ======================================================================
print()
print("SOAL 3: Implement Decorator Pattern")
print("-" * 40)

# Diberikan: Base class untuk filter text
class TextFilter:
    """Base text filter."""
    def apply(self, text):
        raise NotImplementedError

class NoopFilter(TextFilter):
    """Base filter yang tidak mengubah text."""
    def apply(self, text):
        return text

# TODO: Buat abstract class TextFilterDecorator yang:
#       - Wrap TextFilter instance
#       - Pass through apply() ke wrapped filter
class TextFilterDecorator(TextFilter):
    pass  # TODO: implementasikan


# TODO: Buat class UppercaseDecorator (extend TextFilterDecorator)
#       - apply(text) harus return text.upper() setelah wrapped filter
class UppercaseDecorator(TextFilterDecorator):
    pass  # TODO: implementasikan


# TODO: Buat class RemoveSpacesDecorator (extend TextFilterDecorator)
#       - apply(text) harus return text dengan semua spaces dihapus
class RemoveSpacesDecorator(TextFilterDecorator):
    pass  # TODO: implementasikan


# TODO: Buat class ReverseDecorator (extend TextFilterDecorator)
#       - apply(text) harus return text terbalik (reversed)
class ReverseDecorator(TextFilterDecorator):
    pass  # TODO: implementasikan


# ==> PENGUJIAN SOAL 3
print("  Pengujian Soal 3...")

try:
    # Test single decorator
    filter_base = NoopFilter()
    filter_upper = UppercaseDecorator(filter_base)
    result = filter_upper.apply("hello")
    assert result == "HELLO", f"Expected 'HELLO', got '{result}'"
    print("  [OK] Uppercase decorator OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  Uppercase decorator: {err}")

try:
    # Test chaining decorators
    filter_base = NoopFilter()
    filter_chain = RemoveSpacesDecorator(UppercaseDecorator(filter_base))
    result = filter_chain.apply("hello world")
    assert result == "HELLOWORLD", f"Expected 'HELLOWORLD', got '{result}'"
    print("  [OK] Chained decorators (Uppercase + RemoveSpaces) OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  Chained decorators: {err}")

try:
    # Test complex chain
    filter_base = NoopFilter()
    filter_chain = ReverseDecorator(RemoveSpacesDecorator(UppercaseDecorator(filter_base)))
    result = filter_chain.apply("hello world test")
    assert result == "TSELTWDLROWHELLO", f"Expected 'TSELTWDLROWHELLO', got '{result}'"
    print("  [OK] Complex chain (Uppercase + RemoveSpaces + Reverse) OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  Complex chain: {err}")

print()
print("Latihan selesai! Periksa output di atas untuk [OK]/[X].")
