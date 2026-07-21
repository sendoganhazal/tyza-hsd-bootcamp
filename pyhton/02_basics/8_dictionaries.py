# Dictionary
# {key:value}

ogrenci = {
    "isim": "Ali", # isim = key (anahtar), "Ali" = value (değer)
    "yas": 25,
    "bolum": "bilgisayar"
}
print(ogrenci)

#Erişim
ogrenci_isim = ogrenci["isim"]
ogrenci_yas = ogrenci["yas"]

print(f"Öğrencinin ismi {ogrenci_isim}. Öğrenci {ogrenci_yas} yaşındadır")

#Yeni eleman ekleme
ogrenci["not"] = 85
print(ogrenci) #{'isim': 'Ali', 'yas': 25, 'bolum': 'bilgisayar', 'not': 85}

#değer güncelleme
ogrenci["yas"] = 26
print(ogrenci) #{'isim': 'Ali', 'yas': 26, 'bolum': 'bilgisayar', 'not': 85}

#eleman silme
del ogrenci["bolum"]
print(ogrenci) # {'isim': 'Ali', 'yas': 26, 'not': 85}

#key ve valueları alma
anahtarlar = ogrenci.keys() # keyleri (anahtarları) alır
degerler = ogrenci.values() #valueları (değerleri) alır
cift = ogrenci.items() # key -value çifti olarak alır

print(anahtarlar) #dict_keys(['isim', 'yas', 'not'])
print(degerler) #dict_values(['Ali', 26, 85])
print(cift) #dict_items([('isim', 'Ali'), ('yas', 26), ('not', 85)])