import sys
try:
    import pandas as pd
except ImportError:
    print("Unable to import 'pandas'. Please install it with 'pip install pandas'.")
    sys.exit(1)


# TEMEL PANDAS FONKSİYONLARI

veri = {
    "isim": ["Ali", "Ayse", "Mehmet", "Zeynep", "Ahmet"],
    "yas": [25, 30, 28, 35, 22],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500]
}

df = pd.DataFrame(veri)
print(df)
"""
     isim  yas     sehir  maas
0     Ali   25    Ankara  5000
1    Ayse   30  İstanbul  7000
2  Mehmet   28    Ankara  6000
3  Zeynep   35     İzmir  8000
4   Ahmet   22  İstanbul  4500
"""

# head fonksiyonu : ilk satırları gösterir
print(df.head()) # ilk 5 satırı gösterir
"""
     isim  yas     sehir  maas
0     Ali   25    Ankara  5000
1    Ayse   30  İstanbul  7000
2  Mehmet   28    Ankara  6000
3  Zeynep   35     İzmir  8000
4   Ahmet   22  İstanbul  4500
"""

print(df.head(3)) # ilk 3 satırı gösterir
"""
     isim  yas     sehir  maas
0     Ali   25    Ankara  5000
1    Ayse   30  İstanbul  7000
2  Mehmet   28    Ankara  6000
"""
print(df.head(10)) # ilk 10 satırı gösterir

# tail fonksiyonu: son satırları gösterir

print(df.tail()) #son 5 satırı döner
"""
     isim  yas     sehir  maas
0     Ali   25    Ankara  5000
1    Ayse   30  İstanbul  7000
2  Mehmet   28    Ankara  6000
3  Zeynep   35     İzmir  8000
4   Ahmet   22  İstanbul  4500
"""

print(df.tail(3)) # son 3 satırı döner
"""
     isim  yas     sehir  maas
2  Mehmet   28    Ankara  6000
3  Zeynep   35     İzmir  8000
4   Ahmet   22  İstanbul  4500
"""

# info fonksiyonu: dataframe hakkında bilgiler verir
print(df.info())

"""
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   isim    5 non-null      str  
 1   yas     5 non-null      int64
 2   sehir   5 non-null      str  
 3   maas    5 non-null      int64
dtypes: int64(2), str(2)
memory usage: 292.0 bytes
None
"""

#  fonksiyonu : sayısal sütunların temel istatistiksel özeti verir
print(df.describe())
"""
             yas         maas
count   5.000000     5.000000
mean   28.000000  6100.000000
std     4.949747  1431.782106
min    22.000000  4500.000000
25%    25.000000  5000.000000
50%    28.000000  6000.000000
75%    30.000000  7000.000000
max    35.000000  8000.000000
"""

# value_counts fonksiyonu: bir sütundaki değerlerin kaç defa tekrar ettiğini gösterir
print(df["sehir"].value_counts()) # şehir sütunundaki şehirler kaç defa tekrar ediyor?
"""
sehir
Ankara      2
İstanbul    2
İzmir       1
Name: count, dtype: int64
"""

# unique fonksiyonu : bir sütundaki benzersiz değerleri döner
print(df["sehir"].unique())
"""
<StringArray>
['Ankara', 'İstanbul', 'İzmir']
Length: 3, dtype: str
"""

# nunique fonksiyonu : bir sütunda kaç farklı değer olduğunu söyler
print(df["sehir"].nunique())
"""
<StringArray>
['Ankara', 'İstanbul', 'İzmir']
Length: 3, dtype: str
3
"""
