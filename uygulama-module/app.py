
from methods import *

sonuc = urunleriGetir()

urunEkle("Iphone 20", 90000)
urunEkle("Samsung s20", 90000)

for i in urunleriGetir():
     print(i["urunAdi"])

urunGuncelle(1, "Iphone 15 pro",80000)

for i in urunleriGetir():
    print(i["urunAdi"])
