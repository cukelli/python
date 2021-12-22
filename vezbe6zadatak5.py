def main():
    vreme_start = input("Unesite vreme pocetka:")
    vreme_end = input("Unesite vreme kraja:")
    izracunaj_platu(vreme_start,vreme_end)


def izracunaj_platu(vreme_start,vreme_end):
    sati_start,minuti_start = vreme_start.split(":")
    sati_end,minuti_end = vreme_end.split(":")
    start_time = int(sati_start) + int(minuti_start) / 60
    end_time = int(sati_end) + int(minuti_end) / 60
    ukupno = end_time - start_time

    zarada = 0

    if (end_time > 21) and (start_time < 21):
        zarada = (end_time - 21) * 100 + (21 - start_time) * 150
    elif (start_time > 21):
        zarada = ukupno * 100
    else:
        zarada = ukupno * 150 
    
    print("Zarada je",zarada)

main()




