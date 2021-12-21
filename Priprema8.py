def main():
    naziv = input("Unesite naziv proizvoda: ")
    cena = input("Unesite cenu proizvoda: ")
    kolicina = input("Unesite kolicinu proizvoda: ")

    while (naziv != 'quit') and (cena != 'quit') and (kolicina != 'quit'):
        upisi(naziv, cena, kolicina)
        izlistaj()
        naziv = input("Unesite naziv: ")
        cena = input("Unesite cenu proizvoda: ")
        kolicina = input("Unesite kolicinu proizvoda: ")


def upisi(naziv, cena, kolicina):
    fajl = open('proizvodi.txt', 'a')
    fajl.write(naziv + "|" + cena + "|" + kolicina + "\n")
    fajl.close()


def izlistaj():
    fajl = 'proizvodi.txt'
    fajl = open('proizvodi.txt', 'r')
    linije = fajl.readlines()
    for linija in linije:
        print(linija)
    fajl.close()


main()
