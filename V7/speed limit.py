def main():
    brzina = eval(input("Unesite brzinu: "))
    ogranicenje = eval(input("Unesite ogranicenje: "))
    print(kazna(brzina,ogranicenje))
    


def kazna(brzina,ogranicenje):
    if (brzina > ogranicenje):
        kazna = 5000 + (brzina - ogranicenje) * 500
        return kazna 
    elif (brzina > ogranicenje) and (brzina > 120):
        kazna = (5000 + (brzina - ogranicenje ) * 500 ) + 10000
        return kazna 
    else:
         return "Nema kazne"   
    



main()





        