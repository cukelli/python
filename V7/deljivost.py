def main():
    for i in range(1200,2501):
        if (i % 7 == 0) and (i % 11 == 0):
            print(i)
    print("Ovo su svi brojevi deljivi sa 7 i 11")


main()