def main():
    deljivost()
    


def deljivost():

    for broj in range(1200,2501):
        if (broj % 7 == 0) and (broj % 11 == 0):
            print(broj)
    print("Ovo su svi brojevi deljivi sa 7 i 11")




main()