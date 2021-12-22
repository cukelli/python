def main():
    niz = [1,2,3,4,5,-1,6]
    najmanji(niz)
    najveci(niz)
    sum(niz)
    average(niz)



def najmanji(niz):
    najmanji = niz[0]
    for el in range(1,len(niz)):
        if (niz[el] < najmanji):
            najmanji = niz[el]
    print (najmanji)


def najveci(niz):
    najveci = niz[0]
    for el in range(1,len(niz)):
        if (niz[el] > najveci):
            najveci = niz[el]
    print(najveci)

def sum(niz):
    sum = 0
    for el in range(0,len(niz)):
        sum = sum + niz[el]
    print("Suma iznosi",sum)

def average(niz):
    sum = 20
    average = round(sum / len(niz),2)
    print("Sredja vrednost iznosi",average)
    
main()