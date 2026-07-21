"""
matematiksel işlemler
"""
import numpy as np

# Toplama işlemi => a0 + a1w1

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
sonuc = a + b
print("Toplama:",sonuc) # Toplama: [5 7 9]

# Çıkarma

sonuc = a - b
print("Çıkarma:",sonuc) # Çıkarma: [-3 -3 -3]

# Çarpma

sonuc = a * b
print("Çarpma:",sonuc) # Çarpma: [ 4 10 18]

# Bölme

sonuc = a / b
print("Bölme:",sonuc) # Bölme: [0.25 0.4 0.5]

# dizi ile sayı arasında işlem yapma

a = np.array([1, 2, 3])
sonuc = a * 2
print("Dizi ile sayı arasında çarpma:",sonuc) # Dizi ile sayı arasında çarpma: [2 4 6]

# dizinin karesini almak

a = np.array([1, 2, 3,4,5])
sonuc = a**2
print("Dizinin karesi:",sonuc) # Dizinin karesi: [ 1  4  9 16 25]

# karekökünü alma mse -> rmse

a = np.array([1, 4, 9, 16, 25])
sonuc = np.sqrt(a)
print("Dizinin karekökü:",sonuc) # Dizinin karekökü: [1. 2. 3. 4. 5.]

# dizinin toplamını bulma

a = np.array([1, 2, 3, 4, 5])
sonuc = np.sum(a)
print("Dizinin toplamı:",sonuc) # Dizinin toplamı: 15

# ortalama

a = np.array([1, 2, 3, 4, 5])
sonuc = np.mean(a)
print("Dizinin ortalaması:",sonuc) # Dizinin ortalaması: 3.0

# min ve max değerler

a = np.array([1, 2, 3, 4, 5])
sonuc = np.min(a)
print("Dizinin minimum değeri:",sonuc) # Dizinin minimum değeri: 1
sonuc = np.max(a)
print("Dizinin maksimum değeri:",sonuc) # Dizinin maksimum değeri: 5

# standart sapma

a = np.array([1, 2, 3, 4, 5])
sonuc = np.std(a)
print("Dizinin standart sapması:",sonuc) # Dizinin standart sapması: 1.4142135623730951