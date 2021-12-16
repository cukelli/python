#Sekvenca sirakuza

def main():
    x = eval(input("Unesite x: "))
    lista = sirakuza(x)
    print(lista)



def sirakuza(x):
    lista = []
    lista.append(x)

    while (x != 1 ):
        if (x % 2 == 0):
            x = x // 2
        else:
            x = (3 * x) + 1 
        
        lista.append(x)
    
    return lista 
    
main()