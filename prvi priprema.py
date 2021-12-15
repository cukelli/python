# Program koji korisniku trazi rec, i unosi se sve dok poslednje slovo ne bude a
# Brojis broj pogresnih unosa

def main():
    word = input("Enter your word: ")
    pogresni_unosi(word)


def pogresni_unosi(word):
    wrong = 0
    while (word[-1] != 'a'):
        word = input("Enter your word: ")
        wrong = wrong + 1

        if (word[-1] == 'a'):
            print("Broj pogresnih unosa je", wrong)
            break


main()
