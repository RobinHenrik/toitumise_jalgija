import time
from profiilid_sonastikku import profiilid_sõnastikku
from profiilid import profiilid
import andmebaasi_funktsioonid
import toidukorrad
import tagastamine


profiili_andmed = profiilid()
toidu_andmebaas = andmebaasi_funktsioonid.toidud_sõnastikku()

nimi = profiili_andmed['nimi']

while True:
    print("Tänase toitumise lisamiseks sisestage L")
    time.sleep(0.2)
    print("Toitumise ajaloo vaatamiseks sisestage A")
    time.sleep(0.2)
    print("Programmist väljumiseks sisestage X")
    time.sleep(0.2)
    valik = input("Sisestage valik: ").lower()

    if valik == "l":
        toidukorrad.toidukorra_lisamine(nimi, toidu_andmebaas)

    elif valik == "a":
        tagastamine.tagastamine(nimi)

    elif valik == "x":
        break

    else:
        print("Ebakorrektne sisend")
