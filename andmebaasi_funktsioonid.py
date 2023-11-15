def toidud_sõnastikku():
    f = open("toiduandmed.csv", "r", encoding="utf-8")
    toiduandmed = {}
    for rida in f:
        rida = rida.strip("\n")
        rida = rida.split(",")
        toidu_nimi = rida[0].lower()
        kcal = float(rida[1])
        susivesikud = float(rida[2])
        rasvad = float(rida[3])
        kiudained = float(rida[4])
        valgud = float(rida[5])
        suhkrud = float(rida[6])
        toiduandmed[toidu_nimi] = {}
        toiduandmed[toidu_nimi]['kcal'] = kcal
        toiduandmed[toidu_nimi]['süsivesikud'] = susivesikud
        toiduandmed[toidu_nimi]['suhkrud'] = suhkrud
        toiduandmed[toidu_nimi]['rasvad'] = rasvad
        toiduandmed[toidu_nimi]['valgud'] = valgud
        toiduandmed[toidu_nimi]['kiudained'] = kiudained
    return toiduandmed

def lisa_andmebaasi():
    toit = input("Sisesta toit, mida soovid andmebaasi lisada: ").capitalize()
    andmed = toidud_sõnastikku()
    if toit.lower() in andmed.keys():
        print("See toit on juba andmebaasis")
        return False
    f = open("toiduandmed.csv", "a", encoding="utf-8")

    while True:
        try:
            kcal = float(input("Sisesta toidu kcal/100g: "))
        except ValueError:
            print("Kcal peab sisetama numbrina.")
            continue 
        break

    while True:
        try:
            susivesikud = float(input("Sisesta toidu süsivesikud/100g: "))
        except ValueError:
            print("Süsivesikud peab sisetama numbrina.")
            continue
        break

    while True:
        try:
            suhkrud = float(input("Sisesta toidu suhkrud/100g: "))
        except ValueError:
            print("Suhkrud peab sisetama numbrina.")
            continue
        break

    while True:
        try:
            rasvad = float(input("Sisesta toidu rasvad/100g: "))
        except ValueError:
            print("Rasvad peab sisetama numbrina.")
            continue
        break

    while True:
        try:
            valgud = float(input("Sisesta toidu valgud/100g: "))
        except ValueError:
            print("Valgud peab sisetama numbrina.")
            continue
        break
    while True:
        try:
            kiudained = float(input("Sisesta toidu kiudained/100g (kui ei tea sisesta 0): "))
        except ValueError:
            print("Kiudained peab sisetama numbrina.")
            continue
        break
    f.write(f"{toit},{kcal},{susivesikud},{rasvad},{kiudained},{valgud},{suhkrud}\n")
    f.close()

