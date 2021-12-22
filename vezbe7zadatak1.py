def main():
    bodovi = eval(input("Unesite bodove: "))
    ocenjivanje(bodovi)


def ocenjivanje(bodovi):
    if (bodovi <= 55):
        print("Ocena je 5")
    elif (bodovi <= 65):
        print("Ocena je  6")
    elif (bodovi <= 75):
        print("Ocena je 7")
    elif (bodovi <= 85):
        print("Ocena je 8")
    elif (bodovi <= 95):
        print("Ocena je 9")
    elif (bodovi <= 100):
        print("Ocena je 10")
    else:
        print("Niste uneli validne podatke!!!")

 

main()