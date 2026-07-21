"""
Hata yönetimi: 
    - hata (error) ve ististna (exception) 
    - en sık karşılaşılan hata tipleri

Neden önemli:
    - hata yönetimi programın çökmeden kontrollü bir şekilde çalışmasını sağlar

hata yönetimi = can dostumuz

yapay zeka da nerelerde kullanılır?
    - veri hazırlama
    - dosya okuma
    - model eğitim döngüsü
    - rag sistemleri
"""

#yazım hatası (syntax error)
if 5 > 3:  #":" yoksa -> SyntaxError: expected ':'
    print("ok") #NameError: name 'ok' is not defined
    
#name error (tanımsız değişken hatası)

# print(x) #NameError: name 'x' is not defined

#type error (tip hatası)

# print("10" + 5) # TypeError: can only concatenate str (not "int") to str


# value error (değer hatası)
# int("hazal") # ValueError: invalid literal for int() with base 10: 'hazal'

# zero division error (sıfıra bölme hatası)
# print(10/0) # ZeroDivisionError: division by zero

#index error (indeks hatası)
# my_list = [1, 2, 3]

# my_list[10] # IndexError: list index out of range

# key error (anahtar hatası)
ogrenci = {"isim": "hazal"}
# print(ogrenci["yas"]) # KeyError: 'yas'

#file not found error (dosya bulunamadı hatası)
# with open("dosya.txt", "r") as f:
#     print(f.read()) # FileNotFoundError: [Errno 2] No such file or directory: 'dosya.txt'

#module not found error (modül bulunamadı hatası)
# import pandas # ModuleNotFoundError: No module named 'pandas'

#attribute error (özellik hatası)
sayi = 10
# sayi.append(5) # AttributeError: 'int' object has no attribute 'append'