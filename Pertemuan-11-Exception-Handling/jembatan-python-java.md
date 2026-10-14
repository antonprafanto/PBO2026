# 🌉 Jembatan Python ↔ Java Pertemuan 11: *Exception Handling*

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Konsep *exception* di Python dan Java **sama**: *exception* adalah objek, dilempar saat terjadi masalah, merambat ke pemanggil, lalu ditangkap oleh penangkap yang jenisnya cocok. Yang berbeda adalah cara menulisnya, dan dua hal penting: Python punya `else`, sedangkan Java punya *checked exception*. Halaman ini membantumu membaca kode di kedua bahasa dan memahami **mengapa** perbedaan itu ada.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Blok percobaan | `try:` | `try { ... }` |
| Menangkap | `except ValueError:` | `catch (IllegalArgumentException e) { ... }` |
| Nama variabel *exception* | opsional: `except ValueError as e:` | wajib: `catch (Jenis e)` |
| Mengambil pesan | `str(e)` atau `f"{e}"` | `e.getMessage()` |
| Beberapa jenis, satu penanganan | `except (ValueError, IndexError):` | `catch (NumberFormatException \| ArrayIndexOutOfBoundsException e)` |
| Jika tidak ada *exception* | `else:` | tidak ada; tulis di akhir blok `try` |
| Selalu dijalankan | `finally:` | `finally { ... }` |
| Melempar | `raise ValueError("pesan")` | `throw new IllegalArgumentException("pesan");` |
| Melempar ulang | `raise` | `throw e;` |
| *Exception chaining* | `raise BaruError("pesan") from e` | `throw new BaruException("pesan", e);` |
| Membaca penyebab | `e.__cause__` | `e.getCause()` |
| Puncak hierarki | `BaseException` | `Throwable` |
| Induk untuk *exception* buatan sendiri | `Exception` | `Exception` (*checked*) atau `RuntimeException` (*unchecked*) |
| Akhiran nama (kebiasaan) | `...Error` | `...Exception` |
| Wajib ditangani? | tidak pernah | ya, untuk *checked exception* |
| Mengumumkan *exception* sebuah *method* | *docstring*: "Melempar ..." | klausa `throws` di kepala *method* |
| Laporan *exception* yang lolos | *traceback*, dibaca dari **bawah** | *stack trace*, dibaca dari **atas** |
| Penangkap umum ditulis di atas yang spesifik | diterima diam-diam (*bug*) | *error* kompilasi |
| Bersih-bersih otomatis (Pertemuan 15) | `with` | *try-with-resources* |

## 1. *Checked Exception*: Hanya Ada di Java

Kedua versi `cari_menu`/`cariMenu` di KedaiKita melempar *exception* yang sama. Bedanya ada pada apa yang terjadi jika pemanggil **lupa** menangkapnya. Kode di bawah adalah versi ringkas *method* itu dari `kedai.py` dan `Kedai.java` (komentar dipendekkan, indentasi kelas dihilangkan), hanya untuk dibaca.

**Python:**

```python
def cari_menu(self, kode: str) -> Menu:
    """... Melempar MenuTidakDitemukanError jika kode tidak terdaftar."""
    for menu in self._daftar_menu:
        if menu.kode == kode:
            return menu
    raise MenuTidakDitemukanError(kode)
```

**Java:**

```java
public Menu cariMenu(String kode) throws MenuTidakDitemukanException {
    for (Menu menu : daftarMenu) {
        if (menu.getKode().equals(kode)) {
            return menu;
        }
    }
    throw new MenuTidakDitemukanException(kode);
}
```

| Pemanggil lupa menangkap | Python | Java |
|---|---|---|
| Kapan ketahuan? | saat program **berjalan** dan kodenya benar-benar tidak ditemukan | saat **kompilasi**, sebelum program berjalan |
| Pesannya | *traceback* `pengecualian.MenuTidakDitemukanError: ...` | `error: unreported exception MenuTidakDitemukanException; must be caught or declared to be thrown` |

**Mengapa berbeda?** Java ingin *compiler* ikut menjaga: kejadian wajar yang **pasti** perlu diantisipasi (stok habis, *file* tidak ada) dibuat *checked* sehingga tidak ada pemanggil yang lupa. Harganya, kode Java lebih panjang karena `throws` dan `try`/`catch` muncul di banyak tempat. Python memilih kesederhanaan: semua *exception* diperlakukan sama, dan tugas memberi tahu pemanggil diserahkan ke dokumentasi (*docstring*) serta kedisiplinan pemrogram.

## 2. `else`: Hanya Ada di Python

Potongan berikut disederhanakan dari bagian pertama `main.py` dan `Main.java` studi kasus (penangkapnya diringkas menjadi satu), jadi tidak untuk dijalankan sendiri.

**Python:**

```python
try:
    menu = kedai.cari_menu(kode)
    pesanan_budi.tambah_item(menu, jumlah)
except KedaiError as e:
    print(f"  [GAGAL] {e}")
else:
    print(f"  [OK] {jumlah} x {menu.nama}")
```

**Java:**

```java
try {
    Menu menu = kedai.cariMenu(kode);
    pesananBudi.tambahItem(menu, jumlah);
    System.out.println("  [OK] " + jumlah + " x " + menu.getNama());
} catch (KedaiException e) {
    System.out.println("  [GAGAL] " + e.getMessage());
}
```

Hasilnya sama untuk kasus biasa. Bedanya halus: kode di blok `else` Python **tidak** dijaga oleh `except`, sedangkan kode di akhir blok `try` Java **ikut** dijaga oleh `catch`. Misalkan di akhir blok `try` Java kamu menambahkan pemanggilan *method* lain yang juga bisa melempar `KedaiException`. Jika *method* itu gagal, `catch` akan mencetak `[GAGAL]`, padahal item pesanan sudah tercatat. Karena itu, baris tambahan di akhir `try` sebaiknya sederhana.

