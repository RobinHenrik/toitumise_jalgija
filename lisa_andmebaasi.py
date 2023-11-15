def lisa_andmebaasi(toit):
    f = open("toiduandmed.csv", "a", encoding="utf-8")
    kcal = float(input("Sisesta toidu kcal/100g: "))
    susivesikud = float(input("Sisesta toidu süsivesikud/100g: "))
    suhkrud = float(input("Sisesta toidu suhkrud/100g: "))
    rasvad = float(input("Sisesta toidu rasvad/100g: "))
    valgud = float(input("Sisesta toidu valgud/100g: "))
    kiudained = float(input("Sisesta toidu kiudained/100g (kui ei tea sisesta 0): "))
    