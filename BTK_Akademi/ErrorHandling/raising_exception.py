'''
x = 10
if x > 5:
    raise Exception("x cant be take a value greater than 5")
'''
def check_password(psw):
    import re
    if len(psw) <= 8:
        raise ValueError("Password should be at least 8 characters long")
    elif not re.search("[a-z]", psw):
        raise ValueError("Password should contain at least one lowercase letter")
    elif not re.search("[A-Z]", psw):
        raise ValueError("Password should contain at least one uppercase letter")
    elif not re.search("[0-9]", psw):
        raise ValueError("Password should contain at least one digit")
    elif not re.search(r'[\W_]', psw):
        raise ValueError("Password should contain at least one special character")
    #elif re.search("\s", psw):
        #raise ValueError("Password should not contain any whitespace")
    
# Testing the functionsHa
password = "1234a5S6789"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Else : Password is valid")


