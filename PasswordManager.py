from cryptography.fernet import Fernet


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is your master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user: ", user, ", Password: ", str(fer.decrypt(passw.encode())))


def add():
    name = input("Account Name: ")
    pwd = input("password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + str(fer.encrypt(pwd.encode())) + "\n")


while True:
    mode = input("You want add new or use existing: view/add ,If you want to Quit press Quit: ").lower()
    if mode == "quit":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid")
