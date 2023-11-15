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
        suhkrud = float(rida[7])
        toiduandmed[toidu_nimi] = {}
        toiduandmed[toidu_nimi]['kcal'] = kcal
        toiduandmed[toidu_nimi]['süsivesikud'] = susivesikud
        toiduandmed[toidu_nimi]['suhkrud'] = suhkrud
        toiduandmed[toidu_nimi]['rasvad'] = rasvad
        toiduandmed[toidu_nimi]['valgud'] = valgud
        toiduandmed[toidu_nimi]['kiudained'] = kiudained
    return toiduandmed
