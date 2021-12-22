def main():
    satnica = eval(input("Unesite satnicu: "))
    fajl = 'radnici.txt'
    obracunaj_zaradu(satnica, fajl)


def obracunaj_zaradu(satnica, fajl):
    otvori_fajl = open(fajl, 'r')
    linije = otvori_fajl.readlines()
    sum = 0
    otvori_fajl.close()
    for linija in linije:
        sum = int(linija.split("|")[1]) + int(linija.split("|")[2]) + int(
            linija.split("|")[3]) + int(linija.split("|")[4]) + int(linija.split("|")[5])
        print("Suma radnih sati za " +
              str(linija.split("|")[0]) + " je " + str(sum))

        if (sum > 40):
            plata = (sum * satnica) * 1.5
            print("Prekovremeno")
            print("Plata iznosi", plata)
        else:
            plata = (sum * satnica)
            print("Nije prekovremeno ")
            print("Plata iznosi", plata)


main()
