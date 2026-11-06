> **Durum (6 Kasım 2026):** Pilot bölge kararı henüz kesinleşmedi. Bu belge Eindhoven önerisinin tam gerekçesidir; diğer adaylar için [`README.md`](../README.md).
> Bölüm 1–8 seçim sürecinin önceki adımlarıdır (kampüs, Delft, Rotterdam); güncel öneri bölüm 9.

# Pilot Bölge Önerisi ve Coğrafi Veri Kaynakları

*Hazırlanma: 18 Ekim 2026 · Repo: `yagizakkaya01/uav-cuas-datasets` (commit `d06abb6`)*

## Kısa cevap

> **Güncelleme (19 Ekim 2026):** Fiziksel demo, 1 m'den kısa direklerle küçük bir alanda yapılacak ve harita verisi yalnızca karar motorunda kullanılacak. Bu yüzden kampüs zorunluluğu kalktı. **Güncel öneri bölüm 9'da: Eindhoven Havalimanı / Eindhoven Hava Üssü (Hollanda), sivil-askeri ortak havalimanı.** Bölüm 1–6 ilk analizdir; kampüsün veri değerlendirmesi olarak geçerliliğini koruyor.

**Pilot bölge: ODTÜ Kuzey Kıbrıs Kampüsü (Kalkanlı, Güzelyurt), yaklaşık 35.2475 K, 33.0225 D; kampüs ve çevresini kapsayan ~3 × 2.5 km'lik bir AOI.**

Sebebi basit: öneride (proposal) sistem fiziksel olarak, direklere takılmış sensör düğümleri ve 3D baskı dron maketiyle **kampüs gibi korunan bir alanda** gösterilecek. Harita modeli ile demo sahası aynı yer olmazsa, düğüm konumlarını, görüş hattını (line of sight) ve arazi maskelemeyi gerçek kayıtlarla doğrulayamazsınız. "En detaylı veri" Türkiye'de İstanbul gibi bir büyükşehirde olsa da o veriyle demo yapılamaz. En detaylı veriyi, demonun yapılacağı yerde **siz üretirsiniz** (aşağıda bölüm 4).

Önerilen AOI (WGS84 bbox): `33.008, 35.236, 33.037, 35.259`

## 1. Repo incelemesinden çıkan veri ihtiyaçları

| Katman / modül | Gereken coğrafi veri | Repoda şu an seçili kaynak |
|---|---|---|
| Risk motoru (CNG 1): grid, arazi maskeleme, A\*/Dijkstra | Yüzey modeli (DSM), arazi modeli (DTM), yollar, binalar, korunan varlıklar | AW3D30 (birincil), Copernicus GLO-30 (çapraz kontrol), OSM |
| Görüş hattı / kapsama (EEE + CNG 1) | Düğüm koordinatları, direk yükseklikleri, bina yükseklikleri | Ekip ölçümü (planlı, Katman 1.5) |
| Hava trafiği tabanı (CNG 2) | ADS-B izleri, AOI üzerinde birkaç haftalık | OpenSky Trino |
| C2 arayüzü (CNG 4) | Altlık harita / uydu görüntüsü, MIL-STD-2525 semboller | Leaflet / CesiumJS (öneride) |

## 2. Repoda düzeltilmesi gereken önemli nokta

`layers/01-geospatial-sensor-data.md` ve `docs/verified-access-log.md` OSM için **Geofabrik Türkiye extract'ını** veriyor. Kampüs Kuzey Kıbrıs'ta ve Geofabrik'te Kıbrıs ayrı bir bölge: [Cyprus extract](https://download.geofabrik.de/europe/cyprus.html) (~36 MB, 17 Ekim 2026 itibarıyla güncel). Türkiye dosyası (620 MB) kampüsü içermiyor olmalı; indirip boşuna 620 MB işlemek yerine Kıbrıs dosyasını kullanın. (Türkiye dosyasının kampüsü içermediği Geofabrik bölge yapısından çıkarım; `osmium extract -b 33.008,35.236,33.037,35.259` ile bir dakikada doğrulanabilir.)

## 3. Kaynakların kampüs için değerlendirmesi

Aşağıdaki sayılar bu çalışmada gerçekten indirilen/sorgulanan veriden geliyor.

