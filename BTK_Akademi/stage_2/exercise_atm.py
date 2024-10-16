SadikAccount = {
    "name": "Sadik Turan",
    "AccountId": "12345678",
    "Balance" : 3000,
    "SavingAccountBalance": 2000

}

AliAccount = {
    "name": "Ali Turan",
    "AccountId": "12345678",
    "Balance" : 2000,
    "SavingAccountBalance": 1000

}
   
def withdraw():
    name = input("Enter your name:").lower()
    def check():
        withdrawMoney = int(input("How much do you want to withdraw from your account : "))

        if name == SadikAccount["name"].lower():
            if SadikAccount["Balance"] >= withdrawMoney:
               SadikAccount["Balance"] -= withdrawMoney
               print("Withdrawal successful. Your remaining balance is:", SadikAccount["Balance"])
        
            else: 
                GetConsent = input("Do you want to use your savings account ? \n(Yes/No): ")
                if GetConsent.lower() == "yes":
                    if SadikAccount["SavingAccountBalance"] + SadikAccount["Balance"] >= withdrawMoney:
                    
                        SadikAccount["SavingAccountBalance"] -= (withdrawMoney -SadikAccount["Balance"])
                        SadikAccount["Balance"] = 0                                         

                        print("Withdrawal successful. \nYour remaining balance is:", SadikAccount["Balance"])
                        print("Withdrawal from your savings account also successful. \nYour remaining savings balance is:", SadikAccount["SavingAccountBalance"])
                    else:
                        print("Insufficient total funds in your savings account and balance.")
                        print(f"You can withdraw max : {SadikAccount["SavingAccountBalance"] + SadikAccount["Balance"]}")
                        check()
    check()
                   

withdraw()

