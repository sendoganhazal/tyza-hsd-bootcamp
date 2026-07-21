#tuples
koordinatlar = (48.8602311,2.3367602)
renkler = ("kırmızı", "mavi", "yeşil")

print(koordinatlar)
print(renkler)

#liste vs. tuples
# listelerde itemlar değiştirilebilirdir
# tuplelarda itemlar değiştirilemez

liste = [1,2,3]
liste[0] = 99 
print(liste)

tup = (1, 2, 3)
# tup[0] = 99
# print(tup) TypeError: 'tuple' object does not support item assignment

#Indexing {tuple_name(index)}
t = (10,20,30)

t_1 = t[1]
t_last = t[-1]

print(t_1)
print(t_last)

#slicing {tuple_name(start:end)} start'tan end'e kadar olan itemları verir. end dahil değildir
t = (10,20,30,40) 

bir_uc = t[1:3] #1.indexteki elemandan 3. indexteki elemana  kadar (yani 2. elemandan 4. elemana kadar ) olan elemanları alır
print(bir_uc) # (20, 30)

#tek elemanlı tuple
x = (5)
x_type = type(x) # tek değişkenli tuplelarda tuple'nın tipi elemanın tipidir
print(x_type) # <class 'int'>

x = (5,)
x_type = type(x) 
print(x_type) # <class 'tuple'>

#tuple unpacking
koordinatlar = (10,20)
x,y = koordinatlar
print(x)
print(y)

#tuples methods
t = (20, 20, 30, 40)

#counting
print(t.count(20)) #20den 2 adet var

#finding index number
print(t.index(30)) #30'un indexi 2