import matplotlib.pyplot as plt 

# BAR CHART (SÜTUN GRAFİĞİ) 
# kategorik verileri karşılaştırmak için kullanılır

# sütun grafiği oluşturma
isimler = ["Ali", "Ayşe", "Mehmet", "Zeynep"]
notlar = [70, 85, 60, 90]

# plt.bar() sütun grafiği oluşturur
#  x = isimler, y = notlar
renkler = ["red", "blue","green","purple"]
plt.bar(isimler, notlar, color= renkler)
plt.title("Öğrenci Notları") # grafiğe başlık ekler
plt.xlabel("Öğrenciler") # x ekseninin adı
plt.ylabel("Notlar") # y ekseninin adı

plt.show()


# yatay sütun grafiği
plt.barh(isimler,notlar)
plt.show()