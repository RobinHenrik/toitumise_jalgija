import re
from datetime import datetime, timedelta

def tagastamine(profiili_nimi):

    while True:
        kuupaev = input("Mis kuupäeva toitumisinfot soovite näha? (PP/KK/AAAA): ")
        oige_formaat = re.match('^[0-3]{1}[0-9]{1}/[0-1]{1}[0-9]{1}/[0-9]{4}$', kuupaev)
        if oige_formaat:
            break
        else:
            print("Vigane kuupäev")
    

    f = open(f"profiilid/{profiili_nimi}.txt", "r", encoding="utf-8")

    kcal = 0
    susivesikud = 0
    suhkrud = 0
    rasvad = 0
    valgud = 0
    kiudained = 0

    if f"{kuupaev}\n" not in f.readlines():
        print("Selle kuupäeva kohta info puudub.")
        return 0
    
    f.seek(0)

    for line in f:
        if kuupaev in line:
            break
    
    for line_1 in f:
        line_1 = line_1.strip()
        if re.match('^[0-9]{2}/[0-9]{2}/[0-9]{4}$', line_1):
            break
        if line_1 != "":
            andmed = line_1.split(",")
            andmed = andmed[2:]
            kcal += float(andmed[0].split(": ")[1])
            susivesikud += float(andmed[1].split(": ")[1])
            suhkrud += float(andmed[2].split(": ")[1])
            rasvad += float(andmed[3].split(": ")[1])
            valgud += float(andmed[4].split(": ")[1])
            kiudained += float(andmed[5].split(": ")[1])

    print(f"Kuupäeval {kuupaev} tarvitasite kokku {round(kcal, 1)}kcal, {round(susivesikud, 1)}g süsivesikuid, \
{round(suhkrud, 1)}g suhkruid, {round(rasvad, 1)}g rasvu, {round(valgud, 1)}g valke ning {round(kiudained, 1)}g kiudaineid")
