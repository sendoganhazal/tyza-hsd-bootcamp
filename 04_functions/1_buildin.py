"""
Fonksiyon Nedir?
    - belirli bir işi yapan ve çağrıldığında çalışan kod bloğudur.
    - bir fonksiyon genellikle:
        - girdi (input) 
        - bir işlem yapar
        - sonuç (output) üretir

Kahve makinesi:
    - kahve türünü alır (input)
    - kahveyi hazırlar (işlem)
    - kahveyi verir (output)

girdi -> işlem -> çıktı

1) build in functions: pythonda tanımlı fonksiyonlar
2) user defined functions: developer tanımlar
"""

#print : ekrana çıktı üretir
print("merhaba") #ekrana merhaba yazar
"""
girdi: merhaba -> işlem: print -> çıktı: ekrana "merhaba" yazılması
"""

#len : bir set, tuple, listin eleman sayısını ya da stringing karakter sayısını verir
liste = [1,2,3]
print(f"liste: {len(liste)} elemanlı")
"""
girdi: liste -> işlem: eleman sayısının yazılması -> çıktı: "liste: 3 elemanlı"
"""

#type : değişkenin veri tipini verir
x = 3.14
print(type(x)) #<class 'float'>

#veri tipi dönüşüm fonksiyonları: int(), float(), str()
sayi = "10"
print(int(sayi) + 5) #15

# Toplama fonksiyonu: sum(), Max bulma fonk.u max(), Min bulma fonk.u min()
sayilar = [1,2,3,5]
toplam = sum(sayilar) #toplam
maximum = max(sayilar) #sayıların en büyüğü
minimum = min(sayilar) #sayıların en küçüğü

print(f"Toplam = {toplam}") # Toplam = 11
print(f"sayıların en büyüğü = {maximum}") # sayıların en büyüğü = 5
print(f"sayıların en küçüğü = {minimum}") # sayıların en küçüğü = 1

# mutlak değer fonk.u: abs()
x = -8
print(f"{x} sayısının mutlak değeri {abs(x)}")

# yuvarlama: round()

x = 3.5688655555
y = round(x,3)
print(y) #3.569

#sıralama: sorted()
sayilar = [5,7,1,9,2]
siralanmis = sorted(sayilar)
print(siralanmis) #[1, 2, 5, 7, 9]

# machine learning -> sınıflandırma -> sklearn fit()

# derin öğrenme -> tahmin -> tensorflow predict()