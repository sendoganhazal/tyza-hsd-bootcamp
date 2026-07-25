# ============================================================
# SORU 1 (IF)
# Kullanıcıdan bir sayı alın.
# Sayı pozitifse "Pozitif", negatifse "Negatif", sıfırsa "Sıfır" yazdırın.
# ============================================================

print("SORU 1 ÇÖZÜM (IF):")
sayi = int(input("Bir sayı girin: "))
print(f"Girilen sayı: {sayi}")

if sayi > 0 :
    print(f"Sayı Pozitif")
elif sayi == 0:
    print(f"Sayı sıfıra eşit")
else :
    print(f"Sayı negatif")
    

print("-" * 50)

# ============================================================
# SORU 2 (FOR)
# 1'den 10'a kadar (10 dahil) sayıları yazdırın.
# Ayrıca bu sayıların toplamını hesaplayıp ekrana yazdırın.
# ============================================================

print("SORU 2 ÇÖZÜM (FOR):")

toplam = 0

for sayi in range(1,11) :
    print(f"sayi: {sayi}") #birden ona kadar sayıları yazdırdım
    toplam += sayi #sayıları toplamı

print(f"1'den 10'a kadar (10 dahil) sayıların toplamı {toplam}")    

print("-" * 50)

# ============================================================
# SORU 3 (WHILE)
# Kullanıcıdan "q" yazana kadar sürekli giriş alın.
# Kullanıcı her giriş yaptığında "Girdiniz: ..." şeklinde ekrana yazdırın.
# Kullanıcı "q" yazarsa döngü bitsin ve "Çıkış yapıldı" yazsın.
# ============================================================

print("SORU 3 ÇÖZÜM (WHILE):")

giris = " "

while giris != "q" :
    
    giris = input("Lütfen Mesajınızı Girin (Çıkmak için q'ya basın): ")
    
    if giris != "q":
        print(f"Girdiniz: {giris}")
    else:
        print("Çıkış Yapıldı")

print("-" * 50)

# ============================================================
# SORU 4 (NESTED)
# 1'den 20'ye kadar sayıları dolaşın.
# Eğer sayı çiftse "Çift", tekse "Tek" yazdırın.
# Ayrıca sayı 10'dan büyükse yanına "Büyük", değilse "Küçük/Eşit" yazdırın.
# Örnek çıktı: 12 -> Çift - Büyük
# ============================================================

print("SORU 4 ÇÖZÜM (NESTED):")

tur = ""
buyuk_mu = ""
for sayi in range(1,21) :

    if sayi % 2 == 0 :
        tur = "Çift"
    else :
        tur = "Tek"
        
    if sayi > 10 :
        buyuk_mu = "10'dan Büyük"
    elif sayi < 10 :
        buyuk_mu = "10'dan Küçük"
    
    print(f"{sayi} -> {tur} - {buyuk_mu}")

print("-" * 50)

# ÇIKILAR

"""
SORU 1 ÇÖZÜM (IF):
Bir sayı girin: 99
Girilen sayı: 99
Sayı Pozitif
--------------------------------------------------
SORU 2 ÇÖZÜM (FOR):
sayi: 1
sayi: 2
sayi: 3
sayi: 4
sayi: 5
sayi: 6
sayi: 7
sayi: 8
sayi: 9
sayi: 10
1'den 10'a kadar (10 dahil) sayıların toplamı 55
--------------------------------------------------
SORU 3 ÇÖZÜM (WHILE):
Lütfen Mesajınızı Girin (Çıkmak için q'ya basın): merhavaa dünyta
Girdiniz: merhavaa dünyta
Lütfen Mesajınızı Girin (Çıkmak için q'ya basın): ss
Girdiniz: ss
Lütfen Mesajınızı Girin (Çıkmak için q'ya basın): hefhsda
Girdiniz: hefhsda
Lütfen Mesajınızı Girin (Çıkmak için q'ya basın): q
Çıkış Yapıldı
--------------------------------------------------
SORU 4 ÇÖZÜM (NESTED):
1 -> Tek - 10'dan Küçük
2 -> Çift - 10'dan Küçük
3 -> Tek - 10'dan Küçük
4 -> Çift - 10'dan Küçük
5 -> Tek - 10'dan Küçük
6 -> Çift - 10'dan Küçük
7 -> Tek - 10'dan Küçük
8 -> Çift - 10'dan Küçük
9 -> Tek - 10'dan Küçük
10 -> Çift - 10'dan Küçük
11 -> Tek - 10'dan Büyük
12 -> Çift - 10'dan Büyük
13 -> Tek - 10'dan Büyük
14 -> Çift - 10'dan Büyük
15 -> Tek - 10'dan Büyük
16 -> Çift - 10'dan Büyük
17 -> Tek - 10'dan Büyük
18 -> Çift - 10'dan Büyük
19 -> Tek - 10'dan Büyük
20 -> Çift - 10'dan Büyük
--------------------------------------------------
"""


