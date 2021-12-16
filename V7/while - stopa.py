def main():
    kamata = eval(input("Unesite kamatu: "))
    iznos = eval(input("Unesite iznos: "))
    print(godisnjaStopa(kamata,iznos))


def godisnjaStopa(kamata,iznos):

    godina = 0
    dupli_iznos = iznos * 2 

    while (iznos <= dupli_iznos):
        iznos = iznos + iznos * kamata
        godina = godina + 1 
    
    return godina 


main()


