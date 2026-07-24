import matplotlib.pyplot as plt


# ÖRNEK VERİ SETİ
# Aşağıdaki veri seti tüm sorular için kullanılacaktır.

aylar = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"]
satislar = [120, 150, 170, 160, 200, 220]
karlar = [20, 35, 40, 30, 50, 60]
reklam = [5, 8, 10, 7, 12, 15]


# SORU 1
# Aylar ve satışlar verisini kullanarak basit bir çizgi grafiği oluşturun.

plt.plot(aylar,satislar) # x = aylar ve y = satışlar olan bir çizgi grafiği oluşturulur
plt.title("Aylara Göre Satışlar") # grafiğin başlığı Aylara Göre Satışlar olarak ayarlanır
plt.xlabel("Aylar") # x ekseninin etiketi Aylar olarak ayarlandı
plt.ylabel("Satışlar") # y ekseninin etiketi Satışlar olarak ayarlandı
plt.show() # show fonksiyonu ile grafiğin gösterilmesi sağlanır


# SORU 2
# Aylar ve kârlar verisini kullanarak çizgi grafiği oluşturun.
# Çizgi rengi kırmızı olsun.

plt.plot(aylar,satislar, color="red") # x = aylar ve y = satışlar olan, rengi kırmızı olan bir çizgi grafiği oluşturulur
plt.title("Aylara Göre Satışlar") # grafiğin başlığı Aylara Göre Satışlar olarak ayarlanır
plt.xlabel("Aylar") # x ekseninin etiketi Aylar olarak ayarlandı
plt.ylabel("Satışlar") # y ekseninin etiketi Satışlar olarak ayarlandı
plt.show() # show fonksiyonu ile grafiğin gösterilmesi sağlanır


# SORU 3
# Aylar ve satışlar verisini kullanarak marker'lı bir çizgi grafiği oluşturun.

plt.plot(aylar,satislar, marker="o") # x = aylar ve y = satışlar olan, markerı "o" olan bir çizgi grafiği oluşturulur
plt.title("Aylara Göre Satışlar") # grafiğin başlığı Aylara Göre Satışlar olarak ayarlanır
plt.xlabel("Aylar") # x ekseninin etiketi Aylar olarak ayarlandı
plt.ylabel("Satışlar") # y ekseninin etiketi Satışlar olarak ayarlandı
plt.show() # show fonksiyonu ile grafiğin gösterilmesi sağlanır


# SORU 4
# Aylar ve satışlar verisini kullanarak sütun grafiği oluşturun.
plt.bar(aylar,satislar) # x = aylar ve y = satışlar olan bir sütun grafiği oluşturulur
plt.title("Aylara Göre Satışlar") # grafiğin başlığı Aylara Göre Satışlar olarak ayarlanır
plt.xlabel("Aylar") # x ekseninin etiketi Aylar olarak ayarlandı
plt.ylabel("Satışlar") # y ekseninin etiketi Satışlar olarak ayarlandı
plt.show() # show fonksiyonu ile grafiğin gösterilmesi sağlanır


# SORU 5
# Aylar ve reklam verisini kullanarak yeşil renkli bir sütun grafiği oluşturun.

plt.bar(aylar,reklam, color="green") # x = aylar ve y = reklam olan yeşil renkli bir sütun grafiği oluşturulur
plt.title("Aylara Göre Reklam Verileri") # grafiğin başlığı Aylara Göre Reklam Verileri olarak ayarlanır
plt.xlabel("Aylar") # x ekseninin etiketi Aylar olarak ayarlandı
plt.ylabel("Reklam Verileri") # y ekseninin etiketi Reklam Verileri olarak ayarlandı
plt.show() # show fonksiyonu ile grafiğin gösterilmesi sağlanır


# SORU 6
# Satışlar verisini kullanarak pasta grafiği oluşturun.
# Ay isimlerini etiket olarak gösterin ve yüzdeleri ekrana yazdırın.
plt.pie(satislar, labels=aylar, autopct="%1.1f%%") # satışlar verileri kullanılarak, ay isimlerini etiket olarak kullanan pasta grafiği oluşturulur
plt.title("Satışların Aylara Göre Dağılımı") # Grafiğin başlığı Satışların Aylara Göre Dağılımı olarak ayarlandı
plt.show() # show fonksiyonu ile grafiğin gösterilmesi sağlanır


# SORU 7
# Reklam ve satışlar verisini kullanarak scatter plot oluşturun.
plt.scatter(reklam,satislar) # Reklam ve satışlar verisini kullanarak scatter plot oluşturulur
plt.title("Reklam Harcamaları ve Satış Miktarı Arasındaki İlişki") # Grafiğin başlığı Satışların Reklam Harcamaları ve Satış Miktarı Arasındaki İlişki olarak ayarlandı
plt.xlabel("Reklam Verileri") # x ekseninin etiketi Reklam Verileri olarak ayarlandı
plt.ylabel("Satışlar") # y ekseninin etiketi Satışlar olarak ayarlandı
plt.show()  # show fonksiyonu ile grafiğin gösterilmesi sağlanır


