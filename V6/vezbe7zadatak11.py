def prestupna_godina(godina):
    if (godina % 100 == 0):
        if (godina % 400 == 0):
            print("Prestupna je")
        else:
            print("Nije prestupna")
    
    else:
        if (godina % 4 == 0):
            print("Jeste prestupna")
        else:
            print("Nije prestupna")


def main():
    godina = int(input("Unesite godine: "))
    prestupna_godina(godina)


main()