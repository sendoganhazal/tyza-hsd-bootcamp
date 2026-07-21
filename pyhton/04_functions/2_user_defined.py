"""
user defined (kullanıcı tanımlı) fonksiyonlar
    - kendi fonksiyonumuz
    - parametre
    - return
    - print vs return
    - birden fazla output
    - varsayılan ve keyword parametreleri
    - docstring nedir
"""

"""
fonksiyon tanımlama: def 

def fonksiyon_adi():
    kod_blok

"""

#Fonksiyon tanımlama (define)
def selam_ver() :
    print("Selam Dünyalı!")
    
#Fonksiyonu çağırma (call)
selam_ver()

# Parametre KUllanımı
def selam_ver(isim) :
    
    print(f"Selam, Ben {isim} Akıllı Asistanıyım!")

selam_ver("Trai Akademisi")
selam_ver("Ucanble")

# Birden Fazla Parametre Kullanımı
def selam_ver(isim, selamlama_cumlesi) : 
    print(f"{isim} {selamlama_cumlesi}")
    
selam_ver("Kaan Hoca","akıllı asistanı size merhaba diyor")

#Return kullanımı
def topla(a,b) :
    sonuc = a + b
    print(f"sonuc : {sonuc}")
    return sonuc

toplama_islemi_sonucu = topla(3,8)
print(f"toplama islemi sonucu: {toplama_islemi_sonucu}")

#birden fazla değer döndürme

def hesapla(x,y) :
    topla = x + y
    carp = x * y
    return topla,carp

hesapla_topla, hesapla_carp = hesapla(3,9)

print(f"hesapla_topla: {hesapla_topla}")
print(f"hesapla_carp: {hesapla_carp}")

# varsayılan parametre

def selam(isim,mesaj = "Merhaba") :
    print(f"{isim} {mesaj}")
    
selam("Kaan Hocam")
selam("Hazal","Selam")


#keyword argümanı
"""
    # Docstring
    # Description: bu fonksiyon selamlama yapar.
    # Input: 
    #     isim (str): kullanıcının ismi
    #     yas (int): kullanıcının yaşı
    #     meslek, 
    #     c, 
    #     lr, 
    #     epoch
    # Output: None
"""
def selam(isim, yas, meslek, c, lr, epoc) :
    print(isim, yas, meslek, c, lr, epoc)
    
selam( isim = "Hazal", yas = 34, meslek = "Software Developer", c = "0.1", lr = "0.001", epoc = "1000")

# type hint (modern python)
def topla (a : int, b : int) -> int :
    return a + b

toplam = topla(3,4)

print(f"toplam = {toplam}")

# nested function -fonk. içinde fonk. kullanımı

def kare(x) :
    kare = x ** 2 # x * x
    return kare

def yazdir(x) :
    print(kare(x))

yazdir(5)