"""
try - except
    - program hata verdiğinde durmasını istemeyiz
    - hata olursa yakalyıp kontrollü şekilde yönetmesi lazım
"""

# sayi = int(input("Bir sayı girin: "))
# print(f"On sayısının girilen sayıya bölümü: {10/sayi}") # 0 girdiğinde ZeroDivisionError hatası alırız ve program durur. Bunu try-except ile yönetebiliriz.

# print("Program başarılı bir şekilde çalışmaya devam ediyor...") 
try:
    sayi = int(input("Bir sayı girin: "))
    print(f"On sayısının girilen sayıya bölümü: {10/sayi}")
    print("Program başarılı bir şekilde çalışmaya devam ediyor...") 
except:
    print("Bir hata oluştu.")
    

#belirli bir hata tipi yakalama yöntemi
try:
    sayi = int(input("Bir sayı girin: "))
    print(f"On sayısının girilen sayıya bölümü: {10/sayi}")
except ValueError:
    print("Lütfen bir sayı girin.")
except ZeroDivisionError:
    print("Sıfıra bölme hatası oluştu.")
    
# else mantığı: hata oluşmazsa çalışacak kod bloğu
try:
    sayi = int(input("Bir sayı girin: "))
    sonuc = 10/sayi
    print(f"On sayısının girilen sayıya bölümü: {sonuc}")
except (ValueError, ZeroDivisionError):
    print("Hatalı Giriş")
else:
    print(f"Sonuç: {sonuc}") 
    
#finally mantığı: hata oluşsa da oluşmasa da çalışacak kod bloğu
try:
    dosya = open("dosya.txt", "r",encoding="utf-8")
    icerik = dosya.read()
    print(icerik)
except FileNotFoundError:
    print("Dosya bulunamadı.")
finally:
    try:
        dosya.close()
    except:
        pass

#kendi hatamızı oluşturmak
yas = int(input("Yaşınızı girin: "))

if yas < 0:
    raise ValueError("Yaş negatif olamaz.") #ValueError: Yaş negatif olamaz.

#genel hata ayıklama mantığı
try:
    sayi = int(input("Bir sayı girin: "))
    print(f"On sayısının girilen sayıya bölümü: {10/sayi}")
except Exception as e: #Exception sınıfı tüm hataların üst sınıfıdır. Tüm hataları yakalamak için kullanılır.
    print(f"Hata mesajı: {e}")
