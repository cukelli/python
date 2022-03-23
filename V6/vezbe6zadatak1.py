import math 
def main():
    a = eval(input("Unesite a: "))
    b = eval(input("Unesite b: "))
    c = eval(input("Unesite c: "))
    resenja(a,b,c)


def resenja(a,b,c):
    x1 = - b + math.sqrt(b * b - 4 * a * c)
    x2 = -b - math.sqrt(b * b - 4 * a * c)

    print("Resenja kvadratne jednacine su",x1 ,"i",x2)






main()