# SORU 8
# Reklam ve kâr verisini kullanarak kırmızı renkli ve büyük noktalı scatter plot oluşturun.
plt.scatter(reklam,karlar) # Reklam ve Kar verisini kullanarak kırmızı büyük noktalı scatter plot oluşturulur
plt.title("Reklam Harcamaları ve Kar Miktarı Arasındaki İlişki") # Grafiğin başlığı Reklam Harcamaları ve Kar Miktarı olarak ayarlandı
plt.xlabel("Reklam Verileri") # x ekseninin etiketi Reklam Verileri olarak ayarlandı
plt.ylabel("Kar Miktarı") # y ekseninin etiketi Kar Miktarı olarak ayarlandı
plt.show()  # show fonksiyonu ile grafiğin gösterilmesi sağlanır


# SORU 9
# Aynı figür içinde 1 satır 2 sütun olacak şekilde iki grafik oluşturun.
# Solda satışlar için line plot, sağda kârlar için bar chart gösterin.

plt.subplot(1,2,1) # 1 satırlı 2 sütunlu grafiklerin 1.si oluşturuluyor
plt.plot(aylar,satislar) # x = aylar ve y = satışlar olan bir çizgi grafiği oluşturuldu
plt.title("Aylara Göre Satışlar") # grafiğin başlığı Aylara Göre Satışlar olarak ayarlanır
plt.xlabel("Aylar") # x ekseninin etiketi Aylar olarak ayarlandı
plt.ylabel("Satışlar") # y ekseninin etiketi Satışlar olarak ayarlandı

plt.subplot(1,2,2) # 1 satırlı 2 sütunlu grafiklerin 2.si oluşturuluyor
plt.bar(aylar,karlar) # x = aylar ve y = karlar olan bir sütun grafiği oluşturuldu
plt.title("Aylara Göre Karlar") # grafiğin başlığı Aylara Göre Karlar olarak ayarlanır
plt.xlabel("Aylar") # x ekseninin etiketi Aylar olarak ayarlandı
plt.ylabel("Karlar") # y ekseninin etiketi "Karlar olarak ayarlandı

plt.show() # show fonksiyonu ile grafiğin gösterilmesi sağlanır


# SORU 10
# 2 satır 2 sütun olacak şekilde 4 farklı grafik oluşturun.
# 1. grafik: satışlar line plot
# 2. grafik: kârlar bar chart
# 3. grafik: reklam-satış scatter plot
# 4. grafik: satışlar pie chart


plt.subplot(2,2,1) # 2 satırlı 2 sütunlu grafiklerin 1.si oluşturuluyor
plt.plot(aylar,satislar) # x = aylar ve y = satışlar olan bir çizgi grafiği oluşturuldu
plt.title("Aylara Göre Satışlar") # grafiğin başlığı Aylara Göre Satışlar olarak ayarlanır
plt.xlabel("Aylar") # x ekseninin etiketi Aylar olarak ayarlandı
plt.ylabel("Satışlar") # y ekseninin etiketi Satışlar olarak ayarlandı

plt.subplot(2,2,2) # 2 satırlı 2 sütunlu grafiklerin 2.si oluşturuluyor
plt.bar(aylar,karlar) # x = aylar ve y = karlar olan bir sütun grafiği oluşturuldu
plt.title("Aylara Göre Karlar") # grafiğin başlığı Aylara Göre Karlar olarak ayarlanır
plt.xlabel("Aylar") # x ekseninin etiketi Aylar olarak ayarlandı
plt.ylabel("Karlar") # y ekseninin etiketi "Karlar olarak ayarlandı

plt.subplot(2,2,3) # 2 satırlı 2 sütunlu grafiklerin 3.sü oluşturuluyor
plt.scatter(reklam,satislar) # Reklam ve satışlar verisini kullanarak scatter plot oluşturulur
plt.title("Reklam Harcamaları ve Satış Miktarı Arasındaki İlişki") # Grafiğin başlığı Satışların Reklam Harcamaları ve Satış Miktarı Arasındaki İlişki olarak ayarlandı
plt.xlabel("Reklam Verileri") # x ekseninin etiketi Reklam Verileri olarak ayarlandı
plt.ylabel("Satışlar") # y ekseninin etiketi Satışlar olarak ayarlandı

plt.subplot(2,2,4) # 2 satırlı 2 sütunlu grafiklerin 4.sü oluşturuluyor
plt.pie(satislar, labels=aylar, autopct="%1.1f%%") # satışlar verileri kullanılarak, ay isimlerini etiket olarak kullanan pasta grafiği oluşturulur
plt.title("Satışların Aylara Göre Dağılımı") # Grafiğin başlığı Satışların Aylara Göre Dağılımı olarak ayarlandı

plt.show() # show fonksiyonu ile grafiğin gösterilmesi sağlanır

