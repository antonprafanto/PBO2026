# 🌉 Jembatan Python ↔ Java Pertemuan 05: Relasi Antarkelas

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Dependensi, asosiasi, agregasi, dan komposisi adalah konsep desain, jadi **sama persis** di Python dan Java. Yang berbeda adalah cara menulis "boleh kosong", cara menampung banyak objek, dan cara memecah program menjadi beberapa *file*. Halaman ini merangkum perbedaan itu dan menjelaskan *mengapa* perbedaan itu ada.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Atribut berisi objek lain | `self._dosen_wali = dosen` | `private DosenWali dosenWali;` lalu `this.dosenWali = dosen;` |
| "Tidak menunjuk objek apa pun" | `None` | `null` |
| Memeriksa kosong | `if menu is None:` | `if (menu == null)` |
| Menandai hasil yang boleh kosong | petunjuk tipe `-> Menu \| None` | tidak ditulis; setiap tipe kelas boleh `null` |
| Tipe *list* berisi objek | `list[Pemain]` (hanya keterangan) | `List<Pemain>` (diperiksa *compiler*) |
| Membuat *list* kosong | `[]` | `new ArrayList<>()` |
| Menambah, jumlah, isi ke-`i` | `append(x)`, `len(daftar)`, `daftar[i]` | `add(x)`, `daftar.size()`, `daftar.get(i)` |
| Salinan *list* | `list(daftar)` | `new ArrayList<>(daftar)` |
| Objek yang sama? | `a is b` | `a == b` |
| Nomor urut dalam perulangan | `enumerate(daftar, start=1)` | `for (int i = 0; i < daftar.size(); i++)` |
| Satu *file* berisi | modul; boleh beberapa kelas (`pesanan.py`) | satu kelas `public`, nama *file* = nama kelas |
| Memakai kelas dari *file* lain | `from menu import Menu` | tanpa `import` jika satu folder |
| Memakai *list* | bawaan, tanpa `import` | `import java.util.List;` dan `import java.util.ArrayList;` |
| Menjalankan program banyak *file* | `python main.py` | `javac *.java`, lalu `java Main` |
| Fungsi bantu | fungsi modul `format_rupiah()` | *method* `static` `Rupiah.format()` |
| Konstanta | `LEBAR_STRUK = 40` (di modul) | `private static final int LEBAR_STRUK = 40;` |
| Kolom rata kiri dan kanan | `f"{teks:<30}{subtotal:>10}"` | `String.format("%-30s%10s", teks, subtotal)` |
| Nomor dengan nol di depan | `f"P{n:03d}"` | `String.format("P%03d", n)` |
| Garis berulang | `"=" * 40` | `"=".repeat(40)` |

## 1. Menandai "Boleh Kosong"

Berikut *method* `cari_menu()`/`cariMenu()` dari studi kasus di kedua bahasa.

**Python** (potongan dari `python/studi-kasus/kedai.py`):

```python
    def cari_menu(self, kode: str) -> Menu | None:
        """Mengembalikan objek Menu dengan kode tertentu, atau None jika tidak ada."""
        for menu in self._daftar_menu:
            if menu.kode == kode:
                return menu
        return None
```

**Java** (potongan dari `java/studi-kasus/Kedai.java`):

```java
    /** Mengembalikan objek Menu dengan kode tertentu, atau null jika tidak ada. */
    public Menu cariMenu(String kode) {
        for (Menu menu : daftarMenu) {
            if (menu.getKode().equals(kode)) {
                return menu;
            }
        }
        return null;
    }
```

**Mengapa berbeda?** Di Java, variabel bertipe kelas **selalu** boleh berisi `null`, jadi tipe kembalian `Menu` sudah mencakup kemungkinan "tidak ada". Akibatnya, tanda tangan *method* (*method signature*, yaitu nama, parameter, dan tipe kembaliannya) tidak memberi petunjuk apa pun, dan pemanggil harus membaca komentar dokumentasinya. Python dengan petunjuk tipe `Menu | None` menuliskan kemungkinan itu secara terang-terangan. Namun, petunjuk tipe tidak diperiksa saat program berjalan.

Di kedua bahasa, akibat lupa memeriksa hasilnya sama: program berhenti. Python melapor `AttributeError: 'NoneType' object has no attribute ...`, sedangkan Java melapor `NullPointerException`.

## 2. *List*: Bawaan Python vs Koleksi Java

Berikut cara kelas `Tim` di contoh 03 menyiapkan *list* pemainnya.

**Python** (potongan dari `python/contoh/contoh03_agregasi.py`):

```python
        self._daftar_pemain: list[Pemain] = []  # [1] list kosong: 0 pemain
```

**Java** (dua potongan dari `java/contoh/Contoh03Agregasi.java`, yaitu deklarasi *field* dan isi konstruktor):

```java
    private List<Pemain> daftarPemain; // [1] "list berisi Pemain"
```

```java
        this.daftarPemain = new ArrayList<>(); // list kosong: 0 pemain
```

- `list` adalah tipe **bawaan** Python, jadi bisa langsung dipakai. `ArrayList` adalah kelas dari pustaka Java di paket `java.util` sehingga harus di-`import`.
- Di Java, tipe isi *list* ditulis di dalam `< >` (`<Pemain>`) dan diperiksa *compiler*. Jika kamu mencoba `add` sebuah `String` ke `List<Pemain>`, kompilasi gagal. Di Python, `list[Pemain]` hanya keterangan, dan *list* Python tetap bisa diisi apa saja.
- Isi `< >` di Java harus kelas, bukan tipe primitif: `List<Integer>`, bukan `List<int>`. Detailnya di Pertemuan 12.

