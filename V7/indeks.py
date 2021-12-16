def kategorija(masa,visina):
    bmi = masa / (visina **2)

    if bmi < 18.5:
        return "Pothranjenost"
    elif bmi <= 25:
        return "Idealna telesna tezina"
    elif bmi <=30:
        return "Preterana telesna tezina"
    elif bmi >30:
        return "Smrsajte"

    

masa = int(input("Unesite masu: "))
visina = float(input("Unesite visinu:"))

print(kategorija(masa,visina))