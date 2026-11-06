# Why Eindhoven Airport? / Neden Eindhoven Havalimanı?

*Toplantı için konuşma notları. Her madde önce İngilizce, altında Türkçe.*

---

## 1. Kısa giriş (30 saniyelik özet)

**EN:** We propose Eindhoven Airport in the Netherlands as our pilot area. It is a shared civil–military airport, it experienced a real drone incident in November 2025, and it has some of the most detailed open geospatial data in the world.

**TR:** Pilot bölge olarak Hollanda'daki Eindhoven Havalimanı'nı öneriyoruz. Burası sivil ve askeri ortak kullanılan bir havalimanı. Kasım 2025'te gerçek bir dron olayı yaşandı ve dünyadaki en detaylı açık coğrafi verilerin bir kısmına sahip.

---

## 2. Gerekçeler

### 2.1 Civil–military airport / Sivil-askeri havalimanı

**EN:** Eindhoven is used by both civilian airlines and the Royal Netherlands Air Force. This lets us frame the scenario both as critical civil infrastructure protection and as military base protection, which fits the NATO / C4ISR theme of our project.

**TR:** Eindhoven'ı hem sivil havayolları hem de Hollanda Hava Kuvvetleri kullanıyor. Bu sayede senaryoyu hem kritik sivil altyapı koruması hem de askeri üs koruması olarak kurabiliyoruz. Bu da projemizin NATO / C4ISR temasıyla örtüşüyor.

### 2.2 A real, documented incident / Gerçek ve belgelenmiş bir olay

**EN:** On 22 November 2025, all air traffic at Eindhoven was suspended for several hours after multiple drone sightings, and the Dutch Defence Minister confirmed that counter-drone systems were activated. Around the same time, soldiers at nearby Volkel Air Base fired at drones. This gives us a real, citable scenario to test our decision engine against.

**TR:** 22 Kasım 2025'te birden fazla dron görülmesi üzerine Eindhoven'daki tüm hava trafiği saatlerce durduruldu. Hollanda Savunma Bakanı dron savunma sistemlerinin devreye alındığını doğruladı. Aynı günlerde yakındaki Volkel Hava Üssü'nde askerler dronlara ateş açtı. Bu olay, karar motorumuzu test edebileceğimiz gerçek ve kaynak gösterilebilir bir senaryo sunuyor.

### 2.3 Highest-resolution open terrain data / En yüksek çözünürlüklü açık arazi verisi

**EN:** The Netherlands provides a national LiDAR elevation model, AHN, at 0.5 m resolution under a CC0 licence. That is sixty times finer than the 30 m global models we had for our campus. For line-of-sight and masking calculations this difference is decisive.

**TR:** Hollanda, AHN adlı ulusal LiDAR yükseklik modelini 0.5 m çözünürlükte ve CC0 lisansıyla sunuyor. Bu, kampüs için elimizde olan 30 m'lik küresel modellerden altmış kat daha ince. Görüş hattı ve maskeleme hesaplarında bu fark belirleyici.

### 2.4 3D model of every building / Her binanın 3D modeli

**EN:** The 3DBAG dataset provides 3D models of about 10 million Dutch buildings, with heights measured from LiDAR and detailed roof shapes. Low-flying drones are mostly masked by buildings and trees, not by hills, so this is exactly the data our risk engine needs.

**TR:** 3DBAG veri seti, Hollanda'daki yaklaşık 10 milyon binanın LiDAR ile ölçülmüş yükseklikli ve çatı şekilli 3D modelini sunuyor. Alçak uçan dronları çoğunlukla tepeler değil binalar ve ağaçlar gizler. Bu yüzden risk motorumuzun ihtiyaç duyduğu veri tam olarak bu.

### 2.5 Official drone no-fly zones as open data / Resmi dron yasak bölgeleri açık veri olarak

