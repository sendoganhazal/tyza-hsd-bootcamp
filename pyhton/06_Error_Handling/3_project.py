"""
Bozuk veri temizleme
veri:
    70
    85
    abc
    90
    50
    hata
    60
Amaç:
    - dosyayı oku
    - sayıya çevrilemeyen satırları atla
    - geçerli notları topla
    - ortalama hesapla
"""
notlar = [] #notları tutacak liste
hata_sayisi = 0 #hata sayısını tutacak değişken

with open("notlar.txt", "r", encoding="utf-8") as dosya: #dosyayı aç ve oku
    for satir in dosya: #dosyadaki satırları tek tek oku
        try: 
            not_degeri = int(satir.strip()) #satırdaki veriyi sayıya çevir
            notlar.append(not_degeri) #geçerli notları listeye ekle
        except ValueError: #eğer sayıya çevrilemezse
            print(f"Hatalı veri bulundu: {satir.strip()}")
            hata_sayisi += 1 #hata sayısını artır

print(f"Geçerli notlar: {notlar}")
print(f"Hata sayısı: {hata_sayisi}")

ortalama = sum(notlar) / len(notlar)
print(f"Ortalama: {ortalama}")