# 🌉 Jembatan Python ↔ Java Pertemuan 09: Polimorfisme

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Ide polimorfisme **sama** di Python dan Java: satu pemanggilan *method*, banyak perilaku, dan versi yang dijalankan selalu milik objek yang sebenarnya. Perbedaannya muncul dari satu sumber: Java **memeriksa tipe saat kompilasi**, sedangkan Python **memeriksa saat program berjalan**. Dari situlah lahir perbedaan *casting*, *duck typing*, dan *overloading*.

Potongan kode di halaman ini hanya untuk dibandingkan, tidak untuk dijalankan sendiri. Versi lengkapnya ada di folder `contoh/` masing-masing bahasa.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Menimpa *method* induk | `def` dengan nama sama di kelas anak | `@Override` + nama dan daftar parameter sama |
| Pemanggilan polimorfik | `hewan.bersuara()` | `hewan.bersuara()` |
| Variabel menunjuk objek anak | `hewan = Kucing("Oyen")` (variabel tidak bertipe) | `Hewan hewan = new Kucing("Oyen");` (*upcasting* otomatis) |
| *Method* yang boleh dipanggil | Apa saja; diperiksa saat berjalan | Hanya milik **tipe variabel**; diperiksa *compiler* |
| Memeriksa jenis objek | `isinstance(p, Mahasiswa)` | `p instanceof Mahasiswa` |
| *Downcasting* | Tidak perlu | `(Mahasiswa) p` atau `p instanceof Mahasiswa m` (Java 16+) |
| Salah menebak jenis | `AttributeError` saat berjalan | `ClassCastException` saat berjalan |
| *Duck typing* | Ya, tanpa induk bersama | Tidak; butuh tipe bersama (kelas induk, nanti *interface*) |
| *Overloading* | Tidak ada; `def` kedua menimpa `def` pertama | Ada, untuk *method* dan konstruktor |
| Parameter boleh tidak diisi | Nilai bawaan: `jumlah: int = 1` | Versi *overload* yang lebih pendek |
| Memilih parameter lewat nama | Argumen kata kunci: `cari(tahun=1980)` | Tidak ada |
| Jumlah argumen bebas | `*daftar_buku` (*tuple*) | `Buku... daftarBuku` (*array*, *varargs*) |
| Parameter versi anak berbeda dari induk | Lolos, lalu bisa `TypeError` saat dipanggil | Dengan `@Override`: *error* kompilasi. Tanpa: menjadi *overload* diam-diam |

## 1. Kapan Kesalahan Ketahuan?

Misalkan *list*/daftar pengguna berisi seorang `Mahasiswa` dan seorang `Dosen`, lalu kita memanggil *method* yang hanya dimiliki mahasiswa.

**Python:**

```python
for pengguna in daftar:
    print(pengguna.isi_krs(21))   # Mahasiswa: berhasil, Dosen: AttributeError
```

**Java:**

```java
for (Pengguna pengguna : daftar) {
    System.out.println(pengguna.isiKrs(21));   // ditolak compiler: cannot find symbol
}
```

**Mengapa berbeda?** Python baru mencari *method* `isi_krs` saat baris itu dijalankan pada objek tertentu. Putaran pertama berhasil, dan program berhenti di putaran kedua. Java memeriksa sebelum program berjalan. Karena tipe variabelnya `Pengguna` dan `Pengguna` tidak punya `isiKrs`, program bahkan tidak bisa dikompilasi. Python lebih luwes, sedangkan Java lebih cepat menangkap kesalahan.

## 2. *Downcasting*: Wajib di Java, Tidak Dikenal di Python

**Python:**

```python
if isinstance(pengguna, Mahasiswa):
    print(pengguna.isi_krs(21))
```

**Java:**

```java
if (pengguna instanceof Mahasiswa) {               // cara 1 (klasik): cek dulu ...
    Mahasiswa mhs = (Mahasiswa) pengguna;          // ... lalu cast
    System.out.println(mhs.isiKrs(21));
}
if (pengguna instanceof Mahasiswa mhs) {           // cara 2 (Java 16+): cek + cast sekaligus
    System.out.println(mhs.isiKrs(21));
}
```

Di Python, setelah `isinstance` bernilai benar, *method* khusus langsung bisa dipanggil karena variabel tidak punya tipe yang perlu "diyakinkan". Di Java, `instanceof` hanya **bertanya**. *Compiler* tetap memandang `pengguna` sebagai `Pengguna` sampai kita melakukan *cast*. Bentuk `instanceof Mahasiswa mhs` menggabungkan keduanya.

> [!NOTE]
> *Cast* di Java tidak mengubah objek. *Cast* hanya mengubah cara *compiler* memandangnya. Jika tebakannya salah, program Java berhenti dengan `ClassCastException` tepat di baris *cast*. Python tidak punya *cast*, jadi kesalahan serupa baru muncul sebagai `AttributeError` ketika *method* yang dicari ternyata tidak ada.

## 3. *Duck Typing* vs Tipe Bersama

Contoh 05 di kedua jalur menghasilkan *output* yang **sama persis**, tetapi strukturnya berbeda.

**Python** (diringkas dari `contoh05_duck_typing.py`):

```python
class AyamJago:              # tanpa induk bersama
    def bunyikan(self) -> str:
        return "Kukuruyuuuk!"


def bangunkan_semua(daftar: list):
    for benda in daftar:
        print(benda.bunyikan())
```

