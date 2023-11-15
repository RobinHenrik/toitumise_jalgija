from toidud_sonastikku import toidud_sõnastikku

def lisa_andmebaasi():
    toit = input("Sisesta toit, mida soovid andmebaasi lisada: ").capitalize()
    andmed = toidud_sõnastikku()
    if toit.lower() in andmed.keys():
        print("See toit on juba andmebaasis")
        return False
    f = open("toiduandmed.csv", "a", encoding="utf-8-sig")

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

lisa_andmebaasi()