import matplotlib.pyplot as plt

# PIE CHART (Pasta Grafiği)
# bir bütünün parçalarını görmek için kullanırız

# pasta graiği oluşturma
etiketler = ["python", "java", "c++", "javascript"]
degerler = [40, 25, 20, 15]

# plt.pie ile pasta grafiği oluşturulur
# değerler = pasta dilimlerinin büyüklüğü
# labels = etiketleri
# autopct = dilimlerin üstüne yüzdelik oranlarını yazar
# %1.1f%% = yüzdeyi 1 basamaklı ondalık ile gösterir
ayrim = [0.1, 0, 0, 0]
renkler = ["red", "blue", "green", "orange"]
plt.pie(degerler, labels=etiketler, autopct="%1.1f%%", explode=ayrim, colors=renkler)
plt.title("Programlama Dili Kullanım Oranları")

plt.show()