import sys
try:
    import pandas as pd
except ImportError:
    print("Unable to import 'pandas'. Please install it with 'pip install pandas'.")
    sys.exit(1)

# SATIR VE SÜTUN İŞLEMLERİ

# dataframe oluştur
veri = {
    "isim": ["Ali", "Ayşe", "Mehmet"],
    "yas": [25, 30, 28],
    "maas": [5000, 7000, 6000]
}

df = pd.DataFrame(veri)
print(df)
"""
     isim  yas  maas
0     Ali   25  5000
1    Ayşe   30  7000
2  Mehmet   28  6000
"""

# yeni bir sütun ekleme
df["sehir"] = ["Ankara", "İstanbul", "İzmir"]
print(df)
"""
     isim  yas  maas     sehir
0     Ali   25  5000    Ankara
1    Ayşe   30  7000  İstanbul
2  Mehmet   28  6000     İzmir
"""

# hesaplama ile sütun oluşturma
df["yillik_maas"] = df["maas"] * 12
print(df)
"""
     isim  yas  maas     sehir  yillik_maas
0     Ali   25  5000    Ankara        60000
1    Ayşe   30  7000  İstanbul        84000
2  Mehmet   28  6000     İzmir        72000
"""

#sütun silme
df = df.drop("maas",axis=1)
print(df)
"""
    isim  yas     sehir  yillik_maas
0     Ali   25    Ankara        60000
1    Ayşe   30  İstanbul        84000
2  Mehmet   28     İzmir        72000
"""

# sütun isim değiştirme
df = df.rename(columns={"yillik_maas":"yillikMaas"})
print(df)
"""
     isim  yas     sehir  yillikMaas
0     Ali   25    Ankara       60000
1    Ayşe   30  İstanbul       84000
2  Mehmet   28     İzmir       72000
"""

# yeni satır eklemek
df.loc[3] = ["Zeynep",32, "Ankara",8000]
print(df)
"""
     isim  yas     sehir  yillikMaas
0     Ali   25    Ankara       60000
1    Ayşe   30  İstanbul       84000
2  Mehmet   28     İzmir       72000
3  Zeynep   32    Ankara        8000
"""

# satır silme
df = df.drop(0)
print(df)
""" 
     isim  yas     sehir  yillikMaas
1    Ayşe   30  İstanbul       84000
2  Mehmet   28     İzmir       72000
3  Zeynep   32    Ankara        8000
"""

# indeks değerlerini yeniden düzenleme
df = df.reset_index(drop=True)
print(df)
"""
     isim  yas     sehir  yillikMaas
0    Ayşe   30  İstanbul       84000
1  Mehmet   28     İzmir       72000
2  Zeynep   32    Ankara        8000
"""
