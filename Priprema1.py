def main():
    rec = input("Unesite rec: ")
    pogresan_unos(rec)


def pogresan_unos(rec):
    sum = 0

    while (rec[-1] != 'a'):
        rec = input("Unesite rec:")
        sum = sum + 1

    print("Broj pogresnih unosa je", sum)


main()
