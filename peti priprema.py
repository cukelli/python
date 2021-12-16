def main():
    ime = veliko_slovo(input("Unesite ime: "))
    prezime = veliko_slovo(input("Unesite preime: "))
    indeks = proveri_indeks(input("Unesite broj indeksa: "))
    godina = input("Unesite godinu studija:")
    pisanje(ime, prezime, godina, indeks)


def veliko_slovo(ime):
    if ime.istitle() == False:
        ime = input("Unesite ponovo ime,ne moze poceti velikim slovom: ")

    return ime


def proveri_indeks(indeks):
    fajl = open('evidencija.txt', 'r')
    data = fajl.read().replace("\n", "|").split("|")

    while indeks in data:
        indeks = input("Uneli ste vec postojeci indeks,molim Vas ponovo:")

    return indeks


def pisanje(ime, prezime, indeks, godina):
    fajl = open('evidencija.txt', 'a')
    fajl.write("\n" + ime + "|" + prezime + "|" + indeks + "|" + godina)

    fajl.close()

    print("Uspesno dopisano")


main()
