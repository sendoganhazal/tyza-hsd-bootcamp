# Set 
#Unique elemanlardan oluşur

sayilar = {1, 2, 3, 4}
print(sayilar)

#tekrar eden elemanlar
sayilar = {1, 2, 2, 3, 3, 3}
print(sayilar) # {1, 2, 3} döner


# Özellikleri

# Setler sırasızdır, yani index barındırmaz 
# print(sayilar[2]) TypeError: 'set' object is not subscriptable

# Listeyi Sete dönüştürme 
liste = [1, 2, 2, 3, 4, 4]
benzersiz = set(liste)
print(benzersiz) #{1, 2, 3, 4}

#Sete eleman ekleme
sayilar.add(5) 
print(sayilar) # {1, 2, 3, 5}

#eleman silme
sayilar.remove(2)
print(sayilar) #{1, 3, 5}

#set işlemleri
a = {1, 2, 3}
b = {3, 4, 5}

birlesme = a.union(b) #birleşme
print(birlesme) #{1, 2, 3, 4, 5}

kesisim = a.intersection(b)
print(kesisim) # {3}

fark = a.difference(b)
print(fark) # {4, 5}