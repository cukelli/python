def main():
    naziv_fajla = 'radnici.txt'
    nadji_prosecnu_platu(naziv_fajla)


def nadji_prosecnu_platu(naziv_fajla):

    otvori_fajl = open(naziv_fajla, 'r')
    linije = otvori_fajl.readlines()
    brojac = 0
    suma = float()

    for linija in linije:

        if (linija.split("|")[1] == 'Z'):
            brojac = brojac + 1
            suma = suma + float(linija.split("|")[2])

    prosek = suma / brojac
    print("Prosecna plata osoba zenskog pola iznosi", int(prosek))


main()


main()
