"""
    Kontrol yapıları nedir?
        - programın çalışma akışını koşullara bağlı olarak değiştirmesini sağlayan yapılardır
        - kontrol yapıları sayesinde program koşul doğruysa bir kod bloğunu veya koşul yanlış ise başka bir kod bloğunu çalıştırabilir

    if yapısı: bir koşul doğruysa kod bloğunu çalıştırır

    if kosul:
        yapilacak_islem
"""

sayi = 10

if sayi > 0 :
    print(f"{sayi} Sayısı Pozitiftir")
    
# if sayi > 0 :
# print("burası çalışmaz") # IndentationError: expected an indented block after 'if' statement on line 17

#if elsle

sayi = - 3

if sayi > 0 :
    print(f"{sayi} Sayısı Pozitiftir")
else :
    print(f"{sayi} Sayısı Pozitif Değildir")
    
#if - elif - el 
ogrenci_not = 72

if ogrenci_not > 85 : 
    print("A")
elif ogrenci_not > 70 : 
    print("B")
elif ogrenci_not > 60 : 
    print("C")
elif ogrenci_not > 50 : 
    print("D")
else : 
    print("F")
    
#mantıksal operatörler
yas = 20
ogrenci = True 

#eğer öğrencinin yaşı 25Ten küçükse öğrenci indirimi uygula
if yas < 20 and ogrenci == True :
    print("Öğrenci indirimi uygula")
    
if yas < 20 or ogrenci == True :
    print("Öğrenci indirimi uygula")
    
#if ve liste kullanımı 
meyveler = ["elma", "muz", "armut"]

if "elma" in meyveler :
    print("elma listede var")
else :
    print("elma listede yok")
    
#stok kontrol örneği
meyveler = ["elma", "muz", "armut"]

urun = input("Bir meyvele girin:")

if urun in meyveler :
    print("Stokta var")
else : 
   print("Stokta yok")