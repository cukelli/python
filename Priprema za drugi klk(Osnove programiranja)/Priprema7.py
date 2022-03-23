def main():
    petlja()


def petlja():
    suma = 0
    while (suma < 1000):
        num = eval(input("Unesite broj: "))

        if (num % 4 == 0):
            suma = suma + num
    print(suma)


main()
