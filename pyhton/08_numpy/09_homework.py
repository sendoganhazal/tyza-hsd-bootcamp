import numpy as np


# SORU 1
# 1) NumPy kullanarak 1’den 20’ye kadar sayılardan oluşan bir dizi oluşturun.
# 2) Dizinin kaç eleman içerdiğini ekrana yazdırın.

print("SORU 1")

np_array = np.arange(1, 21) # numpy kullanılarak 1’den 20’ye kadar sayılardan oluşan bir dizi oluşturuldu
arr_size = np_array.size # size ile dizinin kaç eleman içerdiği bulunur


print(f"1’den 20’ye kadar sayılardan oluşan bir dizi: {np_array}")
print(f"Dizinin Eleman sayısı: {arr_size}")

print("-" * 50)

# SORU 2
# 1) [5, 10, 15, 20, 25] değerlerinden oluşan bir NumPy dizisi oluşturun.
# 2) Dizideki tüm elemanları 3 ile çarpın.
# 3) Sonucu ekrana yazdırın.

print("SORU 2")

values = [5, 10, 15, 20, 25] # değerlerimiz
np_array = np.array(values) # değerler kullanılarak bir numpy dizisi oluşturuludu
print(f"[5, 10, 15, 20, 25] değerlerinden oluşan bir NumPy dizisi: {np_array}")

multiple = np_array * 3 # Dizideki tüm elemanları 3 ile çarpıldı
print("Dizideki tüm elemanları 3 ile çarpıldı")
print(f"Sonuç: {multiple}")

print("-" * 50)

# SORU 3
# 1) 0’dan 30’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziden sadece 10 ile 20 arasındaki elemanları slicing kullanarak seçin.

print("SORU 3")

np_array = np.arange(0, 31)
selected = np_array[10:21]

print(f"0’dan 30'a kadar sayılardan oluşan bir dizi: {np_array}")
print(f"Seçilen elemanlar: {selected}")

print("-" * 50)

# SORU 4
# 1) [1,2,3] ve [4,5,6] dizilerini oluşturun.
# 2) Bu iki diziyi NumPy kullanarak birleştirin.

print("SORU 4")

a = np.array([1,2,3])
b = np.array([4,5,6])

concat = np.concatenate((a,b))

print(f"a dizisi: {a}")
print(f"b dizisi: {b}")
print(f"a ile b birleşince oluşan dizi: {concat}")

print("-" * 50)

# SORU 5
# 1) 1’den 12’ye kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi reshape kullanarak 3x4 boyutunda bir matrise dönüştürün.
# 3) Matrisin shape değerini yazdırın.

print("SORU 5")

np_array = np.arange(1,13)
matris = np_array.reshape(3,4)

print(f"1’den 13’e kadar sayılardan oluşan bir dizi: {np_array}")
print(f"Dizi Kullanılarak Oluşturulan Matris:\n {matris}")
print(f"Matrisin Shape Değeri: {matris.shape}")

print("-" * 50)

# SORU 6
# 1) Aşağıdaki matrisi oluşturun
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
# 2) İkinci satırı ekrana yazdırın.
# 3) İkinci sütunu ekrana yazdırın.

print("SORU 6")

matris = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

row = matris[1]
col = matris[:,1]

print(f"Oluşturulan Matris: \n {matris}")
print(f"Matrisin İkinci Satırı: {row}")
print(f"Matrisin İkinci Sütunu: {col}")

print("-" * 50)

# SORU 7
# 1) 3x3 boyutunda rastgele sayılardan oluşan bir matris oluşturun.
# 2) Matrisin ortalamasını hesaplayın.
# 3) Matrisin maksimum değerini yazdırın.

print("SORU 7")

matris = np.random.rand(3,3)
mean = np.mean(matris)
maximum = np.max(matris)

print(f"3 * 3'lük Rastgele Oluşturulan Matris:\n {matris}")
print(f"Matrisin Ortalaması: {mean}")
print(f"Matrisin Maksimum Değeri: {maximum}", )

print("-" * 50)