## 3. Satu *File*, Satu Apa?

| | Python | Java |
|---|---|---|
| Satuan *file* | **modul**: wadah berisi kelas, fungsi, dan konstanta | *file* sumber berisi satu kelas `public` |
| Nama *file* | bebas; lazimnya huruf kecil (`pesanan.py`) | harus sama dengan nama kelas `public` (`Pesanan.java`) |
| Isi `pesanan.py` / `Pesanan.java` | `ItemPesanan` **dan** `Pesanan` | hanya `Pesanan`; `ItemPesanan` punya *file* sendiri |
| Fungsi di luar kelas | boleh (`format_rupiah()` di `utilitas.py`) | tidak ada; ditulis sebagai *method* `static` di kelas `Rupiah` |
| Memakai kelas dari *file* lain | wajib `import` | otomatis terlihat jika satu folder (satu paket) |

**Mengapa berbeda?** Java menemukan kelas lewat nama *file*-nya. Saat melihat `new Kedai(...)`, *compiler* mencari `Kedai.java` atau `Kedai.class`. Karena itu, nama *file* wajib sama dengan nama kelas, dan kelas satu folder otomatis saling terlihat. Python menjalankan setiap modul sebagai *file* biasa, jadi setiap *file* harus menyebut sendiri modul mana yang ia butuhkan lewat `import`.

## 4. Menjalankan Program Banyak *File*

| Langkah | Python | Java |
|---|---|---|
| Masuk ke folder | `cd studi-kasus` | `cd studi-kasus` |
| Kompilasi | tidak perlu langkah terpisah | `javac *.java` (menghasilkan *file* `.class`) |
| Menjalankan | `python main.py` | `java Main` (nama kelas, tanpa akhiran) |
| Dengan VS Code | buka `main.py`, klik ▷ (**Run Python File**) | buka `Main.java`, klik **Run** pada **Run \| Debug** (kompilasi otomatis) |
| Setelah mengubah kode | langsung jalankan lagi | lewat terminal: kompilasi ulang dulu |
| Jika *file* lain dijalankan sendiri | tidak tercetak apa-apa | ditolak: tidak ada *method* `main` |
| *File* tambahan yang muncul | folder `__pycache__` | *file* `.class` |
| Pesan khas jika salah folder | `can't open file` atau `ModuleNotFoundError` | `file not found: *.java` atau `Could not find or load main class` |

> [!NOTE]
> Versi Python punya contoh 08 tersendiri untuk program banyak *file* (`contoh08_multi_file/`). Versi Java tidak karena aturan folder `contoh/` kita adalah satu program satu *file*, dan studi kasus Java sudah menjadi contoh program banyak *file* yang lengkap. Sejak JDK 22, `java Main.java` juga bisa menjalankan program banyak *file*, tetapi materi ini memakai `javac *.java` agar berlaku di JDK 17, 21, maupun 25.

## 5. `final` pada *Method* (Khusus Java)

Baris pertama *method* `setHarga()` di `java/studi-kasus/Menu.java`:

```java
    public final void setHarga(int harga) {
```

`final` pada *method* berarti *method* itu tidak boleh di-*override* oleh kelas anak. KedaiKita versi Java memakainya pada `setHarga()` karena *method* itu dipanggil dari konstruktor. Python tidak punya kata kunci seperti ini: semua *method* bisa ditimpa. Memang ada penanda `@final` dari modul `typing`, tetapi penanda itu hanya diperiksa alat bantu seperti pemeriksa tipe, bukan oleh Python saat program berjalan. Pewarisan dan *override* dibahas di Pertemuan 07.

## Yang Sama di Kedua Bahasa

- Keempat jenis relasi dan cara mengenalinya: parameter (dependensi), atribut berisi objek (asosiasi), *list* berisi objek dari luar (agregasi), dan objek bagian yang dibuat di dalam (komposisi).
- Yang disimpan selalu **referensi**, bukan salinan objek. Dua variabel bisa menunjuk objek yang sama.
- Salinan *list* hanya menyalin *list*-nya. Objek di dalamnya tetap objek yang sama.
- Hasil pencarian yang kosong wajib diperiksa sebelum dipakai.
- Program besar dipecah menjadi beberapa *file* dan dijalankan dari folder tempat *file-file* itu berada.
- *Output* studi kasus KedaiKita versi Python dan Java **identik**.

## Jebakan saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Menulis `daftar[0]`, `len(daftar)`, atau `daftar.append(x)`; yang benar `daftar.get(0)`, `daftar.size()`, `daftar.add(x)` |
| Python | Java | Lupa `import java.util.List;` dan `import java.util.ArrayList;` |
| Python | Java | Menjalankan studi kasus dengan `java Main.java` seperti program satu *file* (gagal di JDK 17 dan 21) |
| Python | Java | Lupa kompilasi ulang dengan `javac *.java` setelah mengubah kode |
| Python | Java | Membandingkan teks dengan `==`; pakai `.equals()` |
| Java | Python | Mengira kelas di *file* lain otomatis terlihat; di Python, setiap *file* wajib `import` |
| Java | Python | Menamai *file* `Menu.py` lalu menulis `from menu import Menu`; nama modul harus sama persis dengan nama *file* |
| Java | Python | Menulis `menu == None`; kebiasaan Python adalah `menu is None` |
| Java | Python | Mengira petunjuk tipe `list[Pemain]` akan menolak isi yang salah; Python tidak memeriksanya saat berjalan |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
