def toidud_sõnastikku():
    f = open("toiduandmed.csv", "r", encoding="utf-8")
    toiduandmed = {}
    for rida in f:
        rida = rida.strip("\n")
        rida = rida.split(",")
        toidu_nimi = rida[0].lower()
        kcal = rida[1]
        susivesikud = rida[2]
        rasvad = rida[3]
        kiudained = rida[4]
        valgud = rida[5]
        vesi = rida[6]
        suhkrud = rida[7]
        toiduandmed[toidu_nimi] = {}
        toiduandmed[toidu_nimi]['kcal'] = kcal
        toiduandmed[toidu_nimi]['süsivesikud'] = susivesikud
        toiduandmed[toidu_nimi]['suhkrud'] = suhkrud
        toiduandmed[toidu_nimi]['rasvad'] = rasvad
        toiduandmed[toidu_nimi]['valgud'] = valgud
        toiduandmed[toidu_nimi]['kiudained'] = kiudained
        toiduandmed[toidu_nimi]['vesi'] = vesi
    return toiduandmed

toiduandmed = toidud_sõnastikku()

seahakkliha_kcal = toiduandmed['seahakkliha']['kcal']
print(seahakkliha_kcal)