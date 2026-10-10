import json
import random

with open("kelimeler.json", "r", encoding="utf-8") as f:
    kelime = json.load(f)
kelime_rastgele = random.choice(kelime)

bilme_hakkı = 5  
uzunluk_kelime = len(kelime_rastgele["kelime"])

while True:
    print("Kelimeniz:", uzunluk_kelime * "*", "Uzunluğu:", uzunluk_kelime)
    print("İpucu: ", kelime_rastgele["anlam"])

    kelime_bulma = input("Kelime Tahmininizi Yazınız: ")
    kelime_bulma = kelime_bulma.lower().strip()

    if kelime_bulma == kelime_rastgele["kelime"]:
        print("Doğru cevap bildiniz! Kelimeniz:", kelime_rastgele["kelime"])
        break
    else:
        bilme_hakkı -= 1
        if bilme_hakkı == 0:
            print("Tahmin hakkınız bitti. Kelimeniz:", kelime_rastgele["kelime"])
            break
        print("Cevap yanlış! Bilme hakkınız", bilme_hakkı, "kaldı.")