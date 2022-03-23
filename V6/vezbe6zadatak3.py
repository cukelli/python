def main():
    username = input("Unesite korisnicko ime: ")
    password = input("Unesite lozinku: ")
    save(username,password)


def save(username,password):
    file = open('users.txt','a')
    file.write(username + "/" + password + "\n")


main()