def profiili_loomine():
    nimi = input("Sisestage oma nimi: ")
    vanus = float(input("Sisestage oma vanus: "))
    kaal = float(input("Sisestage oma kehakaal(kg): "))
    pikkus = float(input("Sisestage oma pikkus(cm): "))

    with open("profiilid.txt", encoding="utf-8") as f:
        profiilid = dict(f.readline().strip())

    print(profiilid)
    print(type(profiilid))
    profiilid["margus"] = {}
    profiilid[nimi]["vanus"] = vanus
    profiilid[nimi]["kaal"] = kaal
    profiilid[nimi]["pikkus"] = pikkus
    profiilid[nimi]["bmi"] = kaal / ((pikkus/100) ** 2)


    print(profiilid)


profiili_loomine()