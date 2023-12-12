from andmebaasi_funktsioonid import lisa_andmebaasi
from andmebaasi_funktsioonid import toidud_sõnastikku
from datetime import date
import time
import os

def toidukorra_lisamine(profiili_nimi, toidu_andmebaas):

    tana = date.today()
    kuupaev = tana.strftime("%d/%m/%Y")

    f = open(f"profiilid/{profiili_nimi}.txt", "a+", encoding="utf-8")
    if os.stat(f"profiilid/{profiili_nimi}.txt").st_size != 0:
        f.write("\n")

    f.seek(0)
    if f"{kuupaev}\n" not in f.readlines():
        if os.stat(f"profiilid/{profiili_nimi}.txt").st_size != 0:
            f.write("\n")
            f.write("\n")
        f.write(kuupaev)
        f.write("\n")
    else:
        pass

    while True: 
        
        print("Toiduaine toidukorrale lisamiseks sisestage L")
        time.sleep(0.2)
        print("Lisamise funktsioonist väljumiseks sisestage V")
        time.sleep(0.2)

        tegevus = input("Sisestage valik: ").lower()

        if tegevus == "l":
            toit = input("Sisesta toiduaine: ").lower()

            if toit not in toidu_andmebaas.keys():
                while True:
                    print("Sellist toitu meie andmebaasis ei ole. Võite proovida toiduaine üldisemat nimetamist.")
                    print("Äkki mütlesite mõnda järgnevatest toiduainetest: ")
                    for key in toidu_andmebaas.keys():
                        if toit in key:
                            print(key)
                    valik = input("Kas soovid toidu andmebaasi lisada? (Y/N) ").lower()
                    if valik == "y":
                        lisa_andmebaasi()
                        toidu_andmebaas = toidud_sõnastikku()
                        break
                    elif valik == "n":
                        break
                    else:
                        print("Vigane sisend")
            
            else:

                gramme = int(input("Sisesta toiduaine kogus grammides: ")) / 100
                andmed = toidu_andmebaas[toit]
                kcal = andmed["kcal"] * gramme
                susivesikud = round(andmed["süsivesikud"] * gramme, 2)
                suhkrud = round(andmed["suhkrud"] * gramme, 2)
                rasvad = round(andmed["rasvad"] * gramme, 2)
                valgud = round(andmed["valgud"] * gramme, 2)
                kiudained = round(andmed["kiudained"] * gramme, 2)


                f.write(f"{toit},{gramme * 100}g,kcal: {kcal},süsivesikud: {susivesikud},\
suhkruid: {suhkrud},rasvad: {rasvad},valgud: {valgud},kiudained: {kiudained} \n")
                
        elif tegevus == "v":
            break

        else:
            print("Vigane sisend")
            continue
    f.close()

