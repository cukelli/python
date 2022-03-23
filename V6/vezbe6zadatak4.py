def main():
    fajl = 'users.txt'
    citaj(fajl)


def citaj(fajl):
    otvori = open(fajl,'r')
    linije = otvori.readlines()
    for linija in linije:
        print(linija)



main()