**EN:** The Dutch government publishes official drone no-fly zones as a machine-readable API through PDOK. Our decision engine can use these directly as protected areas instead of drawing them by hand.

**TR:** Hollanda hükümeti resmi dron yasak bölgelerini PDOK üzerinden makine tarafından okunabilir bir API olarak yayımlıyor. Karar motorumuz bunları elle çizmek yerine doğrudan korunan alan olarak kullanabilir.

### 2.6 Real civil air traffic for the baseline / Taban için gerçek sivil hava trafiği

**EN:** Because Eindhoven also has civilian traffic, we can extract normal approach and departure patterns from the OpenSky Network and use them as the baseline for anomaly detection. A purely military base would not give us this.

**TR:** Eindhoven'da sivil trafik de olduğu için OpenSky Network'ten normal iniş ve kalkış örüntülerini çıkarıp anomali tespiti için taban olarak kullanabiliriz. Saf bir askeri üs bize bunu sağlamazdı.

### 2.7 We checked the data ourselves / Veriyi kendimiz kontrol ettik

**EN:** We queried the Overture Maps building layer for the airport area: there are about 4,200 buildings, including 25 hangars, and more than 500 already have height values even before using 3DBAG. For comparison, our campus area has 466 buildings and only 9 with height values.

**TR:** Havalimanı bölgesi için Overture Maps bina katmanını sorguladık. Yaklaşık 4.200 bina var, bunların 25'i hangar. 3DBAG'i kullanmadan bile 500'den fazlasında yükseklik bilgisi mevcut. Karşılaştırma için, kampüs bölgemizde 466 bina var ve yalnızca 9'unda yükseklik bilgisi bulunuyor.

---

## 3. Olası sorulara cevaplar

**Soru: Why not our own campus? / Neden kendi kampüsümüz değil?**

**EN:** Our physical demo is small-scale, with masts under one metre, so the map is used only by the decision engine. Northern Cyprus has no open high-resolution data; we would be limited to 30 m elevation models. We map the tabletop demo area onto the airport with a scaled transformation, so the live detections still run on real terrain and buildings.

**TR:** Fiziksel demomuz küçük ölçekli ve direkler bir metreden kısa. Bu yüzden harita yalnızca karar motorunda kullanılıyor. Kuzey Kıbrıs'ta açık yüksek çözünürlüklü veri yok, 30 m'lik yükseklik modelleriyle sınırlı kalırdık. Masa üstü demo alanını ölçekli bir dönüşümle havalimanına eşliyoruz. Böylece canlı tespitler yine gerçek arazi ve binalar üzerinde çalışıyor.

**Soru: Why not a site in Türkiye? / Neden Türkiye'den bir yer değil?**

**EN:** The richest Turkish data is in Istanbul, but it is not openly downloadable. Military areas in Türkiye are also restricted for mapping by law. Open data in Türkiye does not go beyond 30 m elevation and OpenStreetMap.

**TR:** Türkiye'deki en zengin veri İstanbul'da, ama açık olarak indirilemiyor. Ayrıca Türkiye'deki askeri bölgelerin haritalanması kanunla kısıtlı. Türkiye'deki açık veri, 30 m yükseklik modeli ve OpenStreetMap'in ötesine geçmiyor.

**Soru: Why not a purely military base such as Volkel? / Neden Volkel gibi saf bir askeri üs değil?**

**EN:** A purely military base has no civilian traffic for the baseline, and publishing a detailed analysis of an active military base is sensitive. Eindhoven gives us the military context while keeping the analysis on public, civilian-facing data.

**TR:** Saf bir askeri üste taban için sivil trafik yok. Ayrıca aktif bir askeri üssün ayrıntılı analizini yayımlamak hassas bir konu. Eindhoven bize askeri bağlamı veriyor, analizi de kamuya açık ve sivil tarafa dönük veriler üzerinde tutuyor.

**Soru: Is this ethically and legally safe? / Bu etik ve hukuki olarak güvenli mi?**

