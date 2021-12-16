def main():
    x = eval(input("Unesite prvi broj: "))
    y = eval(input("Unesite drugi broj: "))
    print(NZD(x,y))

def NZD (x,y):
    while (x!= y):
        step = y
        y = x % y 
        x = step
    return y 

main()
    