# SORU 8
# 1) [2,4,6,8] ve [1,3,5,7] dizilerini oluşturun.
# 2) Dizileri eleman bazlı çarpın.
# 3) Sonucu ekrana yazdırın.

print("SORU 8")

a = np.array([2,4,6,8])
b = np.array([1,3,5,7])

multiple = a * b

print(f"a dizisi: {a}")
print(f"b dizisi: {b}")
print(f"a ile b çarpımının sonucu: {multiple}")

print("-" * 50)

# SORU 9
# 1) 1’den 9’a kadar sayılar içeren bir dizi oluşturun.
# 2) Bu diziyi 3x3 matrise dönüştürün.
# 3) Matrisin transpose’unu hesaplayın.

print("SORU 9")

np_array= np.arange(1,10)
matris = np_array.reshape(3,3)

transpose = matris.T


print(f"1’den 9’a kadar sayılar içeren bir dizi: {np_array}")
print(f"Dizi Kullanılarak Oluşturulan Matris:\n {matris}")
print(f"Matris Transpose:\n {transpose}")

print("-" * 50)

# SORU 10
# 1) 1 ile 50 arasında rastgele 10 tam sayı üretin.
# 2) Bu sayılardan oluşan dizinin toplamını hesaplayın.
# 3) Dizinin ortalamasını yazdırın.

print("SORU 10")

random_numbers = np.random.randint(1,51,10)
sum = np.sum(random_numbers)
mean = np.mean(random_numbers)

print(f"1 ile 50 arasında rastgele 10 tam sayı: {random_numbers}")
print(f"Sayıların Toplamı: {sum}")
print(f"Sayıların Ortalaması: {mean}")

print("-" * 50)

# ÇIKTILAR
"""
SORU 1
1’den 20’ye kadar sayılardan oluşan bir dizi: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
Dizinin Eleman sayısı: 20
--------------------------------------------------
SORU 2
[5, 10, 15, 20, 25] değerlerinden oluşan bir NumPy dizisi: [ 5 10 15 20 25]
Dizideki tüm elemanları 3 ile çarpıldı
Sonuç: [15 30 45 60 75]
--------------------------------------------------
SORU 3
0’dan 30'a kadar sayılardan oluşan bir dizi: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30]
Seçilen elemanlar: [10 11 12 13 14 15 16 17 18 19 20]
--------------------------------------------------
SORU 4
a dizisi: [1 2 3]
b dizisi: [4 5 6]
a ile b birleşince oluşan dizi: [1 2 3 4 5 6]
--------------------------------------------------
SORU 5
1’den 13’e kadar sayılardan oluşan bir dizi: [ 1  2  3  4  5  6  7  8  9 10 11 12]
Dizi Kullanılarak Oluşturulan Matris:
 [[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
Matrisin Shape Değeri: (3, 4)
--------------------------------------------------
SORU 6
Oluşturulan Matris: 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
Matrisin İkinci Satırı: [4 5 6]
Matrisin İkinci Sütunu: [2 5 8]
--------------------------------------------------
SORU 7
3 * 3'lük Rastgele Oluşturulan Matris:
 [[0.2418378  0.75363873 0.99172513]
 [0.10711882 0.36484517 0.14957928]
 [0.75215468 0.51485503 0.67587868]]
Matrisin Ortalaması: 0.5057370352432479
Matrisin Maksimum Değeri: 0.991725128556323
--------------------------------------------------
SORU 8
a dizisi: [2 4 6 8]
b dizisi: [1 3 5 7]
a ile b çarpımının sonucu: [ 2 12 30 56]
--------------------------------------------------
SORU 9
1’den 9’a kadar sayılar içeren bir dizi: [1 2 3 4 5 6 7 8 9]
Dizi Kullanılarak Oluşturulan Matris:
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
Matris Transpose:
 [[1 4 7]
 [2 5 8]
 [3 6 9]]
--------------------------------------------------
SORU 10
1 ile 50 arasında rastgele 10 tam sayı: [35 10 50 22  4 42 34 37  1 39]
Sayıların Toplamı: 274
Sayıların Ortalaması: 27.4
--------------------------------------------------
"""
