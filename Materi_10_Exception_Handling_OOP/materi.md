# Materi 10 — Exception Handling OOP

---

## 1. Apa Itu Exception?

**Exception** (pengecualian) adalah kondisi tidak normal yang terjadi saat program berjalan dan menginterupsi alur normal eksekusi. Jika tidak ditangani, exception menyebabkan program berhenti dengan pesan error.

> *"Exception bukan berarti program Anda buruk — itu berarti Anda serius tentang keandalan."*

### Analogi Dunia Nyata

Bayangkan layanan **cetak transkrip di bagian akademik kampus**:

- **Skenario normal**: mahasiswa menyerahkan syarat → staf memproses → transkrip dicetak.
- **Skenario exception**: 
  - Mahasiswa tidak membawa KTM → **IdentitasTidakDitemukanError**
  - Ada tunggakan SPP → **TunggakanAkademikError**
  - Sistem sedang offline → **SistemOfflineError**

Tanpa penanganan, semua skenario itu akan membuat antrean macet total. Dengan penanganan yang baik, setiap kasus ditangani sesuai prosedur masing-masing.

---

## 2. Hierarki Exception di Python

Python memiliki hierarki exception bawaan yang kaya:

```
BaseException
 +-- SystemExit              <- keluar dari interpreter
 +-- KeyboardInterrupt       <- Ctrl+C
 +-- Exception               <- semua exception "biasa"
      +-- ValueError         <- nilai tidak valid
      +-- TypeError          <- tipe data salah
      +-- AttributeError     <- atribut tidak ada
      +-- KeyError           <- kunci dict tidak ditemukan
      +-- IndexError         <- indeks di luar batas
      +-- FileNotFoundError  <- file tidak ada
      +-- ZeroDivisionError  <- dibagi nol
      +-- RuntimeError       <- error runtime umum
      +-- StopIteration      <- iterator habis
      +-- OSError            <- error sistem operasi
           +-- FileNotFoundError
           +-- PermissionError
      ... (dan banyak lagi)
```

Selalu tangkap exception **spesifik** dulu sebelum yang umum.

---

## 3. Sintaks Dasar: try / except / else / finally

```python
try:
    # kode yang mungkin menimbulkan exception
    hasil = 100 / angka
except ZeroDivisionError:
    # ditangani jika dibagi nol
    print("Error: tidak bisa membagi dengan nol")
except (ValueError, TypeError) as e:
    # tangkap beberapa tipe sekaligus
    print(f"Error tipe/nilai: {e}")
except Exception as e:
    # tangkap semua exception lainnya (jaring pengaman)
    print(f"Error tak terduga: {e}")
else:
    # dijalankan HANYA jika try berhasil tanpa exception
    print(f"Hasil: {hasil}")
finally:
    # SELALU dijalankan, exception atau tidak
    print("Proses selesai")
```

### Peran Masing-masing Blok

| Blok | Kapan Dijalankan |
|------|-----------------|
| `try` | Selalu (percobaan kode berisiko) |
| `except` | Hanya jika ada exception yang cocok |
| `else` | Hanya jika `try` selesai TANPA exception |
| `finally` | SELALU — bahkan jika ada `return` di `try`/`except` |

---

## 4. `raise` — Melempar Exception

Anda bisa melempar exception secara eksplisit:

```python
def validasi_ipk(ipk):
    if not isinstance(ipk, (int, float)):
        raise TypeError(f"IPK harus berupa angka, bukan {type(ipk).__name__}")
    if not (0.0 <= ipk <= 4.0):
        raise ValueError(f"IPK harus antara 0.0-4.0, bukan {ipk}")
    return ipk

# Re-raise: teruskan exception setelah logging
try:
    validasi_ipk(5.0)
except ValueError as e:
    print(f"[LOG] Validasi gagal: {e}")
    raise   # lempar ulang exception yang sama
```

### `raise ... from ...` — Exception Chaining

Saat exception B terjadi karena exception A, gunakan chaining agar informasinya lengkap:

```python
try:
    data = ambil_dari_database()
except DatabaseError as e:
    raise ValueError("Data tidak valid") from e
    # Pesan: "ValueError: Data tidak valid" dengan konteks DatabaseError di bawahnya
```

---

## 5. Membuat Custom Exception

Kekuatan sesungguhnya exception handling OOP ada di sini: membuat hierarki exception sendiri.

### Aturan Dasar

- Selalu turunkan dari `Exception` (bukan `BaseException`)
- Beri nama yang deskriptif dan akhiri dengan `Error`
- Bisa menyimpan informasi tambahan sebagai atribut
- Implementasikan `__str__` untuk pesan yang informatif

