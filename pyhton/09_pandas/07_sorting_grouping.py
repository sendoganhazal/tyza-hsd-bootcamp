import sys
try:
    import pandas as pd
except ImportError:
    print("Unable to import 'pandas'. Please install it with 'pip install pandas'.")
    sys.exit(1)


# VERİ SIRALAMA VE GRUPLAMA

# örnek dataframe oluştur
veri = {
    "isim": ["Ali", "Ayse", "Mehmet", "Zeynep", "Ahmet"],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500]
}

df = pd.DataFrame(veri)
print(df)
"""
     isim     sehir  maas
0     Ali    Ankara  5000
1    Ayse  İstanbul  7000
2  Mehmet    Ankara  6000
3  Zeynep     İzmir  8000
4   Ahmet  İstanbul  4500
"""

# veri sıralama
df_sirali = df.sort_values("maas") # maaş sütununa göre sıralama yapar. artan sıralama yapar
print(df_sirali)
"""
     isim     sehir  maas
4   Ahmet  İstanbul  4500
0     Ali    Ankara  5000
2  Mehmet    Ankara  6000
1    Ayse  İstanbul  7000
3  Zeynep     İzmir  8000
"""

# azalan sıralama
df_sirali = df.sort_values("maas",ascending=False)
print(df_sirali)
"""
     isim     sehir  maas
3  Zeynep     İzmir  8000
1    Ayse  İstanbul  7000
2  Mehmet    Ankara  6000
0     Ali    Ankara  5000
4   Ahmet  İstanbul  4500
"""

# birden fazla sütuna göre sıralama
df_sirali = df.sort_values(["sehir","maas"]) # aynı şehirde olanları maaşa göre sıralar
print(df_sirali)
"""
     isim     sehir  maas
0     Ali    Ankara  5000
2  Mehmet    Ankara  6000
4   Ahmet  İstanbul  4500
1    Ayse  İstanbul  7000
3  Zeynep     İzmir  8000
"""


# veri gruplama: groupby

#şehir bazında gruplama
gruplar = df.groupby("sehir") 
print(gruplar) #<pandas.api.typing.DataFrameGroupBy object at 0x000001CD8B0FB0E0>

#grupların ortalama maaşı
sonuc = df.groupby("sehir")["maas"].mean() # şehir bazında ortalama maaş hesaplama
print(sonuc)
"""
Ankara      5500.0
İstanbul    5750.0
İzmir       8000.0
Name: maas, dtype: float64
"""

# grupların toplam maaşı
sonuc = df.groupby("sehir")["maas"].sum() # şehir bazında maaşların toplamını hesaplama
print(sonuc)
"""
sehir
Ankara      11000
İstanbul    11500
İzmir        8000
Name: maas, dtype: int64
"""

# grupların kaç kişi olduğunu bulalım
sonuc = df.groupby("sehir")["isim"].count() # isimleri şehir bazında gruplayıp sayılarını bulur
print(sonuc)
"""
sehir
Ankara      2
İstanbul    2
İzmir       1
Name: isim, dtype: int64
"""


# birden fazla işlem yapmak
sonuc = df.groupby("sehir")["maas"].agg(["mean","min","max"]) # şehirlere göre ortalama, min ve max maaşları hesaplar
print(sonuc)
"""
            mean   min   max
sehir                       
Ankara    5500.0  5000  6000
İstanbul  5750.0  4500  7000
İzmir     8000.0  8000  8000
"""
