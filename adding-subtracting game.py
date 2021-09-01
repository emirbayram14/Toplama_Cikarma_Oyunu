import operator
import random

puan = 0
islemler = [('+', operator.add), ('-', operator.sub)]

for i in range(1,11):
    sayi1 = random.randint(50, 100)
    sayi2 = random.randint(1, 50)
    op, fn = random.choice(islemler)
    soru = "{} {} {} işleminin sonucu nedir? ".format(sayi1, op, sayi2)
    if int(input(soru)) == fn(sayi1, sayi2):
        puan = puan + 1
        print("doğru cevap")
    else:
        print("yanlış cevap")

print("oyun bitti")
print("çözdüğünüz 10 soru sonrasındaki oyun puanınız: ", puan)