@echo off
title AI Destekli Akilli Cuzdan

echo ==========================================
echo  AI Destekli Akilli Cuzdan Baslatiliyor
echo ==========================================
echo.

if not exist venv (
    echo Sanal ortam bulunamadi. Kurulum baslatiliyor...
    call kurulum.bat
)

echo Sanal ortam aktif ediliyor...
call venv\Scripts\activate.bat

echo Uygulama aciliyor...
python main.pyw

echo.
echo Uygulama kapatildi.
pause