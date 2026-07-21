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
print("ÖDEV TAMAMLANDI")