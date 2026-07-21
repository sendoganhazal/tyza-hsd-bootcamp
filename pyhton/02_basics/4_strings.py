#strings
ad = "Hazal"
sirket = "Vivid"

bilgi = "Hazal'ın çalıştığı yer Vivid."
print(bilgi)

#String Concatenation

bilgi2 = ad + "'ın çalıştığı yer" + " " + sirket
print(bilgi2)

#Concatenation string and numbers
ad = "Camille"
yas = 11
int_to_str = str(yas)
# sonuc = ad + "'nin yaşı" + " " + yas #TypeError: can only concatenate str (not "int") to str
sonuc = ad + "'nin yaşı" + " " + int_to_str
print(sonuc)

kurulum_tarihi = 2023
print("Ucanable Teknoloji " + str(kurulum_tarihi) + " yılında kurulmuştur.")
print(f"Ucanable Teknoloji {kurulum_tarihi} yılında kurulmuştur. (f string ile yazılmıştır)") #f string

accuracy = 95
print(f"Karar ağacı accuracy {accuracy}% (f string ile yazılmıştır)") #f string

#string indexing
kelime = "python"

print(f"İlk Karakter {kelime[0]}'dir")
print(f"Üçüncü Karakter {kelime[2]}'dir")

#string methods
metin = "PyThOn"

#harf büyük küçük
metin_kucuk = metin.lower();
metin_buyuk = metin.upper();
metin_ilk_harf = metin.capitalize();

print(f"Metin = {metin}")
print(f"hepsi küçük {metin_kucuk}")
print(f"hepsi büyük {metin_buyuk}")
print(f"metin ilk harf büyük {metin_ilk_harf}")

#length
metin_uzunluk = len(metin);
print(f"Metin {metin_uzunluk} karakterden oluşmaktadır")

#replace
degistir = metin.replace("O","o")
print(degistir)