# Deprem Sonrası Drone ile Yardım Dağıtımı Optimizasyonu

Bu proje, **deprem sonrası yardım malzemelerinin** drone kullanılarak **en verimli şekilde** dağıtımını planlamayı amaçlamaktadır.  
Sistem; **K-Means Kümeleme Algoritması**, **Dijkstra Algoritması** ve **NetworkX** kütüphanesini kullanarak:

-  İhtiyaç noktalarını kümelendirir
-  Her küme için en uygun depoyu belirler
-  En kısa dağıtım rotasını oluşturur
-  Drone kapasitesine göre dağıtımı planlar

---

## Projenin Amacı
Afet sonrası hızlı, planlı ve optimize edilmiş yardım dağıtımı sağlayarak:
- Teslimat süresini en aza indirmek
- Drone kapasitesini verimli kullanmak
- Yardımların **öncelikli ihtiyaç bölgelerine** zamanında ulaşmasını sağlamak

---

## Kullanılan Teknolojiler
- **Python**
- **Pandas** → Veri işlemleri
- **NumPy** → Matematiksel hesaplamalar
- **Scikit-learn (KMeans)** → Kümeleme algoritması
- **NetworkX** → Graf yapısı ve en kısa yol analizi

---

## Çalışma Mantığı
1.  **Excel'den veriler yüklenir** (ihtiyaç noktaları ve mesafeler)
2.  **K-Means** ile ihtiyaç noktaları kümelenir
3.  Her küme için en yakın depo belirlenir
4.  **Dijkstra algoritması** ile en kısa yol hesaplanır
5.  Drone kapasitesine göre dağıtım planı oluşturulur

---

## Proje Dosya Yapısı
```
📁 Drone-ile-Deprem-Yardim-Dagitim-Optimizasyonu
├──  Rapor.docx → Proje raporu
├──  ihtiyac_tablosu.xlsx → İhtiyaç noktaları verisi
├──  mesafe_tablosu.xlsx → Mesafe matrisi
├──  yapay.py → Ana Python kodu
└──  .DS_Store → Sistem dosyası
```

---

##  Kurulum ve Çalıştırma
1. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install pandas numpy scikit-learn networkx
2. Python dosyasını çalıştırın:
    ```bash
    python yapay.py
    ```
## Geliştirme Fikirleri
- Gerçek zamanlı GPS verileri ile dinamik rota güncelleme
- Hava durumu verilerini rota planlamasına dahil etme
- Drone batarya seviyesine göre rota optimizasyonu
- Harita görselleştirmesi ekleme
