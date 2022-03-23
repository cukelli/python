def main():
    korisnici = 'korisnici.txt'
    racuni = 'racuni.txt'


def pisi_u_fajl(korisnici, racuni):

    fajl_korisnici = open(korisnici, 'r')
    fajl_racuni = open(racuni, 'r')

    linije_korisnici = fajl_korisnici.readlines()
    linije_racuni = fajl_racuni.readlines()

    fajl_racuni.close()
    fajl_korisnici.close()

    statistika = 'statistika.txt'
    fajl_statistika = open('statistika.txt', 'w')

    for j in range(0, len(linije_korisnici)):
        suma = 0
        # uglasta je zato sto SVAKU liniju splitujes po kosoj crti
        temp = linije_racuni[j].split("|")

        for i in temp:
            suma = suma + int(i)
            formatirana_suma = '{:.2f}'.format(suma)

        prosek = suma / len(temp)
        formatiran_prosek = '{:.2f}'.format(prosek)

        fajl_statistika.write(linije_korisnici[j].split(
            "|")[0] + "|" + str(formatirana_suma) + "|" + str(formatiran_prosek))
        fajl_statistika.write("\n")


main()
