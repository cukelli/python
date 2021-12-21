def main():
    prvi_string = input("Unesite prvi string: ")
    drugi_string = input("Unesite drugi string: ")
    strings(prvi_string,drugi_string)

def strings(prvi_string,drugi_string):
    novi_string = 2 * prvi_string[0:3] + drugi_string[-3:len(drugi_string)]
    print(novi_string)







main()