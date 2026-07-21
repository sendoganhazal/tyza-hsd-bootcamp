"""
Dizi birleştirme ve bölme
"""
import numpy as np

# dizi birleştirme
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sonuc = np.concatenate((a, b))

print("birleştirilmiş dizi",sonuc)  # [1 2 3 4 5 6]

# iki boyutlu dizi birleştirme

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
sonuc = np.concatenate((a, b))
print("iki boyutlu dizi birleştirme",sonuc)

"""
varsayılan olarak satır yönünde birleştirdik
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
"""

# axis parametresi
# axis = 0 -> satır yönünde birleştirme
# axis = 1 -> sütun yönünde birleştirme
sonuc = np.concatenate((a, b), axis=0) # satır yönünde birleştirme
print("satır yönünde birleştirme",sonuc)

sonuc = np.concatenate((a, b), axis=1) # sütun yönünde birleştirme
print("sütun yönünde birleştirme",sonuc)

"""
[[1 2 5 6]
 [3 4 7 8]]
"""

# vstack (dikey birleştirme): axis = 0 gibi yapar
sonuc = np.vstack((a, b))
print("dikey birleştirme",sonuc)

# hstack (yatay birleştirme): axis = 1 gibi yapar
sonuc = np.hstack((a, b))
print("yatay birleştirme",sonuc)

# diziyi parçalara bölme
a = np.array([1, 2, 3, 4, 5, 6])
sonuc = np.split(a, 2) # 2 parçaya bölme
print("diziyi 2 parçaya bölme",sonuc)

sonuc = np.split(a, 3) # 3 parçaya bölme
print("diziyi 3 parçaya bölme",sonuc)

# 2 boyutlu dizilerde bölme

matris = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

sonuc = np.split(matris, 2) # satır bazında 2 parçaya bölme
print("2 boyutlu diziyi satır bazında 2 parçaya bölme",sonuc)

"""
[array([[1, 2],
       [3, 4]]), 
       
array([[5, 6],
       [7, 8]])]
"""

sonuc = np.split(matris, 2, axis=1) # sütun bazında 2 parçaya bölme
print("2 boyutlu diziyi sütun bazında 2 parçaya bölme",sonuc)
"""
[array([[1],
       [3],
       [5],
       [7]]), 
array([[2],
       [4],
       [6],
       [8]])]
"""