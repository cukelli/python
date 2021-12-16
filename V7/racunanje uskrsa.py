def uskrs(year):
    if (year >= 1900) or (year <= 2099):
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        date = 22 + d + e 

        if (year in [1954,1981,2049,2076]):
            date = date + 7 
        if (date <= 31):
            return "Uskrs je " + str(date) + ". marta" + str(year) + " .godine"
        else:
            date = date - 31 
            if (date <= 31):
                return "Uskrs je" + str(date) + " .aprila" + str(year) + " .godina"
            else:
                date = date - 31 
                return "Usrks je " + str(date) + " .maja" + str(year) + ". godine"
    else:
        return "Godina nije u predvidjenom opsegu"


def main():
    year = eval(input("Unesite godinu: "))


main()