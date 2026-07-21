# Lists (Listeler)
sayilar = [1, 2, 3, 4, 5] #integer list
isimler = ["Hazal","Alex","Charou", "Cassie"] # string listesi
karisik = ["Hazal", "Alex", 55, 65.5] #farklı veri tiplerini aynı anda saklayabilir

print (karisik)

#Listelerde indexleme (Indexing)
#index 0'dan başlar
meyveler = ["Elma", "Muz", "Kivi"]

print(f"1. eleman {meyveler[0]}") #elma
print(f"2. eleman {meyveler[1]}") #muz 
print(f"3. eleman {meyveler[2]}") #kivi
print(f"3. eleman {meyveler[-1]}") #kivi # sonuncu elemanı verir


#liste uzunluğu (eleman sayısı) - Length
eleman_sayisi = len(meyveler)
print(f"eleman sayısı = {eleman_sayisi}")

# Slicing - Dilimleme
sayilar = [10, 20, 30, 40, 50, 60]

iki_dort = sayilar[1:4] # 2., 3. ve 4. itemları yazdırmak  yazdırmak istiyorum. # [a:b] a: dahil, b: dahil değil
print(iki_dort) #20, 30, ve 40

ilk_uc = sayilar[0:3] # ilk üç elemanı yazdırmak istiyorum. 
# [:3] yazarsak da ilk üç itemı getirir.
print(ilk_uc) # 10, 20, 30

uc_sonrasi = sayilar[2:] # üçüncü elemandan sonrasını yazdırır
print(uc_sonrasi) #30, 40,50, 60


#Listeye eleman ekleme
sayilar = [1,2,3]
sayilar.append(4)

print(sayilar) # [1,2,3,4]


#Insert (index, item) => (index). indexe (item) ekler
sayilar.insert(1,100) # index 1 olacak şekilde (2. eleman olarak) 100'ü ekler
print(sayilar) # [1 , 100, 2, 3, 4]

#eleman çıkarma => remove(item)
sayilar.remove(100) #100'ü sayilar listesinden çıkartır
print(sayilar) # [1,2,3,4]

#son elemanı çıkarma => pop()
sayilar.pop()
print(sayilar) # [1,2,3]

#belirli indexteki elemanı çıkarma => pop(index)
sayilar.pop(0) # ilk itemı siler
print(sayilar) # [2,3]

#belirli bir indexteki değeri değiştirme
sayilar[0] =  999
print(sayilar) #[999,3]