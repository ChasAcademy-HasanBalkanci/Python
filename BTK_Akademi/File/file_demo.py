# firstname, lastname, 3 degrees, savingfile, average, grade AA, BA, BB,CB, CC, DD, FF
info_degree = []
info_dict = {}
def get_info():
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    count = 0
    degree = ""
    global info_degree, info_dict

    for i in range(1,4):
        count = i
        degree += str(count)
        degree = (input(f"Enter your degree_{i} : "))
        info_degree.append(degree)

    info_dict.update({"firstname": firstname, "lastname": lastname, "degree": info_degree})

    #calculate_average_grade()

"""def calculate_average_grade():
    
    global info_degree, info_dict, avarege_degree

    avarege_degree = sum(int(num) for num in info_degree) / len(info_degree)

    if avarege_degree >= 90:
        info_dict.update({"avarege_degree": avarege_degree, "grade": "AA"})
    elif avarege_degree >= 80:
        info_dict.update({"avarege_degree": avarege_degree, "grade": "BA"})
        
    elif avarege_degree >= 70:
        info_dict.update({"avarege_degree": avarege_degree, "grade": "BB"})
        
    elif avarege_degree >= 60:
        info_dict.update({"avarege_degree": avarege_degree, "grade": "CB"})
        
    elif avarege_degree >= 50:
        info_dict.update({"avarege_degree": avarege_degree, "grade": "CC"})
    elif avarege_degree >= 40:
        info_dict.update({"avarege_degree": avarege_degree, "grade": "DD"})
    else:
        info_dict.update({"avarege_degree": avarege_degree, "grade": "FF"})

    return info_dict
"""
    
#get_info()

def save_file():
    count = 0
    try:
        with open("student1.txt", "x", encoding="utf-8") as file:
            pass
            
    except Exception as ex:
        pass
    
    finally:
        count += 1
    
        with open("student1.txt", "a", encoding="utf-8") as file:
            file.write(f"{count}.\t{str(get_info())}\n")

        with open("student1.txt", "r", encoding="utf-8") as file:
            print(file.read())

save_file()




