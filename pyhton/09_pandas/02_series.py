
import sys

try:
    import pandas as pd
except ImportError:
    print("Unable to import 'pandas'. Please install it with 'pip install pandas'.")
    sys.exit(1)

# SERIES Veri Yapısı

veri = pd.Series([10, 20, 30, 40])

print(veri)
"""
0    10
1    20
2    30
3    40
dtype: int64
"""

# series içindeki verilere erişmek
veri = pd.Series([10, 20, 30, 40])

print(veri[0]) #10
print(veri[2]) #30

# series için özel index belirleme
veri = pd.Series([10,20,30], index = ["a","b","c"])

print(veri)
"""
a    10
b    20
c    30
dtype: int64
"""


print(veri["b"]) #20


# dictionary ile seri oluşturma

veri = { # key - value
    "ali": 80,
    "ayse": 90,
    "mehmet": 75
}

s = pd.Series(veri)
print(s)

"""
index    value

ali       80
ayse      90
mehmet    75
"""

#series özellikleri

idx = s.index # indexe erişmek
print(idx) # Index(['ali', 'ayse', 'mehmet'], dtype='str')

values = s.values # değerlere erişmek
print(values) # [80 90 75]

tip = s.dtype # tipini öğrenmek
print(tip) # int64


# series ile matematiksel işlemler
veri = pd.Series([10,20,30,40])

carpim = veri * 2
print(carpim)
"""
0    20
1    40
2    60
3    80
"""

# series filtreleme
yas = pd.Series([10,20,30,40,50])
filtre = yas > 25
sonuc = yas[filtre]

print("filtre \n",filtre)
"""
filtre 
0    False
1    False
2     True
3     True
4     True
"""


print("filtrelenmiş sonuç \n", sonuc)
"""
filtrelenmiş sonuç 
2    30
3    40
4    50
"""
