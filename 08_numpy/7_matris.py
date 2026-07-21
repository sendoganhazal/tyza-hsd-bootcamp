import numpy as np

"""
Matris işlemleri
"""

# matris oluşturma
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

#matris işlemleri

toplam = a + b # eleman bazlı toplama
carpim = a * b # eleman bazlı çarpım
bolme = a / b # eleman bazlı bölme
cikarma = a - b # eleman bazlı çıkarma

print("toplam",toplam)
print("çarpım",carpim)
print("bölme",bolme)
print("çıkarma",cikarma)

# gerçek matris çarpımı
sonuc = np.dot(a, b)
print("gerçek matris çarpımı",sonuc)
"""
[1, 2],
[3, 4]
*
[5, 6],
[7, 8]
=
[[19 22]
 [43 50]]
"""

# matris transpose (matrisin ters çevrilmesi)
matris_transpose = a.T
print("a matrisinin transpose'u",matris_transpose)

"""
[1, 2],
[3, 4]

[[1 3]
 [2 4]]
"""

# matris determinantı
determinant = np.linalg.det(a)
print("a matrisinin determinantı",determinant) #  -2.0000000000000004

# matrisin tersi
ters = np.linalg.inv(a)
print("a matrisinin tersi",ters)
"""
[[-2.   1. ]
 [ 1.5 -0.5]]
"""