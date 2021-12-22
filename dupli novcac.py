def main():
    kamata = eval(input("Unesite kamatu u procentima: "))
    iznos = eval(input("Unesite iznos: "))
    udvostrucen_novac(kamata, iznos)


def udvostrucen_novac(kamata, iznos):
    dupli_iznos = iznos * 2

    novi_iznos = iznos + (iznos / 100) * kamata
    godina = 1

    while (novi_iznos < dupli_iznos):
        godina = godina + 1
        novi_iznos = novi_iznos + (novi_iznos / 100) * kamata
    print("Broj godina potreban da se novac udvostruci je ", godina)


main()
