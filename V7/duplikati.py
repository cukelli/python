def main():
    niz = input("Unesite reci odvojene zarezom: ")
    niz = niz.split(",")
    print(eliminate_duplicates(niz))


def eliminate_duplicates(niz):
    unique_elements = []
    for word in niz:
        unique = True 
        for unique_element in unique_elements:
            if (word == unique_element):
                unique = False 
        
        if unique:
            unique_elements.append(word)
    
    return ",".join(unique_elements)



main()
