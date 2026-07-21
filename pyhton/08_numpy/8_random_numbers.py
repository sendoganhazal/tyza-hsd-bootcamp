import numpy as np

"""
Rastgele sayı üretme
"""

# rastgele ondalık sayılar üretme [0-1] arasında
rastgele_sayi = np.random.rand(5)
print("rastgele 5 ondalık sayılar",rastgele_sayi) # [0.555416   0.09727275 0.89972012 0.00780787 0.86983443]

# rastgele matris oluşturma
rastgele_matris = np.random.rand(3,3)
print("rastgele 3x3 matris",rastgele_matris)



# rastgele tam sayı üretme
rastgele_tam_sayi = np.random.randint(1, 10, 5) # 1-10 arasında 5 adet rastgele tam sayı üretir
print("rastgele 5  adet tam sayılar",rastgele_tam_sayi)

# rastgele tam sayı matrisi üretme
rastgele_tam_sayi_matris = np.random.randint(1, 20, (3, 4)) # 1-20 arasında 3 satır 4 sütun dan oluşan matris üretir
print("rastgele 3x4 tam sayılar",rastgele_tam_sayi_matris)

# aynı rastgele sonucu üretmek için (seed)
np.random.seed(42)
rastgele_sayi_seed = np.random.rand(5)
print("rastgele 5 ondalık sayılar (seed ile)",rastgele_sayi_seed) # [0.37454012 0.95071431 0.73199394 0.59865848 0.15601864]

# bir diziden rastgele eleman seçmek
dizi = np.array([10, 20, 30, 40, 50])
secim = np.random.choice(dizi)
print("rastgele seçilen eleman",secim) # 30

# birden fazla eleman seçme 
secim_coklu = np.random.choice(dizi, size=3, replace=False) # replace=False ile tekrar eden eleman seçilmez
print("rastgele seçilen 3 eleman",secim_coklu) # [40 20 10]