**Java** (diringkas dari `Contoh05TipeBersama.java`):

```java
class AyamJago extends SumberBunyi {     // wajib punya induk bersama
    @Override
    public String bunyikan() {
        return "Kukuruyuuuk!";
    }
}

static void bangunkanSemua(List<SumberBunyi> daftar) { ... }
```

**Mengapa berbeda?** Python hanya bertanya "bisakah objek ini `bunyikan()`?" saat program berjalan. Java harus yakin sejak kompilasi, jadi setiap objek di `List<SumberBunyi>` wajib bertipe `SumberBunyi`. Hubungan "ayam jago **adalah** sumber bunyi" terasa dipaksakan. Di Pertemuan 10, Java memakai ***interface*** untuk kemampuan bersama seperti ini. Python juga punya `typing.Protocol`, semacam *duck typing* yang diresmikan.

## 4. *Overloading* vs Nilai Bawaan dan `*args`

Contoh 06 di kedua jalur juga menghasilkan *output* yang sama persis.

**Python** (satu *method*):

```python
# di dalam kelas Perpustakaan:
def cari(self, kata_kunci: str = "", tahun: int = 0) -> list[Buku]:
    ...

# di dalam main():
pusat.cari("Pe")          # judul saja
pusat.cari(tahun=1980)    # tahun saja (argumen kata kunci)
pusat.cari("a", 2006)     # keduanya
```

**Java** (tiga *method* bernama sama):

```java
// di dalam kelas Perpustakaan:
public List<Buku> cari(String kataKunci) { return cari(kataKunci, 0); }
public List<Buku> cari(int tahun) { return cari("", tahun); }
public List<Buku> cari(String kataKunci, int tahun) { ... }

// di dalam main:
pusat.cari("Pe");         // cari(String)
pusat.cari(1980);         // cari(int)
pusat.cari("a", 2006);    // cari(String, int)
```

**Mengapa berbeda?** Di dalam kelas Python, nama *method* hanya bisa menunjuk **satu** fungsi. `def` kedua dengan nama sama menimpa yang pertama, tanpa pesan *error*. Java membedakan *method* dari **nama + daftar tipe parameter** (disebut *signature* atau tanda tangan *method*) sehingga `cari(String)` dan `cari(int)` adalah dua *method* berbeda. *Compiler* memilih salah satunya saat kompilasi.

Pola yang sama muncul di studi kasus KedaiKita dan di konstruktor contoh 06:

| Kebutuhan | Python | Java |
|---|---|---|
| Pesan 1 porsi tanpa menulis jumlah (studi kasus) | `def tambah_item(self, menu: Menu, jumlah: int = 1)` | `tambahItem(Menu menu)` yang memanggil `tambahItem(menu, 1)` |
| Nama perpustakaan bawaan (contoh 06) | `def __init__(self, nama: str = "Perpustakaan Kampus")` | `Perpustakaan()` yang memanggil `this("Perpustakaan Kampus")` |

## 5. Contoh 07: Hanya Ada di Java

Jalur Java punya contoh tambahan, `Contoh07OverloadVsOverride.java`. Isinya membuktikan bahwa versi *overload* dipilih berdasarkan **tipe variabel** argumen (saat kompilasi), sedangkan versi *override* dipilih berdasarkan **tipe objek** (saat berjalan). Akibatnya, `resepsionis.sambut(rina)` memakai versi `sambut(Tamu)` walaupun objek Rina sebenarnya `TamuVip`.

Python tidak punya padanannya karena Python tidak punya *overloading*. Di Python, semua pemilihan *method* terjadi saat program berjalan, berdasarkan objek yang sebenarnya.

## Yang Sama di Kedua Bahasa

- Polimorfisme waktu berjalan = *override* + pemilihan versi berdasarkan **objek yang sebenarnya**.
- Jika kelas objek tidak meng-*override*, versi kelas induk yang dipakai.
- `self`/`this` di dalam *method* induk tetap menunjuk objek sebenarnya, jadi *method* induk yang memanggil *method* lain juga polimorfik.
- Koleksi polimorfik: satu *list*/`List` berisi berbagai kelas anak, diproses dengan satu perulangan.
- Pemeriksaan jenis (`isinstance`/`instanceof`) sebaiknya dipakai hanya untuk fitur khusus. Untuk perilaku bersama, pakai *override*.
- *Output* studi kasus KedaiKita, contoh 01—06, dan semua solusi latihan **identik** di kedua bahasa.

## Jebakan saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Memanggil *method* khusus anak lewat variabel bertipe induk tanpa *cast* (`cannot find symbol`) |
| Python | Java | Memasukkan objek "yang kebetulan punya *method* sama" ke `List` tanpa induk bersama. Java tidak mengenal *duck typing* |
| Python | Java | Mengira versi *overload* dipilih berdasarkan objek sebenarnya. Padahal *compiler* memilihnya dari tipe variabel argumen saat kompilasi (lihat contoh 07) |
| Python | Java | Lupa `@Override` sehingga salah parameter diam-diam menjadi *overload* |
| Java | Python | Menulis dua `def` bernama sama dan mengira itu *overloading*. `def` kedua menimpa yang pertama |
| Java | Python | Mencari cara *casting*. Python tidak membutuhkannya: cukup `isinstance`, lalu panggil |
| Java | Python | Mengira Python memeriksa parameter versi anak. Parameter yang berbeda baru gagal saat dipanggil (`TypeError`) |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
