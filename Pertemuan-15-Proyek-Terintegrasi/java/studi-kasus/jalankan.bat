@echo off
rem Menjalankan aplikasi kasir KedaiKita (versi Java) di Windows.
rem
rem Pemakaian:
rem     jalankan.bat          -> mode interaktif (kasir mengetik pilihan)
rem     jalankan.bat --demo   -> mode demo (tanpa input)
rem
rem Skrip ini pindah ke foldernya sendiri (agar folder data\ ditemukan),
rem mengompilasi semua file di src\kedaikita ke folder out\, lalu menjalankan
rem kelas kedaikita.Main dengan argumen yang sama.
setlocal
cd /d "%~dp0"
javac -d out src\kedaikita\*.java
if errorlevel 1 (
    echo Kompilasi gagal. Periksa pesan error di atas.
    exit /b 1
)
java -cp out kedaikita.Main %*
