"""
indeksleme (indexing) - dilimleme (slicing)
"""
import numpy as np

# dizilerde indeksleme
dizi = np.array([10, 20, 30, 40, 50])
print("ilk eleman",dizi[0])  # 10

# negatif indeksleme
print("sonuncu eleman",dizi[-1])  # 50
print("sondan önceki eleman",dizi[-2])  # 40

# slicing (dilimleme)
# genel kullanım: dizi[başlangıç:bitiş]
print("birden dördüncüye kadar",dizi[1:4])  # [20 30 40]

# baştan dilimleme
print("ilk üç eleman",dizi[:3])  # [10 20 30]

# son elemana kadar dilimleme
print("2.den sonuna kadar gitme",dizi[2:])  # [30 40 50]

# adım (step) kullanımı
print("adım kullanımı",dizi[::2])  # [10 30 50] => diziden her 2. elemanı alır

# 2 boyutlu dizilerde indeksleme
matris = np.array(
   [
        [1,2,3],
        [4,5,6],
        [7,8,9]
   ]
)

print("matris",matris)
print("ilk satırın ilk elemanı",matris[0,0])  # 1

# belirli bir satırı seçmek
print("ikinci satır",matris[1,:])  # [4 5 6]

# belirli bir sutunu seçmek
print("ikinci sütun",matris[:,1])  # [2 5 8]

# matris dilimleme
print("ilk iki satır ve ilk iki sütun",matris[0:2,0:2])  # [[1 2] [4 5]]