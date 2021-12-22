def racunanje_uskrsa(godina):
    if godina in range(1982,2048):
          a = godina % 19
          b = godina % 4
          c = godina % 7
          d = (19 * a + 24) % 30
          e = (2 * b + 4 * c + 6 * d + 5) % 7
          datum = 22 + d + e 

          if (datum <= 31):
              return "Uskrs je" + str(datum) + ".marta" + str(godina) + ".godine"
          else:
              datum = datum - 31 
              return "Uskrs je" + str(datum) + " .aprila" + str(godina) + ".godine"
    else:
        return "Godina nije u predvidjenom opsegu"
 


def main():
    godina = int(input("Unesite godinu: "))
    racunanje_uskrsa(godina)


main()