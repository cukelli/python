def main():
    korisnici = 'korisnici.txt'
    racuni = 'racuni.txt'
    snimi_u_fajl(korisnici, racuni)


def snimi_u_fajl(korisnici, racuni):
    fajl_korisnici = open(korisnici, 'r')
    fajl_racuni = open(racuni, 'r')

    linije_korisnici = fajl_korisnici.readlines()
    linije_racuni = fajl_racuni.readlines()

    fajl_korisnici.close()
    fajl_racuni.close()

    statistika = 'statistika.txt'

    fajl_statistika = open('statistika.txt', 'w')

    for j in range(0, len(linije_korisnici)):
        temp = linije_racuni[j].split("|")
        rez = 0
        for i in temp:
            rez = rez + int(i)

        sum = (rez/len(temp))

        fajl_statistika.write(linije_korisnici[j].split(
            "|")[0] + "|" + str(rez) + "|" + str(sum))
        fajl_statistika.write("\n")


main()
