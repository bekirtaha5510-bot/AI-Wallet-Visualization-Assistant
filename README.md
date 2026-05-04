# 💰 AI Destekli Akıllı Cüzdan

### Kişisel Bütçe Analizi • Veri Görselleştirme • Bütçe Yorumlama Sistemi

---

## 📌 Proje Tanımı

**AI Destekli Akıllı Cüzdan**, kullanıcının aylık gelir ve harcama bilgilerini analiz eden, bu verileri grafiklerle görselleştiren ve kullanıcıya bütçe yorumu sunan bir masaüstü uygulamasıdır.

Bu proje, **Veri Görselleştirmeye Giriş** dersi kapsamında geliştirilmiştir. Amaç, kişisel bütçe verilerini anlamlı hale getirerek kullanıcının harcama alışkanlıklarını daha kolay yorumlamasını sağlamaktır.

Uygulama; gelir-gider analizi, bar grafik, pasta grafik ve bütçe yorumu özelliklerini bir araya getirerek veri görselleştirme konularını gerçek hayata yakın bir senaryo üzerinde uygular.

---

## 🎯 Projenin Amacı

Bu projenin temel amacı, kişisel finans verilerini analiz ederek kullanıcıya anlaşılır ve görsel bir bütçe raporu sunmaktır.

Proje kapsamında:

- Kullanıcıdan aylık gelir bilgisi alınır.
- Harcama kategorileri ve tutarları sisteme eklenir.
- Toplam gider ve kalan bütçe hesaplanır.
- Harcama oranı ve tasarruf oranı belirlenir.
- En yüksek harcama kategorisi bulunur.
- Bar grafik ile harcama kategorileri karşılaştırılır.
- Pasta grafik ile harcama dağılımı yüzdelik olarak gösterilir.
- Kullanıcıya bütçe yorumu ve tasarruf önerileri sunulur.

---

## ❓ Neden Bu Proje?

Günlük hayatta birçok kişi gelir ve giderlerini takip etmekte zorlanır. Harcamalar yalnızca liste halinde görüldüğünde, hangi kategoriye daha fazla para ayrıldığını anlamak her zaman kolay olmayabilir.

Bu proje:

- Ham harcama verisini anlamlı bilgiye dönüştürür.
- Kullanıcıya temel bütçe durumunu hesaplanmış şekilde sunar.
- Grafiklerle hızlı yorumlama imkânı sağlar.
- Veri görselleştirme tekniklerini gerçek bir problem üzerinde uygular.
- Kullanıcının tasarruf farkındalığını artırır.

---

## 🧠 Projenin Özgün Yönü

Bu proje, klasik bir gelir-gider takip uygulamasından farklı olarak verileri sadece listelemez; aynı zamanda analiz eder ve görselleştirir.

Uygulamada:

- **Bar chart** ile harcama kategorileri karşılaştırılır.
- **Pie chart** ile harcamaların toplam gider içindeki payı gösterilir.
- **Kural tabanlı bütçe yorumu** ile kullanıcıya anlaşılır finansal değerlendirme yapılır.
- Veri görselleştirme kavramları kişisel bütçe örneği üzerinden uygulanır.

Bu yönüyle proje, **Veri Görselleştirmeye Giriş** dersindeki teorik konuları pratik bir masaüstü uygulamasına dönüştürmektedir.

---

## 🏗️ Sistem Mimarisi

### 1️⃣ Veri Girişi Katmanı

Kullanıcı uygulama arayüzü üzerinden aylık gelirini ve harcama bilgilerini girer.

Girilen temel bilgiler:

- Aylık gelir
- Harcama kategorisi
- Harcama tutarı

Örnek harcama kategorileri:

- Kira
- Market
- Ulaşım
- Fatura
- Eğlence
- Diğer

---

### 2️⃣ Analiz Katmanı

Uygulama, kullanıcının girdiği veriler üzerinden temel bütçe hesaplamaları yapar.

Hesaplanan değerler:

- Toplam gelir
- Toplam gider
- Kalan bütçe
- Harcama oranı
- Tasarruf oranı
- En yüksek harcama kategorisi

