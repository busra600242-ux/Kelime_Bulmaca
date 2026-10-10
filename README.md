# 🎮 Kelime Tahmin Oyunu

Python ile geliştirilmiş, rastgele seçilen kelimeyi verilen ipucundan tahmin etmeye dayalı basit bir kelime tahmin oyunu.

## 📌 Proje Hakkında

Bu projede Python'un `random` ve `json` modülleri kullanılarak bir kelime tahmin oyunu oluşturulmuştur.

Program, `kelimeler.json` dosyasından rastgele bir kelime seçer ve oyuncudan bu kelimeyi tahmin etmesini ister. Oyuncuya kelimenin anlamı ipucu olarak verilir. Oyuncunun doğru kelimeyi bulmak için 5 tahmin hakkı vardır.

## ✨ Özellikler

- 🎲 JSON dosyasından rastgele kelime seçimi
- 💡 Kelimenin anlamını gösteren ipucu sistemi
- ⭐ Kelimenin uzunluğunu yıldızlarla gösterme
- 🔢 Her oyun için 5 tahmin hakkı
- 🔤 Büyük ve küçük harf farklılıklarını ortadan kaldırma
- 🧹 Kullanıcı girişindeki baştaki ve sondaki boşlukları temizleme
- ✅ Doğru cevap verildiğinde oyunu bitirme
- ❌ Tahmin hakları bittiğinde doğru kelimeyi gösterme

## 🛠️ Kullanılan Teknolojiler

- **Python:** Oyunun temel programlama dili
- **JSON:** Kelimeleri ve anlamlarını saklamak için kullanılan veri formatı
- **random:** Kelimeler arasından rastgele seçim yapmak için kullanılan modül

## 📁 Proje Dosyaları

Proje aşağıdaki dosyalardan oluşur:

```text
kelime-tahmin-oyunu/
├── main.py
├── kelimeler.json
└── README.md
```

- `main.py`: Oyunun çalışma mantığını ve tahmin sürecini içerir.
- `kelimeler.json`: Tahmin edilecek kelimeleri ve bu kelimelerin anlamlarını içerir.
- `README.md`: Projenin açıklamasını ve kullanım talimatlarını içerir.

## 🚀 Kurulum ve Çalıştırma

**1.** Python'un bilgisayarınızda kurulu olduğundan emin olun.

**2.** Proje dosyalarını bilgisayarınıza indirin veya GitHub deposunu klonlayın.

**3.** `main.py` ve `kelimeler.json` dosyalarının aynı klasörde bulunduğundan emin olun.

**4.** Terminali proje klasöründe açın ve aşağıdaki komutu çalıştırın:

```bash
python main.py
```

Bazı sistemlerde şu komutu kullanmanız gerekebilir:

```bash
python3 main.py
```

Projenin çalışması için ayrıca bir Python paketi yüklemeniz gerekmez. Kullanılan `json` ve `random` modülleri Python'un standart kütüphanesinde bulunur.

## 🎯 Nasıl Oynanır?

1. Program, JSON dosyasından rastgele bir kelime seçer.
2. Kelimenin harf sayısı yıldızlarla gösterilir.
3. Kelimenin anlamı ipucu olarak ekrana yazdırılır.
4. Oyuncu tahminini girer.
5. Doğru tahmin yapılırsa oyun sona erer.
6. Yanlış tahminde kalan hak sayısı bir azalır.
7. Beş tahmin hakkı da kullanılırsa doğru kelime açıklanır ve oyun sona erer.

### Örnek Oyun

```text
Kelimeniz: ****** Uzunluğu: 6
İpucu: Yazın dilimlenince serinleten, içi kırmızı, kabuğu yeşil çizgili dev meyve
Kelime Tahmininizi Yazınız: karpuz
Doğru cevap bildiniz! Kelimeniz: karpuz
```

## 🗂️ JSON Veri Yapısı

`kelimeler.json` dosyasında her kelime, `kelime` ve `anlam` anahtarlarına sahip bir nesne olarak saklanır.

Örnek:

```json
[
    {
        "kelime": "muz",
        "anlam": "Kabuğuna basan kayar, maymunların da gözdesi olan sarı meyve"
    },
    {
        "kelime": "kiraz",
        "anlam": "Pastanın tepesinde duran, çift çift sallanan küçük kırmızı meyve"
    }
]
```

Yeni kelimeler eklemek için JSON listesine aynı yapıda yeni nesneler eklenebilir.

## 📚 Öğrenilen Konular

Bu proje geliştirilirken aşağıdaki Python konuları uygulanmıştır:

- Dosya işlemleri (`open`)
- JSON verilerini okuma (`json.load`)
- Rastgele seçim (`random.choice`)
- Döngüler (`while`)
- Koşullu ifadeler (`if-else`)
- Kullanıcıdan veri alma (`input`)
- String işlemleri (`lower`, `strip`)
- Değişkenler ve sayaç mantığı
- Liste ve sözlük yapıları

## 📄 Lisans

Bu proje eğitim ve kişisel gelişim amacıyla hazırlanmıştır.
