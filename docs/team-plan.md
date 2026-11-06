# Görev Dağılımı ve Dönem Planı

> **İlk plan (15 Ekim 2026).** Plan rollerle yazıldı; roller ve kişiler:
>
> | Rol | Kişi |
> |---|---|
> | EEE | Adil Mert İş |
> | CNG 1 | Yaren Duyan |
> | CNG 2 | Aydan Doğan |
> | CNG 3 | Yağız Akkaya |
> | CNG 4 | Mert Gökalp |

Oct 15, 2026 · @yağız akkaya

## Özet

Ekip 5 kişi (4 CNG + 1 EEE) ve sistem 5 katmanlı; herkes bir **birincil katmanın** sahibi olur, yoğunluğu ters zamana düşen bir **ikincil iş** de alır. Böylece birinin işi azaldığında diğer işi yoğunlaşır ve dönem boyunca kimse boş kalmaz.

Dengenin anahtarı ilk haftalarda yazılacak **arayüz sözleşmeleridir** (track mesajı, risk grid API, RAG API). Bunlar sayesinde herkes sahte (mock) veriyle ilk haftadan çalışabilir; kimse başkasının modülünü beklemez.

Varsayım: ESC 491 için 14 haftalık dönem, 1. hafta Eylül sonu; bugün yaklaşık 3–4. haftadayız. Takvim farklıysa fazlar kaydırılır.

## Kim hangi katmandan sorumlu

Birincil katmanlar README'deki rol tablosuyla aynıdır; yeni olan ikincil işler ve bunların hangi haftalarda devreye girdiğidir.

| Kişi | Birincil (sahibi olduğu katman) | İkincil (ters zamanda yoğunlaşan iş) | Birincilin yoğun haftaları | İkincilin yoğun haftaları |
| --- | --- | --- | --- | --- |
| EEE | Sensör düğümü donanımı + Wi-Fi/RF kontrol linki tespiti (Katman 1, sensör kısmı) | Tespit menzili / link bütçesi modeli ve RCS gerekçesi (Katman 4); saha testi lideri | 4–12 | 1–3 ve 11–14 |
| CNG 1 | Arazi + OSM modeli, grid risk yayılımı, görüş hattı, A\*/Dijkstra rota (Katman 1 harita + Katman 3) | Risk modelinin FAA/ACLED kayıtlarıyla doğrulanması, performans testleri; C2 haritasına katman verisi | 1–9 | 9–14 |
| CNG 2 | Kamera ile edge-AI tespit ve sürü takibi (Katman 1, görüntü kısmı) | EEE ile Jetson'a TensorRT kurulumu; sahada kendi veri setimizin kaydı ve etiketlenmesi | 3–10 | 10–14 |
| CNG 3 | Doktrin bilgi bankası, RAG + yerel LLM, kaynakça zorunluluğu (Katman 2) | Test senaryoları ve değerlendirme metrikleri; raporların editörü; arayüzdeki açıklama metinleri | 1–9 | 8–14 |
| CNG 4 | Füzyon, tehdit skoru, öneri motoru, C2 web arayüzü + MIL-STD-2525 semboller (Katman 4 + 5) | Sistem mimarisi, arayüz sözleşmeleri ve sahte veri simülatörü; entegrasyon lideri | 6–14 | 1–5 |

## Boş kalma riski nerede

Katmanlar aynı anda yoğunlaşmadığı için, önlem alınmazsa iki kişi dönem başında, bir kişi dönem sonunda boşta kalır.

- **CNG 4 (füzyon/C2) başta boş kalır**, çünkü tüm katmanların çıktısını bekler. Önlem: ilk 5 haftada mimariyi, mesaj şemalarını ve sahte track üreten simülatörü yazar; arayüz iskeletini bu sahte veriyle kurar.
- **EEE başta donanımı bekler** (Jetson/Pi, kamera, Wi-Fi adaptörü, direk, 3D baskı). Önlem: donanım gelene kadar DroneRF verisiyle RF tespitini masa başında geliştirir ve link bütçesi / menzil modelini kurar.
- **CNG 3 (RAG) erken biter**, çünkü bilgi bankası diğer katmanlardan bağımsızdır. Önlem: 8. haftadan itibaren test senaryoları, değerlendirme ve rapor editörlüğü ona geçer.
- **CNG 1 ve CNG 2 ortada çok yoğun**, sonda hafifler. Önlem: sonda doğrulama, saha verisi ve edge kurulumu gibi ikincil işleri alırlar.

## 14 haftalık takvim: her fazda herkesin işi

Dönem 5 faza bölünür ve her hücre o kişinin o fazdaki somut işidir; boş hücre yoktur. Her faz çalışan bir çıktıyla biter.

