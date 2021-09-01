import random
islem = input('Hangi işlemi yapmak istersiniz? ')
puan = 0
while True: 
        for i in range(1,11): 
            if islem == 'toplama': 
                sayi1 = random.randint(1, 100)
                sayi2 = random.randint(1, 100) 
                sayi3 = int(sayi1) 
                sayi4 = int(sayi2) 
                print(f"{sayi3} ve {sayi4} sayılarının toplamı kaçtır? ")
                tahmin = input() 
                tahmin2 = int(tahmin)
                if tahmin2 == sayi3 + sayi4: 
                    print("doğru cevap")
                    puan = puan + 1
                else:
                    print('yanlış cevap')
            elif islem == 'çıkarma': 
                sayi1= random.randint(1, 100) 
                sayi2 = random.randint(1, 100) 
                sayi3 = int(sayi1) 
                sayi4 = int(sayi2)
                print(f"{sayi3} ve {sayi4} sayılarından, büyük sayıyı küçük sayıdan çıkarırsak sonuç nedir? ") #Ekrana sayi3'ten  sayi4 çıkarılırsa kaç kalır diye sorduk
                tahmin = input() 
                tahmin2 = int(tahmin) 
                if tahmin2 == sayi3 - sayi4 or sayi4 - sayi3:
                    print("doğru cevap")
                    puan = puan + 1
                else:
                    print('yanlış cevap')
        break

print("oyun bitti")
print("çözdüğünüz 10 soru sonrasındaki oyun puanınız: ", puan)