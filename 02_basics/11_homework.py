# ============================================================
# SORU 1
# Bir değişken tanımlayalım: ad = "Kaan", yas = 25, ortalama = 3.45
# Bu değişkenlerin tiplerini type() ile yazdıralım.
# ============================================================

print("SORU 1 ÇÖZÜM")
ad = "Kaan"
yas = 25,
ortalama = 3.45

tip_ad = type(ad)
tip_yas = type(yas)
tip_ort = type(ortalama)

print(f"ad değişkeninin tipi: {tip_ad}")
print(f"yas değişkeninin tipi: {tip_yas}")
print(f"ortalama değişkeninin tipi: {tip_ort}")

print("-" * 50)

# ============================================================
# SORU 2
# Kullanıcıdan yaş bilgisini input() ile alalım.
# Bu yaşın tipini ekrana basalım ve 5 yıl ekleyip sonucu yazdıralım.
# Not: input() her zaman string döndürür, int'e çevirmeyi unutmayalım.
# ============================================================
print("SORU 2 ÇÖZÜM")

yas = int(input("Lutfen yasinizi giriniz: "))
yas_tip = type(yas)

print(f"Girilen yaş değişkeninin tipi {yas_tip}")

toplam = yas + 5

print("Girilen yaşa 5 eklendi")
print(f"Bulunan sonuç {toplam}")

print("-" * 50)

# ============================================================
# SORU 3
# Bir ürün fiyatı (float) alalım. %18 KDV hesaplayalım.
# Toplam fiyatı 2 basamak olacak şekilde yazdıralım.
# ============================================================
print("SORU 3 ÇÖZÜM")

urun_fiyat = float(input("Lutfen urun fiyatini giriniz: "))

kdv_tutar = (urun_fiyat * 18) / 100
kdvli_fiyat = urun_fiyat + kdv_tutar

print(f"Ürünün kdv'li fiyatı {kdvli_fiyat} TL'dir")

print("-" * 50)

# ============================================================
# SORU 4
# Bir liste oluşturalım: sayilar = [10, 20, 30, 40, 50]
# - İlk elemanı yazdıralım
# - Son elemanı yazdıralım
# - 2. indexten sona kadar olan parçayı yazdıralım
# - Listeye 60 ekleyelim
# - Listedeki 20 değerini silelim
# ============================================================
print("SORU 4 ÇÖZÜM")

sayilar = [10, 20, 30, 40, 50]

#ilk elemanı yazdırma
ilk = sayilar[0]
print(f"İlk eleman: {ilk}") 

#son elemanı yazdırma
son = sayilar[-1]
print(f"Son eleman: {son}") 

#2. indexten sona kadar olan sayıları yazdırma
iki_son = sayilar[2:] 
print(f"2. indexten sona kadar olan sayılar: {iki_son}") 

print("-" * 50)

# ============================================================
# SORU 5
# Bir tuple oluşturalım: koordinat = (12, 34)
# - Tuple içindeki değerleri unpacking ile x ve y değişkenlerine alalım
# - x ve y'yi yazdıralım
# - Tuple'ın değiştirilemediğini göstermek için (yorum satırıyla) örnek verelim
# ============================================================
print("SORU 5 ÇÖZÜM")

koordinat = (12, 34) #tuple oluşturdum
x,y = koordinat #unpacking ile x ve y'e atadım
print(f"x: {x}, y: {y}") #x ve y'i yazdırdım

# koordinat[0] = 21 #'tuple' object does not support item assignment
# koordinat[1] = 50 #'tuple' object does not support item assignment

print("-" * 50)

# SORU 6
# Bir sözlük (dictionary) oluşturalım:
# ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
# - Öğrencinin ismini yazdıralım
# - "not" anahtarı ile 90 ekleyelim
# - "yas" değerini 23 yaparak güncelleyelim
# - Tüm anahtarları ve tüm değerleri yazdıralım
# ============================================================
print("SORU 6 ÇÖZÜM")

ogrenci = {
    "isim": "Hazal",
    "yas": 22,
    "bolum":"Yazılım"
} # öğrenci dictionary'si oluşturuldu

print(f"Öğrencinin adı {ogrenci["isim"]}") #öğrencinin adı yazdırıldı

ogrenci["not"] = 90 #öğrencinin notu eklendi
ogrenci["yas"] = 23 #öğrencinin yasi güncellendi

print(ogrenci.keys()) # tüm anahtarlar yazdırıldı
print(ogrenci.values()) #tüm değerler yazıdıldı
print("-" * 50)

# ============================================================
# SORU 7
# Set oluşturalım ve tekrar edenleri temizleyelim:
# liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
# - listeyi set'e çevirip benzersiz isimleri yazdıralım
# - benzersiz isim sayısını yazdıralım
# ============================================================
print("SORU 7 ÇÖZÜM")

liste = ["Mehmet", "Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]

benzersiz_isimler = set(liste) #liste'yi sete çevirdik
print(f"Benzersiz isimler: {benzersiz_isimler}") #sete dönüştürülmüş listeyi yazdırdık

isim_sayisi = len(benzersiz_isimler) #benzersiz isim sayısını bulduk
print(f"Benzersiz isim sayısı {isim_sayisi}") #benzersiz isim sayısını yazdırdık


print("-" * 50)