### 3.1 Yükseklik (DEM)

- **Copernicus GLO-30**, AWS'den indirildi (`Copernicus_DSM_COG_10_N35_00_E033_00_DEM`, 16 MB). AOI içinde 86 × 108 hücre, yükseklik **50 m ile 152 m arası** (medyan 87 m). Yani ~100 m'lik rölyef var; arazi maskelemenin anlamlı olacağı bir saha.
- **AW3D30**: repoda zaten doğrulanmış, aynı 30 m çözünürlük. Düşey datum farkı (EGM96 / EGM2008) zaten notlarda var.
- **Sınır**: 30 m hücre, birbirine birkaç yüz metre uzaktaki direkler için kaba. Bir bina ya da ağaç sırası tek hücrede kaybolur. Demo ölçeğinde görüş hattı hesabı için yetersiz.
- **Kıbrıs Cumhuriyeti DLS / INSPIRE verileri** (5 m DEM, bina izleri, ör. [Zenodo bina seti, CC BY 4.0](https://zenodo.org/records/16600733)) yalnızca Cumhuriyet'in kontrolündeki alanı kapsıyor; Kalkanlı için kullanılamaz. [Figshare'deki Kıbrıs DEM'i](https://figshare.com/articles/A_Digital_Elevation_Model_for_Cyprus_based_on_the_ALOS_2_W3D30_Digital_Surface_Model/3159991) de AW3D30 türevi, ek çözünürlük getirmez.
- KKTC Harita Dairesi için açık bir indirme portalı bulamadım. Danışman üzerinden kurumsal talep denenebilir (resmi ortofoto / 1:5000 pafta), ama buna güvenerek plan yapmayın.

### 3.2 Bina ve yol (OSM / Overture)

Overture Maps (2026-09-23.1 sürümü, OSM + Microsoft ML Buildings birleşimi) AOI için sorgulandı:

- **466 bina**: 411'i OpenStreetMap, 55'i Microsoft ML. Sınıflar arasında `university` (19), `dormitory` (17), `terrace`, `apartments` var.
- **Bina yüksekliği zayıf**: yalnızca 9 binada `height`, 141 binada `num_floors` var.
- **441 yol segmenti**: 122 footway, 70 path, 64 tertiary, 58 track, 56 service, 19 primary. Kampüs içi yaya ağı iyi çizilmiş, rota planlama için yeterli.

Sonuç: kampüs OSM'de iyi haritalanmış. Eksik olan yükseklik bilgisi.

### 3.3 Uydu görüntüsü ve arazi örtüsü

- **Sentinel-2** (10 m, ücretsiz; AWS `sentinel-cogs` kovası erişilebilir): bitki örtüsü / açık alan ayrımı için.
- **ESA WorldCover** (10 m, CC BY 4.0; AWS kovası erişilebilir): ağaçlık alanları görüş hattında engel olarak işlemek için.
- C2 arayüzü altlığı için Esri World Imagery veya Bing gibi karo servisleri görsel olarak çok daha net, ama lisansları gösterim içindir; analiz verisi olarak kullanmayın.

### 3.4 Hava trafiği (OpenSky)

Ercan (LCEN) ve Türkiye bağlantılı uçuşlar Kıbrıs üzerinden geçiyor, ama Güzelyurt civarında alçak irtifa ADS-B kapsaması belirsiz. **Bunu doğrulamadım.** İlk iş olarak AOI'yi 20 km genişleterek `state_vectors_data4` üzerinde birkaç haftalık bir sayım sorgusu atın; sonuç azsa bbox'ı büyütün.

## 4. Kampüs için en detaylı veriyi nasıl elde edersiniz

1. **Kendi yüksek çözünürlüklü DSM'inizi üretin.** Kampüsün belirli bir bölümünü (demo sahası) telefon ya da kamera fotoğraflarıyla fotogrametri (ör. OpenDroneMap / WebODM) ile modelleyin. İzinli bir dron uçuşu yapılabilirse 5 cm'lik ortofoto ve DSM çıkar. Bu, "ekip tarafından toplanan veri" (Katman 1.5) olarak repoya çok iyi oturur. Dron uçuşu için KKTC sivil havacılık ve kampüs yönetimi izni gerekir; yalnızca yer fotoğraflarıyla yapılan fotogrametri izin gerektirmez.
2. **Direk ve düğüm konumlarını GNSS ile ölçün** (telefon RTK yoksa, birden çok ölçümün ortalaması). Repo bunu zaten planlıyor.
3. **Bina yüksekliklerini OSM'e ekleyin.** Demo sahasındaki 20–30 binanın kat sayısı ve yüksekliğini girip `building:levels` / `height` etiketlerini doldurun. Hem veriniz iyileşir hem OSM'e katkı yapmış olursunuz (ODbL).
4. **Katmanlı model**: 30 m Copernicus/AW3D30 geniş alan risk ızgarası için; ekip DSM'i ve OSM bina yükseklikleri demo sahasındaki görüş hattı hesabı için.

## 5. Alternatif (yalnızca demo kampüs dışında olsaydı)

Türkiye'de açık coğrafi veri açısından en zengin yer büyük ihtimalle İstanbul (İBB Açık Veri Portalı ve İBB CBS katmanları). Ancak demo orada yapılmayacağı için pilot bölge olarak önermiyorum. Raporda "yöntem, veri zengin bir bölgeye de taşınabilir" diye bir cümleyle anılması yeterli.

## 6. Önerilen ilk adımlar

1. Repodaki OSM kaynağını Geofabrik **Cyprus** extract ile değiştirin, erişim kaydına ekleyin.
2. AOI bbox'ını (`33.008, 35.236, 33.037, 35.259`) repoda sabitleyin.
3. Copernicus GLO-30 N35 E033 karosunu ve AW3D30'u bu AOI'ye kırpıp PostGIS'e yükleyin.
4. OpenSky'da AOI için bir hacim sorgusu atın.
5. Demo sahasını belirleyip fotogrametri / GNSS çalışmasını planlayın.

---

## 7. Yalnızca veri zenginliğine göre karşılaştırma (dünya + Türkiye)

*Eklendi: 18 Ekim 2026. Demo yeri kısıtı olmadan, projenin ihtiyaç duyduğu katmanlara göre: yüksek çözünürlüklü DSM/DTM, 3D bina, ortofoto, açık lisans.*

| Sıra | Bölge | Yükseklik | 3D bina | Lisans / erişim | Not |
|:---:|---|---|---|---|---|
| 1 | **Hollanda** (ör. TU Delft) | AHN: 0.5 m DTM + DSM, ülke geneli ([AHN3, CC0](https://developers.google.cn/earth-engine/datasets/catalog/AHN_AHN3?hl=en)) | [3DBAG](https://www.gim-international.com/content/article/3dbag-automatically-generated-3d-models-of-10-million-buildings): ~10 milyon bina, LoD1.3 ve LoD2.2 (çatı şekilli) | Açık, kayıtsız indirme; CityJSON, GPKG, WFS | Her şey tek yerden, ücretsiz ve kayıtsız. **1. öneri** |
| 2 | **İsviçre** | swissALTI3D 0.5 m DTM, swissSURFACE3D (LiDAR) | [swissBUILDINGS3D 2.0 / 3.0 beta](https://opendata.swiss/en/dataset/swissbuildings3d-2-0), çatı geometrili | swisstopo açık veri (OGD) | Dağlık arazi, maskeleme senaryosu için çok iyi |
| 3 | **Danimarka** | [DHM](https://help.emd.dk/mediawiki/index.php/Danish_Elevation_Model): 0.4 m, düşey doğruluk ~5 cm | Ayrı bir 3D bina seti yok (DSM'den türetilir) | Ücretsiz, atıf şartı | |
| 4 | **Almanya / NRW** | DGM1 (1 m LiDAR) | [3D-Gebäudemodell LoD1/LoD2](https://ckan.open.nrw.de/tl/dataset/3d-gebaudemodell-nw-lod2-geo-nrw/resource/1a7cd83d-3257-4ebf-8e84-da00be88bb2a) | open.NRW, ücretsiz | Belgeler Almanca |
| 5 | **ABD** | [USGS 3DEP 1 m DEM](https://catalog.data.gov/dataset/usgs-1-meter-digital-elevation-model), kamu malı | Microsoft / Overture bina izleri | Kamu malı | Repodaki **FAA olay kayıtları** ABD'de. Risk modeli olay verisiyle doğrulanacaksa tek uygun aday |
| **TR-1** | **İstanbul** | 2012–2014 uçuşu: 16 nokta/m² LiDAR, 25 cm DSM/DEM/nDSM, 5 cm ortofoto, ~5.400 km² ([GIM](https://www.gim-international.com/content/article/3d-city-modelling-of-istanbul)) | ~1,5 milyon bina LoD2, 3.800 yapı LoD3 | **Açık indirme bulamadım.** İBB/BİMTAŞ ile kurumsal protokol gerekiyor | Türkiye'nin en zengin verisi, ama açık değil |
| TR-2 | Ankara (ODTÜ ana kampüs) | Açık kaynaklarda yalnızca 30 m | Belediyede 3D çalışmalar var; açık indirme bulamadım | | |

### Aynı veri kaynağında (Overture 2026-09-23.1) yaptığım bina sayımı

Overture'ın OSM ve Microsoft verilerinden oluşan birleşik bina katmanını, her bölge için yaklaşık 3 × 2 km'lik bir kutuda sorguladım:

| Bölge (bbox) | Bina | `height` dolu | `num_floors` dolu |
|---|---:|---:|---:|
| Delft merkez + TU Delft (`4.355,51.990,4.385,52.008`) | 6.283 | 493 | 1.600 |
| İTÜ Maslak (`29.015,41.095,29.045,41.115`) | 4.658 | 6 | 105 |
| ODTÜ Ankara (`32.765,39.880,32.795,39.900`) | 475 | 6 | 25 |
| ODTÜ KKK (`33.008,35.236,33.037,35.259`) | 466 | 9 | 141 |

Delft'te OSM'de bile yükseklik bilgisi çok daha dolu. Asıl fark ise 3DBAG'den geliyor: orada **her binanın** LiDAR'dan ölçülmüş yüksekliği hazır. Türkiye'deki adaylarda yükseklik bilgisi neredeyse hiç yok.

### Sonuç

- **Dünyada:** Hollanda. Açık, kayıtsız, ülke geneli 0.5 m LiDAR ve LoD2 bina verisinin bir arada olduğu en olgun yer.
- **Türkiye'de:** İstanbul, ama veri açık değil. Açık veriyle çalışınca Türkiye'deki hiçbir bölge kampüse göre belirgin bir avantaj sağlamıyor (30 m DEM + OSM). İstanbul ancak İBB'den veri alınırsa anlam kazanır; bunun için danışman üzerinden resmi talep gerekir ve süresi belirsiz.
- Fiziksel demo kampüste kalacağı için önerim aynı: **kampüs (demo) + Delft (yazılım, yüksek çözünürlüklü karşılaştırma)**.

*Doğrulama notu: Bina sayıları bu oturumda Overture'dan sorgulandı. Kaynakların çözünürlük ve lisans bilgileri yayımlanmış sayfalardan okundu, ama bu oturumda indirilmedi. İstanbul verisinin açık olmadığı, bulunamamasından yapılan bir çıkarım.*

---

## 8. Güncel öneri: harita yalnızca karar motorunda (19 Ekim 2026)

Demo masa ölçeğinde olacağı için, pilot bölgenin demo sahasıyla aynı yer olması gerekmiyor. Seçimi tamamen karar motorunun ihtiyaçları belirliyor.

### Öneri: Hollanda, Delft – Rotterdam The Hague Havalimanı (RTM) koridoru

Önerilen AOI (WGS84 bbox): yaklaşık `4.34, 51.94, 4.45, 52.02` (~7 × 9 km)

Bu bölge **korunan kritik bir tesis** olarak bir havalimanını, bir üniversite kampüsünü (TU Delft), yoğun yerleşimi ve otoyolları bir arada içeriyor. Karar motorunun ihtiyaç duyduğu her katmanın açık ve resmi bir kaynağı var:

| Karar motoru ihtiyacı | Kaynak |
|---|---|
| Yüksek çözünürlüklü yüzey ve arazi modeli | AHN: 0.5 m DSM ve DTM, CC0 |
| Görüş hattı ve maskeleme için bina yükseklikleri | 3DBAG: her bina LoD1.3 ve LoD2.2, LiDAR'dan ölçülmüş |
| Korunan bölgeler / yasak alanlar | [LVNL drone no-fly zones, PDOK OGC API](https://api.pdok.nl/lvnl/drone-no-flyzones/ogc/v1). Resmi dron yasak bölgeleri, makine tarafından okunabilir |
| Normal hava trafiği tabanı | OpenSky; Hollanda alıcı yoğunluğu en yüksek bölgelerden biri (çıkarım, sorguyla doğrulanmalı) |
| Yol ağı ve tesisler | OSM: Delft'te 6.283 bina, 1.600'ünde kat bilgisi (Overture sorgusu) |

### Bilinen zayıf nokta

Hollanda düz bir ülke; arazi kaynaklı maskeleme neredeyse yok. Alçak irtifada uçan dronlar için asıl engel binalar ve ağaçlar, bu yüzden kentsel bir AOI'de maskelemeyi 3DBAG ve AHN DSM sağlar. Raporda arazi (rölyef) maskelemesini ayrıca göstermek istenirse ikinci senaryo olarak **İsviçre** eklenebilir. swisstopo verileri 2021'den beri ücretsiz ([Free geodata OGD](https://www.swisstopo.admin.ch/en/free-geodata-ogd)); swissALTI3D / swissSURFACE3D 0.5 m ve swissBUILDINGS3D sunuyor.

### Demoyu haritaya bağlamak

Masa üstündeki demo alanını AOI'de bir bölgeye ölçekli olarak eşleyin (ör. 1 m masa = 100 m arazi). Düğümlerin masadaki konumları bu ölçekle haritaya, örneğin havalimanının çevresine yerleştirilir. Maket tespit edildiğinde ölçülen konumu aynı dönüşümle haritaya düşer; karar motoru gerçek binalar, gerçek yasak bölgeler ve gerçek hava trafiği üzerinde çalışır. Bu dönüşüm basit bir benzerlik dönüşümü (ölçek + döndürme + öteleme) ve bir konfigürasyon dosyasında tutulabilir.

### Türkiye

Değişen bir şey yok. Türkiye'nin en zengin verisi İstanbul'da, ama açık değil. Açık veriyle Türkiye'de hiçbir bölge 30 m DEM + OSM'in ötesine geçmiyor.

### Repoda değişmesi gerekenler

- Katman 1'e AHN, 3DBAG ve PDOK no-fly zones kaynaklarını ekleyin. Erişimleri doğrulandıkça `docs/verified-access-log.md`'ye yazın.
- AW3D30 / Copernicus 30 m'yi geniş alan veya yedek kaynak olarak bırakabilirsiniz.
- Öneride (proposal) "Terrain is taken from the ALOS World 3D 30 m surface model" cümlesi, seçilen bölgeye göre güncellenmeli.

*Doğrulama notu: Bu oturumdan PDOK, 3DBAG ve swisstopo sunucularına ağ erişimi yoktu; bu kaynakların bilgileri yayımlanmış sayfalardan okundu. İlk iş bu üç kaynaktan AOI için birer küçük indirme yapıp erişimi doğrulamak.*

---

## 9. Askeri / havalimanı odaklı öneri: Eindhoven (19 Ekim 2026)

### Öneri: Eindhoven Havalimanı / Eindhoven Hava Üssü, Hollanda

Önerilen AOI (WGS84 bbox): `5.355, 51.440, 5.420, 51.470` (~4.5 × 3.3 km, pist ve çevresi)

**Neden Eindhoven:**

1. **Sivil ve askeri ortak bir havalimanı.** Aynı pisti hem sivil hem askeri uçuşlar kullanıyor. Senaryo hem "kritik sivil altyapı" hem "askeri tesis koruması" olarak çerçevelenebilir. Bildiğim kadarıyla üs, NATO ve AB ortak birliklerine (çok uluslu MRTT tanker filosu, EATC) ev sahipliği yapıyor; bunu raporda kullanmadan önce resmi kaynaktan doğrulayın.
2. **Gerçek bir C-UAS olayı yaşanmış.** 22 Kasım 2025'te birden fazla dron görüldükten sonra Eindhoven'da tüm hava trafiği saatlerce durduruldu. Savunma Bakanı dron savunma sistemlerinin devreye alındığını söyledi ([Al Jazeera](https://www.aljazeera.com/news/2025/11/22/air-traffic-suspended-at-netherlands-airport-after-drone-sightings)). Aynı akşamlarda Volkel Hava Üssü'nde de dronlar görüldü ve askerler yerden ateş açtı ([Militär Aktuell](https://militaeraktuell.at/en/drones-over-dutch-airfields-armed-forces-opened-fire/)). Bu, sistemin "olay yeniden canlandırma" senaryosu için gerçek ve kaynaklı bir referans.
3. **Hollanda'nın açık verileri burada da tam:** AHN 0.5 m DSM/DTM, 3DBAG, PDOK dron yasak bölgeleri ve OpenSky.
4. **Bina verisi** (Overture 2026-09-23.1, bu oturumda sorgulandı): AOI'de 4.171 bina var, 543'ünde yükseklik bilgisi dolu. Sınıflar arasında 25 `hangar`, 142 `industrial` ve 26 `office` bulunuyor. 3DBAG ile bütün binaların yüksekliği hazır gelir.

### Karar motoru için senaryo fikri

- **Korunan varlıklar:** Pist, apron, hangarlar ve terminal. OSM'deki `aeroway=*` etiketleri ve PDOK yasak bölgesi poligonu kullanılır.
- **Hava trafiği tabanı:** OpenSky'dan Eindhoven'a iniş ve kalkış yapan trafik çekilir; normal yaklaşma koridorları buradan çıkarılır.
- **Tehdit:** Masadaki maket, ölçekli dönüşümle (bölüm 8) havalimanı çevresine yerleştirilir. Karar motoru izi yasak bölge, pist yaklaşma koridoru ve bina maskelemesine göre puanlar.
- **Öneri:** ATP 3-01.81 gibi doktrin belgelerine dayanarak, ör. "uçuşları durdur", "sensörleri şu sektöre yönlendir", "güvenli tahliye rotası".
- **Doğrulama:** 22 Kasım 2025 olayının kamuya açık zaman çizelgesi (trafik durdurma süresi) ile sistemin önerdiği tepki karşılaştırılabilir. OpenSky'dan o geceye ait trafik kesintisi de görülebilir (çıkarım, sorguyla doğrulanmalı).

### Alternatifler

| Bölge | Artısı | Neden ikinci planda |
|---|---|---|
| **Volkel Hava Üssü (NL)** | Saf askeri üs, Kasım 2025'te dron olayı yaşandı | Çok hassas bir üs ve yanında sivil trafik yok, OpenSky tabanı zayıf kalır. Gerçek bir askeri üssün açık analizini yayımlamak riskli |
| **Rotterdam The Hague (NL)** | Bölüm 8'deki öneri, TU Delft'e yakın | Askeri bileşeni yok |
| **Geilenkirchen (DE, NRW)** | NATO E-3A AWACS üssü, NRW 1 m LiDAR + LoD2 | Saf askeri üs (Volkel ile aynı sorun) |
| **Türkiye'deki askeri bölgeler** | Ulusal bağlam | 2565 sayılı Askeri Yasak Bölgeler Kanunu nedeniyle haritalama ve görüntüleme kısıtlı. Açık veri de yok. **Önermiyorum** |

### Dikkat edilmesi gereken bir nokta

Repo herkese açık. Gerçek ve aktif bir askeri tesis için **ayrıntılı zafiyet çıktılarını** (sensör kör noktaları, en az tespit edilen yaklaşma koridorları) herkese açık yayımlamayın. Sistem savunma amaçlı olsa da bu çıktılar tersine kullanılabilir. Öneri:

- Repoda yalnızca açık kaynakları ve yöntemi tutun.
- Eindhoven'a özgü risk haritalarını ve kör nokta analizlerini raporda ve demoda gösterin, ama herkese açık repoya koymayın (ya da gerçek koordinatları kaydırılmış / anonimleştirilmiş bir sürüm koyun).
- Bu sınırı danışmanlarla da konuşun; jüri için iyi bir "etik ve güvenlik" maddesi olur.
