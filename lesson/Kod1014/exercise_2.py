def repeat():
    text = input("Write a sentence : ")
    repeat = input ("How many times do you want to repeat :")
    
    if repeat.isdigit():
        repeat = int(repeat)
        for i in range(repeat):
            print(text)

    else:
        print("Invalid input. Please enter a positive integer.")

repeat()
