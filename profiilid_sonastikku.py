def profiilid_sõnastikku():
    f = open("profiilid.txt", "r", encoding="utf-8")
    profiilid  = {}
    for rida in f:
        rida = rida.strip("\n")
        rida = rida.split(",")
        profiili_nimi = rida[0].lower()
        vanus = float(rida[1])
        kehakaal = float(rida[2])
        pikkus = float(rida[3])
        bmi = float(rida[4])


        profiilid[profiili_nimi] = {}
        profiilid[profiili_nimi]['vanus'] = vanus
        profiilid[profiili_nimi]['kehakaal'] = kehakaal
        profiilid[profiili_nimi]['pikkus'] = pikkus
        profiilid[profiili_nimi]['bmi'] = bmi
        

    return profiilid

print(profiilid_sõnastikku())