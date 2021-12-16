def main():
    start = input("Unesite pocetno vreme: ")
    end = input("Unesite zavrsno vreme: ")
    print(izracunaj_platu(start,end))


def izracunaj_platu(start,end):
    sati_start,minuti_start = start.split(":")
    sati_end,minuti_end = end.split(":")
    start_time =  int(sati_start) + int(minuti_start)  / 60
    end_time =   int(sati_end) + int(minuti_end)  / 60
    ukupno_sati = end_time - start_time

    zarada = 0
    if (end_time > 21) and (start_time < 21):
        zarada = (end_time - 21) * 100 + (21 - start_time) * 150
    elif (start_time > 21):
        zarada = 100 * ukupno_sati
    else:
        zarada = ukupno_sati * 150
    
    return zarada

main()



        
    
    


    