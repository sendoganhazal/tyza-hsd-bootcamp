# veri tipi kontrolü
x = 10
x_type = type(x)

print(f"x değişkeninin tipi {x_type}") # <class 'int'>

y = "10"
y_type = type(y);

print(f"y değişkeninin tipi {y_type}") # <class 'str'>

#tip dönüşümleri (casting)

a = "10" #str
str_to_int = int(a)
str_to_flo = float(a)
tip_a = type(a);

print(f"a'nın tipi {tip_a}")
print(f"a'yı stringden {type(str_to_int)}'a dönüştürdüm")
print(f"a'yı stringden {type(str_to_flo)}'a dönüştürdüm")

b = 25
int_to_str = str(b);
tip_b = type(b)

print(f"b'nın tipi {tip_b}")
print(f"b'yi {tip_b}'dan {type(str_to_int)}'a dönüştürdüm")

sayi = input("Lütfen bir sayı giriniz:") #<class 'str'>
sayi2 = int(sayi)

print(f"girilen sayi {sayi2}, tipi {type(sayi2)}")