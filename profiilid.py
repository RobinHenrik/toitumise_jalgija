import time

def faili_lugemine():
    global andmed
    with open('profiilid.txt', encoding='utf-8') as f:
        andmed = []
        for rida in f:
            if rida.strip() != '':
                andmed.append(rida.strip().split(','))

    for jar in andmed:                #TEEN KÕIK ANDMED FAILIS PEALE NIME FLOATIDEKS
        for i in range(1, len(jar)):
            jar[i] = float(jar[i])
    return andmed


def profiili_loomine():
    tehtud = 0
    while tehtud == 0:
        try:
            nimi = input("Sisestage oma nimi: ")
            vanus = float(input("Sisestage oma vanus: "))
            kaal = float(input("Sisestage oma kehakaal(kg): "))
            pikkus = float(input("Sisestage oma pikkus(cm): "))
            with open("profiilid.txt", "a", encoding="utf-8") as f:
                f.write(f"{nimi},{vanus},{kaal},{pikkus},{round(kaal / ((pikkus/100) ** 2), 2)}\n") #LISAN FAILI PROFIILI: NIMI,VANUS,KAAL,PIKKUS,BMI
            andmed = faili_lugemine()
            tehtud += 1

        except ValueError:
            print("Sisestasite midagi valesti. Vanus, kaal ja pikkus peavad olema numbrilised.\nProovige uuesti.")
            time.sleep(0.5)




def prindi_profiilinimed():
    profiile_prinditud = 1
    for rida in andmed:         #PRINDIB VÄLJA OLEMASOLEVAD PROFIILID(profiilinimede suured tähed on nii nagu profiili luues sisestati)
        if profiile_prinditud < len(andmed):
            print(rida[0], end=", ")
            profiile_prinditud += 1
        else:
            print(rida[0])



def profiili_kustutamine(kustutatav): #PROFIILIDE KUSTUTAMINE
    kustutatud = 0 #KUI MINGI RIDA EI KIRJUTATA UUESTI FAILI, SIIS MUUTUB SELLE VÄÄRTUS SUUREMAKS JA SAAN ANDA KASUTAJALE TEADA, ET RIDA EI KUSTUTATUD

    with open('profiilid.txt', encoding='utf-8') as f:
        andmed = f.readlines()
    
    with open('profiilid.txt', "w", encoding='utf-8') as f:
        for i in range(len(andmed)):
            andmed[i] = andmed[i].strip().split(",")
            if andmed[i][0].lower() != kustutatav.lower():
                f.write(",".join(andmed[i]) + "\n")
            else:
                kustutatud += 1
    faili_lugemine()
    return kustutatud



def profiili_muutmine(muudetav):
    print("Sisestage andmed uuesti.")
    kustutatud = profiili_kustutamine(muudetav)
    if kustutatud == 0:
        print("Profiil antud nimega puudub, äkki sisestasid profiilinime valesti?")
    else:
        profiili_loomine()
        print("Profiil muudetud!")



andmed = faili_lugemine()
if andmed == []:            #KUI ANDMED PUUDUVAD, PEAB PROFIILI LOOMA
    print("Loo endale profiil.")
    profiili_loomine()
    print("Profiil loodud!")
    #andmed = faili_lugemine()

tegu = ""
while tegu != "c":
    time.sleep(0.2)
    print("Uue profiili loomiseks sisestage A")
    time.sleep(0.2)
    print("Profiili muutmiseks sisestage B")
    time.sleep(0.2)
    print("Profiili valimiseks sisestage C")
    time.sleep(0.2)
    print("Profiili kustutamiseks sisestage X")
    tegu = input("Sisestage valik: ").lower()

    if tegu == "a": #profiili loomine
        print("Loo endale profiil.")
        profiili_loomine()
        print("Profiil loodud!")
        #andmed = faili_lugemine()

    elif tegu == "b": #profiili muutmine
        prindi_profiilinimed()
        muudetav = input("Muudetava profiili nimi: ")
        sobis = profiili_muutmine(muudetav)
        #if sobis == False:
            #print("Profiil antud nimega puudub, äkki sisestasid profiilinime valesti?")

    elif tegu == "x": #profiili kustutamine
        prindi_profiilinimed()
        kustutatav = input("Sisesta kustutatava profiili nimi(C kui soovid tühistada): ").lower()
        if kustutatav != "c":
            kustutatud = profiili_kustutamine(kustutatav)
            if kustutatud == 0:            
                print("Ühtegi profiili ei kustutatud, äkki sisestasid profiilinime valesti?")
                time.sleep(1)
            else:
                print("Profiil edukalt kustutatud")
                time.sleep(1)

    elif tegu == "c":
        break

    else:
        print("Peate sisestama A, B, C või C")


prindi_profiilinimed()        #PRINDIB VÄLJA OLEMASOLEVAD PROFIILID(profiilinimede suured tähed on nii nagu profiili luues sisestati)


for jär in andmed:          #PROFIILINIMED VÄIKESEKS
    jär[0] = jär[0].lower()


valik = input("Vali väljatoodud profiilidest enda profiil: ").lower()
for jär in andmed:
    print(jär[0])
