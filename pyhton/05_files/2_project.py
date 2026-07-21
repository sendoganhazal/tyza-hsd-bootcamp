# SORU 1
# "notlar.txt" adında bir dosya oluşturun ve içine
# 5 öğrencinin notunu yazın. Her not ayrı satırda olsun.

with open("notlar.txt","w",encoding="UTF-8") as dosya :
    dosya.write("88\n")
    dosya.write("23\n")
    dosya.write("56\n")
    dosya.write("75\n")
    dosya.write("96\n")

# SORU 2
# Bu dosyayı okuyun ve:
# - Notların ortalamasını hesaplayın
# - En yüksek notu bulun
# - En düşük notu bulun

notlar = []

with open("notlar.txt", "r",encoding="UTF-8") as dosya :
    for satir in dosya :
        ogrenci_notu = int(satir.strip())
        notlar.append(ogrenci_notu)

not_toplam = sum(notlar)
not_sayisi = len(notlar)

ortalama = not_toplam / not_sayisi
print(f"Not Ortalaması: {ortalama}")

max_not = max(notlar)
min_not = min(notlar)

print(f"En Yüksek Not: {max_not}")
print(f"En Düşük Not: {min_not}")

# SORU 3
# Eğer ortalama 50'den büyükse "Sınıf geçti"
# değilse "Sınıf kaldı" sonucunu
# "sonuc.txt" dosyasına kaydedin.

with open("sonuc.txt", "w", encoding="UTF-8") as dosya :
    if ortalama >= 50 :
       dosya.write("Sınıf Geçti")
    else :
        dosya.write("Sınıf Kaldı")