```python
# Exception dasar untuk modul akademik
class AkademikError(Exception):
    """Exception dasar untuk semua error sistem akademik."""
    pass

# Exception spesifik
class MahasiswaTidakDitemukanError(AkademikError):
    def __init__(self, nim):
        self.nim = nim
        super().__init__(f"Mahasiswa dengan NIM '{nim}' tidak ditemukan")

class IPKTidakValidError(AkademikError):
    def __init__(self, ipk, alasan=""):
        self.ipk    = ipk
        self.alasan = alasan
        pesan = f"IPK {ipk} tidak valid"
        if alasan:
            pesan += f": {alasan}"
        super().__init__(pesan)

class TunggakanSPPError(AkademikError):
    def __init__(self, nim, jumlah_tunggakan):
        self.nim               = nim
        self.jumlah_tunggakan  = jumlah_tunggakan
        super().__init__(
            f"Mahasiswa {nim} memiliki tunggakan SPP "
            f"Rp {jumlah_tunggakan:,.0f}"
        )
```

### Penggunaan

```python
def proses_krs(nim):
    mahasiswa = cari_mahasiswa(nim)       # bisa raise MahasiswaTidakDitemukanError
    cek_tunggakan(mahasiswa)              # bisa raise TunggakanSPPError
    return buat_krs(mahasiswa)

try:
    proses_krs("2301999")
except MahasiswaTidakDitemukanError as e:
    print(f"[NIM ERROR] {e}")
    print(f"  NIM yang dicari: {e.nim}")
except TunggakanSPPError as e:
    print(f"[SPP ERROR] {e}")
    print(f"  Jumlah tunggakan: Rp {e.jumlah_tunggakan:,.0f}")
except AkademikError as e:
    print(f"[AKADEMIK ERROR] {e}")   # tangkap semua AkademikError lainnya
```

---

## 6. Hierarki Custom Exception

Desain hierarki exception yang baik mencerminkan domain masalah:

```
Exception
 +-- AkademikError               (base untuk sistem akademik)
      +-- DataError               (masalah data)
      |    +-- MahasiswaTidakDitemukanError
      |    +-- DosenTidakDitemukanError
      |    +-- MataKuliahTidakDitemukanError
      +-- ValidasiError           (data tidak valid)
      |    +-- IPKTidakValidError
      |    +-- SKSTidakValidError
      |    +-- NIMFormatError
      +-- BisnisProsesError       (aturan bisnis dilanggar)
           +-- TunggakanSPPError
           +-- KapasitasKelasError
           +-- PrasyaratTidakTerpenuhiError
```

Keuntungan hierarki:
- Bisa tangkap semua `ValidasiError` dengan satu `except`
- Bisa juga tangkap `NIMFormatError` secara spesifik
- Kode lebih modular dan mudah diperluas

---

## 7. Context Manager: `contextlib`

Selain mengimplementasikan `__enter__`/`__exit__` (Materi 09), Python menyediakan cara lebih ringkas via `contextlib`:

### `@contextmanager`

```python
from contextlib import contextmanager

@contextmanager
def sesi_database(nama_db):
    koneksi = buka_koneksi(nama_db)   # setup
    try:
        yield koneksi                  # beri kontrol ke blok 'with'
    except Exception as e:
        koneksi.rollback()
        raise                          # teruskan exception
    finally:
        koneksi.close()                # cleanup selalu berjalan

# Penggunaan identik dengan kelas context manager
with sesi_database("akademik.db") as db:
    db.simpan(data)
```

### `suppress` — Abaikan Exception Tertentu

```python
from contextlib import suppress

# Abaikan FileNotFoundError saat menghapus file yang mungkin tidak ada
with suppress(FileNotFoundError):
    os.remove("file_sementara.txt")
# Tanpa contextlib: try/except FileNotFoundError: pass
```

---

## 8. Best Practices Exception Handling

### Lakukan (Do)

```python
# 1. Tangkap exception spesifik
except ValueError as e:
    ...

# 2. Simpan informasi berguna di exception
class KoneksiGagalError(Exception):
    def __init__(self, host, port, alasan):
        self.host   = host
        self.port   = port
        self.alasan = alasan
        super().__init__(f"Gagal koneksi ke {host}:{port} -- {alasan}")

# 3. Gunakan finally untuk cleanup
finally:
    file.close()   # atau gunakan 'with' yang lebih baik

# 4. Logging sebelum re-raise
except Exception as e:
    logger.error(f"Error di proses_nilai: {e}", exc_info=True)
    raise

# 5. Exception chaining
raise ProsesGagalError("Transkrip tidak bisa dibuat") from original_error
```

