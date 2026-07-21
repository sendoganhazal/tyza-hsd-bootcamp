import sys
try:
    import pandas as pd
    import openpyxl
except ImportError:
    print("Unable to import 'pandas'. Please install it with 'pip install pandas'.")
    sys.exit(1)

# DOSYA OKUMA VE YAZMA

# csv (comma seperated values) dosyası okuma 
df = pd.read_csv("veri.csv")
print(df)
"""
     isim   yas   not
0    kaan    35    90
1     can    25    95
2  yılmaz    30    85
"""

# excel dosyası okuma

df = pd.read_excel("veri_excel.xlsx")
print("excel \n",df)
"""
excel 
      isim  yas  not
0    kaan   35   95
1     can   25   90
2  yılmaz   30   85
"""


veri = {
    "isim": ["Ali","Ayse","Mehmet"],
    "yas": [25,30,28],
    "sehir":["Ankara","İstanbul","İzmir"]
}

df = pd.DataFrame(veri)

#csv dosyası yazma
df.to_csv("veri_output.csv", index=False)

# excel dosyası yazma
df.to_excel("veri_output.excel",index=False)