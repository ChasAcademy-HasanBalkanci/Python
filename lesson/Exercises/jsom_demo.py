import json
import os
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
        path = "D:\\GitHubChassAcadmey/Python/lesson/Exercises/users.json"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    self.users.append(User(user["username"], user["password"], user["email"]))
        else:
            print("User file not found.")


    def register(self, user: User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanici olusturuldu")

    def login(self):
        pass
    def savetoFile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))
        os.chdir("D:\\GitHubChassAcadmey/Python/lesson/Exercises")

        with open("users.json", "w", encoding="utf-8") as file:
            json.dump(list, file, indent=4)

repository = UserRepository()

while True:
    print("Menu".center(50, "*"))
    print("1. Register\n2. Login\n3. Logout\n4. Identity\n5. Exit: \n")

    secim = input("Seciminiz: ")
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



