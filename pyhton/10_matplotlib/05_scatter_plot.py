import matplotlib.pyplot as plt

# SCATTER PLOT (Dağılım Grafiği)
# iki değişken arasında ki ilişkiyi görmek için kullanılır

# dağılım grafiği oluşturma
calisma_saat = [1, 2, 3, 4, 5, 6]
notlar = [50, 55, 65, 70, 80, 90]

# plt.scatter dağılım grafiği oluşturur
# x = calisma_saat, y = notlar
# s = nokta büyüklüğünü değiştirme
plt.scatter(calisma_saat, notlar, color="red", s=100)
plt.title("Çalışma Süresi ve Sınav Notu İlişkisi")
plt.xlabel("Çalışma Süresi")
plt.ylabel("Sınavdan alınan notlar")

plt.show()


# birden fazla veri grubu görselleştirme

#fen sonuçları
x1 = [1, 2, 3, 4]
y1 = [50, 60, 70, 80]

#matematik sonuçalrı
x2 = [1, 2, 3, 4]
y2 = [55, 65, 75, 85]

plt.scatter(x1, y1, color="blue", label="fen")
plt.scatter(x2,y2, color="red", label="matematik")
plt.legend()

plt.show()