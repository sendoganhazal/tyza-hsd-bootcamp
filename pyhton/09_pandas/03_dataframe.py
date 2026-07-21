import sys

try:
    import pandas as pd
except ImportError:
    print("Unable to import 'pandas'. Please install it with 'pip install pandas'.")
    sys.exit(1)


# DATAFRAME

veri = {
    "isim": ["Ali","Ayse","Mehmet"],
    "yas": [25,30,28],
    "sehir":["Ankara","İstanbul","İzmir"]
}

df = pd.DataFrame(veri)
print(df)
"""
sütunlar (columns): veri kategorileri
satırlar (rows): her bir kayıt

    isim   yas     sehir
0     Ali   25    Ankara
1    Ayse   30  İstanbul
2  Mehmet   28     İzmir
"""

# sütun işlemler

coln = df.columns # sütun isimlerini öğrenme
print(coln) #Index(['isim', 'yas', 'sehir'], dtype='str')

# satır işlemleri
rowl = df.shape # satır sayısını öğrenme
print(rowl) # (3, 3)

# sütunlara erişmek
print(df["isim"])
"""
0       Ali
1      Ayse
2    Mehmet
"""

#birden fazla sütun seçmek
print(df[["isim","yas"]])
"""
     isim  yas
0     Ali   25
1    Ayse   30
2  Mehmet   28
"""

# yeni sütun eklemek 
df["maas"] = [5000,7000,6000]
print(df)
"""
     isim  yas     sehir  maas
0     Ali   25    Ankara  5000
1    Ayse   30  İstanbul  7000
2  Mehmet   28     İzmir  6000
"""

#sütun silme
df = df.drop("sehir",axis=1)
print(df)
"""
     isim  yas  maas
0     Ali   25  5000
1    Ayse   30  7000
2  Mehmet   28  6000
"""

# ilk satırları görüntüleme
print(df.head()) # ilk 5 satırı görüntüler

#son satırları görüntüleme
print(df.tail()) # son 5 satırı görüntüler

# dataframe hakkında bilgi almak

info = df.info() # dataframe hakkında bilgileri döndürür
print(info)
"""
<class 'pandas.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   isim    3 non-null      str  
 1   yas     3 non-null      int64
 2   maas    3 non-null      int64
dtypes: int64(2), str(1)
memory usage: 204.0 bytes
None
"""
