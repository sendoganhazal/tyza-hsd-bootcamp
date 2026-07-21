# Floats (Ondalık Sayılar)
pi = 3.14
sicaklik = 35.5
urun_fiyat = 99.99

print("pi sayısı", "=", pi)
print("hava", sicaklik, "santigrat derece")
print("ürünün fiyatı", urun_fiyat, "TL")


#matematiksel işlemler
a = 3.5
b = 2.00

print("a+b", a + b)
print("a-b", a - b)
print("a*b", a * b)
print("a/b", a / b)

#ondalık hassasiyeti
x = 0.1
y = 0.2

print("0.1 + 0.2 = 0.3", x + y)

#yuvarlama
sonuc = x + y
yuvarlama = round(sonuc,2)

print("0.1 + 0.3 = 0.4", yuvarlama)

#Proje : %20 kdv hesaplama

fiyat = float(input("Fiyat Giriniz:"))
print("Fiyat:",fiyat)

kdv =  (fiyat * 20) / 100

kdvli_fiyat = fiyat + kdv;
print("Kdv'li Fiyat:",kdvli_fiyat)
