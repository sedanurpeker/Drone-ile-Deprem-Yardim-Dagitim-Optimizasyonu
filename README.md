# Deprem Sonrası Drone ile Yardım Dağıtımı Optimizasyonu  
Bu proje, **drone kullanarak** deprem sonrası yardım malzemelerinin en verimli şekilde dağıtımını optimize etmeyi amaçlamaktadır.  

## Proje Açıklaması  
Bu sistem; **K-Means Kümeleme Algoritması**, **Dijkstra Algoritması** ve **NetworkX grafik yapıları** kullanarak:  
- **İhtiyaç noktalarını kümelendirir**,  
- **Her küme için en uygun depoyu belirler**,  
- **En kısa dağıtım rotasını oluşturur**,  
- **Drone kapasitesine göre dağıtımı planlar**.  

## Kullanılan Teknolojiler  
- **Python**  
- **Pandas** (Veri işlemleri için)  
- **NumPy** (Matematiksel hesaplamalar için)  
- **Scikit-learn (KMeans)** (Kümeleme algoritması için)  
- **NetworkX** (Graf yapısı ve en kısa yol analizi için)  

## Çalışma Mantığı  
1. **Excel'den veriler yüklenir**
2. **K-Means ile ihtiyaç noktaları kümelenir** 
3. **Her küme için en yakın depo belirlenir**
4. **Dijkstra algoritmasıyla en kısa yol hesaplanır** 
5. **Drone kapasitesine göre dağıtım planlanır** 
