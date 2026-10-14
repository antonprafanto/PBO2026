@echo off
rem Menjalankan unit test KedaiKita (versi Java) di Windows.
rem
rem Pemakaian:
rem     uji.bat
rem
rem Skrip ini pindah ke foldernya sendiri, mengompilasi semua file di
rem src\kedaikita ke folder out\, lalu menjalankan kelas kedaikita.UjiKedaiKita.
setlocal
cd /d "%~dp0"
javac -d out src\kedaikita\*.java
if errorlevel 1 (
    echo Kompilasi gagal. Periksa pesan error di atas.
    exit /b 1
)
java -cp out kedaikita.UjiKedaiKita %*
