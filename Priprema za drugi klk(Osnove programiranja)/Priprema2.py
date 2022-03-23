def main():
    num = eval(input("Unesite broj"))
    neparni(num)


def neparni(num):

    sum = 0

    while (num % 2 == 0):
        sum = sum + num
        num = eval(input("Unesite broj: "))

    print("Suma parnih brojeva iznosi", sum)


main()
