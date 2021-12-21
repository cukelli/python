def main():
    fajl = 'bank_log.txt'
    odredi_stanje(fajl)


def odredi_stanje(fajl):
    otvori = open(fajl, 'r')
    linije = otvori.readlines()

    svi_korisnici = []

    for linija in linije:
        svi_korisnici.append(linija.split(" ")[0])
    otvori.close()

    jedinstveni_korisnici = odredi_jedinstvene(svi_korisnici)
    fajl = open('korisnici.txt','w')

    for korisnik in jedinstveni_korisnici:
        stanje = float()
        for linija in linije:
            if (korisnik == linija.split(" ")[0]):
                if (linija.split(" ")[1] == 'withdrawal'):
                    stanje = stanje - float(linija.split(" ")[2])
                else:
                    stanje = stanje + float(linija.split(" ")[2])
        fajl.write(korisnik + " " + str(stanje) + "\n")
        print(korisnik, stanje)



def odredi_jedinstvene(korisnici):
    jedinstveni_korisnici = []
    for korisnik in korisnici:
        unique = True
        for jedinstven_korisnik in jedinstveni_korisnici:
            if (korisnik == jedinstven_korisnik):
                unique = False

        if unique:
            jedinstveni_korisnici.append(korisnik)

    return jedinstveni_korisnici


main()
