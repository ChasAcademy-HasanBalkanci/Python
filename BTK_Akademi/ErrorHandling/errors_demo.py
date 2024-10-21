liste = ["1", "2", "5a", "10b", "abc"]

# 1: Find the numbers in the list
'''num_list = []
for num in liste:
    if num.isdigit():
        num_list.append(int(num))
    else:
        for i in num:
            if i.isdigit():
                num_list.append(int(i)) 
''' 

'''
num_list = [int(i)  for num in liste for i in num if i.isdigit()]
print(num_list)
'''

'''def new_func(liste):
    for num in liste:
        try:
            result = int(num)
            print(result)
            continue 
        except Exception as ex:
            print(ex)

new_func(liste)
'''

# Ensure that all input is integer under the user doen't enter "q"
'''
def check_num():
    num = input("Enter a number to keep going or write 'q' to quit: ")
    if num.isdigit():
        return int(num)
    elif num.lower() == "q":
        raise SystemExit
        
    else:
        print("Please enter a valid number.")
        return check_num()

while True:
    try:
        check_num()

    except Exception as ex:
        print(ex)
        print("Please enter a valid number.")
'''
   
     
'''
    
while True:
    value_input = input("Please enter a number to keep going or write 'q' to quit: ")
    if value_input.lower() == "q":
        raise SystemExit
        #break
    try:
        
        result = int(value_input)
        print(result)
        continue        
    
    except Exception as ex:
        print(ex)

'''   
# 3 in the entered pasword prompt raies an error message "Swedish charecters are not allowed" 
"""
def check_password():
    import re
    password = input("Enter your password: ")
    if re.search("[ä,ö,å,Ö,Å,Ä]", password):
        raise ValueError("Swedish charecters are not allowed")
    else:
        print("Password is valid")

check_password()

"""


"""
import re
password = input("Enter your password: ")
result = re.search("[ä,ö,å,Ö,Å,Ä]", password)

try:
    if result:
        raise ValueError("Swedish charecters are not allowed")
except Exception as ex:
    print(ex)
else:
    print("Password is valid")
"""


 # 4 Create factorial function and rise error mesage if input is not integer 

def factorial_func():
     from math import factorial
     global num
     num = input("Enter a number to calculate its factorial: ")
     num_factorial = 1
     if num.isdigit():
        num_factorial = factorial(int(num))
        print(f"{num}! = {num_factorial}") #print(num_factorial)
        
     else:
        raise ValueError("Please enter a valid number.")

factorial_func()
    
    

    