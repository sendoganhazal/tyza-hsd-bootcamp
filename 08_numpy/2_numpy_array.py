"""
Diziler (array)
    - ndarray: n-dimensional array
"""
import numpy as np

# Arrays -> arraylerde elemanlar aynı veri tipinde olmalıdır. (int, float, str, bool)

liste = [1, 2, 3, 4, 5]
print("Liste:",liste)

# np.array() fonksiyonu ile listeyi diziye çevirebiliriz
dizi = np.array(liste)
print("Dizi:",dizi)

#nmpy tipini inceleme
print("Dizi tipi:",type(dizi)) # Dizi tipi: <class 'numpy.ndarray'>

# numpy dizisinin boyutunu inceleme
print("Dizi boyutu:",dizi.shape) # Dizi boyutu: (5,) -> 5 elemanlı tek boyutlu bir dizi

# numpy dizisinin elemanlarının veri tipini inceleme
print("Dizi elemanlarının veri tipi:",dizi.dtype) # Dizi elemanlarının veri tipi: int64

# numpy dizi oluşturmanın farklı yolları

dizi = np.zeros(5) # 5 elemanlı sıfırlardan oluşan bir dizi oluşturur
print("Sıfırlardan oluşan dizi:",dizi) # Sıfırlardan oluşan dizi: [0. 0. 0. 0. 0.]

dizi = np.ones(5) # 5 elemanlı birlerden oluşan bir dizi oluşturur
print("Birlerden oluşan dizi:",dizi) # Birlerden oluşan dizi: [1. 1. 1. 1. 1.]

# belirli bir aralıkta bir dizi oluşturmak için np.arange() fonksiyonu kullanılır
dizi = np.arange(0, 10) # 0'dan 10'a kadar eşit aralıklı sayılardan oluşan bir dizi oluşturur
print("Belirli bir aralıkta oluşan dizi:",dizi) # Belirli bir aralıkta oluşan dizi: [0 1 2 3 4 5 6 7 8 9]

# belirli bir aralıklarla sayı dizisi oluşturmak
dizi = np.arange(0, 10, 2) # 0'dan 10'a kadar 2'şer artan sayılardan oluşan bir dizi oluşturur
print("Belirli bir aralıkta ve belirli bir adımla oluşan dizi:",dizi) # Belirli bir aralıkta ve belirli bir adımla oluşan dizi: [0 2 4 6 8]

# belirli bir aralıkta eşit sayıda sayı dizisi oluşturmak için np.linspace() fonksiyonu kullanılır
dizi = np.linspace(0, 10, 5) # 0'dan 10'a kadar eşit aralıklı 5 sayıdan oluşan bir dizi oluşturur
print("Belirli bir aralıkta eşit sayıda oluşan dizi:",dizi) # Belirli bir aralıkta eşit sayıda oluşan dizi: [ 0. 2.5  5. 7.5 10. ]
