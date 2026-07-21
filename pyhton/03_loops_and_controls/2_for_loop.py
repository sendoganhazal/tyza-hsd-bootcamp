"""
Döngü (loop) nedir?
    - bir işlemi tekrar tekrar yapmamıza sağlayan yapılardır.
    - örn: bir listede ki tüm elemanları yazdırmak

For loop:

for degisken in koleksiyon:
    yapilacak_islem

degisken: her turda (iterasyon) değişen geçici isim
koleksiyon: liste, tuple gibi veri yapıları
"""
#For döngüsü
sayilar = [10, 20, 30]

for sayi in sayilar :
    print(f"{sayi} + 5 = {sayi + 5}")
    
#range fonksiyonu ile for döngüsü

for i in range(5) : 
    print(i)
    
for i in range(1, 7): 
    print(i)
    
#for ile toplama işlemi
sayilar = [10, 20, 30]
toplam = 0

for s in sayilar :
    print(f"sayı: {sayi}")
    toplam = toplam + s
   
print(f"listedeki sayıların toplamı = {toplam}")

#for + if kullanımıi
sayilar = [1,2,3,4,5,6]

for sayi in sayilar :
    
    if sayi % 2 == 0 :
        print(f"Çift sayı : {sayi}")
        
#string üzerinden for döngüsü
kelime = "ucanble"

for harf in kelime:
    print(f"harf: {harf}")