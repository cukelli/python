def main():
    broj = eval(input("Unesite broj: "))
    pogresan_unos(broj)


def pogresan_unos(broj):
    suma = 0

    while (broj % 2 == 0):
        suma = suma + broj
        broj = eval(input("Unesite broj: "))

        if (broj % 2 != 0):
            print("Suma iznosi", suma)
            break


main()
