import matplotlib.pyplot as plt

# LINE PLOT (Çizgi Grafiği)
# zaman içerisinde değişen verileri görselleştirmek için kullanırız

#çizgi grafiği oluşturma
gunler = [1, 2, 3, 4, 5]
sicaklik = [22, 24, 23, 25, 27]

# x = günler , y = sicaklik
# color = çizginin rengini değiştirir
# marker = noktaları gösterir
plt.plot(gunler, sicaklik, color = "red", marker="o") # (x,y) grafiği oluşturur.
plt.title("Günlere Göre Sıcaklık") #Grafik başlığı
plt.xlabel("Günler") # x ekseni etiketi
plt.ylabel("Sıcaklık") #y ekseni etiketi
plt.grid(True)

plt.show() #grafiği ekranda gösterir