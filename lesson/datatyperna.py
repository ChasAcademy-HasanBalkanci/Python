while True:
    print("Welcome to menu")
   #2 print("Write 'exit' to exit the program")
    
    val = input("Could you kindly write a variable to detect the type of them: ")
    if type(val) == int:
        print(f"The type of {val} is int")
    elif type(val) == str:
        print(f"The type of {val} is str")
    elif type(val) == float:
        print(f"The type of {val} is float")
    elif type(val) == bool:
        print(f"The type of {val} is bool")
    elif type(val) == complex:
        print(f"The type of {val} is complex")
else:
    exit()




        