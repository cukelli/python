def main():
    niz = [1,2,3,4,5,-1,6]
    print("Najmanji element niza je",najmanji(niz))
    print( "Najveci element niza je",najveci(niz))
    print("Suma niza je",suma(niz))
    print("Srednja vrednost niza je",srednja_vrednost(niz))


def najmanji(niz):
    minimalni = min(niz)
    return minimalni


def najveci(niz):
    maksimalni = max(niz)
    return maksimalni 

def suma(niz):
    zbir = sum(niz)
    return zbir 

def srednja_vrednost(niz):
    srednja = round( sum(niz) / len(niz),2)
    return srednja 




main()



