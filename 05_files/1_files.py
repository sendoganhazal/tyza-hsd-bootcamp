"""
Dosya işlemleri: 
    - dosyadan veri okuma
    - okunan verinin işlenmesi
    - dosyaya veri yazma veya keydetme
    - with yapısı

Neden dosya işlemleri yapıyoruz?
    - yapay zeka veriden öğrenir, veriyi python ortamına yüklememiz ve işlememiz lazım bu nedenle dosya işlemlerinin mantığını öğrenicez

Dosya: verinin kalıcı olarak saklandığı yapılar.
    - kullanıcı listeleri
    - not kayıtları
    - log dosyaları
    - csv veri dosyaları
"""

# dosya açma ve okuma
# "r" = read -> okuma modu
dosya = open("ornek.txt","r", encoding = "UTF-8")

icerik = dosya.read() #tüm dosyayı okur

print(f"Dosya İçeriği: \n{icerik}")

dosya.close() # dosyayı kapar

#satır satır okuma
dosya = open("ornek.txt","r", encoding="UTF-8")

for satir in dosya:
    
    print(f"Satır: {satir.strip()}") # strip() -> satır sonundaki boşlukları temizler

dosya.close()

# dosya içeriğinin işlenmesi
dosya = open("ornek.txt","r", encoding = "UTF-8")
icerik = dosya.read()
dosya.close()

print(icerik)

yeni_icerik = icerik.upper()
print(f"Yeni İçerik: \n{yeni_icerik}")

#satır sayısını bulmak
dosya = open("ornek.txt","r", encoding = "UTF-8")
satirlar = dosya.readlines()
dosya.close()

satir_sayisi = len(satirlar)
print(f"Toplam Satır Sayısı: {satir_sayisi}")

# dosyaya yazma
# "w" -> yazma işlemi. dosyaya yazar
dosya = open("yeni_dosya.txt","w", encoding="UTF-8")

dosya.write("Merhaba Dünya\n")
dosya.write("Python öğreniyoruz")

dosya.close()

# oku -> işle -> kaydet
dosya = open("ornek.txt","r", encoding = "UTF-8")
icerik = dosya.read()
dosya.close()

yeni_icerik = icerik.upper()

dosya = open("islenmisi_ornek.txt","w",encoding="UTF-8")
dosya.write(yeni_icerik)
dosya.close()

# with yapısı: dosya otomatik olarak kapanır, daha temiz bir kod yazılmış olur

with open("ornek.txt","r",encoding="UTF-8") as dosya :
    icerik = dosya.read()
    print(f"with ile alınan içerik: \n{icerik}")
    
#with ile yazma
with open("with_dosya_yazma","w",encoding="UTF-8") as dosya :
    dosya.write("with ile yazma işlemi gerçekleştirildi")