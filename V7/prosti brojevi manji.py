import math as m

def prost_broj(broj):
    kraj = m.sqrt(broj)
    delilac = 2

    while (delilac < kraj):
        if (broj % delilac ==0):
            return False
        else:
            delilac = delilac + 1
    return True 

def prosti_brojevi(kraj_intervala):
    lista = []
    broj  = 1

    while (broj < kraj_intervala):
        temp = prost_broj(broj)

        if (temp):
            lista.append(broj)
            broj = broj + 1 
        else:
            broj = broj + 1 
    
    return lista 



def main():
    broj = eval(input("Unesite broj: "))
    print(prosti_brojevi(broj))


main()