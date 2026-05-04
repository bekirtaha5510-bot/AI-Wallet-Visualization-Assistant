@echo off
title AI Destekli Akilli Cuzdan Kurulum

echo ==========================================
echo  AI Destekli Akilli Cuzdan Kurulum
echo ==========================================
echo.

echo Python surumu kontrol ediliyor...
python --version

echo.
echo Sanal ortam olusturuluyor...
python -m venv venv

echo.
echo Sanal ortam aktif ediliyor...
call venv\Scripts\activate.bat

echo.
echo pip guncelleniyor...
python -m pip install --upgrade pip

echo.
echo Gerekli kutuphaneler yukleniyor...
pip install -r requirements.txt

echo.
echo Kurulum tamamlandi.
echo Uygulamayi baslatmak icin BASLAT.bat dosyasini calistirin.
echo.

pause