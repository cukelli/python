import math as m

def prost_broj(broj):
    kraj = m.sqrt(broj)
    delilac = 2

    while (delilac <= kraj):
        if (broj % delilac == 0):
            return False
        else:
            delilac = delilac + 1
            
    return True 

def main():
    broj = eval(input("Unesite broj: "))
    print(prost_broj(broj))

main()

  