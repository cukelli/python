def main():
    fajl = 'bank_log.txt'
    korisnik = input("Unesite korisnika: ")
    stanje_na_racunu(fajl, korisnik)


def stanje_na_racunu(fajl, korisnik):
    fajl = 'bank_log.txt'
    otvori_fajl = open(fajl, 'r')
    linije = otvori_fajl.readlines()
    stanje = float()
    otvori_fajl.close()

    stanje = float()
    for linija in linije:
        if (linija.split(" ")[0] == korisnik):
            if (linija.split(" ")[1] == 'withdrawal'):
                stanje = stanje - float(linija.split(" ")[2])
            else:
                stanje = stanje + float(linija.split(" ")[2])
    print(korisnik, stanje_na_racunu)


main()
