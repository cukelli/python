def main():
    reci = input("Unesite reci odvojene zarezom: ")
    reci = reci.split(",")
    print(izbaci_duple(reci))



def izbaci_duple(reci):

    unikatne_reci = []
    for rec in reci:
        unique = True 
        for unikatna_rec in unikatne_reci:
            if (rec == unikatna_rec):
                unique = False 
        if unique:
            unikatne_reci.append(rec)

    return ",".join(unikatne_reci)


main()
            



        
