# Prosecna plata svih osoba zenskog pola

def main():
    ime_fajla = 'file.txt'
    nadji_prosecnu_platu(ime_fajla)


def nadji_prosecnu_platu(ime_fajla):
    fajl = open(ime_fajla, 'r')
    linije = fajl.readlines()
    suma = float()
    brojac = 0
    for linija in linije:

        if (linija.split("|")[1] == "Z"):
            brojac = brojac + 1
            suma = suma + float(linija.split("|")[2])
        else:
            suma = suma + 0
            brojac = brojac + 0
    prosek = suma / brojac
    print("Prosecna plata osoba zenskog pola iznosi", int(prosek))

    fajl.close()


main()