| Faz | EEE | CNG 1 (harita + risk) | CNG 2 (görüntü tespit) | CNG 3 (bilgi bankası) | CNG 4 (füzyon + C2) |
| --- | --- | --- | --- | --- | --- |
| **F1 · Hafta 1–3** Gereksinim ve sözleşmeler | Donanım listesi ve sipariş; link bütçesi ve tespit menzili hesabı; RF mesaj alanlarını tanımlar | Kampüs test alanını seçer; AW3D30 + OSM'yi PostGIS'e yükler | DUT Anti-UAV, UAVSwarm, Halmstad indirme ve format dönüşümü; YOLO baseline | Doktrin korpusunu toplar (ATP 3-01.81, RAND, CNAS…), sayfa numaralı parçalar | Sistem mimarisi; track / risk / RAG JSON şemaları; repo, Docker, GitHub proje panosu |
| **F2 · Hafta 4–6** Bağımsız prototipler | DroneRF ile RF tespit modeli; ilk Pi/ESP32 monitor-mode denemesi | Grid risk yayılımı + görüş hattı (terrain masking) | YOLO eğitimi ve mAP ölçümü | FAISS/Qdrant + Ollama ile kaynak gösteren RAG | Sahte track simülatörü; Leaflet haritası + milsymbol iskeleti |
| **F3 · Hafta 7–9** İlk uçtan uca (masa başı) | Tek düğümün kamera + Wi-Fi ile kurulumu; RF track mesajı yayınlar | A\*/Dijkstra güvenli rota; risk API'si | Çoklu hedef / sürü takibi; kayıtlı videodan track mesajı | RAG API'si; ilk test senaryoları (8. haftadan) | Füzyon + tehdit skoru; tüm modülleri kayıtlı veriyle birleştirir |
| **F4 · Hafta 10–12** Donanımda ve sahada | 2–3 düğüm, direkler, güç; 3D baskı dron maketi + verici; saha testi yönetimi | Risk modelini FAA/ACLED ile doğrular; performans | EEE ile Jetson'da TensorRT; saha kayıtlarını etiketler | Senaryo bazlı değerlendirme (doğruluk, kaynak isabeti); açıklama metinleri | Öneri motoru; canlı veriyle arayüz; gecikme ölçümü |
| **F5 · Hafta 13–14** Final | Donanım ve saha testi bölümü; demo kurulumu | Algoritma bölümü + harita figürleri | Tespit sonuçları bölümü | Rapor editörlüğü, kaynakça, sunum akışı | Mimari bölümü; demo senaryosu ve canlı gösterim |

ESC 491 yalnızca tasarım raporuyla bitiyorsa F4 ve F5'in uygulama kısmı ESC 492'ye kayar; dağılım aynı kalır.

## Teslim noktaları ve denge kuralları

Her faz sonunda herkesin gösterebileceği bir çıktı olur; bir kişi bunu gösteremiyorsa iş dağılımı o hafta düzeltilir.

| Hafta | Teslim | Sorumlu |
| --- | --- | --- |
| 3 | Arayüz sözleşmeleri (JSON şemaları) ve donanım siparişi | CNG 4, EEE |
| 6 | Her katman sahte veriyle tek başına çalışıyor | Herkes |
| 8 | Ara rapor / ilerleme sunumu | CNG 3 (editör), herkes kendi bölümü |
| 9 | Kayıtlı veriyle uçtan uca demo (masa başı) | CNG 4 |
| 12 | Sahada tek düğümlü canlı tespit, haritada gösterim | EEE, CNG 2 |
| 14 | Final rapor, sunum, demo v1 | Herkes |

- **Haftalık 15 dakikalık toplantı:** herkes "bu hafta çalışan ne gösteriyorum" sorusuna cevap verir.
- **Her iş bir GitHub issue'su:** sahibi ve hafta etiketi olur; panoda bir kişinin açık işi kalmadıysa ikincil listesinden çeker.
- **Dönüşümlü entegrasyon nöbetçisi:** her hafta bir kişi ana dalın çalıştığını kontrol eder; böylece entegrasyon yükü yalnız CNG 4'e kalmaz.
- **Rapor yazımı sürekli:** herkes kendi bölümünü faz sonunda bir sayfa olarak yazar; son iki haftaya yığılmaz.
- **EEE yalnız değil:** donanım işlerinde her fazda bir CNG kişisi eş olarak atanır (F1–F2 CNG 4, F3–F5 CNG 2), çünkü 1 EEE kişisi fiziksel demonun tamamını taşıyamaz.

## ESC 492'de devam

Aynı birincil sahiplikler korunur; ikinci dönemde yoğunluk sahaya ve iyileştirmeye kayar.

- **EEE:** düğüm sayısını artırma, RF'den yaklaşık yön/konum, güç ve dayanıklılık.
- **CNG 1:** çoklu düğüm görüş alanıyla risk haritası, dinamik yeniden rota.
- **CNG 2:** saha verisiyle ince ayar (fine-tune), sürü senaryoları, OpenSky anomali tespiti.
- **CNG 3:** RAG kalitesinin ölçülmesi, final raporun editörlüğü, kullanıcı testi.
- **CNG 4:** çoklu sensör füzyonu, operatör arayüzünün cilası, final demo senaryosu.
