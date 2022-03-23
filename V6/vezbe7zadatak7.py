def prestupna(godina):
    if (godina % 100 == 0):
        if (godina % 400 == 0):
            return 1
            
        else:
            return 0
    else:
        if (godina % 4 == 0):
            return 1
        else:
            return 0 
def dan_u_godini(datum):
    dan = int(datum.split("/")[0])
    mesec = int(datum.split("/")[1])
    godina = int(datum.split("/")[2])

    dann_u_godini = int(31 * (mesec - 1) + dan)


    if (mesec > 2) and prestupna(godina):
        dann_u_godini = int(dann_u_godini + 1)
        
    if (mesec > 2):
        dann_u_godini = int(dann_u_godini - (4 * mesec + 23) / 10)
        
    print(dann_u_godini)
    
    
def main():
    datum = input("Unesite datum: ")
    dan_u_godini(datum)
main()