Temel formüller:

```text
Toplam Gider = Tüm harcama tutarlarının toplamı

Kalan Bütçe = Gelir - Toplam Gider

Harcama Oranı = Toplam Gider / Gelir * 100

Tasarruf Oranı = Kalan Bütçe / Gelir * 100
3️⃣ Görselleştirme Katmanı

Uygulama, harcama verilerini grafiklerle sunar.

Kullanılan grafik türleri:

Bar Grafik
Pasta Grafik

Bar grafik, harcama kategorilerini karşılaştırmak için kullanılır.

Pasta grafik, harcamaların toplam gider içindeki oranını göstermek için kullanılır.

4️⃣ Yorumlama Katmanı

Uygulama, analiz edilen bütçe verilerine göre kullanıcıya anlaşılır bir bütçe yorumu üretir.

Yorum içerisinde:

Genel bütçe durumu
Harcama oranı
Tasarruf oranı
En yüksek harcama kategorisi
Kalan bütçe değerlendirmesi
Risk yorumu
Tasarruf önerileri
Veri görselleştirme açıklaması

bulunur.

🔄 Sistem Akışı
✨ Özellikler
📊 Temel Özellikler
Gelir bilgisi girişi
Harcama kategorisi ekleme
Harcama tutarı ekleme
Toplam gider hesaplama
Kalan bütçe hesaplama
Harcama oranı hesaplama
Tasarruf oranı hesaplama
En yüksek harcama kategorisini bulma
📈 Veri Görselleştirme Özellikleri
Kategorilere göre bar grafik oluşturma
Harcama dağılımını pasta grafik ile gösterme
Harcamaları görsel olarak karşılaştırma
Parça-bütün ilişkisini yüzdelik olarak sunma
🧠 Bütçe Yorumu Özellikleri
Genel bütçe değerlendirmesi
Risk yorumu
Tasarruf önerileri
Veri görselleştirme açıklaması
Kullanıcıya sade ve anlaşılır sonuç sunma
📚 Veri Görselleştirme ile İlişkisi

Bu proje, Veri Görselleştirmeye Giriş dersindeki temel kavramları uygulamalı olarak göstermektedir.

Ders Kavramı	Projedeki Karşılığı
Kategorik veri	Harcama kategorileri
Sayısal veri	Harcama tutarları
Bar chart	Kategoriler arası harcama karşılaştırması
Pie chart	Harcamaların toplam gider içindeki oranı
Karşılaştırma	Hangi kategoriye daha fazla harcama yapıldığını gösterme
Parça-bütün ilişkisi	Her kategorinin toplam giderdeki payı
Veri analizi	Gelir, gider, oran ve kalan bütçe hesaplamaları
🛠️ Kullanılan Teknolojiler
Teknoloji	Görevi
Python	Uygulamanın ana programlama dili
Tkinter	Masaüstü arayüz oluşturma
Matplotlib	Bar grafik ve pasta grafik oluşturma
Pandas	Veri işleme sürecini destekleme
Requests	Harici bağlantılar için kullanılabilecek yardımcı kütüphane
Batchfile	Kurulum ve başlatma işlemlerini kolaylaştırma
📁 Proje Dosya Yapısı
AI-Wallet-Visualization-Assistant
│
├── main.pyw
├── requirements.txt
├── BASLAT.bat
├── kurulum.bat
└── README.md
⚙️ Kurulum

Projeyi çalıştırmadan önce bilgisayarda Python kurulu olmalıdır.

Python sürümünü kontrol etmek için:

python --version

Gerekli Python kütüphanelerini yüklemek için:

pip install -r requirements.txt

Alternatif olarak otomatik kurulum dosyası kullanılabilir:

kurulum.bat
🚀 Uygulamayı Başlatma

Uygulamayı başlatmak için:

python main.pyw

veya Windows üzerinde:

BASLAT.bat

dosyası çalıştırılabilir.

BASLAT.bat dosyası sanal ortamı aktif eder ve uygulamayı başlatır.

⚡ Kullanım
Uygulamayı başlat.
Aylık gelir bilgisini gir.
Harcama kategorisini yaz.
Harcama tutarını gir.
Harcama Ekle butonuna bas.
Tüm harcamaları ekledikten sonra Bütçe Analizi Yap butonuna bas.
Bar Grafik Göster butonu ile kategori karşılaştırmasını görüntüle.
Pasta Grafik Göster butonu ile harcama dağılımını görüntüle.
AI Yorum Al butonu ile bütçe yorumunu görüntüle.
🧪 Örnek Veri
Aylık Gelir: 15000 TL

Kira: 6000 TL
Market: 3000 TL
Ulaşım: 1200 TL
Fatura: 1000 TL
Eğlence: 1500 TL
Diğer: 800 TL
🧾 Örnek Analiz Çıktısı
Geliriniz 15000.00 TL, toplam gideriniz 13500.00 TL ve kalan bütçeniz 1500.00 TL'dir.

Toplam gideriniz gelirinizin %90.00'lık kısmını oluşturmaktadır.
Tasarruf oranınız %10.00 olarak hesaplanmıştır.

En yüksek harcama kategoriniz "Kira" kategorisidir.
Bu kategori için 6000.00 TL harcama yapılmıştır.

Toplam gideriniz gelirinizin büyük bölümünü oluşturmaktadır.
Bu nedenle bütçe riskiniz yüksek seviyededir.
📊 Grafik Açıklamaları
Bar Grafik

Bar grafik, harcama kategorilerini karşılaştırmak için kullanılır.

Bu grafik sayesinde kullanıcı hangi kategoriye daha fazla harcama yaptığını kolayca görebilir.

Örneğin:

Kira harcaması diğer kategorilerden fazla mı?
Market gideri toplam bütçede önemli bir yer tutuyor mu?
Eğlence gideri azaltılabilir mi?

gibi sorulara görsel olarak cevap verilebilir.

Pasta Grafik

Pasta grafik, her harcama kategorisinin toplam gider içindeki oranını göstermek için kullanılır.

Bu grafik sayesinde kullanıcı, toplam harcamasının hangi alanlara dağıldığını yüzdelik olarak görebilir.

✅ Hata Kontrolleri

Uygulamada temel giriş kontrolleri bulunmaktadır.

Kontrol edilen durumlar:

Gelir alanı boş bırakılamaz.
Harcama kategorisi boş bırakılamaz.
Tutar alanı sayısal değer olmalıdır.
Sıfır veya negatif harcama tutarı kabul edilmez.
Grafik oluşturmak için en az bir harcama eklenmelidir.
Analiz yapmak için gelir bilgisi girilmelidir.
🌟 Proje Türü
Akademik Proje ✔
Gerçek Dünya Uygulaması ✔
Veri Görselleştirme Aracı ✔
Kişisel Finans Yardımcı Uygulaması ✔
Bütçe Analiz Sistemi ✔
🚀 Yenilikçi Yön

Bu proje, kişisel bütçe verilerini yalnızca sayısal olarak göstermek yerine, görsel ve yorumlanabilir hale getirir.

Bu sayede:

Kullanıcı harcama alışkanlıklarını daha kolay analiz eder.
Kategoriler arası farklar grafiklerle daha net görülür.
Bütçe durumu hesaplanan oranlar üzerinden yorumlanır.
Veri görselleştirme teknikleri gerçek hayat problemine uygulanır.
🎓 Proje Katkısı

Bu proje aşağıdaki alanları bir araya getirir:

Veri analizi
GUI geliştirme
Veri görselleştirme
Kişisel bütçe yönetimi
Karar destek sistemi
⚠️ Not

Bu proje eğitim amaçlıdır.

Uygulama tarafından üretilen bütçe yorumları genel değerlendirme niteliğindedir. Profesyonel finansal danışmanlık yerine geçmez.

👨‍💻 Geliştirici

Bu proje, Veri Görselleştirmeye Giriş dersi kapsamında kişisel bütçe verilerinin analiz edilmesi ve görselleştirilmesi amacıyla geliştirilmiştir.