**EN:** We use only openly published data. Our repository will contain only the sources and the method. Detailed vulnerability outputs, such as sensor blind spots, will be shown only in the report and the demo, not published in the public repository.

**TR:** Yalnızca açık olarak yayımlanmış verileri kullanıyoruz. Repomuz sadece kaynakları ve yöntemi içerecek. Sensör kör noktaları gibi ayrıntılı zafiyet çıktıları yalnızca raporda ve demoda gösterilecek, herkese açık repoda yayımlanmayacak.

**Soru: What is the weakness of this choice? / Bu seçimin zayıf noktası ne?**

**EN:** The Netherlands is flat, so terrain masking from hills is minimal; masking comes mainly from buildings. If needed, we can add a second scenario in Switzerland, which offers free 0.5 m data in mountainous terrain.

**TR:** Hollanda düz bir ülke, bu yüzden tepelerden kaynaklı arazi maskelemesi çok az; maskeleme çoğunlukla binalardan geliyor. Gerekirse İsviçre'de ikinci bir senaryo ekleyebiliriz. İsviçre dağlık arazide ücretsiz 0.5 m veri sunuyor.

---

## 4. Kapanış cümlesi

**EN:** In short, Eindhoven combines a NATO-relevant military context, a real and recent drone incident, and world-class open data in one place.

**TR:** Kısacası Eindhoven, NATO ile ilişkilendirilebilecek askeri bağlamı, yakın tarihli gerçek bir dron olayını ve dünya standartlarında açık veriyi tek bir yerde bir araya getiriyor.

---

## Online kaynaklar

**Olay (22 Kasım 2025)**
- Al Jazeera, "Air traffic suspended at Netherlands airport after drone sightings" (22 Kasım 2025): https://www.aljazeera.com/news/2025/11/22/air-traffic-suspended-at-netherlands-airport-after-drone-sightings
- Militär Aktuell, "Drones over Dutch airfields: armed forces opened fire" (23 Kasım 2025): https://militaeraktuell.at/en/drones-over-dutch-airfields-armed-forces-opened-fire/
- blue News, "Drones disrupt air traffic in Eindhoven": https://www.bluewin.ch/en/news/international/drones-disrupt-air-traffic-in-eindhoven-2975461.html

**Coğrafi veri**
- AHN, Hollanda 0.5 m DTM/DSM, CC0 (Google Earth Engine katalog sayfası): https://developers.google.cn/earth-engine/datasets/catalog/AHN_AHN3?hl=en
- 3DBAG, 10 milyon binanın 3D modeli (GIM International): https://www.gim-international.com/content/article/3dbag-automatically-generated-3d-models-of-10-million-buildings
- PDOK / LVNL, dron yasak bölgeleri OGC API: https://api.pdok.nl/lvnl/drone-no-flyzones/ogc/v1
- Hollanda hükümeti, "Where can I fly a drone?": https://www.government.nl/faq/aviation/where-can-i-fly-a-drone
- OpenSky Network: https://opensky-network.org
- Overture Maps (bina sayımında kullanılan 2026-09-23.1 sürümü): https://overturemaps.org

**Alternatif / karşılaştırma**
- swisstopo ücretsiz coğrafi veri (OGD): https://www.swisstopo.admin.ch/en/free-geodata-ogd
- İstanbul 3D kent modeli ve LiDAR (GIM International): https://www.gim-international.com/content/article/3d-city-modelling-of-istanbul

---

*Not: Bina sayıları bu çalışmada Overture'dan sorgulandı. AHN, 3DBAG ve PDOK bilgileri yayımlanmış sayfalardan alındı, veriler henüz indirilmedi. Toplantıdan önce ekipten biri AHN veya 3DBAG'den küçük bir indirme yapıp `docs/verified-access-log.md`'ye eklerse, "veriye kendimiz eriştik" demek daha güçlü olur.*
