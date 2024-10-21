import json
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUser()

    def loadUser(self):
        pass
    def register(self, user: User):
        self.users.append(user)
        # self.savetoFile()
        print("Kayıt tamamlandı")

    def login(self):
        pass
    def savetoFile(self):
        with open("users.json", "a", encoding="utf-8") as file:
            json.dump(self.users, file, indent=4)
            
repository = UserRepository()
while True:
    print("Menu".center(50, "*"))
    secim = input("1. Register\n2. Login\n3. Logout\n4. Identity\n5. Exit: ")
    if secim == "5":
        break
    else:
        if secim == "1":
            #register
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            user = User(username, password, email)
            repository.register(user)
            print(repository.users)
        elif secim == "2":
            #login
            pass
        elif secim == "3":
            #logout
            pass
        elif secim == "4":
            #identity, display username
            pass
        else:
            print("Hatalı giriş")
