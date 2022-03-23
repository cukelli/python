def main():
    tezina = eval(input("Unesite tezinu: "))
    visina = float(input("Unesite visinu: "))
    bmi(visina,tezina)


def bmi(tezina,visina):

    bmi = tezina / visina * visina

    if (bmi < 18.5):
        print("Pothranjeni ste")
    elif (bmi < 25):
        print("Idealna telesna tezina")
    elif (bmi <30):
        print("Preterana telesna tezina")
    else:
        print("Gojaznost")










main()