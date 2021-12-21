def main():
    ime = veliko_slovo(input("Unesite ime: "))
    prezime = veliko_slovo(input("Unesite prezime: "))
    broj_indeksa = proveri_indeks(input("Unesite broj indeksa: "))
    godina_studija = input("Unesite godinu studija: ")
    pisi(ime, prezime, broj_indeksa, godina_studija)


def veliko_slovo(ime):
    if (ime.istitle() == False):
        ime = input("Unesite ponovo ime: ")

    return ime


def proveri_indeks(indeks):
    fajl = open('evidencija.txt', 'r')
    data = fajl.read().replace("\n", "|").split("|")

    while indeks in data:
        indeks = input("Unesite indeks ponovo, ovaj vec postoji: ")
    return indeks


def pisi(ime, prezime, broj_indeksa, godina_studija):
    fajl = open('evidencija.txt', 'a')
    fajl.write("\n" + ime + "|" + prezime + "|" +
               broj_indeksa + "|" + godina_studija)

    fajl.close()

    print("Uspesno dopisano!")


main()
