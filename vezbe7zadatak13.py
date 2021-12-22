def main():
    word = input("Unesite rec: ")
    palindrome(word)

def palindrome(word):

    if (word == word[::-1]):
        print("String je palindrom")
    else:
        print("String nije palindrom")
  

main()