import numpy as np

"""
Çok boyutlu diziler
"""
# 2 boyutlu dizi oluşturma
matris = np.array(
    [
        [1, 2 ,3],
        [4, 5, 6],
        [7, 8, 9]
    ]
)
print("2 boyutlu dizi",matris)
# dizinin boyutunu öğrenme
boyut = matris.shape
print("dizinin boyutu",boyut) # (3, 3)

# dizinin kaç boyutlu olduğunu öğrenmek
boyutlu = matris.ndim
print("dizinin kaç boyutlu olduğu",boyutlu) # 2

# dizideki eleman sayısı
eleman_sayisi = matris.size
print("dizideki eleman sayısı",eleman_sayisi) # 9

# 3 boyutlu dizi oluşturma
"""
görsel -> (height, width) -> (yükseklik ve genişlik) -> (1920, 1080), (1920, 1080), (1920, 1080), ... (1920, 1080) -> (N, 1920, 1080)
"""

dizi3 = np.array(
  [
        [
            [1,2],
            [3,4]
        ],
        [
            [5,6],
            [7,8]
        ]
  ]
)
print("3 boyutlu dizi",dizi3)

boyut3 = dizi3.shape
print("3 boyutlu dizinin boyutu",boyut3) # (2, 2, 2)

"""
(2 adet matris, her matriste 2 satır, her matriste 2 satır)
"""


# numpy ile çok boyutlu dizi oluşturma (reshape)
dizi = np.arange(12) # 0'dan 11'e kadar olan sayıları içeren bir dizi oluşturur
print("dizi",dizi) # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# matrise dönüştürma
matris = dizi.reshape(3, 4) # 3 satır, 4 sütun
print("3 satır, 4 sütun",matris)

"""
3 satır, 4 sütun
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
"""

# matris = dizi.reshape(3, 5) # ValueError: cannot reshape array of size 12 into shape (3,5)
