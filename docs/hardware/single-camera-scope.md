> **Not (6 Kasım 2026):** Bu belge kapsamı daraltan varsayımların ve mimarinin kaynağıdır. Hocalara gönderilip kabul edilen nihai kalem ve fiyat listesi [`README.md`](./README.md) dosyasındadır; fiyat veya kalem farkı varsa o geçerlidir.

# Asgari Donanım Listesi: Tek IP Kamera, Tek Düğüm

*ESC 491/492 · 2 Kasım 2026 · Taslak: ekip onayı bekliyor*

Meryem hoca bütçe bilgisi olmadığını ve listenin olabildiğince basit, ucuz tutulması gerektiğini söyledi. Bu yüzden Sohail hocanın üç kamera seçeneğinden Raspberry Pi'siz IP kamera seçeneği, tek kamera ve tek düğümle alındı. Kapsam aşağıdaki varsayımlarla daraltıldı. Ayrıntılı karşılaştırma: `birlesik-donanim-listesi.md`.

## Mimari

```
[IP kamera] ──Cat6 ~30 m──► [PoE enjektörü] ──► Dizüstü (tespit, risk motoru, C2, LLM API)
                                                  ▲
                         [ESP32 alıcı] ──USB──────┘   (dizüstünün yanında, alan kenarında)
```

- Kamera gücü ve görüntüsü tek kablodan gelir. Görüntü doğrudan dizüstüne akar. Pi ve switch gerekmez.
- ESP32 alıcı dizüstünün yanında durur ve USB'den hem güç alır hem veri gönderir. Görevi drone'un varlığını ve kimliğini doğrulamak, konum bulmak değil. Bu yüzden alanın kenarında durması yeterli.

## Talep tablosu

| # | Kalem | Adet | Yaklaşık fiyat | Kullanım |
|---|---|---|---|---|
| 1 | Dış mekan PoE IP kamera, 4 MP, motorlu varifokal lens (2,8–12 mm), RTSP/ONVIF. Örn. **Hikvision DS-2CD1643G2-LIZSU** (model kodunu teyit edin) | 1 | ~₺5.000 | Görsel tespit |
| 2 | PoE enjektörü (802.3af, gigabit) | 1 | ~₺500–800 (tahmin) | Kameraya güç; dizüstüne veri |
| 3 | Dış mekan Cat6 kablo, ~30 m, uçları takılı | 1 | ~₺750 | Kamera → enjektör |
| 4 | ESP32 geliştirme kartı (alıcı) | 1 | ~₺400 | Wi-Fi dinleme: MAC ve sinyal gücü |
| 5 | ESP32 için USB veri kablosu | 1 | ~₺200 | ESP32 → dizüstü |
| 6 | Tripod / sehpa (1,5–2 m) | 1 | ~₺1.500 | Kamera sabitleme |
| 7 | Montaj aksesuarı (vida, kablo bağı, rakor) | 1 set | ~₺200–400 | Kurulum |
| 8 | Uzatma kablosu + çoklu priz | 1 | ~₺400–600 (tahmin) | Enjektör ve dizüstü gücü |
| 9 | ESP32 geliştirme kartı (verici, drone üzerinde) | 1 | ~₺400 | *Maket drone kararı kesinleşirse.* Sohail hocanın önerisi |
| 10 | 10.000 mAh powerbank | 1 | ~₺500 | *Madde 9 ile birlikte.* Sohail hoca: yerelden alınabilir, en kötü ihtimalle ödünç alınır, satın almak şart değil |

**Toplam: ~₺9.850–10.550.** Madde 9 ve 10 düşerse ~₺8.950–9.650. Fiyatlar Sohail hocanın listesinden; "tahmin" yazanlar tedarikçiden teyit edilmeli.

**Ekipten:** dizüstü (Ethernet girişi yoksa USB-Ethernet adaptörü), drone, şerit metre. **Formda ayrıca:** alan kullanım izni, dış mekanda drone uçurma izni, priz erişimi.

## Projeyi daraltan varsayımlar (rapora ve forma yazılabilir)

1. **Tek kamera, tek düğüm.** Sistem tek bir sensör düğümüyle gösterilir. Çok düğümlü mimari raporda ölçeklenebilir tasarım olarak anlatılır ama bitirme kapsamında kurulmaz (Sohail hocanın da gerekçesi: tüm düğümler aynı işi yapıyor).
   - **Sabit kamera, belirli bir alanı görür.** "Motorlu lens" yalnızca odak uzaklığının motorla 2,8–12 mm arasında ayarlanması demek; kamera dönmez (PTZ değil). Ölçekleme varsayımı (Sohail hoca): bir kamera ~60° görüyorsa 360° kapsama için 6 kamera gerekir. Bu raporda belirtilir ama 6 kamera alınmaz.
2. **Konum tek kameradan, bilinen uçuş yüksekliğiyle.** Üçgenleme yapılmaz. Drone'un sabit ve bilinen bir yükseklikte (ör. 3 m) uçtuğu varsayılır. Görüntüdeki konumu bu yükseklikle yere izdüşürülerek haritadaki konumu kestirilir.
3. **Uçuş bölgesi kamera görüş alanıyla sınırlı.** Drone kameradan en fazla ~15–20 m uzakta, lensin ayarlandığı açı içinde uçar. Bu sınır yazılımda geofence ile uygulanır.
4. **Tek hedef, gündüz, açık hava.** Aynı anda tek drone. Gece, yağmur ve sis kapsam dışı.
5. **RF tarafı yalnızca doğrulama yapar.** Tek ESP32 drone'un varlığını ve kimliğini (bilinen MAC) doğrular, konum vermez. Kampüs Wi-Fi'ı ve telefonlar gibi diğer yayınlar MAC filtresiyle ayıklanır (Sohail hocanın parazit notu).
6. **İşlem merkezde.** Tespit, risk motoru ve arayüz dizüstünde çalışır. Dil modeli demo için API üzerinden kullanılır.
7. **Başarı ölçütü baştan tanımlı.** Örneğin "kameradan X m'ye kadar Y saniyede tespit" gibi bir hedef hocalarla birlikte yazılı belirlenir. Demo bu hedefe göre değerlendirilir. Saha test videoları yedek kanıt olarak saklanır.

## Sohail hocanın yönlendirmesi (2 Kasım)

Bitirme projesinde tam çalışan ürün beklenmiyor, fikir sunuluyor. Tek kamerayla çalışırsa 3 kamerayla da çalışır (üç paralel işlem). Basit tutmak daha iyi. Üniversitenin her şeyi almasını beklemeyin; ana kalemleri alırsa iyi sayılır. **Ana kalemler önceliği:** 1 (kamera), 2 (PoE enjektörü), 3 (kablo), 4–5 (ESP32 alıcı). Tripod, aksesuar, uzatma ve powerbank gerekirse ekipten veya ödünç karşılanır.

## Açık konular

- Maket drone + ESP32 verici mi, Tello sınıfı gerçek drone mu? (Madde 9–10'u belirler.)
- Ekip bu daraltmayı onaylıyor mu?
