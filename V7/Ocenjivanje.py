def main():
    bodovi = eval(input("Unesite bodove: "))
    print(ocenjivanje(bodovi))
    


def ocenjivanje(bodovi):
    if (bodovi >= 0) and (bodovi <=55):
        ocena = 5
    elif (bodovi >=56) and (bodovi <= 65):
        ocena = 6 
    elif (bodovi >= 66) and (bodovi <=75):
        ocena = 7 
    elif (bodovi >=76) and (bodovi <=85):
        ocena = 8 
    elif (bodovi >=86) and (bodovi <=95):
        ocena = 9 
    elif (bodovi >= 96) and (bodovi <=100):
        ocena = 10
    else:
        print("Niste uneli bodove u dobrom opsegu")



    print("Ocena je:",end=" ")    

    return ocena 
    
    
    
    
    
    
main()