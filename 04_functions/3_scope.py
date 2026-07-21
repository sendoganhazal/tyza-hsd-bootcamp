"""
Scope (local ve global)
    - bir değişkenin nerede erişilebilir olduğunu ifade eder
    - bir değişken nerede tanımlıysa orada geçerlidir.
"""

# Local Variables - Lokal (yerel) değişkenler: fonksiyon içerisinde tanımlanan değişkenlerdir.

def test() :
    x = 10 #fonksiyon içerisinde tanımlanan değişkenlerdir.
    print(f"Fonksiyon ici: {x}")
    
test()

# print(x) #NameError: name 'x' is not defined

# Global Variables  - Global (genel) değişkenler: : fonksiyon dışında tanımlanan değişken

x = 15 #fonksiyon dışında tanımlanan değişken

def test() :
    print(f"Fonksiyon dışı: {x}")
    
test()

# Aynı isimli değişkenler

x = 11
def test() :
    x = 5
    print(f"fonksiyon içi: {x}")
    
test()

print(f"fonksiyon dışı: {x}")

# global keyword

x = 9

def test() : 
    global x
    x = 5 # lokal -> global

test()

print(x)