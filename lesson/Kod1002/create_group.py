import random 

names = []
groupstorlek = 0
groups = []
y = 1

def meny():
    print("\nChoose an option:")
    print("1. Mata in namn")
    print("2. Ta bort namn")
    print("3. Välj groupstorlek")
    print("4. Skapa grupper")
    print("5. Avsluta programmet")

    choice = input("Välj en siffra: ")
    return int(choice)

def mata_in_namn():
    while True:
        print("\nSkriv 'Exit' för att gå till meny: ")
        name = input("Ange namn: ")
        if name.lower() == "exit":
            break
        else:
            names.append(name)
        
    return names

def ta_bort_namn():
    while True:
        print("\nSkriv 'Exit' för att gå till meny: ")
        namn = input("Ange namn att ta bort: ")
        if namn.lower() == "exit":
            break
        elif namn in names:
            names.remove(namn)
            print(f"Namn List: {names}")
        else:
            print("Namnet hittades inte.")
    return names

def valj_groupstorlek():
    global groupstorlek 
    groupstorlek = int(input("Mata in groupstorlek: "))
    return groupstorlek

def skapa_grupper():
    global groups
    if groupstorlek > len(names):
        print("Groupstorleken är större än antalet namn.")
    else:
        groups = []  # Clear existing groups
        shuffled_names = names[:]
        random.shuffle(shuffled_names)
        
        while len(shuffled_names) >= groupstorlek:
            group = shuffled_names[:groupstorlek]
            groups.append(group)
            shuffled_names = shuffled_names[groupstorlek:]
        for x in groups:
            global y
            print(f"\n\tGroup{y}: {x}")
            y += 1

        if shuffled_names:  # If there are remaining names, add them to the last group
            groups[-1].extend(shuffled_names)
        

def main():
    while True:
        choice = meny()
        if choice == 1:
            mata_in_namn()
            print(f"Namn List: {names}")
            
        elif choice == 2:
            ta_bort_namn()
            print(f"Namn List: {names}")
        
        elif choice == 3:
            valj_groupstorlek()
            print(f"Vald groupstorlek: {groupstorlek}")
        
        elif choice == 4:
            if names and groupstorlek:
                skapa_grupper()
            else:
                print("Namnlista eller groupstorlek är tom.")

        elif choice == 5:
            print("Avslutar programmet.")
            break

if __name__ == "__main__":
    main()