## 3. Membaca Laporan *Exception*: Arahnya Berlawanan

Berikut kerangka laporan program patungan dari [halaman konsep](README.md#4-jika-tidak-ada-yang-menangkap-traceback-dan-stack-trace), dengan isi yang disingkat menjadi `...`:

```text
Python (traceback)                       Java (stack trace)
---------------------------------------  ---------------------------------------
Traceback (most recent call last):       Exception in thread "main" JENIS: PESAN
  File ... in <module>         <- awal     at ...hitungPatungan(...:3)  <- lahir
  File ... in main                         at ...main(...:8)            <- awal
  File ... in hitung_patungan  <- lahir
JENIS: PESAN
```

Tanda `<- lahir` menunjuk tempat *exception* lahir, sedangkan `<- awal` menunjuk titik awal program. Python mencetak panggilan **terbaru di bawah** (*most recent call last*). Java mencetak tempat *exception* lahir **di atas**. Di kedua bahasa, telusuri laporan sesuai arah bacanya sampai bertemu baris pertama yang menyebut *file* milikmu.

## 4. Pesan dan Data Tambahan

Berikut versi ringkas `StokTidakCukupError` (dari `pengecualian.py`) dan `StokTidakCukupException` (dari `StokTidakCukupException.java`). Sebagian atribut dan konstruktornya sengaja tidak ditulis.

**Python:**

```python
class StokTidakCukupError(KedaiError):
    def __init__(self, nama_menu: str, diminta: int, tersedia: int):
        super().__init__(f"Stok {nama_menu} tidak cukup: "
                         f"diminta {diminta}, tersedia {tersedia}")
        self.tersedia = tersedia  # dibaca langsung: e.tersedia
```

**Java:**

```java
public class StokTidakCukupException extends KedaiException {
    private static final long serialVersionUID = 1L;
    private int tersedia;
    // konstruktor memanggil super("Stok ... tidak cukup: ...")
    public int getTersedia() { return tersedia; }  // dibaca: e.getTersedia()
}
```

- Pesan sama-sama dititipkan ke konstruktor induk (`super().__init__(pesan)` / `super(pesan)`), lalu dibaca dengan `str(e)` / `e.getMessage()`.
- Python menyimpan data tambahan sebagai atribut biasa. Java memakai *field* `private` dan *getter*, sesuai aturan enkapsulasi Pertemuan 04.
- Java menambahkan `serialVersionUID`, "nomor versi" untuk serialisasi. Python tidak membutuhkannya.

## 5. Melempar Ulang dan *Chaining*

| | Python | Java |
|---|---|---|
| Lempar ulang yang sama | `raise` (tanpa apa pun) | `throw e;` |
| Bungkus + simpan penyebab | `raise TransferGagalError(pesan) from e` | `throw new TransferGagalException(pesan, e);` |
| Syarat | semua *exception* bisa memakai `from` | konstruktornya harus menerima `Throwable` dan meneruskannya ke `super(pesan, penyebab)` |
| Tampilan saat lolos | *The above exception was the direct cause of the following exception* | `Caused by: ...` |

## 6. Banyak Penangkap

- Python memakai ***tuple***: `except (ValueError, IndexError):`. Java memakai **garis tegak**: `catch (A | B e)`.
- Java menolak *multi-catch* yang jenisnya berhubungan induk-anak, misalnya `NumberFormatException | IllegalArgumentException`. Python tidak memeriksanya.
- Java menolak penangkap yang tidak mungkin terpakai (`has already been caught`). Python menjalankan penangkap pertama yang cocok tanpa peringatan apa pun, jadi urutan yang salah menjadi *bug* diam-diam.

## Yang Sama di Kedua Bahasa

- *Exception* adalah **objek** dari sebuah **kelas**, tersusun dalam hierarki pewarisan. Menangkap induk berarti menangkap semua turunannya.
- *Exception* merambat ke pemanggil sampai ada yang menangkap. Sisa blok `try` dan sisa *method* yang dilewati tidak dijalankan.
- `finally` selalu berjalan: saat berhasil, saat ditangkap, dan saat *exception* lanjut merambat.
- Penangkap diperiksa dari atas ke bawah. Yang spesifik ditulis lebih dulu.
- *Exception* buatan sendiri dibuat dengan pewarisan dan boleh membawa data tambahan.
- *Output* studi kasus KedaiKita versi Python dan Java **identik**.

## Jebakan saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Lupa `new`: `throw IllegalArgumentException("...")` dianggap memanggil *method* (`cannot find symbol`) |
| Python | Java | Lupa `throws` atau `try`/`catch` untuk *checked exception* sehingga kompilasi gagal |
| Python | Java | Mencari blok `else`, padahal tidak ada |
| Python | Java | `Integer.parseInt(" 7 ")` gagal karena spasi; Python `int(" 7 ")` berhasil. Pakai `trim()` |
| Python | Java | `10.0 / 0` di Java menghasilkan `Infinity` tanpa *exception*, sedangkan di Python melempar `ZeroDivisionError` |
| Java | Python | Menulis `throw`, `catch`, atau `new`: `throw ValueError(...)` ditolak dengan `SyntaxError: invalid syntax` |
| Java | Python | Mengira urutan `except` yang salah akan diprotes, padahal Python diam saja |
| Java | Python | Indeks `-1` tidak melempar *exception*, melainkan mengambil elemen terakhir |
| Java | Python | Menulis `except:` tanpa jenis seperti "tangkap semua": bentuk ini ikut menangkap Ctrl+C. Pakai `except Exception:` |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
