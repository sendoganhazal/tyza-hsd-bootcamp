"""
Veri analizi aracı
    - sayı listesi tutma
    - bu sayıların toplamını hesapla
    - ortalamasını bul
    - en büyük ve en küçük değerleri göster
"""


class VeriAnalizAraci:
    def __init__(self,veriler):
        self.veriler = veriler
    def veriyi_goster(self):
        print(f"Veriler: {self.veriler}")
    def toplam(self):
       toplam = sum(self.veriler)
       print(f"Toplam: {toplam}")
    def ortalama(self):
        ortalama = sum(self.veriler)/len(self.veriler)
        print(f"Ortalama: {ortalama}")
    def en_buyuk(self) :
        buyuk = max(self.veriler)
        print(f"Listedeki en büyük sayı: {buyuk}")
    def en_kucuk(self) :
        kucuk = min(self.veriler)
        print(f"Listedeki en küçük sayı: {kucuk}")
        
veri_analizi = VeriAnalizAraci([10,20,30,40,50,60])

veri_analizi.veriyi_goster()
veri_analizi.toplam()
veri_analizi.ortalama()
veri_analizi.en_buyuk()
veri_analizi.en_kucuk()