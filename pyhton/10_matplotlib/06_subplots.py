import matplotlib.pyplot as plt

# SUBPLOTS (Alt Grafikler)
# birden fazla grafiği aynı anda gösterme  

x = [1, 2, 3, 4]
y1 = [10, 20, 30, 40]
y2 = [40, 30, 20, 10]

# plt.subplot(row_quantity, col_quantity,index)
plt.subplot(1, 2, 1) # 1 satır 2 sütundan oluşan 1. grafiği oluşturuyoruz.
plt.plot(x,y1) 
plt.title("Grafik 1")

plt.subplot(1, 2, 2) # 1 satır 2 sütundan oluşan 21. grafiği oluşturuyoruz.
plt.plot(x,y2) 
plt.title("Grafik 2")


plt.show()

# farklı grafik türlerini kullanma
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Line Plot")

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("Bar Plot")

plt.show()


# 2 x 2 grafik oluşturma
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("Grafik 1")

plt.subplot(2,2,2)
plt.bar(x,y)
plt.title("Grafik 2")

plt.subplot(2,2,3)
plt.scatter(x,y)
plt.title("Grafik 3")

plt.subplot(2,2,4)
plt.pie(y)
plt.title("Grafik 4")


plt.show()