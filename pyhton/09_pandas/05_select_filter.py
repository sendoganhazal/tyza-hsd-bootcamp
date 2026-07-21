import sys
try:
    import pandas as pd
    import openpyxl
except ImportError:
    print("Unable to import 'pandas'. Please install it with 'pip install pandas'.")
    sys.exit(1)
    
# VERİ SEÇME VE FİLTRELEME

# örnek dataframe oluştur
veri = {
    "isim": ["Ali", "Ayse", "Mehmet", "Zeynep", "Ahmet"],
    "yas": [25, 30, 28, 35,22],
    "sehir":["Ankara","İstanbul","İzmir", "Ankara", "Bursa"],
    "maas": [5000, 7000, 6000, 8000, 4500]
}

df = pd.DataFrame(veri)
print(df)
"""
     isim  yas     sehir  maas
0     Ali   25    Ankara  5000
1    Ayse   30  İstanbul  7000
2  Mehmet   28     İzmir  6000
3  Zeynep   35    Ankara  8000
4   Ahmet   22     Bursa  4500
"""

# sütun seçme
print(df["isim"])

#birden fazla sütun seçme
print(df[["isim","maas"]])

# satır seçme : iloc
str0 = df.iloc[0] #0. satırı bize verir
print(str0)
""""
isim        Ali
yas          25
sehir    Ankara
maas       5000
Name: 0, dtype: object
"""

# birden fazla satır seçme
strmult = df.iloc[0:3] # 0dan 3. satıra kadar olan satırlardaki verileri alır
print(strmult)
"""
     isim  yas     sehir  maas
0     Ali   25    Ankara  5000
1    Ayse   30  İstanbul  7000
2  Mehmet   28     İzmir  6000
"""


# etiketlerine göre satır seçme: loc
print(df.loc[2])
"""
isim     Mehmet
yas          28
sehir     İzmir
maas       6000
Name: 2, dtype: object
"""

# belirli bir satır(lar) ve belirli bir sütun(lar) seçme
selection = df.loc[:,["isim","maas"]]
print(selection)
"""
     isim  maas
0     Ali  5000
1    Ayse  7000
2  Mehmet  6000
3  Zeynep  8000
4   Ahmet  4500
"""

selection = df.loc[:2,["isim","maas"]]
print(selection)
"""
     isim  maas
0     Ali  5000
1    Ayse  7000
2  Mehmet  6000
"""

# koşullu filtreleme
filtre = df["yas"] > 30
print(filtre)
"""
0    False
1    False
2    False
3     True
4    False
Name: yas, dtype: bool
"""

sonuc = df[filtre]
print(sonuc)
"""
     isim  yas   sehir  maas
3  Zeynep   35  Ankara  8000
"""

diger_yol = df[df["yas"] > 30]
print(diger_yol)
"""
     isim  yas   sehir  maas
3  Zeynep   35  Ankara  8000
"""


# birden fazla koşul varsa
# şehir ankara ve maaş 6000den büyük olan kişileri getir

sonuc = df[(df["sehir"] == "Ankara") & (df["maas"] > 6000)]
print(sonuc)
"""
     isim  yas   sehir  maas
3  Zeynep   35  Ankara  8000
"""


# belirli bir değeri içerenleri getir
sonuc = df[df["sehir"] == "Ankara"]
print(sonuc)
"""
     isim  yas   sehir  maas
0     Ali   25  Ankara  5000
3  Zeynep   35  Ankara  8000
"""

# sadece belirli sütunları gösterme
# yaşı 25den büyük olan verinin sadece isim ve maaşını göster
sonuc = df[df["yas"] > 25][["isim","yas"]]
print(sonuc)
"""
     isim  yas
1    Ayse   30
2  Mehmet   28
3  Zeynep   35
"""
