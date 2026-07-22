import pandas as pd


# ÖRNEK VERİ SETİ
# Aşağıdaki veri seti tüm sorular için kullanılacaktır.

veri = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet", "Elif"],
    "yas": [25, 30, 28, 35, 22, 27],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500, 6500]
}

df = pd.DataFrame(veri)

print("VERİ SETİ")
print(df)
print("-" * 50)



# SORU 1
# DataFrame'in ilk 3 satırını gösterin.

print("SORU 1 CEVAP")

first_three = df.head(3)
print("DataFrame'in ilk 3 satırı \n",first_three)

print("-" * 50)



# SORU 2
# DataFrame'deki sütun isimlerini ekrana yazdırın.

print("SORU 2 CEVAP")

column_names = df.columns
print("DataFrame'deki sütun isimleri \n",column_names)

print("-" * 50)



# SORU 3
# Sadece "isim" sütununu seçin.

print("SORU 3 CEVAP")

names = df["isim"]
print("isim sütunu \n",names)

print("-" * 50)



# SORU 4
# Sadece "isim" ve "maas" sütunlarını birlikte gösterin.

print("SORU 4 CEVAP")

name_salary = df[["isim","maas"]]
print("sadece isim ve maaş sütunları \n",name_salary)

print("-" * 50)



# SORU 5
# Yaşı 28'den büyük olan kişileri filtreleyin.

print("SORU 5 CEVAP")

filtered_data = df[df["yas"] > 28]
print("Yaşı 28'den büyük olan kişiler \n",filtered_data) 

print("-" * 50)



# SORU 6
# Maaşı 6000'den büyük olan kişilerin sadece isim ve maaş bilgilerini gösterin.

print("SORU 6 CEVAP")

filtered_data = df[df["maas"] > 6000]
name_salary = filtered_data[["isim","maas"]]

print("Maaşı 6000'den büyük olan kişilerin sadece isim ve maaş bilgileri \n",name_salary) 

print("-" * 50)



# SORU 7
# Maaşa göre küçükten büyüğe sıralayın.

print("SORU 7 CEVAP")

sort_by_salary_asc = df.sort_values("maas")

print("Maaşa göre küçükten büyüğe sıralama \n",sort_by_salary_asc) 

print("-" * 50)



# SORU 8
# Maaşa göre büyükten küçüğe sıralayın.

print("SORU 8 CEVAP")

sort_by_salary_desc = df.sort_values("maas", ascending=False)

print("Maaşa göre büyükten küçüğe sıralama \n",sort_by_salary_desc) 

print("-" * 50)



# SORU 9
# Şehirlere göre gruplama yapın ve her şehir için ortalama maaşı hesaplayın.

print("SORU 9 CEVAP")

gruplar = df.groupby("sehir") # şehre göre gruplandım
sonuc = gruplar["maas"].mean() # şehir bazında maaşların ortalamasını hesapladım

print("Şehir bazında maaşların ortalaması \n",sonuc) 

print("-" * 50)



# SORU 10
# "yillik_maas" adında yeni bir sütun oluşturun.
# Bu sütun maaşın 12 ile çarpılması ile oluşturulacaktır.


print("SORU 10 CEVAP")

df["yillik_maas"] = df["maas"] * 12
print(df)

print("-" * 50)

# SONUÇLAR

"""
VERİ SETİ
     isim  yas     sehir  maas
0     Ali   25    Ankara  5000
1    Ayşe   30  İstanbul  7000
2  Mehmet   28    Ankara  6000
3  Zeynep   35     İzmir  8000
4   Ahmet   22     Bursa  4500
5    Elif   27  İstanbul  6500
--------------------------------------------------
SORU 1 CEVAP
DataFrame'in ilk 3 satırı 
      isim  yas     sehir  maas
0     Ali   25    Ankara  5000
1    Ayşe   30  İstanbul  7000
2  Mehmet   28    Ankara  6000
--------------------------------------------------
SORU 2 CEVAP
DataFrame'deki sütun isimleri 
 Index(['isim', 'yas', 'sehir', 'maas'], dtype='str')
--------------------------------------------------
SORU 3 CEVAP
isim sütunu 
 0       Ali
1      Ayşe
2    Mehmet
3    Zeynep
4     Ahmet
5      Elif
Name: isim, dtype: str
--------------------------------------------------
SORU 4 CEVAP
sadece isim ve maaş sütunları 
      isim  maas
0     Ali  5000
1    Ayşe  7000
2  Mehmet  6000
3  Zeynep  8000
4   Ahmet  4500
5    Elif  6500
--------------------------------------------------
SORU 5 CEVAP
Yaşı 28'den büyük olan kişiler 
      isim  yas     sehir  maas
1    Ayşe   30  İstanbul  7000
3  Zeynep   35     İzmir  8000
--------------------------------------------------
SORU 6 CEVAP
Maaşı 6000'den büyük olan kişilerin sadece isim ve maaş bilgileri 
      isim  maas
1    Ayşe  7000
3  Zeynep  8000
5    Elif  6500
--------------------------------------------------
SORU 7 CEVAP
Maaşa göre küçükten büyüğe sıralama 
      isim  yas     sehir  maas
4   Ahmet   22     Bursa  4500
0     Ali   25    Ankara  5000
2  Mehmet   28    Ankara  6000
5    Elif   27  İstanbul  6500
1    Ayşe   30  İstanbul  7000
3  Zeynep   35     İzmir  8000
--------------------------------------------------
SORU 8 CEVAP
Maaşa göre büyükten küçüğe sıralama 
      isim  yas     sehir  maas
3  Zeynep   35     İzmir  8000
1    Ayşe   30  İstanbul  7000
5    Elif   27  İstanbul  6500
2  Mehmet   28    Ankara  6000
0     Ali   25    Ankara  5000
4   Ahmet   22     Bursa  4500
--------------------------------------------------
SORU 9 CEVAP
Şehir bazında maaşların ortalaması 
 sehir
Ankara      5500.0
Bursa       4500.0
İstanbul    6750.0
İzmir       8000.0
Name: maas, dtype: float64
--------------------------------------------------
SORU 10 CEVAP
     isim  yas     sehir  maas  yillik_maas
0     Ali   25    Ankara  5000        60000
1    Ayşe   30  İstanbul  7000        84000
2  Mehmet   28    Ankara  6000        72000
3  Zeynep   35     İzmir  8000        96000
4   Ahmet   22     Bursa  4500        54000
5    Elif   27  İstanbul  6500        78000
--------------------------------------------------

"""