### Hindari (Don't)

```python
# 1. JANGAN tangkap semua tanpa alasan
except Exception:
    pass   # menyembunyikan bug!

# 2. JANGAN tangkap BaseException (kecuali sangat perlu)
except BaseException:
    ...

# 3. JANGAN gunakan exception untuk flow control normal
try:
    return data["kunci"]
except KeyError:
    return None   # lebih baik: data.get("kunci")

# 4. JANGAN biarkan pesan error yang tidak informatif
raise ValueError("Error")   # tidak membantu debugging
```

---

## 9. `warnings` — Peringatan (Bukan Error)

Untuk kondisi yang tidak ideal tapi tidak fatal:

```python
import warnings

class IPKRendahWarning(UserWarning):
    """Peringatan saat IPK mendekati batas minimum."""
    pass

def evaluasi_mahasiswa(mahasiswa):
    if mahasiswa.ipk < 2.0:
        raise IPKTidakMemenuhiSyaratError(mahasiswa.nim, mahasiswa.ipk)
    elif mahasiswa.ipk < 2.5:
        warnings.warn(
            f"IPK {mahasiswa.nim} ({mahasiswa.ipk:.2f}) mendekati batas minimum",
            IPKRendahWarning,
            stacklevel=2
        )
    return "Lulus evaluasi"
```

---

## 10. Exception dalam Konteks OOP

### Exception sebagai Bagian Antarmuka Kelas

Setiap kelas/modul sebaiknya mendokumentasikan exception yang bisa dilemparnya:

```python
class RepositoriMahasiswa:
    """
    Raises:
        MahasiswaTidakDitemukanError: jika NIM tidak ada di database
        DatabaseError: jika koneksi database gagal
    """

    def cari(self, nim):
        ...

    def simpan(self, mahasiswa):
        ...
```

### Pattern: Guard Clause

Alih-alih nested if-else, lempar exception lebih awal untuk validasi:

```python
# Tanpa guard clause (sulit dibaca)
def daftar_matkul(mahasiswa, kode_mk):
    if mahasiswa is not None:
        if not mahasiswa.ada_tunggakan():
            if mahasiswa.ips >= 2.0:
                return proses_pendaftaran(mahasiswa, kode_mk)
            else:
                raise IPSKurangError(mahasiswa.nim)
        else:
            raise TunggakanSPPError(mahasiswa.nim, mahasiswa.tunggakan)
    else:
        raise MahasiswaTidakDitemukanError("None")

# Dengan guard clause (lebih bersih)
def daftar_matkul(mahasiswa, kode_mk):
    if mahasiswa is None:
        raise MahasiswaTidakDitemukanError("None")
    if mahasiswa.ada_tunggakan():
        raise TunggakanSPPError(mahasiswa.nim, mahasiswa.tunggakan)
    if mahasiswa.ips < 2.0:
        raise IPSKurangError(mahasiswa.nim)
    return proses_pendaftaran(mahasiswa, kode_mk)
```

---

## 11. Tabel Ringkasan

### Sintaks Exception Handling

| Sintaks | Fungsi |
|---------|--------|
| `try: ... except E:` | Tangkap exception tipe E |
| `except (E1, E2):` | Tangkap beberapa tipe |
| `except E as e:` | Akses objek exception via `e` |
| `else:` | Jalankan jika try sukses |
| `finally:` | Selalu jalankan (cleanup) |
| `raise E(...)` | Lempar exception baru |
| `raise` | Re-raise exception aktif |
| `raise E from original` | Exception chaining |

### Membuat Custom Exception

| Komponen | Keterangan |
|----------|-----------|
| Turunan `Exception` | Wajib (bukan `BaseException`) |
| Nama diakhiri `Error` | Konvensi Python |
| `__init__` dengan atribut | Simpan data kontekstual |
| `super().__init__(pesan)` | Teruskan pesan ke Exception |
| `__str__` (opsional) | Format pesan kustom |

---

## Referensi

- [Python Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [contextlib — Utilities for with-statement contexts](https://docs.python.org/3/library/contextlib.html)
- [PEP 3134 — Exception Chaining and Embedded Tracebacks](https://peps.python.org/pep-3134/)
- Fluent Python, 2nd Ed. — Luciano Ramalho (Bab 18)
- Clean Code — Robert C. Martin (Bab 7: Error Handling)
